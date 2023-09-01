from dataclasses import dataclass
from .configuration import AnalyticsFileConfiguration


@dataclass(frozen=True)
class Mergeable:
    orders_file_path: str
    configuration: AnalyticsFileConfiguration
