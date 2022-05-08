from datetime import datetime
from fastapi import HTTPException
from fastapi import APIRouter
from configs.globals import *
from dinning_records.models import *
from generic_apps.filter_app import *
from pkgs.mongodb.mongodb import Type4DB


router = APIRouter(
    prefix="/dinning_records",
    tags=["dinning_records"]
)


@router.get("/fget/form_fields")
async def get_dinning_records_form_field():
    dinning_records = DinningRecords(foods="foo, bar", spicyness=SpicinessEnum.not_spicy)
    return {
        "fields": [
            {
                "name": "meal_date",
                "verbose": "Date",
                "type": "date",
                "value": dinning_records.meal_date,
                "required": True,
                "header": "📆"
            },
            {
                "name": "meal_time",
                "verbose": "Time",
                "type": "select",
                "value": [[e.name, e.value] for e in GenericTimeEnum],
                "required": True,
                "display": "value",
                "header": "⏰"
            },
            {
                "name": "is_expired",
                "verbose": "Expired",
                "type": "checkbox",
                "value": dinning_records.is_expired,
                "required": True,
                "header": "💀"
            },
            {
                "name": "spicyness",
                "verbose": "Spicyness",
                "type": "select",
                "value": [[e.name, e.value] for e in SpicinessEnum],
                "required": True,
                "display": "name",
                "header": "🌶️"
            },
            {
                "name": "foods",
                "verbose": "Foods",
                "type": "textarea",
                "placeholder": "beef, lemon tea",
                "required": True,
                "header": "🍲"
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
async def add_and_update_dinning_records(dinning_record: DinningRecords):
    mongo = Type4DB("dinning_records")
    
    # update or insert into dinning_records
    dinning_record_dict = dict(dinning_record)
    foods = list(set(dinning_record_dict["foods"].lower().replace(", ", ',').split(',')))
    print(len(foods) == 1 and foods[0] == '')
    if len(foods) == 1 and foods[0] == '':
        mongo.client.close()
        raise HTTPException(status_code=500, detail="Foods must not be empty")
    else:
        dinning_record_dict["foods"] = foods
        meal_date = list(map(int, dinning_record_dict["meal_date"].split('-')))
        meal_datetime = TZ.localize(
            datetime(meal_date[0], meal_date[1], meal_date[2], dinning_record_dict["meal_time"])
        )
        dinning_record_dict["meal_datetime"] = meal_datetime
        filter_string = {"meal_datetime": meal_datetime}
        mongo.collection.update_one(
            filter_string,
            {"$set": dinning_record_dict},
            upsert=True
        )
        # mongo.collection.insert_one(dinning_record_dict)

        # update or insert into food_names
        mongo.set_collection("food_names")
        for food in foods:
            mongo.collection.find_one_and_update(
                {"food": food},
                {"$set": {"food": food, "last_consumed": dinning_record_dict["meal_datetime"]}},
                upsert=True
            )
        mongo.client.close()
        return {"success": True}

@router.get("/fget/records_filter")
async def get_dinning_records_form_field():
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
async def get_dinning_records(filter: RecordsDatetimeFilterEnum = None):
    mongo = Type4DB("dinning_records")
    dinning_records = get_datetime_filter_records(mongo, filter, "meal_datetime")
    for e, record in enumerate(dinning_records):
        foods = ""
        for food in record["foods"]: foods += f"{food}, "
        foods = foods[:-2]
        dinning_records[e]["foods"] = foods
        dinning_records[e]["meal_date"] = record["meal_date"].replace('-', '.')
    return {"data": dinning_records}