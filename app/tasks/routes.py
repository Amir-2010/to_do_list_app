
from fastapi import APIRouter

router = APIRouter()

# in here if we get tags to the router the label change from default to tag we want
# the rags should be in a list
@router.get("/tasks",tags=["get task"])
async def read_user():
    return []