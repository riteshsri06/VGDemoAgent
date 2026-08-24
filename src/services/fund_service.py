from __future__ import annotations

from typing import Any

import yfinance as yf

from models import Fund


class FundService:
    """Small Yahoo Finance adapter used by the demo tools."""

    def search_fund(self, ticker: str) -> dict[str, Any]:
        symbol = self._normalize_ticker(ticker)
        if not symbol:
            return {"found": False, "message": "A ticker is required."}

        try:
            info = yf.Ticker(symbol).info
            name = info.get("longName") or info.get("shortName")
            if not name:
                return {"found": False, "message": "Data not available for the requested fund or ETF."}
            return {"found": True, "ticker": symbol, "fund_name": name}
        except Exception:
            return {"found": False, "message": "Data not available for the requested fund or ETF."}

    def get_fund_details(self, ticker: str) -> Fund | None:
        symbol = self._normalize_ticker(ticker)
        if not symbol:
            return None

        try:
            info = yf.Ticker(symbol).info
            name = info.get("longName") or info.get("shortName")
            if not name:
                return None

            return Fund(
                ticker=symbol,
                fund_name=name,
                aum=self._number(info.get("totalAssets")),
                expense_ratio=self._number(
                    info.get("annualReportExpenseRatio", info.get("netExpenseRatio"))
                ),
                average_return=self._average_annual_return(symbol),
            )
        except Exception:
            return None

    def compare_funds(self, tickers: list[str]) -> list[Fund]:
        funds = []
        for ticker in tickers:
            fund = self.get_fund_details(ticker)
            if fund is not None:
                funds.append(fund)
        return funds

    @staticmethod
    def _normalize_ticker(ticker: str) -> str:
        return ticker.strip().upper() if isinstance(ticker, str) else ""

    @staticmethod
    def _number(value: Any) -> float | None:
        return float(value) if isinstance(value, (int, float)) else None

    @staticmethod
    def _average_annual_return(ticker: str) -> float | None:
        history = yf.Ticker(ticker).history(period="5y", auto_adjust=False)
        if history.empty or "Adj Close" not in history:
            return None
        annual_prices = history["Adj Close"].resample("YE").last().dropna()
        annual_returns = annual_prices.pct_change().dropna()
        return float(annual_returns.mean()) if not annual_returns.empty else None