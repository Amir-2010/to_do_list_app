
from fastapi import FastAPI
from tasks.routes import router

# title change the title of run code
app = FastAPI(title="to do list application")
app.include_router(router)