from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("cash", "forecast", "liquidity", "controls", "authorization"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_treasury_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_treasury_support_package", approved_context())["allowed"] is True


def test_cash_position_gap_blocks():
    assert authorize("release_treasury_support_package", approved_context() | {"cash_position_gap": True})["allowed"] is False


def test_liquidity_risk_blocks():
    assert authorize("release_treasury_support_package", approved_context() | {"liquidity_funding_risk": True})["allowed"] is False


def test_payment_control_risk_blocks():
    assert authorize("release_treasury_support_package", approved_context() | {"payment_control_risk": True})["allowed"] is False


def test_fraud_security_risk_blocks():
    assert authorize("release_treasury_support_package", approved_context() | {"fraud_security_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
