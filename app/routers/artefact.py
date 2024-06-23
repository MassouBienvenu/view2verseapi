from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/artefact",
    tags=["artefacts"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.Artefact)
def create_artefact(artefact: schemas.ArtefactCreate, db: Session = Depends(get_db)):
    db_artefact = models.Artefact(**artefact.dict())
    db.add(db_artefact)
    db.commit()
    db.refresh(db_artefact)
    return db_artefact

@router.get("/", response_model=list[schemas.Artefact])
def read_artefacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    artefacts = db.query(models.Artefact).offset(skip).limit(limit).all()
    return artefacts

@router.get("/{artefact_id}", response_model=schemas.Artefact)
def read_artefact(artefact_id: int, db: Session = Depends(get_db)):
    artefact = db.query(models.Artefact).filter(models.Artefact.id == artefact_id).first()
    if artefact is None:
        raise HTTPException(status_code=404, detail="Artefact not found")
    return artefact

@router.put("/{artefact_id}", response_model=schemas.Artefact)
def update_artefact(artefact_id: int, artefact: schemas.ArtefactCreate, db: Session = Depends(get_db)):
    db_artefact = db.query(models.Artefact).filter(models.Artefact.id == artefact_id).first()
    if db_artefact is None:
        raise HTTPException(status_code=404, detail="Artefact not found")
    for key, value in artefact.dict().items():
        setattr(db_artefact, key, value)
    db.commit()
    db.refresh(db_artefact)
    return db_artefact

@router.delete("/{artefact_id}", response_model=schemas.Artefact)
def delete_artefact(artefact_id: int, db: Session = Depends(get_db)):
    db_artefact = db.query(models.Artefact).filter(models.Artefact.id == artefact_id).first()
    if db_artefact is None:
        raise HTTPException(status_code=404, detail="Artefact not found")
    db.delete(db_artefact)
    db.commit()
    return db_artefact
