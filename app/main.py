from fastapi import FastAPI, APIRouter

from .routers import items_router


app = FastAPI()

api_router = APIRouter(prefix='/api')
api_router.include_router(items_router)
app.include_router(api_router)