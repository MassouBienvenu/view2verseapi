
# Repeat similarly for other tables like Artefact, Espece, EtatsMonde, etc.
from sqlalchemy.orm import Session
from . import models, schemas


def create_annee(db: Session, annee: schemas.AnneeCreate):
    db_annee = models.Annee(**annee.dict())
    db.add(db_annee)
    db.commit()
    db.refresh(db_annee)
    return db_annee

def get_annee(db: Session, annee_id: str):
    return db.query(models.Annee).filter(models.Annee.id_annee == annee_id).first()

def get_annees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Annee).offset(skip).limit(limit).all()

def update_annee(db: Session, annee_id: str, annee: schemas.AnneeCreate):
    db_annee = db.query(models.Annee).filter(models.Annee.id_annee == annee_id).first()
    if db_annee:
        for key, value in annee.dict().items():
            setattr(db_annee, key, value)
        db.commit()
        db.refresh(db_annee)
    return db_annee

def delete_annee(db: Session, annee_id: str):
    db_annee = db.query(models.Annee).filter(models.Annee.id_annee == annee_id).first()
    if db_annee:
        db.delete(db_annee)
        db.commit()
    return db_annee
