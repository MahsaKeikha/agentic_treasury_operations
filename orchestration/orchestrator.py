from AGENTS import authorization_agent, cash_agent, controls_agent, forecast_agent, liquidity_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "cash": cash_agent.run(case),
        "forecast": forecast_agent.run(case),
        "liquidity": liquidity_agent.run(case),
        "controls": controls_agent.run(case),
        "authorization": authorization_agent.run(case),
    }
    governance = authorize("release_treasury_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
