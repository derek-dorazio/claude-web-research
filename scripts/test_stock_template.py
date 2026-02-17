#!/usr/bin/env python3
"""Test the stock analysis slides template by building a sample deck."""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from templates import stock_analysis_slides as t

def test_template():
    deck = t.StockAnalysisDeck()
    prs = deck.prs

    # Slide 1: Title
    t.build_title_slide(prs, "TEST", "Test Corp", "2026-02-17", "Buy", 100.0, 130.0)

    # Slide 2: Executive Summary
    t.build_executive_summary(prs, [
        "Bullet point one",
        "Bullet point two",
        "Bullet point three",
    ])

    # Slide 3: Valuation Snapshot
    t.build_valuation_snapshot(prs, [
        ["Forward P/E", "20.0x", "In line with peers"],
        ["PEG Ratio", "1.2", "Fairly valued"],
        ["EV/EBITDA", "15.0x", "Reasonable"],
    ])

    # Slide 4: Income Statement
    t.build_income_statement(prs, ["FY2025", "FY2024", "FY2023"], [
        ["Revenue", "$10.0B", "$9.0B", "$8.0B"],
        ["Net Income", "$2.0B", "$1.8B", "$1.5B"],
    ], note="Test note for income statement.")

    # Slide 5: Balance Sheet
    t.build_balance_sheet_cashflow(prs, ["FY2025", "FY2024", "FY2023"], [
        ["Cash", "$5.0B", "$4.0B", "$3.0B"],
        ["Total Debt", "$2.0B", "$2.5B", "$3.0B"],
        ["Free Cash Flow", "$3.0B", "$2.5B", "$2.0B"],
    ], note="Improving cash position.")

    # Slide 6: Peer Comparison
    t.build_peer_comparison(prs, "TEST", ["PEER1", "PEER2"], [
        ["Market Cap", "$50B", "$40B", "$30B"],
        ["Forward P/E", "20x", "18x", "22x"],
    ])

    # Slide 7: Valuation Summary
    t.build_valuation_summary(prs, [
        ["DCF", "$120.00", "+20%", "50%"],
        ["Comps", "$140.00", "+40%", "50%"],
        ["Weighted Avg", "$130.00", "+30%", "—"],
    ])

    # Slide 8: Sensitivity
    t.build_sensitivity_analysis(prs,
        ["$3B Bear", "$4B Base", "$5B Bull"],
        ["WACC 8%", "WACC 10%", "WACC 12%"],
        [["$150", "$120", "$100"], ["$180", "$150", "$125"], ["$210", "$175", "$150"]],
        note="Test sensitivity note.")

    # Slide 9: Bull/Bear
    t.build_bull_bear(prs,
        ["Strong growth", "Market leader", "Expanding margins"],
        ["High valuation", "Competition risk", "Macro headwinds"])

    # Slide 10: Catalysts
    t.build_catalysts(prs, [
        "[Q1 2026] Product launch",
        "[Q3 2026] Earnings catalyst",
    ])

    # Slide 11: Recommendation
    t.build_recommendation(prs, "Buy", 100.0, 130.0, "Medium",
                           "Strong Buy ($135 median)", "Compelling risk/reward at current levels.")

    output = "/tmp/test_stock_template.pptx"
    deck.save(output)

    # Verify
    verify_prs = t.Presentation(output)
    slide_count = len(verify_prs.slides)
    print(f"PASS: Generated {slide_count} slides")
    assert slide_count == 11, f"Expected 11 slides, got {slide_count}"

    # Clean up
    os.remove(output)
    print("PASS: All 11 slide builders work correctly")
    print("PASS: Template test complete")

if __name__ == "__main__":
    test_template()
