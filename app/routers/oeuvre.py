from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database  # Assurez-vous que le chemin vers database.py est correct

router = APIRouter(
    prefix="/oeuvre",
    tags=["oeuvres"]
)

get_db = database.get_db
@router.post("/", response_model=schemas.Oeuvre)
def create_oeuvre(oeuvre: schemas.OeuvreCreate, db: Session = Depends(get_db)):
    db_oeuvre = models.Oeuvre(**oeuvre.dict())
    db.add(db_oeuvre)
    db.commit()
    db.refresh(db_oeuvre)
    return db_oeuvre
@router.get("/", response_model=list[schemas.Oeuvre])
def read_oeuvres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    oeuvres = db.query(models.Oeuvre).offset(skip).limit(limit).all()
    return oeuvres
@router.put("/{oeuvre_id}", response_model=schemas.Oeuvre)
def update_oeuvre(oeuvre_id: int, oeuvre: schemas.OeuvreCreate, db: Session = Depends(get_db)):
    db_oeuvre = db.query(models.Oeuvre).filter(models.Oeuvre.id_oeuvre == oeuvre_id).first()
    if db_oeuvre is None:
        raise HTTPException(status_code=404, detail="Oeuvre not found")
    for key, value in oeuvre.dict().items():
        setattr(db_oeuvre, key, value)
    db.commit()
    db.refresh(db_oeuvre)
    return db_oeuvre
@router.delete("/{oeuvre_id}", response_model=schemas.Oeuvre)
def delete_oeuvre(oeuvre_id: int, db: Session = Depends(get_db)):
    db_oeuvre = db.query(models.Oeuvre).filter(models.Oeuvre.id_oeuvre == oeuvre_id).first()
    if db_oeuvre is None:
        raise HTTPException(status_code=404, detail="Oeuvre not found")
    db.delete(db_oeuvre)
    db.commit()
    return db_oeuvre
