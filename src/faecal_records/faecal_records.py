from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter
from configs.globals import *
from faecal_records.models import *
from generic_apps.filter_app import *
from pkgs.mongodb.mongodb import Type4DB
from generic_apps.filter_by_id import *
from generic_apps.delete_a_record import *


router = APIRouter(
    prefix="/faecal_records",
    tags=["faecal_records"]
)


@router.get("/fget/form_fields")
async def get_dinning_records_form_field():
    faecal_records = FaecalRecords()
    return {
        "fields": [
            {
                "name": "faecal_date",
                "verbose": "Date",
                "type": "date",
                "value": faecal_records.faecal_date,
                "required": True,
                "header": "📆"
            },
            {
                "name": "faecal_time",
                "verbose": "Time",
                "type": "select",
                "value": [[e.name, e.value] for e in GenericTimeEnum],
                "required": True,
                "display": "value",
                "header": "⏰",
                "selected": HOUR_DICT[int(TZ.localize(datetime.now()).strftime("%H"))]
            },
            {
                "name": "faecal_type",
                "verbose": "Type",
                "type": "select",
                "value": [[e.name, e.value] for e in FaecalTypeEnum],
                "required": True,
                "display": "name",
                "header": "💩"
            },
            {
                "name": "remarks",
                "verbose": "Remarks",
                "type": "textarea",
                "placeholder": "( Optional )",
                "required": False,
                "header": "📝"
            },
        ]
    }

@router.post("/add")
async def add_and_update_faecal_records(faecal_record: FaecalRecords, id: str = None):
    mongo = Type4DB("faecal_records")
    
    # update or insert into dinning_records
    faecal_record_dict = dict(faecal_record)
    faecal_date = list(map(int, faecal_record_dict["faecal_date"].split('-')))
    faecal_datetime = TZ.localize(
        datetime(faecal_date[0], faecal_date[1], faecal_date[2], faecal_record_dict["faecal_time"])
    )
    faecal_record_dict["faecal_datetime"] = faecal_datetime
    if id == None:
        mongo.collection.insert_one(faecal_record_dict)
    else:
        filter_string = {"_id": ObjectId(id)}
        mongo.collection.update_one(
            filter_string,
            {"$set": faecal_record_dict},
            upsert=True
        )

    mongo.client.close()
    return {"success": True}

@router.get("/fget/records_filter")
async def get_faecal_records_form_field():
    return {
        "fields": {
            "filter": {
                "type": "select",
                "value": [[e.name, e.value] for e in RecordsDatetimeFilterEnum],
                "required": True
            }
        }
    }

@router.get("/get")
async def get_faecal_records(filter: RecordsDatetimeFilterEnum = None):
    mongo = Type4DB("faecal_records")
    faecal_records = get_datetime_filter_records(mongo, filter, "faecal_datetime")
    for e, record in enumerate(faecal_records):
        faecal_records[e]["faecal_date"] = record["faecal_date"].replace('-', '.')
    return {"data": faecal_records}

@router.get("/get/with")
async def get_faecal_records(id: str):
    mongo = Type4DB("faecal_records")
    faecal_records = get_by_id(mongo, id)
    return {"data": faecal_records}

@router.get("/remove")
async def remove_faecal_records(id: str):
    mongo = Type4DB("faecal_records")
    success = remove_by_id(mongo, id)
    return {"success": success}