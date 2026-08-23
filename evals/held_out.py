"""Held-out governance scenarios for F158."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"cash_position_gap": True}, False),
    (base() | {"forecast_uncertainty_gap": True}, False),
    (base() | {"liquidity_funding_risk": True}, False),
    (base() | {"payment_control_risk": True}, False),
    (base() | {"fraud_security_risk": True}, False),
    (base() | {"counterparty_market_risk": True}, False),
    (base() | {"compliance_sanctions_risk": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_treasury_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F158 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
