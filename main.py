from datetime import date
from parser.bybit_parser import BybitOrderParser
from parser.huobi_parser import HuobiOrderParser

from dotenv import load_dotenv

from exchange_analytics.analytics import OrdersAnalytics
from merger.order_merger import merge
from t.configuration import get_configuration_by_preset
from t.mergeable import Mergeable
from utils.utils import convert_ru_date_to_timestamp

load_dotenv()

def main(): 
	orders = merge(
		Mergeable(
			orders_file_path='bybit.xls',
			configuration=get_configuration_by_preset('bybit')
		),
		Mergeable(
			orders_file_path='huobi.xlsx',
			configuration=get_configuration_by_preset('huobi')
		),
	)

	analytics = OrdersAnalytics(orders)

	statistics = analytics.analyze()

	analytics.statistics_to_excel(statistics)


if __name__ == '__main__':
	# b = BybitOrderParser()
	# b.get_orders(date(2023, 9, 12))
	h = HuobiOrderParser()
	h.get_orders(date(2023, 9, 12))

