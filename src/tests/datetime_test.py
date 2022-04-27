import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
from configs.globals import *


def test_datetime():
    now = TZ.localize(
        datetime.now()
    ).strftime("%Y-%m-%d %H")
    print(now)
    assert True