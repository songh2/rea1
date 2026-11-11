# Upstage MCP 도구 매핑

확인 시점: 2026-11-11, 원본 버전 0.31.0. 실제 등록된 도구 스키마를 재확인한다.

| 연구비 지급 업무 | MCP 도구 | 주요 입력 | 제한 |
|---|---|---|---|
| 도구 검색 | find_tool | query | 후보일 뿐 적용 판단 아님 |
| 거주자 원천징수 | withholding_tax | kind, amount, year | 소득세분만 계산. 기타소득은 필요경비·과세최저한 확인 후 과세대상 금액 입력 |
| 비거주자 지급 | nonresident_withholding | income_kind, amount, recipient_type, residence_country, treaty_rate?, service_location? | 조세조약·거주자성 별도 확인 |
| 근로소득 연간 참고 | wage_income_tax | gross_pay, year, tax_base? | 월별 간이세액표 아님 |
| 일용근로 | daily_worker_withholding | daily_wage, year | 일용근로자 해당 여부 판단 선행 |
| 부가세 매입 공제 | vat_input_tax_deduction | period, filing, items | 과세·면세 여부 선행 |
| 공통매입세액 | vat_common_input_allocation | common_tax, total_supply, exempt_supply | 실제 공급액 필요 |
| 엑셀 검토용 | export_workbook | title, calls, output_dir?, layout? | 비식별 데이터만 사용 |

원본: https://github.com/UpstageAI/korean-tax-calc-mcp/blob/main/korean_tax_calc_mcp/server.py

주의: 200,000원 일회 강연료 사례에서 기타소득금액 80,000원이 확인된 경우 원본 withholding_tax의 amount에는 200000이 아니라 80000을 넣어야 한다.
