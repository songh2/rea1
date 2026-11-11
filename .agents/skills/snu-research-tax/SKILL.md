---
name: snu-research-tax
description: "Review National University Corporation Seoul National University (SNU) corporate-account tax and nonprofit accounting first: taxable versus non-taxable activities, corporate income tax, business versus nonprofit books, reserve for designated purposes, donations, VAT, withholding, closing and filings. Also supports SNU research-administration tax as a secondary area. Use for questions about SNU corporation accounting, VAT invoices, revenue classification, tax adjustment, year-end close, business units and tax calendars."
---

# SNU corporate accounting and tax review

**Primary focus: the corporate accounts of National University Corporation Seoul National University.** Research administration is secondary. Answer users in Korean. This is a source-checked decision-support Skill, not an accountant, tax agent, official SNU rulebook, filing system, or substitute for an authorized approver. Never modify original Upstage code or directly file, pay, post or approve entries.

## 1. Mandatory routing

1. Determine the **legal entity** responsible for the transaction: SNU university corporation, SNU Industry-Academic Cooperation Foundation, university development fund, another affiliate, or unknown. Never treat them as the same taxpayer because their names contain SNU. Establish separate taxpayer registration, book and filing unit using evidence, not inference.
2. Establish transaction date, underlying business period, monetary unit and evidence. Distinguish statutory SNU accounting year (**Mar 1 to end of following February**; SNU establishment act Art. 19), the verified corporate-tax business-year registration and the VAT half-year filing period. They are not interchangeable. See references/entity-periods.md.
3. Separate **accounting recognition**, **corporate-tax characterization**, **VAT treatment**, **withholding**, and **SNU internal authority**. Never infer legal tax exemption from public-university or non-profit status alone.
4. Route to the pertinent reference before calculating:
   - Business income, nonprofit purpose, tax adjustments, deductible versus non-deductible costs: references/corporate-tax.md.
   - Reserve under Corporate Tax Act Art. 29 and special treatment under Restriction of Special Taxation Act Art. 74: references/reserve-and-donations.md.
   - VAT on tuition, training, commissions, real-estate leases, licensing, mixed-use purchases, imports and overseas services: references/vat.md.
   - Payroll, honoraria and research costs: references/decision-matrix.md.
   - Authoritative evidence and security: references/authority-check.md.
5. Use the connected UpstageAI korean-tax-calc-mcp tools only after verifying the actual schema, supported period and legal applicability; use find_tool if uncertain. See references/tool-map.md. Tool output cannot itself establish legal characterization or the current law.

## 2. Special nonprofit reserve risk (required)

NTS guidance lists SNU among the entities addressed by Restriction of Special Taxation Act Art. 74; the published special 100% reserve treatment concerns **business years ending on or before 2028-12-31**, subject to law and deduction requirements at the relevant date. Verify current enacted law and transitional clauses every time. Do not transform the special deduction ceiling into automatic full tax exemption. Track booked amount, qualified income, reserve use, unused balance and recapture. Never assume 100% is an allowable booked amount or that any income is automatically taxable.

**Important upstream implementation risk:** the upstream nonprofit_reserve_limit calculator was observed to gate its special rate on year <= 2028 rather than on the business-year **ending date**. For SNU's hypothetical 2028-03-01 to 2029-02-28 year, a naive input of year=2028 could misclassify the sunset. Run scripts/periods.py and explicitly assess the ending date before calling this tool. If any clash arises, flag 'manual review required'; do not silently patch or trust the numeric output.

## 3. Computation and safety

- Inputs can be fictional or pseudonymized transaction attributes only; never send personal identifiers, bank details, real taxpayer IDs, contracts, faculty payroll, internal ledgers or third-party confidential information to external MCP/PDF services. Upstage PDF tools with an API key may transmit document content. Use local redaction and minimal data extraction.
- Do not connect to tax accounts or trigger filing, payment, journal posting or dispatch. Never expose official verdicts without current citations to articles, official guidance, effective dates and SNU institution rules where applicable.
- Missing entity, taxable-activity classification, reporting period, contract evidence, special reserve conditions or applicable law -> return **REVIEW REQUIRED** with missing facts instead of an unqualified tax figure.
- Preserve known zero as 0, unknown as unconfirmed and not-applicable as N/A. Show the calculation tool/version, assumptions and rounding. The scripts/reconcile.py helper checks arithmetic only, not tax applicability.

## 4. Required output (in Korean)

1. **Conclusion/status**: review required, conditional computation or checked computation (never claim official approval).
2. **Entity and periods**: entity/registration verified or not, SNU fiscal year, corporate-tax business year, VAT period, transaction date.
3. **Five-lens table**: accounting treatment; corporate tax; VAT; withholding; school/internal regulation. Mark each confirmed, conditional or unknown separately.
4. **Calculation and reconciliation**, only if justified: source facts, formulas, national/local tax, book-to-tax adjustments, evidence and filing/adjustment calendar.
5. **Authority trail**: governing provision, actual amendment/effective date, official URL, original tool name/version and unresolved conflicts.
6. **Next action**: supporting documents, accountant/corporate accounting team review and specific unresolved question. Keep final decision with responsible institution.

## 5. Resources and validation

- references/entity-periods.md: taxpayer separation and three calendars.
- references/corporate-tax.md: nonprofit income and book/tax reconciliations.
- references/reserve-and-donations.md: 100% sunset, 5-year use and evidence.
- references/vat.md: mixed taxable/exempt VAT and import/overseas services.
- references/tool-map.md: upstream tools and cautions.
- references/decision-matrix.md: research and honoraria secondary branch.
- references/example-cases.md: reference test cases.
- references/setup.md: optional MCP registration on macOS.
- scripts/periods.py: deterministic SNU fiscal-year and sunset-date precheck.
- scripts/reconcile.py: arithmetic verification after tax amounts are independently validated.

Execute python3 -m unittest discover -s scripts -p 'test_*.py' -v in the Skill root. These local tests do NOT constitute legal or integration verification against the current Upstage MCP.

Upstream license/source: https://github.com/UpstageAI/korean-tax-calc-mcp (MIT, copyright Upstage 2026); no upstream calculator code bundled. SNU law: https://www.law.go.kr/LSW/lsInfoP.do?lsId=011316 . NTS nonprofit guidance: https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7983&mi=6557 . This Skill is not officially endorsed by SNU.
