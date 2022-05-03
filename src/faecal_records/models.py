from datetime import datetime
from enum import IntEnum, Enum
from pydantic import BaseModel, constr
from time import time
from typing import List
from configs.globals import *


class FaecalTypeEnum(IntEnum):
    extremely_hard = 1
    hard = 2
    slightly_hard = 3
    normal = 4
    slightly_watery = 5
    watery = 6
    extremely_watery = 7


class FaecalRecords(BaseModel):
    faecal_date: constr(regex=r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$') = TZ.localize(datetime.now()).strftime("%Y-%m-%d")
    faecal_time: int = int(TZ.localize(datetime.now()).strftime("%H"))
    faecal_type: FaecalTypeEnum = FaecalTypeEnum.normal
    remarks: str = ""
    created: int = int(time() * 1000)