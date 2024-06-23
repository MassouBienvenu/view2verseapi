from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/espece",
    tags=["especes"]
)

@router.post("/", response_model=schemas.Espece)
def create_espece(espece: schemas.EspeceCreate, db: Session = Depends(get_db)):
    db_espece = models.Espece(**espece.dict())
    db.add(db_espece)
    db.commit()
    db.refresh(db_espece)
    return db_espece

@router.get("/", response_model=list[schemas.Espece])
def read_especes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    especes = db.query(models.Espece).offset(skip).limit(limit).all()
    return especes

@router.get("/{espece_id}", response_model=schemas.Espece)
def read_espece(espece_id: int, db: Session = Depends(get_db)):
    espece = db.query(models.Espece).filter(models.Espece.id == espece_id).first()
    if espece is None:
        raise HTTPException(status_code=404, detail="Espece not found")
    return espece

@router.put("/{espece_id}", response_model=schemas.Espece)
def update_espece(espece_id: int, espece: schemas.EspeceCreate, db: Session = Depends(get_db)):
    db_espece = db.query(models.Espece).filter(models.Espece.id == espece_id).first()
    if db_espece is None:
        raise HTTPException(status_code=404, detail="Espece not found")
    for key, value in espece.dict().items():
        setattr(db_espece, key, value)
    db.commit()
    db.refresh(db_espece)
    return db_espece

@router.delete("/{espece_id}", response_model=schemas.Espece)
def delete_espece(espece_id: int, db: Session = Depends(get_db)):
    db_espece = db.query(models.Espece).filter(models.Espece.id == espece_id).first()
    if db_espece is None:
        raise HTTPException(status_code=404, detail="Espece not found")
    db.delete(db_espece)
    db.commit()
    return db_espece
