from datetime import datetime
from dateutil.relativedelta import relativedelta
from enum import Enum
from pkgs.mongodb.mongodb import *


class RecordsDatetimeFilterEnum(Enum):
    one_days = "1d"
    seven_days = "7d"
    one_month = "1month"
    three_months = "3months"
    six_months = "6months"
    one_year = "1year"


def get_datetime_filter_records(mongo: Type4DB, filter: RecordsDatetimeFilterEnum, filter_datetime: str):
    if filter == None:
        filter = RecordsDatetimeFilterEnum.seven_days
    filter_offset_dict = {
        filter.one_days: relativedelta(days=1),
        filter.seven_days: relativedelta(days=7),
        filter.one_month: relativedelta(months=1),
        filter.three_months: relativedelta(months=3),
        filter.six_months: relativedelta(months=6),
        filter.one_year: relativedelta(years=1),
    }
    now = datetime.now(TZ)
    now = now.replace(minute=0, second=0, microsecond=0)
    offset_datetime = now - filter_offset_dict[filter]
    filter_string = {filter_datetime: {"$gte": offset_datetime, "$lte": now}}
    records = [i for i in mongo.collection.find(filter_string)]
    for record in records: del record["_id"]
    mongo.client.close()
    return records