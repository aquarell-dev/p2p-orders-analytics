from typing import Dict, List
import pandas as pd

from t.order import Order
from t.statistics import Statistics
from t.turnover import Turnover


class OrdersAnalytics:
	def __init__(self, orders: List[Order]) -> None:
		self._orders = orders

	def _get_orders_grouped_by_date(self) -> Dict[str, List[Order]]:
		grouped_orders = {}

		for order in self._orders:
			order_date_str = order.date_time.strftime('%d-%m-%Y')
			
			if order_date_str in grouped_orders:
				grouped_orders[order_date_str].append(order)
			else:
				grouped_orders[order_date_str] = [order]

		return grouped_orders
	
	def _get_turnover(self, orders: List[Order]) -> Turnover:
		total = 0
		buy = 0
		sell = 0

		for order in orders:
			amount = round(order.fiat_amount)

			total += amount

			if order.order_type == 'sell':
				sell += amount
			elif order.order_type == 'buy':
				buy += amount

		return Turnover(total_turnover=total, buy_turnover=buy, sell_turnover=sell)
	
	def _get_avg_spread(self, turnover: Turnover) -> float:
		if turnover.buy_turnover == 0: return -1

		spread = turnover.sell_turnover / turnover.buy_turnover - 1

		return round(spread * 100, 2)

	def analyze(self) -> List[Statistics]:
		grouped_orders = self._get_orders_grouped_by_date()
		stats = []

		for key, value in grouped_orders.items():
			turnover = self._get_turnover(value)

			stats.append(Statistics(
				date=key,
				turnover=turnover,
				avg_spread=self._get_avg_spread(turnover),
				profit=turnover.sell_turnover-turnover.buy_turnover
			))

		return stats
	
	def statistics_to_excel(self, statistics: List[Statistics]) -> None:
		df = pd.DataFrame.from_records([s.to_dict() for s in statistics])

		print(df)

		df.to_excel('output.xlsx')
		