# F158 | Agentic Treasury Operations | L3 Gold Standard | v1.0

A governed five-agent reference architecture for treasury operations support across cash visibility, forecasting, liquidity, funding, payment controls, fraud prevention, banking relationships, counterparty risk, market risk, compliance, provenance, and qualified human authorization.

F158 is a treasury decision-support system. It is not a bank portal, payment rail, dealer platform, investment manager, borrowing authority, settlement engine, custodian, or autonomous treasurer. It cannot move or transfer funds, release or approve payments, change bank accounts or signatories, execute hedges or investments, draw or repay borrowing, or override treasury risk or control limits.

## Treasury lifecycle

```text
Cash and Bank Position
        -> Forecast and Working Capital View
        -> Liquidity and Funding Analysis
        -> Payment, Fraud, Counterparty, and Market-Risk Review
        -> Compliance and Control Review
        -> Qualified Treasury Authorization
        -> Human-Controlled Treasury Action
```

The workflow fails closed when required reviews are missing or when material cash-position, forecast, liquidity, payment-control, fraud, counterparty, market-risk, sanctions, compliance, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Cash Agent | Organizes bank balances, ledger cash, restricted cash, settlement items, currency, legal entity, account ownership, and reconciliation | What cash is actually available, where is it, and under what restrictions? |
| Forecast Agent | Builds short-, medium-, and long-horizon cash forecasts using collections, disbursements, payroll, tax, debt, capex, financing, and scenario assumptions | What cash movements are expected and how uncertain are they? |
| Liquidity Agent | Reviews buffers, funding sources, maturities, covenants, collateral, concentration, trapped cash, stress conditions, and contingency liquidity | Can obligations be met under normal and stressed conditions? |
| Controls Agent | Reviews payment controls, dual authorization, bank instructions, fraud risk, sanctions, counterparty exposure, segregation of duties, and policy limits | Are treasury actions sufficiently controlled and compliant? |
| Authorization Agent | Synthesizes cash, forecast, liquidity, risk, controls, compliance, and evidence for accountable human treasury approval | Is the support package complete enough for an authorized treasury professional to act? |

## Repository structure

```text
AGENTS/
├── cash_agent.py
├── forecast_agent.py
├── liquidity_agent.py
├── controls_agent.py
└── authorization_agent.py

SKILLS/
├── cash_reasoning.py
├── forecast_reasoning.py
├── liquidity_reasoning.py
├── control_reasoning.py
└── authorization_reasoning.py

TOOLS/
├── cash_registry.py
├── forecast_matrix.py
├── liquidity_stress.py
├── control_checklist.py
└── payment_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Treasury operating model

Treasury should connect cash, legal entities, bank accounts, forecast, liquidity, debt, investments, payments, market exposures, counterparties, controls, approvals, accounting, and risk limits. F158 supports this analysis while preserving human-only authority over actual transactions.

## Cash architecture

The executable policy requires `cash_position_reviewed`. `cash_position_gap` blocks release when material bank balance, ledger, restricted cash, settlement, trapped cash, currency, or reconciliation issues remain unresolved.

`TOOLS/cash_registry.py` can preserve legal entity, bank, account, currency, balance type, value date, statement date, ledger balance, available balance, restriction, owner, source, and reconciliation state.

## Bank balances

Treasury should distinguish bank-reported balances, general-ledger balances, available balances, collected funds, pending settlements, restricted cash, pledged cash, and trapped cash.

## Reconciliation

Bank-to-ledger reconciliation should identify timing items, unidentified transactions, duplicate postings, fees, returned payments, stale checks, settlement differences, and unresolved exceptions.

F158 must not fabricate reconciling items merely to force a balance.

## Restricted cash

Restricted, pledged, escrowed, regulated, covenant-restricted, customer, trust, or legally segregated cash should not be treated as freely available liquidity.

## Trapped cash

Cash can be economically or legally difficult to move because of capital controls, tax, regulatory requirements, local obligations, minority interests, sanctions, bank constraints, or legal-entity restrictions.

## Legal entities

Treasury actions should preserve the legal entity that owns cash, owes obligations, holds debt, enters hedges, or maintains bank accounts. Group-level cash should not erase entity-level rights and restrictions.

## Bank account inventory

An authoritative account inventory can include bank, account identifier, legal owner, currency, purpose, signatories, electronic entitlements, payment capabilities, limits, service type, status, and last review.

## Bank-account governance

`change_bank_account_or_signatory` is protected. Opening, closing, modifying, or changing signatories or entitlements requires authorized human action and bank-approved procedures.

## Cash concentration

Treasury can use physical pooling, notional pooling, sweeps, zero-balance arrangements, intercompany funding, and other structures where legally and operationally appropriate.

F158 can analyze structures but cannot initiate cash concentration transfers.

## In-house banking

In-house bank structures can centralize payments, collections, FX, intercompany funding, and netting. They require careful legal-entity, accounting, tax, regulatory, banking, and control design.

## Forecast architecture

The executable policy requires `forecast_reviewed`. `forecast_uncertainty_gap` blocks release when material forecast assumptions, timing, variance, scenarios, collections, disbursements, or data-quality issues remain unresolved.

`TOOLS/forecast_matrix.py` can preserve date, entity, currency, category, source, expected amount, probability or confidence where appropriate, scenario, actual amount, variance, owner, and update time.

## Forecast horizons

Treasury can use daily, weekly, 13-week, monthly, quarterly, annual, and strategic horizons. Detail and certainty should generally decrease with longer horizons.

## Receipts

Forecast receipts can include customer collections, asset sales, financing, investment maturities, tax refunds, insurance proceeds, intercompany flows, and other expected inflows.

## Disbursements

Forecast disbursements can include suppliers, payroll, taxes, debt service, capex, acquisitions, dividends, rent, insurance, benefits, intercompany transfers, and operating expenses.

## Forecast timing

Invoice due date does not always equal cash date. Payment behavior, collection patterns, weekends, bank holidays, settlement cutoffs, payroll dates, tax dates, and approval timing can affect actual cash movement.

## Forecast variance

Variance analysis should separate timing variance, amount variance, missing flows, new events, forecast bias, and classification errors.

## Forecast bias

Persistent optimism or conservatism should be measured and corrected where appropriate. A forecast should not be adjusted solely to support a preferred funding decision.

## Scenario forecasting

Base, downside, severe downside, upside, acquisition, disruption, refinancing, customer-loss, commodity, FX, rate, and other scenarios can support planning.

## Working capital

Treasury can analyze receivables, payables, inventory, customer terms, supplier terms, collections, payment timing, and working-capital programs while coordinating with finance, procurement, sales, and operations.

## Receivables

Collections risk can include customer concentration, aging, disputes, credit deterioration, payment method, geography, seasonality, and operational delays.

## Payables

Payment timing should respect contractual, legal, supplier, discount, operational, and relationship considerations. F158 should not recommend withholding legitimate payments merely to inflate cash balances.

## Supply-chain finance

Supplier-finance arrangements can affect liquidity, accounting presentation, disclosure, supplier resilience, and counterparty exposure. Structure and disclosure require qualified review.

## Liquidity architecture

The executable policy requires `liquidity_stress_reviewed`. `liquidity_funding_risk` blocks release when material liquidity buffers, funding concentration, covenant, maturity, collateral, market-access, or stress issues remain unresolved.

`TOOLS/liquidity_stress.py` can support scenario analysis across opening liquidity, operating cash flows, debt maturities, committed facilities, collateral, investments, contingencies, and severe but plausible outflows.

## Liquidity buffer

A liquidity buffer can include unrestricted cash, highly liquid investments, committed facilities, and other reliable sources subject to haircuts, availability conditions, legal-entity access, and stress assumptions.

## Minimum liquidity

Minimum liquidity requirements should be linked to operating needs, volatility, access to markets, legal-entity constraints, covenants, ratings, seasonality, and stress scenarios.

## Funding sources

Funding can include operating cash, revolving credit, term loans, commercial paper, bonds, securitization, factoring, equity, intercompany funding, and asset monetization.

F158 analyzes funding and does not execute borrowing.

## Borrowing boundary

`draw_or_repay_borrowing` is protected. Drawing facilities, issuing debt, repaying debt, changing borrowing terms, or making binding lender commitments requires authorized human action.

## Debt maturity profile

Treasury should track principal, interest, maturity, currency, rate basis, call or put features, covenants, collateral, guarantees, and refinancing windows.

## Covenant management

Covenant calculations should use controlled definitions and reconciled financial inputs. Forecast headroom and cure options should be explicit.

## Refinancing risk

Refinancing depends on maturity timing, market conditions, credit quality, ratings, covenant performance, lender appetite, collateral, and access to capital markets.

## Committed versus uncommitted facilities

Uncommitted lines should not be treated as equivalent to legally committed liquidity.

## Collateral

Collateral availability, eligibility, valuation, haircut, perfection, concentration, and encumbrance can affect funding capacity.

## Liquidity stress testing

Stress tests can combine revenue decline, delayed collections, supplier acceleration, margin calls, rating downgrade, facility loss, cyber disruption, acquisition, litigation, tax, and market closure.

## Reverse liquidity stress

Reverse stress testing asks what combination of events would cause a liquidity shortfall, covenant breach, inability to settle, or emergency funding need.

## Contingency funding plan

A contingency funding plan can define indicators, escalation, sources, priorities, communications, restrictions, legal-entity actions, and executive approvals.

F158 can support preparation but cannot activate funding actions autonomously.

## Payments architecture

The executable policy requires `payment_control_reviewed`. `payment_control_risk` blocks release when material beneficiary, invoice, amount, bank instruction, dual-control, approval, segregation-of-duties, or payment-process issues remain unresolved.

## Payment lifecycle

A controlled payment workflow can include request, evidence, vendor validation, invoice verification, accounting approval, treasury review, sanctions screening, bank instruction preparation, independent authorization, release, settlement, reconciliation, and exception handling.

## Payment boundary

`move_or_transfer_funds` and `release_or_approve_payment` are protected. F158 must never execute or approve payments autonomously.

## Dual control

High-risk payment processes should separate preparation from approval and, where required, approval from release.

## Segregation of duties

The same individual or autonomous process should not create a beneficiary, enter a payment, approve it, release it, and reconcile it without independent controls.

## Beneficiary changes

Changes to bank details are high risk. Institution-approved callback or out-of-band verification processes should be used where required.

## Invoice fraud

Payment requests should be checked for duplicate invoices, altered instructions, suspicious timing, changed beneficiaries, mismatched entities, unusual amounts, and inconsistent supporting documents.

## Business email compromise

The executable policy requires `fraud_security_reviewed`. `fraud_security_risk` blocks release when material BEC, account takeover, credential compromise, payment diversion, social engineering, or cyber concerns remain unresolved.

## Social engineering

Urgency, secrecy, executive impersonation, vendor impersonation, legal-threat language, and unusual process bypass requests can be fraud indicators.

F158 should favor verification over urgency when controls conflict with a payment request.

## Credentials

F158 should not store or request bank passwords, payment tokens, hardware-token secrets, private keys, full authentication answers, or other secrets capable of moving funds.

## Bank portals

A reference implementation should not require production bank credentials with payment authority.

## Fraud recovery

Recall, freeze, bank notification, law-enforcement contact, cyber response, insurer notification, and incident escalation can be time critical after suspected payment fraud. Actual external actions require authorized personnel.

## Counterparty architecture

The executable policy requires `counterparty_market_risk_reviewed`. `counterparty_market_risk` blocks release when material bank, counterparty, FX, rate, investment, hedge, valuation, collateral, or market-risk issues remain unresolved.

## Bank counterparty risk

Treasury can monitor bank credit quality, exposures, deposits, investments, derivatives, operational dependency, clearing dependency, geographic concentration, and service concentration.

## Counterparty limits

Limits should be defined by policy and approved human governance. F158 cannot override them.

## Investment of surplus cash

Treasury investments can involve deposits, money-market instruments, government securities, funds, commercial paper, certificates, and other policy-permitted assets.

`execute_hedge_or_investment` is protected.

## Investment objectives

Corporate cash investment policies often prioritize preservation of principal, liquidity, diversification, and yield in that order or another approved hierarchy.

## Investment policy

Policy can define permitted instruments, ratings, maturities, duration, concentration, counterparties, currencies, liquidity, and approval limits.

## Credit risk

Issuer and counterparty credit risk should consider exposure, maturity, collateral, concentration, ratings, market signals, and internal analysis where available.

## Market risk

Treasury market risk can include foreign exchange, interest rates, commodity exposure, basis risk, volatility, and investment-price risk.

## FX exposure

Exposure can arise from transactions, forecasts, balance sheets, debt, investments, intercompany positions, acquisitions, and foreign subsidiaries.

## FX risk identification

Treasury should distinguish booked exposure, forecast exposure, translation exposure, economic exposure, and structural exposure.

## Hedging

Hedging can use forwards, swaps, options, natural offsets, netting, debt, pricing, and operational measures under approved policy.

F158 can analyze hedge alternatives but cannot transact.

## Hedge objectives

A hedge should identify exposure, objective, horizon, notional, instrument, accounting considerations, counterparty, policy authority, effectiveness measures, and residual risk.

## Over-hedging

Forecast uncertainty can create over-hedging when expected exposures do not occur. Hedge ratios should account for confidence and policy limits.

## Interest-rate risk

Treasury can analyze fixed versus floating debt, refinancing, investments, swaps, duration, repricing, benchmark transition, and sensitivity to rate changes.

## Commodity risk

Some organizations hedge energy, metals, agriculture, fuel, or other inputs. Hedging must follow approved mandate and specialist review.

## Derivatives governance

Derivative activity can create counterparty, collateral, liquidity, valuation, legal, accounting, basis, and operational risk. Confirmations and master agreements require authorized review.

## Hedge accounting

Accounting designation, effectiveness, documentation, OCI treatment, fair value, and discontinuation can require qualified accounting professionals. F158 does not certify hedge-accounting treatment.

## Valuation

Derivative and investment valuations should preserve pricing source, timestamp, model, market inputs, independent price verification where required, and unresolved differences.

## Collateral and margin

Derivative collateral and margin calls can create liquidity stress. F158 can forecast them but cannot post collateral autonomously.

## Compliance and sanctions architecture

The executable policy requires `compliance_sanctions_reviewed`. `compliance_sanctions_risk` blocks release when material sanctions, AML, restricted-party, legal-entity, policy, regulatory, tax, or compliance concerns remain unresolved.

## Sanctions

Payments, counterparties, banks, beneficiaries, owners, geographies, and currencies can require screening according to applicable law and policy.

F158 does not independently clear sanctions alerts.

## AML and financial crime

Treasury should coordinate with authorized compliance functions for suspicious payment patterns, unusual counterparties, source-of-funds concerns, or transactions requiring enhanced review.

## Tax

Cross-border cash movements, intercompany loans, pooling, withholding, investments, and financing can create tax consequences. F158 can flag tax review requirements but does not provide binding tax conclusions.

## Legal agreements

Banking, credit, derivatives, investment, guarantee, security, intercompany, and cash-pooling agreements require authorized legal review where applicable.

## Policy limits

Treasury policies can define authorities, bank limits, counterparty limits, instrument eligibility, maturities, liquidity minimums, FX limits, hedge ratios, debt limits, and escalation thresholds.

`override_treasury_risk_or_control_limit` is protected.

## Authorization architecture

The executable policy requires `qualified_treasury_authorization`. Human authorization should verify the request, evidence, entity, amount, currency, beneficiary or counterparty, authority, risk, compliance, policy, and downstream action.

## Approval matrices

Approval thresholds can depend on amount, instrument, entity, currency, risk, transaction type, counterparty, urgency, and policy.

## Delegated authority

Authority should be documented, current, scoped, and revocable. F158 does not infer authority from job title alone.

## Board and executive authority

Debt, major investments, acquisitions, large hedges, guarantees, capital actions, and other material treasury decisions can require executive or board approval.

## No autonomous execution

Passing all F158 governance reviews means only that a support package can be released for human treasury action. It never means the underlying transaction is authorized or executed.

## Cash pooling and intercompany funding

Intercompany balances should be documented with legal entity, currency, terms, interest, maturity, tax, accounting, regulatory, and transfer-pricing considerations where applicable.

## Netting

Payment and FX netting can reduce settlement volume and exposure but requires controlled cutoffs, legal entity mapping, currency rules, counterparty agreement, and reconciliation.

## Payment factories

Centralized payment structures require strong entitlement, master-data, segregation, sanction-screening, file-integrity, approval, bank-connectivity, and reconciliation controls.

## Bank connectivity

Host-to-host, APIs, SWIFT, file transfer, EBICS, bank portals, and other channels require authentication, encryption, entitlement, signing, nonrepudiation, monitoring, and incident response.

F158 should not expose production credentials or weaken payment security.

## SWIFT and messaging

Financial messages can create binding consequences. F158 can organize message requirements but cannot transmit live payment or treasury instructions.

## Payment files

Files should be controlled for source, integrity, beneficiary data, amounts, currency, duplicate detection, approvals, encryption, signing, transmission, acknowledgment, and reconciliation.

## Treasury management systems

TMS platforms can centralize cash, debt, investments, derivatives, accounting, payments, bank accounts, forecasts, and risk. Integrations should use least privilege and segregation of duties.

## ERP integration

ERP, accounts payable, accounts receivable, payroll, tax, procurement, and accounting data can feed treasury. Interface failures should be monitored and reconciled.

## Master data

Bank accounts, vendors, beneficiaries, counterparties, legal entities, currencies, settlement instructions, and signatories are sensitive master data requiring controlled change processes.

## Reconciliation controls

Payments, receipts, bank statements, debt, investments, derivatives, interest, fees, and intercompany balances should reconcile to source systems and accounting records.

## Accounting interface

Treasury accounting can include cash, debt, interest, derivatives, investments, FX, bank fees, intercompany, and realized or unrealized gains and losses. F158 does not replace qualified accounting review.

## Close process

Month-end and quarter-end treasury close can include confirmations, bank reconciliations, valuations, interest accruals, debt balances, covenant calculations, cash classification, hedge accounting, and disclosures.

## Audit evidence

Audit evidence should be genuine and traceable. F158 must not manufacture bank confirmations, approvals, reconciliations, valuations, or control evidence.

## Business continuity

Treasury continuity should address payment capability, bank access, staffing, alternate channels, fraud risk, liquidity, market access, settlement, cyber incidents, and emergency authorization procedures.

Emergency procedures should not eliminate dual control unless formally approved and appropriately mitigated.

## Bank outage

A bank, portal, payment rail, or communications outage can create liquidity and settlement risk. Alternate methods should be preapproved rather than improvised with weak controls.

## Cyber incident

Treasury cyber incidents can involve credential theft, BEC, ransomware, bank connectivity, data compromise, payment diversion, and operational shutdown. F158 supports defensive coordination only.

## Settlement risk

Settlement timing differences can create principal, counterparty, intraday liquidity, and operational risk.

## Intraday liquidity

Organizations with high payment volumes may need to monitor timing of receipts, payments, collateral, and clearing obligations within the day.

## Cash investments and maturity ladders

Investment maturity schedules should align with expected cash needs and stress liquidity requirements.

## Concentration

Treasury concentration can occur by bank, counterparty, country, currency, funding source, maturity, investment issuer, payment channel, or technology provider.

## Ratings

External ratings can be useful inputs but should not be the sole counterparty-risk measure.

## Bank failures and resolution

Treasury should understand deposit protection where relevant, legal entity exposure, operational dependencies, sweep structures, custody, investment ownership, and contingency access.

## Sovereign and country risk

Cash and bank accounts can be exposed to capital controls, currency restrictions, sovereign stress, expropriation, bank instability, or payment-system disruption.

## Currency convertibility

Not all currencies are freely convertible or transferable. Local legal, regulatory, market, and banking conditions can constrain treasury action.

## Forecast and actual currency

Forecasts should distinguish transaction currency, functional currency, reporting currency, and exchange-rate assumptions.

## Treasury KPIs

Potential metrics include forecast accuracy, liquidity buffer, cash concentration, bank concentration, payment exception rate, fraud losses, return on permitted cash, debt maturity profile, covenant headroom, hedge ratio, FX variance, and control exceptions.

Metrics should not encourage unsafe optimization, such as minimizing idle cash below prudent liquidity levels.

## Monitoring and alerts

Monitoring can include low liquidity, unexpected outflows, failed payments, duplicate payments, changed bank details, unusual payment amounts, counterparty deterioration, FX limits, rate exposure, covenant headroom, fraud indicators, and sanctions escalation.

## Incident logs

Treasury incidents should preserve event, amount, entity, systems, bank or counterparty, control failure, customer or supplier impact, recovery, root cause, owner, actions, and lessons learned.

## Provenance

`provenance_documentation_gap` blocks release when cash, forecast, payment, bank instruction, risk, hedge, investment, borrowing, approval, or decision provenance is incomplete.

F158 must never fabricate balances, forecasts, bank instructions, signatory authority, payment approvals, hedge confirmations, investment trades, debt transactions, sanctions clearance, counterparty limits, valuations, or settlement status.

## Memory and state

The `memory/` layer can preserve cash positions, account inventory, forecasts, liquidity assumptions, debt, investments, exposures, counterparties, controls, approvals, payment cases, hedge proposals, limits, incidents, and unresolved questions.

Sensitive bank and transaction data should be minimized and access controlled.

## Observability

The `observability/` layer supports traceability across cash freshness, reconciliation, forecast changes, liquidity stress, payment controls, fraud flags, counterparty exposures, market risks, compliance reviews, approvals, and protected-action attempts.

Useful telemetry includes stale statements, unreconciled cash, forecast bias, liquidity breaches, covenant headroom, changed beneficiaries, payment exceptions, unusual instructions, counterparty limit usage, sanctions-review state, and authorization status.

## Required reviews

The executable policy requires all eight conditions:

```text
cash_position_reviewed
forecast_reviewed
liquidity_stress_reviewed
payment_control_reviewed
fraud_security_reviewed
counterparty_market_risk_reviewed
compliance_sanctions_reviewed
qualified_treasury_authorization
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- bank balance, ledger, restricted cash, settlement, trapped cash, currency, or reconciliation issues remain unresolved
- forecast assumptions, timing, variance, scenarios, collections, disbursements, or data quality remain unresolved
- liquidity buffer, funding concentration, covenant, maturity, collateral, market access, or stress issues remain unresolved
- beneficiary, invoice, amount, bank instruction, dual control, approval, segregation, or payment-process issues remain unresolved
- BEC, account takeover, credential compromise, payment diversion, social engineering, or cyber concerns remain unresolved
- counterparty, bank concentration, FX, rate, investment, hedge, valuation, collateral, or market-risk issues remain unresolved
- sanctions, AML, restricted-party, legal-entity, policy, regulatory, tax, or compliance concerns remain unresolved
- cash, forecast, payment, bank instruction, risk, hedge, investment, borrowing, approval, or decision provenance is incomplete
- any required review is missing
- qualified treasury authorization is missing

The system exposes blockers rather than manufacturing balances, liquidity, authority, payment legitimacy, sanctions clearance, hedge suitability, counterparty approval, or settlement certainty.

## Protected actions

```text
move_or_transfer_funds
release_or_approve_payment
change_bank_account_or_signatory
execute_hedge_or_investment
draw_or_repay_borrowing
override_treasury_risk_or_control_limit
```

These remain outside autonomous authority even after every required review passes.

## Human authority boundaries

F158 must not autonomously transfer money, release payments, modify bank accounts, change signatories, enter trades, execute hedges, invest cash, draw debt, repay debt, move collateral, override limits, clear sanctions issues, or represent a treasury transaction as authorized when human approval is missing.

Authorized treasury professionals, finance leaders, bank signatories, payment approvers, dealers, investment authorities, compliance officers, legal counsel, accounting professionals, risk managers, executives, and boards retain their respective authority.

## Explicit failure states

```text
CASH POSITION REVIEW REQUIRED
FORECAST REVIEW REQUIRED
LIQUIDITY STRESS REVIEW REQUIRED
PAYMENT CONTROL REVIEW REQUIRED
FRAUD AND SECURITY REVIEW REQUIRED
COUNTERPARTY AND MARKET RISK REVIEW REQUIRED
COMPLIANCE AND SANCTIONS REVIEW REQUIRED
QUALIFIED TREASURY AUTHORIZATION REQUIRED
CASH POSITION GAP
FORECAST UNCERTAINTY GAP
LIQUIDITY OR FUNDING RISK
PAYMENT CONTROL RISK
FRAUD OR SECURITY RISK
COUNTERPARTY OR MARKET RISK
COMPLIANCE OR SANCTIONS RISK
PROVENANCE DOCUMENTATION GAP
FUND MOVEMENT PROHIBITED
PAYMENT RELEASE OR APPROVAL PROHIBITED
BANK ACCOUNT OR SIGNATORY CHANGE PROHIBITED
HEDGE OR INVESTMENT EXECUTION PROHIBITED
BORROWING DRAW OR REPAYMENT PROHIBITED
TREASURY RISK OR CONTROL OVERRIDE PROHIBITED
```

## End-to-end reference workflow

1. Load legal entities, bank accounts, currencies, balances, ledger positions, restrictions, bank statements, and reconciliation status.
2. Produce short- and medium-term forecasts from receivables, payables, payroll, taxes, capex, debt, investments, financing, and scenario assumptions.
3. Reconcile forecast versus actual and expose timing, amount, missing-flow, and structural forecast bias.
4. Assess unrestricted liquidity, committed facilities, debt maturities, covenants, collateral, trapped cash, funding concentration, and contingency capacity.
5. Run severe but plausible liquidity scenarios and reverse stress tests.
6. Review payment requests for beneficiary, invoice, bank instruction, amount, currency, entity, approvals, dual control, segregation, fraud, and sanctions risk.
7. Review bank, counterparty, investment, FX, rate, hedge, collateral, valuation, and concentration risks against approved policy limits.
8. Review legal, tax, accounting, AML, sanctions, policy, regulatory, and contractual dependencies.
9. Preserve provenance for cash, forecast, payment, bank instruction, risk, hedge, investment, debt, approval, and decision evidence.
10. Apply fail-closed governance and require qualified treasury authorization.
11. Route the reviewed support package to the correct human authority.
12. Keep all fund movement, payment release, account changes, hedging, investing, borrowing, and limit overrides outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test cash-position integrity, reconciliation discipline, forecast quality, variance analysis, liquidity stress, covenant awareness, payment-control reasoning, BEC resistance, sanctions escalation, counterparty and market risk, segregation of duties, provenance, and protected-action boundaries.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved treasury-support release, cash-position gaps, forecast uncertainty, liquidity-funding risks, payment-control risks, fraud-security risks, counterparty-market risks, compliance-sanctions risks, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent treasury workflow.

## Reproducibility

A reproducible treasury decision-support case should preserve as-of time, entity, currency, bank and ledger source, reconciliation status, forecast version, assumptions, liquidity inputs, debt and investment state, counterparty exposure, risk limits, payment evidence, approvals, compliance findings, and unresolved issues.

## Extension points

Organization-specific implementations can add governed integrations for TMS platforms, ERP, bank statements, bank-account management, market-data systems, debt systems, investment systems, derivative platforms, sanctions screening, payment factories, SWIFT gateways, bank APIs, forecasting systems, and accounting platforms.

Any integration capable of moving funds, changing bank master data, releasing payments, executing trades, drawing debt, moving collateral, or overriding limits should remain behind explicit authorization, least privilege, segregation of duties, strong authentication, dual control, audit logging, transaction limits, and accountable human execution.

## Example applications

Potential governed uses include daily cash positioning, 13-week cash forecasting, liquidity planning, debt maturity review, covenant monitoring, counterparty-limit reporting, payment-risk review, bank-account inventory, working-capital analysis, FX exposure analysis, hedge proposal review, treasury control assessment, contingency funding planning, and treasury quality assurance.

F158 is not an autonomous treasurer, bank signatory, payment approver, dealer, investment manager, borrower, lender, custodian, settlement engine, compliance officer, or cash-movement system.

## Design principles

1. Ground treasury decisions in reconciled cash, legal-entity ownership, current bank data, and explicit restrictions.
2. Treat forecast uncertainty, liquidity stress, funding concentration, covenants, collateral, and trapped cash as first-class treasury risks.
3. Protect payment master data, dual control, segregation of duties, beneficiary verification, sanctions review, and fraud controls.
4. Treat BEC, social engineering, credential compromise, and urgent requests to bypass controls as high-risk events.
5. Never fabricate balances, bank instructions, payment approvals, hedge trades, investments, debt transactions, sanctions clearance, or settlement status.
6. Preserve counterparty, bank, currency, rate, investment, hedge, and concentration risk within approved human-defined limits.
7. Fail closed when cash, forecast, liquidity, payments, fraud, market risk, compliance, provenance, or qualified authorization is incomplete.
8. Use least privilege, strong authentication, dual control, reconciliation, and auditability for any downstream treasury integration.
9. Keep all movement of money, bank-account changes, trading, borrowing, investing, hedging, and control overrides under accountable human authority.

## Scope statement

F158 demonstrates a governed multi-agent architecture for treasury operations support. It combines specialized cash, forecast, liquidity, controls, and authorization agents with deterministic cash, forecast, stress, control, and payment-gate tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over payments, cash transfers, banking changes, borrowing, investments, derivatives, collateral, and treasury risk limits.

Author: Mahsa Keikha
