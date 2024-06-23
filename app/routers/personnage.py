from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/personnage",
    tags=["personnages"]
)

@router.post("/", response_model=schemas.Personnage)
def create_personnage(personnage: schemas.PersonnageCreate, db: Session = Depends(get_db)):
    db_personnage = models.Personnage(**personnage.dict())
    db.add(db_personnage)
    db.commit()
    db.refresh(db_personnage)
    return db_personnage

@router.get("/", response_model=list[schemas.Personnage])
def read_personnages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    personnages = db.query(models.Personnage).offset(skip).limit(limit).all()
    return personnages

@router.get("/{personnage_id}", response_model=schemas.Personnage)
def read_personnage(personnage_id: int, db: Session = Depends(get_db)):
    personnage = db.query(models.Personnage).filter(models.Personnage.id == personnage_id).first()
    if personnage is None:
        raise HTTPException(status_code=404, detail="Personnage not found")
    return personnage

@router.put("/{personnage_id}", response_model=schemas.Personnage)
def update_personnage(personnage_id: int, personnage: schemas.PersonnageCreate, db: Session = Depends(get_db)):
    db_personnage = db.query(models.Personnage).filter(models.Personnage.id == personnage_id).first()
    if db_personnage is None:
        raise HTTPException(status_code=404, detail="Personnage not found")
    for key, value in personnage.dict().items():
        setattr(db_personnage, key, value)
    db.commit()
    db.refresh(db_personnage)
    return db_personnage

@router.delete("/{personnage_id}", response_model=schemas.Personnage)
def delete_personnage(personnage_id: int, db: Session = Depends(get_db)):
    db_personnage = db.query(models.Personnage).filter(models.Personnage.id == personnage_id).first()
    if db_personnage is None:
        raise HTTPException(status_code=404, detail="Personnage not found")
    db.delete(db_personnage)
    db.commit()
    return db_personnage
