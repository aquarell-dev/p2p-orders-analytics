import os
from datetime import date
from parser.parser_base import OrderParserBase
from typing import List

import requests

from assets.assets import default_headers
from t.order import Order


class HuobiOrderParser(OrderParserBase):
	def __init__(self) -> None:
		super().__init__(os.getenv('HUOBI_USER_TOKEN'))

	_api_url = 'https://www.huobi.com/-/x/otc/v1/trade/order/list'

	def _fetch_orders(self) -> dict:
		headers = {
			**default_headers,
			'token': self._api_key,
		}

		params = {
			'beginDate': 1693861200000,
			'endDate': 1694638800000,
			'orderStatus': 'completed',
			'orderType': 'c2c',
			'secondaryType': '',
			'side': 'all',
			'currPage': 1
		}

		response = requests.get(self._api_url, headers=headers, params=params)

		print(response.url)

		print(response.json())

	def get_orders(self, start_time: date, end_time: date = None) -> List[Order]:
		if end_time is None:
			end_time = date.today()

		self._fetch_orders()