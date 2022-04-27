from datetime import datetime
from enum import IntEnum, Enum
from pydantic import BaseModel, constr
from time import time
from typing import List
from configs.globals import *


# class MealTimeEnum(IntEnum):
#     breakfast = 0
#     brunch = 1
#     lunch = 2
#     tea = 3
#     dinner = 4
#     midnight = 5


class SpicinessEnum(IntEnum):
    not_spicy = 0
    bb = 1
    little = 2
    mid = 3
    more = 4
    killing = 5


class DinningRecordsMealDatetimeFilterEnum(Enum):
    one_days = "1d"
    seven_days = "7d"
    one_month = "1month"
    three_months = "3months"
    six_months = "6months"
    one_year = "1year"


class DinningRecords(BaseModel):
    meal_date: constr(regex=r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$') = TZ.localize(datetime.now()).strftime("%Y-%m-%d")
    meal_time: int = int(TZ.localize(datetime.now()).strftime("%H"))
    foods: str
    # foods: List[str] = []
    is_expired: bool = False
    spicyness: SpicinessEnum = SpicinessEnum.not_spicy
    remarks: str = ""
    created: int = int(time() * 1000)

    @staticmethod
    def default_values() -> dict:
        return {"expired_date": "1900-01-01"}