
from fastapi import APIRouter,Depends,Query,status
from sqlalchemy.orm import Session
from app.database import get_db
from tasks.models import users_models
from tasks.hashing_file import hash_class

user_router = APIRouter()

@user_router.post("/signup",tags=["user signup"],status_code=status.HTTP_201_CREATED)
async def user_signup(user_name:str=Query(description="Select your user name"),
                      user_password:str=Query(description="Select your password"),
                      db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    check_duplicate = query.where(users_models.name==user_name).all()
    if check_duplicate == []:
        user_obj = users_models(name=user_name,password=hash_obj.hash_password(user_password))
        db.add(user_obj)
        db.commit()
        return {"status code":status.HTTP_201_CREATED,"detail":"user created"}
    else:
        return {"status code":status.HTTP_409_CONFLICT,"detail":"duplicate name"}

@user_router.get("/login",tags=["user login"],status_code=status.HTTP_200_OK)
async def user_login(user_name:str=Query(description="Enter your user name"),
                     user_password:str=Query(description="Enter your password"),
                     db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    find_user = query.where(users_models.name==user_name).one_or_none()
    if find_user:
        find_password = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).one_or_none()
        if find_password:
            return {"status code":status.HTTP_200_OK,"detail":"login successfully"}
        else:
            return {"status code":status.HTTP_404_NOT_FOUND,"detail":"wrong password"}
    else:
        return {"status code":status.HTTP_404_NOT_FOUND,"detail":"name not found"}

@user_router.put("/change_name",tags=["change name"])
async def change_name(user_name:str=Query(description="Enter your user name"),
                      user_password:str=Query(description="Enter your user password"),
                      new_name:str=Query(description="Enter your new user name"),
                      db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    find_name = query.where(users_models.name==user_name).all()
    if find_name:
        check_password = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).all()
        if check_password:
            check_duplicate = query.where(users_models.name==new_name).first()
            if check_duplicate is None:
                find_name[0].name=new_name
                db.commit()
                return {"status":status.HTTP_202_ACCEPTED,"detail":"name update successfully"}
            else:
                return {"status code":status.HTTP_409_CONFLICT,"detail":"duplicate name"}
        else:
            return {"status":status.HTTP_401_UNAUTHORIZED,"detail":"wrong password"}
    else:
        return {"status":status.HTTP_404_NOT_FOUND,"detail":"name not found"}

@user_router.put("/change_password",tags=["change password"])
async def change_password(user_name:str=Query(description="Enter your user name"),
                          user_password:str=Query(description="Enter your user password"),
                          new_password:str=Query(description="Enter your new password"),
                          db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    find_name = query.where(users_models.name==user_name).all()
    if find_name:
        check_password = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).all()
        if check_password:
            find_name[0].password=hash_obj.hash_password(new_password)
            db.commit()
            return {"status":status.HTTP_202_ACCEPTED,"detail":"password update successfully"}
        else:
            return {"status":status.HTTP_401_UNAUTHORIZED,"detail":"wrong password"}
    else:
        return {"status":status.HTTP_404_NOT_FOUND,"detail":"name not found"}

@user_router.put("/change_status",tags=["change status"])
async def change_status(user_name:str=Query(description="Enter your user name"),
                        user_password:str=Query(description="Enter your user password"),
                        db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    find_name = query.where(users_models.name==user_name).all()
    if find_name:
        check_password = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).all()
        if check_password:
            find_name[0].user_status = not find_name[0].user_status
            db.commit()
            return {"status":status.HTTP_202_ACCEPTED,"detail":"status update successfully"}
        else:
            return {"status":status.HTTP_401_UNAUTHORIZED,"detail":"wrong password"}
    else:
        return {"status":status.HTTP_404_NOT_FOUND,"detail":"name not found"}

@user_router.delete("/delete_user",tags=["delete user account"])
async def delete_user(user_name:str=Query(description="Enter your user name"),
                      user_password:str=Query(description="Enter your user password"),
                      db:Session=Depends(get_db)):
    query = db.query(users_models)
    hash_obj = hash_class()
    find_name = query.where(users_models.name==user_name).all()
    if find_name:
        check_password = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).all()
        if check_password:
            user_account = query.where(users_models.name==user_name,users_models.password==hash_obj.hash_password(user_password)).first()
            db.delete(user_account)
            db.commit()
            return {"status":status.HTTP_204_NO_CONTENT,"detail":"user deleted"}
        else:
            return {"status":status.HTTP_401_UNAUTHORIZED,"detail":"wrong password"}
    else:
        return {"status":status.HTTP_404_NOT_FOUND,"detail":"name not found"}