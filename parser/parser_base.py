from datetime import date
from typing import List

from t.order import Order


class OrderParserBase:
	def __init__(self, api_key: str) -> None:
		self._api_key = api_key

	_time_format = '%d-%m-%Y'

	def get_orders(self, start_time: date, end_time: date = None) -> List[Order]:
		raise NotImplementedError
