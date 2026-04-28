from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.staticfiles import StaticFiles
import os


import models

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app=FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {"request": request}
    )

@app.post("/register", response_class=HTMLResponse)
def register(request:Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    repeat_password: str = Form(...),
    db: Session = Depends(get_db)
):
    
    username = username.strip()
    email = email.strip()
    password = password.strip()
    repeat_password = repeat_password.strip()

    if username=="" or email=="" or password=="":
        return templates.TemplateResponse(
            "error_empty_message.html",
            {"request": request}
        )  
    
    
    if password != repeat_password:
        return templates.TemplateResponse(
            "error_password_message.html",
            {"request": request}
        )
    
    existing_user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if existing_user:
        return templates.TemplateResponse(
            "error_email_exists.html",
            {"request": request}
    )
    
    hashed_password = hash_password(password)

    new_user = models.User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return templates.TemplateResponse(
        "success.html",
        {"request":request}
    )
