# Upstage MCP 법인회계 우선 도구 맵

확인: UpstageAI/korean-tax-calc-mcp 0.31.0 (2026-11-11). 실제 연결된 도구 목록과 현재 세법을 재검증한다.

| 우선순위 | 업무 | 후보 도구 | 필수 법적·입력 전제 |
|---|---|---|---|
| 핵심 | 비영리 고유목적사업준비금 | nonprofit_reserve_limit | 특례 적용자격과 실제 **사업연도 종료일**; year <= 2028 방식의 upstream 일몰 판정 신뢰 금지 |
| 핵심 | 법인세 | corporate_tax, income_adjustment_total | 수익사업·비수익사업 구분경리, 익금·손금 및 공제 확인 |
| 핵심 | 기부금 | donation_limit | 받은 기부금과 지급 기부금 구별, 적격 지출 판단 |
| 핵심 | 감가상각·보조금 | depreciation_adjustment, asset_grant_reserve | 자산·수익 인식, 법인세 적용 판단 선행 |
| 핵심 | 매입세액 | vat_input_tax_deduction, vat_common_input_allocation, common_input_tax | 과세·면세 거래와 공통매입액 분리 |
| 핵심 | 부가세 신고·해외 용역 | vat_return_general, vat_reverse_charge, vat_supply_timing | 신고 법인·거래시기·역외 공급 검증 |
| 보조 | 국내 지급 원천세 | withholding_tax, wage_income_tax, daily_worker_withholding | 소득 종류 판별; 기타소득은 필요경비·과세최저한 먼저 검토 |
| 보조 | 비거주자 지급 | nonresident_withholding | 국내원천·거주자성·조세조약 근거 검증 |
| 공통 | 도구 확인·검토 엑셀 | find_tool, export_workbook | 비식별 자료만; 서식은 자동 신고서가 아님 |

법인세·부가세 도구가 일반 기업 상황을 전제할 수 있으므로 대학법인의 구분경리·특례를 먼저 판단한다. nonprofit_reserve_limit 는 연도 정수로만 일몰을 판단하므로 scripts/periods.py 및 최신 공식 법령 검증이 필수다.

원본: https://github.com/UpstageAI/korean-tax-calc-mcp
