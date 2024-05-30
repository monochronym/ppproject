import os

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from pathlib import Path
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from starlette import status
from starlette.responses import RedirectResponse

from db_interraction import crud, models, login
from db_interraction.database import engine, get_db
from db_interraction.login import router_jwt
from api import router_api

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.include_router(router_jwt)
app.include_router(router_api)


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)
templates = Jinja2Templates(directory="templates")
files = {
    item: os.path.join('samples_directory', item)
    for item in os.listdir('samples_directory')
}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

@app.get("/login_access")
async def login_on_site(request:Request, db: Session = Depends(get_db)):
    try:
        user = login.get_current_user(request)
        user = crud.get_user_by_id(db, user.uuid)
        return RedirectResponse(f"../user/{user.uuid}", status_code=status.HTTP_303_SEE_OTHER)
    except:
        return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signin")
async def signin(request:Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/user/{user_id}")
async def user_page(request:Request,db: Session = Depends(get_db)):
    try:
        user = login.get_current_user(request)
        # if request.cookies.get("User_id") != str(user_id):
        #     raise HTTPException(
        # status_code=status.HTTP_401_UNAUTHORIZED,
        # detail="Could not validate credentials",
        # headers={"WWW-Authenticate": "Bearer"},
        # )
        user = crud.get_user_by_id(db, user.uuid)
        return templates.TemplateResponse("user.html", {"request":request, "user":{"user_id": user.uuid, "user_login":user.email, "username": user.username}})
    except:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/user/{user_id}")
async def user_page(request:Request, db: Session = Depends(get_db)):
    try:
        user = login.get_current_user(request)
        # if request.cookies.get("User_id") != str(user_id):
        #     raise HTTPException(
        # status_code=status.HTTP_401_UNAUTHORIZED,
        # detail="Could not validate credentials",
        # headers={"WWW-Authenticate": "Bearer"},
        # )
        user = crud.get_user_by_id(db, user.uuid)
        return templates.TemplateResponse("user.html", {"request":request, "user":{"user_id": user.uuid, "user_login":user.email, "username": user.username}})
    except:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )



