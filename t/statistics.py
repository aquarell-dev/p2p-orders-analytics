from dataclasses import dataclass

from .turnover import Turnover


@dataclass(frozen=True)
class Statistics:
    date: str
    turnover: Turnover
    avg_spread: float
    profit: int

    def to_dict(self) -> dict:
        return {
            "Дата": self.date,
            "Оборот, ₽": self.turnover.total_turnover,
            "Продажа, ₽": self.turnover.sell_turnover,
            "Закуп, ₽": self.turnover.buy_turnover,
            "Ср. Спред, %": self.avg_spread,
            "Профит, ₽": self.profit,
        }