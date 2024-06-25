from fastapi import FastAPI

from app.routers import oeuvre, utilisateurs
from . import models
from .database import engine
from .routers import annee, artefact, espece, personnage

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(annee.router)
app.include_router(artefact.router)
app.include_router(espece.router)
app.include_router(personnage.router)
app.include_router(utilisateurs.router)
app.include_router(oeuvre.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/favicon.ico")
def read_favicon():
    return {"message": "Favicon not found"}
