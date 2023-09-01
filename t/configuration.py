from dataclasses import dataclass
import json


@dataclass(frozen=True)
class AnalyticsFileConfiguration:
	order_amount_column: str
	order_type_column: str
	completed_status_caption: str
	status_column: str
	order_time_column: str


def get_configuration_by_preset(exchange: str) -> AnalyticsFileConfiguration:
	with open('presets.json', 'r', encoding='utf-8') as f:
		data = json.load(f)[exchange]

	return AnalyticsFileConfiguration(
		order_amount_column=data['order_amount_column'],
		order_type_column=data['order_type_column'],
		completed_status_caption=data['completed_status_caption'],
		status_column=data['status_column'],
		order_time_column=data['order_time_column'],
	)