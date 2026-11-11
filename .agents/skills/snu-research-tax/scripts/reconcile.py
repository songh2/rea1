#!/usr/bin/env python3
"""Arithmetic reconciliation of independently verified tax amounts; no tax rules."""
import argparse
import json


def reconcile(gross: int, national_tax: int, local_tax: int) -> dict:
    if any(type(x) is not int or x < 0 for x in (gross, national_tax, local_tax)):
        raise ValueError("금액은 0 이상의 정수 원 단위여야 합니다")
    withheld = national_tax + local_tax
    if withheld > gross:
        raise ValueError("원천징수합계가 총지급액을 초과합니다")
    return {
        "gross_won": gross,
        "national_tax_won": national_tax,
        "local_tax_won": local_tax,
        "total_withheld_won": withheld,
        "net_won": gross - withheld,
    }


def won(value: str) -> int:
    if not value.isascii() or not value.isdecimal():
        raise argparse.ArgumentTypeError("원 단위 0 이상의 정수를 입력하세요")
    return int(value)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="검증된 국세/지방세 지급액 산술검산")
    p.add_argument("--gross", type=won, required=True)
    p.add_argument("--national-tax", type=won, required=True)
    p.add_argument("--local-tax", type=won, required=True)
    a = p.parse_args()
    try:
        print(json.dumps(reconcile(a.gross, a.national_tax, a.local_tax), ensure_ascii=False, indent=2))
    except ValueError as e:
        p.error(str(e))
