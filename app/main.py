
from fastapi import FastAPI
from tasks.routes import router
from tasks.users_routes import user_router

# title change the title of run code
app = FastAPI(title="to do list application")
app.include_router(router)
app.include_router(user_router)