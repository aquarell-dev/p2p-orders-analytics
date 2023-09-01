from dataclasses import dataclass


@dataclass(frozen=True)
class Turnover:
    total_turnover: int 
    sell_turnover: int
    buy_turnover: int