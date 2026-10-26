from fastapi import FastAPI
from models import Menu
from database import engine,Base

from routers.qr import router as qr_router


app=FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(qr_router)