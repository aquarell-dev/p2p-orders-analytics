from exchange_analytics.analytics import OrdersAnalytics
from merger.order_merger import merge
from t.configuration import get_configuration_by_preset
from t.mergeable import Mergeable


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
	main()


