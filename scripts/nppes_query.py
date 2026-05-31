#!/usr/bin/env python3
"""Query the CMS NPPES NPI Registry for organizational healthcare providers.

Public REST API, no key required: https://npiregistry.cms.hhs.gov/api/?version=2.1

Used by the `industry-fragmentation` and `deal-sourcing` skills to gauge how many
provider organizations operate in a vertical + geography (a fragmentation signal)
and to build a proprietary target longlist with names and addresses.

Examples:
    python3 scripts/nppes_query.py --taxonomy "Home Health" --state FL --limit 100
    python3 scripts/nppes_query.py --taxonomy "Physical Therapist" --state TX --city Austin --csv
    python3 scripts/nppes_query.py --taxonomy "Skilled Nursing Facility" --state OH --json > targets.json

Notes:
    - Filters to organizational providers (enumeration_type=NPI-2), i.e. companies, not individuals.
    - The API caps each response at 200 records and 1200 records total per query (skip <= 1000).
      Narrow by --city or --postal when a state returns more than ~1200 orgs.
"""
import argparse
import csv
import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request

API_URL = "https://npiregistry.cms.hhs.gov/api/"
PAGE_SIZE = 200          # API maximum per request
MAX_SKIP = 1000          # API rejects skip > 1000
USER_AGENT = "analyze-rollup-research/1.0 (search-fund research; contact via repo)"

# Candidate CA bundles, in priority order. Some Homebrew Python builds ship without
# a usable trust store, so we prefer a known-good full bundle over the (sometimes
# partial) one referenced by SSL_CERT_FILE. See commands/setup-rollup-research.md.
CA_CANDIDATES = [
    "/opt/homebrew/etc/ca-certificates/cert.pem",  # Homebrew (Apple Silicon)
    "/usr/local/etc/ca-certificates/cert.pem",      # Homebrew (Intel)
    "/etc/ssl/cert.pem",                             # macOS / BSD
    "/etc/ssl/certs/ca-certificates.crt",            # Debian/Ubuntu
]

_INSECURE = False  # set from --insecure; opt-in only


def ssl_context():
    """Build an SSL context, preferring a known-good CA bundle. --insecure disables
    verification entirely (last resort for strict MITM proxies like Zscaler)."""
    if _INSECURE:
        sys.stderr.write("warning: TLS verification disabled (--insecure).\n")
        return ssl._create_unverified_context()
    try:
        import certifi  # optional; only if the user installed it
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for path in CA_CANDIDATES:
        if os.path.exists(path):
            return ssl.create_default_context(cafile=path)
    return ssl.create_default_context()


def fetch_page(params):
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{API_URL}?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30, context=ssl_context()) as resp:
        return json.loads(resp.read().decode("utf-8"))


def query_providers(taxonomy, state, city=None, postal=None, limit=None):
    """Page through NPPES results, returning a list of normalized provider dicts."""
    base = {
        "version": "2.1",
        "enumeration_type": "NPI-2",   # organizations only
        "taxonomy_description": taxonomy,
        "country_code": "US",
        "limit": PAGE_SIZE,
    }
    if state:
        base["state"] = state.upper()
    if city:
        base["city"] = city
    if postal:
        base["postal_code"] = postal

    providers = []
    skip = 0
    while True:
        params = dict(base, skip=skip)
        data = fetch_page(params)
        results = data.get("results", []) or []
        if not results:
            break
        for r in results:
            providers.append(normalize(r))
            if limit and len(providers) >= limit:
                return providers[:limit]
        if len(results) < PAGE_SIZE:
            break
        skip += PAGE_SIZE
        if skip > MAX_SKIP:
            sys.stderr.write(
                "warning: hit NPPES 1200-record ceiling; narrow with --city/--postal "
                "for a complete count.\n"
            )
            break
        time.sleep(0.2)  # be polite to a free public API
    return providers


def normalize(r):
    basic = r.get("basic", {})
    addresses = r.get("addresses", []) or []
    location = next((a for a in addresses if a.get("address_purpose") == "LOCATION"), {})
    if not location and addresses:
        location = addresses[0]
    taxonomies = r.get("taxonomies", []) or []
    primary = next((t for t in taxonomies if t.get("primary")), taxonomies[0] if taxonomies else {})
    return {
        "npi": r.get("number"),
        "name": basic.get("organization_name") or basic.get("name"),
        "taxonomy": primary.get("desc"),
        "address": location.get("address_1"),
        "city": location.get("city"),
        "state": location.get("state"),
        "postal": (location.get("postal_code") or "")[:5],
        "phone": location.get("telephone_number"),
    }


def main():
    ap = argparse.ArgumentParser(description="Query NPPES NPI Registry for provider organizations.")
    ap.add_argument("--taxonomy", required=True,
                    help='Provider taxonomy description, e.g. "Home Health", "Physical Therapist".')
    ap.add_argument("--state", help="Two-letter state code, e.g. FL.")
    ap.add_argument("--city", help="City name to narrow results.")
    ap.add_argument("--postal", help="5-digit ZIP to narrow results.")
    ap.add_argument("--limit", type=int, help="Stop after N providers.")
    out = ap.add_mutually_exclusive_group()
    out.add_argument("--json", action="store_true", help="Emit JSON array to stdout.")
    out.add_argument("--csv", action="store_true", help="Emit CSV to stdout.")
    ap.add_argument("--insecure", action="store_true",
                    help="Disable TLS verification (last resort behind a MITM proxy). Off by default.")
    args = ap.parse_args()

    global _INSECURE
    _INSECURE = args.insecure

    providers = query_providers(args.taxonomy, args.state, args.city, args.postal, args.limit)

    if args.json:
        json.dump(providers, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif args.csv:
        writer = csv.DictWriter(
            sys.stdout,
            fieldnames=["npi", "name", "taxonomy", "address", "city", "state", "postal", "phone"],
        )
        writer.writeheader()
        writer.writerows(providers)
    else:
        scope = " / ".join(x for x in [args.taxonomy, args.city, args.state] if x)
        print(f"NPPES organizational providers — {scope}")
        print(f"Total found: {len(providers)}\n")
        for p in providers[:25]:
            loc = ", ".join(x for x in [p["city"], p["state"]] if x)
            print(f"  {p['name']}  ({loc})  NPI {p['npi']}")
        if len(providers) > 25:
            print(f"  ... and {len(providers) - 25} more (use --csv or --json for the full list)")


if __name__ == "__main__":
    main()
