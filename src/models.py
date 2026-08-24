from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class Fund:
    ticker: str
    fund_name: str | None
    aum: float | None
    expense_ratio: float | None
    average_return: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)