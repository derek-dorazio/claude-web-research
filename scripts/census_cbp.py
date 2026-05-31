#!/usr/bin/env python3
"""Query US Census County Business Patterns (CBP) for establishment counts by NAICS.

Public REST API. A free key is optional for low volume but recommended:
https://api.census.gov/data/key_signup.html  (set CENSUS_API_KEY in your env)

Used by the `industry-fragmentation` and `rollup-thesis` skills to size *any*
services vertical by NAICS code — establishment counts (ESTAB), employment (EMP),
and annual payroll (PAYANN) — and to compute rough per-firm averages. This is the
generic path that works for non-healthcare "other services" firms.

Examples:
    python3 scripts/census_cbp.py --naics 6216 --geo "state:12"          # FL home health
    python3 scripts/census_cbp.py --naics 8123 --geo "us:*"              # US dry cleaning/laundry
    python3 scripts/census_cbp.py --naics 5617 --geo "state:48" --year 2022 --json

Geo syntax follows the Census API "for=" clause, e.g.:
    "us:*"            national
    "state:12"        a single state (FIPS; FL=12, TX=48, CA=06)
    "county:*&in=state:12"   all counties in FL
"""
import argparse
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request

VARS = ["ESTAB", "EMP", "PAYANN"]  # establishments, employment, annual payroll ($1,000s)
KEY_SIGNUP = "https://api.census.gov/data/key_signup.html"

# See scripts/nppes_query.py for the rationale behind CA-bundle discovery.
CA_CANDIDATES = [
    "/opt/homebrew/etc/ca-certificates/cert.pem",
    "/usr/local/etc/ca-certificates/cert.pem",
    "/etc/ssl/cert.pem",
    "/etc/ssl/certs/ca-certificates.crt",
]

_INSECURE = False


def ssl_context():
    if _INSECURE:
        sys.stderr.write("warning: TLS verification disabled (--insecure).\n")
        return ssl._create_unverified_context()
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for path in CA_CANDIDATES:
        if os.path.exists(path):
            return ssl.create_default_context(cafile=path)
    return ssl.create_default_context()


def build_url(year, naics, geo):
    base = f"https://api.census.gov/data/{year}/cbp"
    # geo may include an "&in=" clause; split it into for=/in= params.
    if "&in=" in geo:
        for_clause, in_clause = geo.split("&in=", 1)
    else:
        for_clause, in_clause = geo, None
    params = [
        ("get", ",".join(["NAME", "NAICS2017_LABEL"] + VARS)),
        ("for", for_clause),
        ("NAICS2017", naics),
    ]
    if in_clause:
        params.append(("in", in_clause))
    key = os.environ.get("CENSUS_API_KEY")
    if not key:
        sys.stderr.write(
            "error: the Census API now requires a key. It's free and instant — "
            f"sign up at {KEY_SIGNUP}\n       then: export CENSUS_API_KEY=...\n"
        )
        sys.exit(2)
    params.append(("key", key))
    return f"{base}?{urllib.parse.urlencode(params)}"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "analyze-rollup-research/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=ssl_context()) as resp:
        body = resp.read().decode("utf-8")
    if "Missing Key" in body or "Invalid Key" in body:
        sys.stderr.write(f"error: Census rejected the API key. Check CENSUS_API_KEY (sign up: {KEY_SIGNUP}).\n")
        sys.exit(2)
    return json.loads(body)


def to_records(rows):
    """Census returns a header row followed by value rows; zip into dicts."""
    if not rows or len(rows) < 2:
        return []
    header = rows[0]
    return [dict(zip(header, r)) for r in rows[1:]]


def main():
    ap = argparse.ArgumentParser(description="Query Census County Business Patterns by NAICS.")
    ap.add_argument("--naics", required=True,
                    help="NAICS code (2017 vintage), e.g. 6216 (home health), 8123 (laundry).")
    ap.add_argument("--geo", default="us:*",
                    help='Census geography, e.g. "state:12", "us:*", "county:*&in=state:12".')
    ap.add_argument("--year", default="2022", help="CBP data year (default 2022).")
    ap.add_argument("--json", action="store_true", help="Emit raw JSON records to stdout.")
    ap.add_argument("--insecure", action="store_true",
                    help="Disable TLS verification (last resort behind a MITM proxy). Off by default.")
    args = ap.parse_args()

    global _INSECURE
    _INSECURE = args.insecure

    url = build_url(args.year, args.naics, args.geo)
    try:
        rows = fetch(url)
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"Census API error {e.code}: {e.reason}\nURL: {url}\n")
        if e.code == 404:
            sys.stderr.write("Tip: check the --year (data lags ~2 yrs) and NAICS vintage.\n")
        sys.exit(1)

    records = to_records(rows)
    if args.json:
        json.dump(records, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return

    if not records:
        print(f"No CBP data for NAICS {args.naics} in {args.geo} ({args.year}).")
        return

    label = records[0].get("NAICS2017_LABEL", args.naics)
    print(f"County Business Patterns {args.year} — NAICS {args.naics}: {label}")
    print(f"{'Geography':<32} {'Estab':>10} {'Employees':>12} {'Payroll $K':>14} {'Emp/Estab':>10}")
    print("-" * 80)
    tot_estab = 0
    for r in records:
        estab = int(r.get("ESTAB") or 0)
        emp = int(r.get("EMP") or 0)
        pay = int(r.get("PAYANN") or 0)
        tot_estab += estab
        per = f"{emp / estab:.1f}" if estab else "-"
        name = (r.get("NAME") or "")[:31]
        print(f"{name:<32} {estab:>10,} {emp:>12,} {pay:>14,} {per:>10}")
    if len(records) > 1:
        print("-" * 80)
        print(f"{'TOTAL establishments':<32} {tot_estab:>10,}")


if __name__ == "__main__":
    main()
