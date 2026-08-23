"""Fail-closed governance for F158 Agentic Treasury Operations."""

PROTECTED_ACTIONS = {
    "move_or_transfer_funds",
    "release_or_approve_payment",
    "change_bank_account_or_signatory",
    "execute_hedge_or_investment",
    "draw_or_repay_borrowing",
    "override_treasury_risk_or_control_limit",
}

REQUIRED_REVIEWS = (
    "cash_position_reviewed",
    "forecast_reviewed",
    "liquidity_stress_reviewed",
    "payment_control_reviewed",
    "fraud_security_reviewed",
    "counterparty_market_risk_reviewed",
    "compliance_sanctions_reviewed",
    "qualified_treasury_authorization",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "fund movement, payment release, bank-account change, hedging, investment, borrowing, or control override is outside autonomous treasury authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required treasury review", "missing": missing}
    checks = {
        "cash_position_gap": "material bank balance, ledger, restricted cash, settlement, trapped cash, currency, or reconciliation issue unresolved",
        "forecast_uncertainty_gap": "material forecast assumption, timing, variance, scenario, collection, disbursement, or data-quality issue unresolved",
        "liquidity_funding_risk": "material liquidity buffer, funding concentration, covenant, maturity, collateral, market-access, or stress issue unresolved",
        "payment_control_risk": "material beneficiary, invoice, amount, bank instruction, dual-control, approval, segregation-of-duties, or payment-process issue unresolved",
        "fraud_security_risk": "material business-email compromise, account takeover, credential compromise, payment diversion, social engineering, or cyber concern unresolved",
        "counterparty_market_risk": "material counterparty, bank concentration, FX, rate, investment, hedge, valuation, collateral, or market-risk issue unresolved",
        "compliance_sanctions_risk": "material sanctions, AML, restricted-party, legal-entity, policy, regulatory, tax, or compliance concern unresolved",
        "provenance_documentation_gap": "cash, forecast, payment, bank instruction, risk, hedge, investment, borrowing, approval, or decision provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "treasury governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "treasury operations support package approved after qualified human authorization"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
