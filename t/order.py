from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Order:
    fiat_amount: float
    date_time: date
    order_type: str
