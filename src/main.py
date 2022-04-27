from fastapi import FastAPI
from dinning_records import dinning_records
from faecal_records import faecal_records
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dinning_records.router)
app.include_router(faecal_records.router)


@app.get("/")
async def root():
    return {"healthcheck": "connected"}
