from datetime import datetime
from enum import IntEnum, Enum
from pydantic import BaseModel, constr
from time import time
from typing import List
from configs.globals import *


class FaecalTypeEnum(IntEnum):
    i = 1
    ii = 2
    iii = 3
    iv = 4
    v = 5
    vi = 6
    vii = 7


class FaecalRecords(BaseModel):
    faecal_date: constr(regex=r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$') = TZ.localize(datetime.now()).strftime("%Y-%m-%d")
    faecal_time: int = int(TZ.localize(datetime.now()).strftime("%H"))
    faecal_type: FaecalTypeEnum = FaecalTypeEnum.iv
    remarks: str = ""
    created: int = int(time() * 1000)