#!/usr/bin/env python3
"""SNU fiscal-year date screening only, not legal tax eligibility."""
import argparse
import calendar
import json
from datetime import date

SUNSET = date(2028, 12, 31)

def fiscal_year(year: int) -> dict:
    if type(year) is not int or not (1900 <= year <= 9998):
        raise ValueError("invalid fiscal year")
    end = date(year + 1, 2, calendar.monthrange(year + 1, 2)[1])
    return {"fiscal_year": year, "start": date(year, 3, 1).isoformat(),
            "end": end.isoformat(), "sunset_date": SUNSET.isoformat(),
            "within_published_sunset_by_date_only": end <= SUNSET,
            "warning": "Verify actual corporate-tax business year and current law."}

def cutoff_check(end_date: str) -> dict:
    try:
        end = date.fromisoformat(end_date)
    except (ValueError, TypeError) as exc:
        raise ValueError("expected YYYY-MM-DD") from exc
    return {"business_year_end": end.isoformat(), "sunset_date": SUNSET.isoformat(),
            "within_published_sunset_by_date_only": end <= SUNSET,
            "warning": "Date comparison only. Tax-law eligibility not established."}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--fiscal-year", type=int)
    group.add_argument("--business-year-end")
    a = p.parse_args()
    try:
        obj = fiscal_year(a.fiscal_year) if a.fiscal_year is not None else cutoff_check(a.business_year_end)
    except ValueError as exc:
        p.error(str(exc))
    print(json.dumps(obj, ensure_ascii=False, indent=2))
