import datetime
import os
from datetime import date
from parser.parser_base import OrderParserBase
from typing import List

import requests

from assets.assets import default_headers
from t.order import Order
from utils.utils import (convert_ru_date_to_timestamp,
                         convert_utc_timestamp_to_ru_date)


class BybitOrderParser(OrderParserBase):
	def __init__(self) -> None:
		super().__init__(os.getenv('BYBIT_USER_TOKEN'))

	_api_url = 'https://api2.bybit.com/fiat/otc/order/list'
	_completed_order_status = 50

	def _fetch_orders(self, start_time: date, end_time: date) -> dict:
		headers = {
			**default_headers,
			"UserToken": self._api_key 
		}

		data = {
			'beginTime': convert_ru_date_to_timestamp(start_time),
			'endTime': convert_ru_date_to_timestamp(end_time, True),
			'page': 1,
			'size': 10
		}

		try:
			response = requests.post(
				self._api_url,
				headers=headers,
				json=data
			)
		except Exception as e: # todo fix too broad exception clause
			raise RuntimeError('Error while getting Bybit orders', str(e))


		if response.status_code != 200:
			raise RuntimeError('Error while getting Bybit orders')
		
		return response.json()['result']['items']

	def get_orders(self, start_time: date, end_time: date = None) -> List[Order]:
		if end_time is None:
			end_time = date.today()

		response_orders = self._fetch_orders(start_time, end_time)
		
		orders: List[Order] = []

		for order in response_orders:
			if order['status'] != self._completed_order_status:
				continue

			orders.append(
				Order(
					fiat_amount=float(order['amount']),
					order_type='buy' if order['side'] == 0 else 'sell',
					date_time=convert_utc_timestamp_to_ru_date(int(order['createDate']) / 1000)
				)
			)

		return orders
