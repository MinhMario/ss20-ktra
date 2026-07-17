from fastapi import FastAPI
from routers.routers import router as routers
from database import Base , engine

Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(routers)
