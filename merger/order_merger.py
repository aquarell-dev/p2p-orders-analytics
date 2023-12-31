import os
from datetime import date
from typing import List

import pandas as pd

from t.mergeable import Mergeable
from t.order import Order
from utils.utils import convert_us_datetime_to_date_object


def _get_orders(mergeable: Mergeable) -> List[Order]:
    file_path = os.path.join('files', mergeable.orders_file_path)

    df: pd.DataFrame = pd.ExcelFile(file_path).parse().reset_index()

    # drop those rows which status is not "completed"
    filtered_df = df[df[mergeable.configuration.status_column] == mergeable.configuration.completed_status_caption]

    orders: List[Order] = []

    for _, row in filtered_df.iterrows():
        order = Order(
            fiat_amount=float(row[mergeable.configuration.order_amount_column]),
            date_time=convert_us_datetime_to_date_object(str(row[mergeable.configuration.order_time_column])),
            order_type=str(row[mergeable.configuration.order_type_column]).lower()
        )

        orders.append(order)

    return orders

def merge(*args: Mergeable) -> List[Order]:
    """
    Takes order files from different exchanges and merges 'em into one single file

    :return: a list of all orders

    """
    orders = []

    for mergeable in args:
        orders += _get_orders(mergeable)

    return orders
    