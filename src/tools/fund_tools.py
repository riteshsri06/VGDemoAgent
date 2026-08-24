import json

from langchain_core.tools import tool

from services.fund_service import FundService


fund_service = FundService()


@tool
def search_fund(ticker: str) -> str:
    """Check whether a fund or ETF ticker is available in Yahoo Finance."""
    print(f"Searching for fund: {ticker}")
    return json.dumps(fund_service.search_fund(ticker))


@tool
def get_fund_details(ticker: str) -> str:
    """Get ticker, name, AUM, expense ratio, and average annual return for a fund or ETF."""
    print(f"Getting fund details for: {ticker}")
    fund = fund_service.get_fund_details(ticker)
    if fund is None:
        return "Data not available for the requested fund or ETF."
    return json.dumps(fund.to_dict())


@tool
def compare_funds(tickers: list[str]) -> str:
    """Return factual side-by-side fund data for the supplied tickers; do not rank or recommend them."""
    print(f"Comparing funds: {tickers}")
    funds = fund_service.compare_funds(tickers)
    if not funds:
        return "Data not available for the requested fund or ETF."
    return json.dumps([fund.to_dict() for fund in funds])


FUND_TOOLS = [search_fund, get_fund_details, compare_funds]