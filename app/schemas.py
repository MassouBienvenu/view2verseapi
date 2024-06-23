from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
class AnneeBase(BaseModel):
    libelle: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class AnneeCreate(AnneeBase):
    pass

class Annee(AnneeBase):
    id_annee: UUID

    class Config:
        orm_mode = True

class ArtefactBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    pouvoir: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class ArtefactCreate(ArtefactBase):
    pass

class Artefact(ArtefactBase):
    id_artefact: str

    class Config:
        orm_mode = True

class EspeceBase(BaseModel):
    nom: Optional[str] = None
    caracteristiques: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class EspeceCreate(EspeceBase):
    pass

class Espece(EspeceBase):
    id_espece: str

    class Config:
        orm_mode = True

class EtatMondeBase(BaseModel):
    annee_id: Optional[str] = None
    population: Optional[str] = None
    technologie: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class EtatMondeCreate(EtatMondeBase):
    pass

class EtatMonde(EtatMondeBase):
    id_etat: str

    class Config:
        orm_mode = True

class EvenementBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    annee_id: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class EvenementCreate(EvenementBase):
    pass

class Evenement(EvenementBase):
    id_evenement: str

    class Config:
        orm_mode = True

class InteractionBase(BaseModel):
    type: Optional[str] = None
    date_interaction: Optional[str] = None
    evenement_id: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

class Interaction(InteractionBase):
    id_interaction: str

    class Config:
        orm_mode = True

class InteractionPersonnageBase(BaseModel):
    interaction_id: Optional[str] = None
    personnage_id: Optional[str] = None

class InteractionPersonnageCreate(InteractionPersonnageBase):
    pass

class InteractionPersonnage(InteractionPersonnageBase):
    id_interaction_personnage: str

    class Config:
        orm_mode = True

class LieuBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    coordonnees: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class LieuCreate(LieuBase):
    pass

class Lieu(LieuBase):
    id_lieu: str

    class Config:
        orm_mode = True

class OeuvreBase(BaseModel):
    nom: Optional[str] = None
    type: Optional[str] = None
    auteur: Optional[str] = None
    contenu: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class OeuvreCreate(OeuvreBase):
    pass

class Oeuvre(OeuvreBase):
    id_oeuvre: str

    class Config:
        orm_mode = True

class PanierBase(BaseModel):
    utilisateur_id: Optional[str] = None
    date_creation: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class PanierCreate(PanierBase):
    pass

class Panier(PanierBase):
    id_panier: str

    class Config:
        orm_mode = True

class ParametreBase(BaseModel):
    nom: Optional[str] = None
    valeur: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class ParametreCreate(ParametreBase):
    pass

class Parametre(ParametreBase):
    id_parametre: str

    class Config:
        orm_mode = True

class PersonnageBase(BaseModel):
    nom: Optional[str] = None
    en_vie: Optional[str] = None
    capacites: Optional[str] = None
    histoire: Optional[str] = None
    observation: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None
    id_race: Optional[str] = None
    id_espece: Optional[str] = None
    id_pouvoir: Optional[str] = None
    id_relation: Optional[str] = None

class PersonnageCreate(PersonnageBase):
    pass

class Personnage(PersonnageBase):
    id_personnage: str

    class Config:
        orm_mode = True

class PersonnageArtefactBase(BaseModel):
    personnage_id: Optional[str] = None
    artefact_id: Optional[str] = None

class PersonnageArtefactCreate(PersonnageArtefactBase):
    pass

class PersonnageArtefact(PersonnageArtefactBase):
    id_personnage_artefact: str

    class Config:
        orm_mode = True

class PersonnagePouvoirBase(BaseModel):
    id_pouvoir: Optional[str] = None

class PersonnagePouvoirCreate(PersonnagePouvoirBase):
    pass

class PersonnagePouvoir(PersonnagePouvoirBase):
    personnage_id: str

    class Config:
        orm_mode = True

class PersonnageRelationBase(BaseModel):
    personnage1_id: Optional[str] = None
    personnage2_id: Optional[str] = None
    id_relation: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class PersonnageRelationCreate(PersonnageRelationBase):
    pass

class PersonnageRelation(PersonnageRelationBase):
    id_personnage_relation: str

    class Config:
        orm_mode = True

class PouvoirBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class PouvoirCreate(PouvoirBase):
    pass

class Pouvoir(PouvoirBase):
    id_pouvoir: str

    class Config:
        orm_mode = True

class ProduitBase(BaseModel):
    nom: Optional[str] = None
    statut: Optional[str] = None
    description: Optional[str] = None
    prix_unitaire: Optional[int] = None
    qte_en_stock: Optional[int] = None
    lien_ftp_cover: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id_produit: str

    class Config:
        orm_mode = True

class ProduitsDansPanierBase(BaseModel):
    panier_id: Optional[str] = None
    produit_id: Optional[str] = None
    quantite: Optional[int] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class ProduitsDansPanierCreate(ProduitsDansPanierBase):
    pass

class ProduitsDansPanier(ProduitsDansPanierBase):
    id_produit_panier: str

    class Config:
        orm_mode = True

class RaceBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class RaceCreate(RaceBase):
    pass

class Race(RaceBase):
    id_race: str

    class Config:
        orm_mode = True

class RelationBase(BaseModel):
    relation: Optional[str] = None
    id_perso_1: Optional[str] = None
    id_perso_2: Optional[str] = None
    datajoutserver: Optional[str] = None
    roles: Optional[str] = None
    effacer: Optional[str] = None

class RelationCreate(RelationBase):
    pass
class UtilisateurBase(BaseModel):
    nom: Optional[str] = None
    email: Optional[str] = None
    mot_de_passe: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None
class UtilisateurCreate(UtilisateurBase):
    pass
class Utilisateur(UtilisateurBase):
    id_utilisateur: str
    class Config:
        orm_mode = True
class Relation(RelationBase):
    id_relation: str

    class Config:
        orm_mode = True

class RessourceBase(BaseModel):
    nom: Optional[str] = None
    quantite: Optional[str] = None
    annee_id: Optional[str] = None
    datajoutserver: Optional[str] = None
    effacer: Optional[str] = None

class RessourceCreate(RessourceBase):
    pass


class Ressource(RessourceBase):
    id_ressource: str
    datajoutserver: str
    effacer: str

    class Config:
        orm_mode = True
