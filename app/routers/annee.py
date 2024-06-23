from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/annee",
    tags=["annee"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Annee)
def create_annee(annee: schemas.AnneeCreate, db: Session = Depends(get_db)):
    return crud.create_annee(db=db, annee=annee)

@router.get("/{annee_id}", response_model=schemas.Annee)
def read_annee(annee_id: str, db: Session = Depends(get_db)):
    db_annee = crud.get_annee(db, annee_id=annee_id)
    if db_annee is None:
        raise HTTPException(status_code=404, detail="Annee not found")
    return db_annee

@router.get("/", response_model=List[schemas.Annee])
def read_annees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_annees(db, skip=skip, limit=limit)

@router.put("/{annee_id}", response_model=schemas.Annee)
def update_annee(annee_id: str, annee: schemas.AnneeCreate, db: Session = Depends(get_db)):
    return crud.update_annee(db=db, annee_id=annee_id, annee=annee)

@router.delete("/{annee_id}", response_model=schemas.Annee)
def delete_annee(annee_id: str, db: Session = Depends(get_db)):
    return crud.delete_annee(db=db, annee_id=annee_id)
