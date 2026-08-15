
from fastapi import APIRouter,Depends,status,HTTPException,Query
from sqlalchemy.orm import Session
from app.database import get_db
from tasks.models import task_models

router = APIRouter()

# in here if we get tags to the router the label change from default to tag we want
# the rags should be in a list
@router.get("/get_all_works",tags=["get all works"])
async def read_works(db:Session=Depends(get_db)):
    query = db.query(task_models)
    return query.all()

@router.get("/find_a_work",tags=["get one work"],status_code=status.HTTP_200_OK)
async def get_work(work_title,db:Session=Depends(get_db)):
    query = db.query(task_models)
    result = query.where(task_models.title.like(f"%{work_title}%")).all()
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="work not found")

@router.get("/find_complete_or_incomplete_works",tags=["get complete or incomplete"])
def get_complete_or_incomplete_works(
    find_status:bool=Query(None),
    db:Session=Depends(get_db),
    limited:int|None=Query(default=None,ge=0,description="this is how many data you want to see"),
    offset_var:int|None=Query(default=None,ge=0,description="this for how many data did you see")
    ):
    query = db.query(task_models)
    if find_status != None:
        result = query.where(task_models.work_status==find_status)
        return result.limit(limited).offset(offset_var).all()
    else:
        return query.limit(limited).offset(offset_var).all()

@router.post("/add_work",tags=["add work"])
async def add_work(work_title:str,description:str|None=None,db:Session=Depends(get_db)):
    query = db.query(task_models)
    check_duplicate = query.where(task_models.title == work_title).one_or_none()
    if check_duplicate == None:
        get_id = query.where(task_models.title==work_title).one_or_none()
        work_obj = task_models(title=work_title,description=description,user_id=get_id)
        db.add(work_obj)
        db.commit()
        result = query.where(task_models.title == work_title).one_or_none()
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="duplicate work")

@router.put("/new_title",tags=["update title"])
async def update_work(work_title:str,new_title:str,db:Session=Depends(get_db)):
    query = db.query(task_models)
    find_work = query.where(task_models.title == work_title).one_or_none()
    if find_work:
        find_work.title = new_title
        db.commit()
        db.refresh(find_work)
        return find_work
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="work not found")

@router.put("/new_description",tags=["update description"])
async def change_description(work_title:str,new_description:str|None=None,db:Session=Depends(get_db)):
    query = db.query(task_models)
    find_work = query.where(task_models.title == work_title).one_or_none()
    if find_work:
        find_work.description = new_description
        db.commit()
        result = query.where(task_models.title == work_title).one_or_none()
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="work not found")

@router.put("/new_status",tags=["update status"])
async def change_status(work_title:str,db:Session=Depends(get_db)):
    query = db.query(task_models)
    find_work = query.where(task_models.title == work_title).one_or_none()
    if find_work:
        find_work.work_status = not find_work.work_status
        db.commit()
        result = query.where(task_models.title == work_title).one_or_none()
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="work not found")

@router.delete("/delete_works",tags=["delete works"])
async def delete_work(work_title,db:Session=Depends(get_db)):
    query = db.query(task_models)
    find_work = query.where(task_models.title == work_title).one_or_none()
    if find_work:
        db.delete(find_work)
        db.commit()
        return {"detail":"work deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="work not found")