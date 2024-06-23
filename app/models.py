from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Annee(Base):
    __tablename__ = "annee"
    id_annee = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    libelle = Column(String)
    datajoutserver = Column(String)
    effacer = Column(String)
class Artefact(Base):
    __tablename__ = 'artefact'

    id_artefact = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    pouvoir = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Espece(Base):
    __tablename__ = 'espece'

    id_espece = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    caracteristiques = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class EtatMonde(Base):
    __tablename__ = 'etats_monde'

    id_etat = Column(String(255), primary_key=True)
    annee_id = Column(String(255), ForeignKey('annee.id_annee'))
    population = Column(String(255), nullable=True)
    technologie = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Evenement(Base):
    __tablename__ = 'evenements'

    id_evenement = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    annee_id = Column(String(255), ForeignKey('annee.id_annee'))
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Interaction(Base):
    __tablename__ = 'interactions'

    id_interaction = Column(String(255), primary_key=True)
    type = Column(String(255), nullable=True)
    date_interaction = Column(String(255), nullable=True)
    evenement_id = Column(String(255), ForeignKey('evenements.id_evenement'))
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class InteractionPersonnage(Base):
    __tablename__ = 'interactions_personnages'

    id_interaction_personnage = Column(String(255), primary_key=True)
    interaction_id = Column(String(255), ForeignKey('interactions.id_interaction'))
    personnage_id = Column(String(255), ForeignKey('personnage.id_personnage'))

class Lieu(Base):
    __tablename__ = 'lieux'

    id_lieu = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    coordonnees = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Oeuvre(Base):
    __tablename__ = 'oeuvre'

    id_oeuvre = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    auteur = Column(String(255), nullable=True)
    contenu = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Panier(Base):
    __tablename__ = 'panier'

    id_panier = Column(String(255), primary_key=True)
    utilisateur_id = Column(String(255), nullable=True)
    date_creation = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Parametre(Base):
    __tablename__ = 'parametres'

    id_parametre = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    valeur = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Personnage(Base):
    __tablename__ = 'personnage'

    id_personnage = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    en_vie = Column(String(255), nullable=True)
    capacites = Column(String(255), nullable=True)
    histoire = Column(String(255), nullable=True)
    observation = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)
    id_race = Column(String(255), nullable=True)
    id_espece = Column(String(255), nullable=True)
    id_pouvoir = Column(String(255), nullable=True)
    id_relation = Column(String(255), nullable=True)

class PersonnageArtefact(Base):
    __tablename__ = 'personnage_artefact'

    id_personnage_artefact = Column(String(255), primary_key=True)
    personnage_id = Column(String(255), ForeignKey('personnage.id_personnage'))
    artefact_id = Column(String(255), ForeignKey('artefact.id_artefact'))

class PersonnagePouvoir(Base):
    __tablename__ = 'personnage_pouvoir'

    personnage_id = Column(String(255), ForeignKey('personnage.id_personnage'), primary_key=True)
    id_pouvoir = Column(String(255), ForeignKey('pouvoir.id_pouvoir'), primary_key=True)

class PersonnageRelation(Base):
    __tablename__ = 'personnage_relation'

    id_personnage_relation = Column(String(255), primary_key=True)
    personnage1_id = Column(String(255), ForeignKey('personnage.id_personnage'))
    personnage2_id = Column(String(255), ForeignKey('personnage.id_personnage'))
    id_relation = Column(String(255), ForeignKey('relation.id_relation'))
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Pouvoir(Base):
    __tablename__ = 'pouvoir'

    id_pouvoir = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Produit(Base):
    __tablename__ = 'produit'

    id_produit = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    statut = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    prix_unitaire = Column(Integer, nullable=True)
    qte_en_stock = Column(Integer, nullable=True)
    lien_ftp_cover = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class ProduitsDansPanier(Base):
    __tablename__ = 'produitsdanspanier'

    id_produit_panier = Column(String(255), primary_key=True)
    panier_id = Column(String(255), ForeignKey('panier.id_panier'))
    produit_id = Column(String(255), ForeignKey('produit.id_produit'))
    quantite = Column(Integer, nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Race(Base):
    __tablename__ = 'race'

    id_race = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Relation(Base):
    __tablename__ = 'relation'

    id_relation = Column(String(255), primary_key=True)
    relation = Column(String(255), nullable=True)
    id_perso_1 = Column(String(255), nullable=True)
    id_perso_2 = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)

class Ressource(Base):
    __tablename__ = 'ressources'

    id_ressource = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    quantite = Column(String(255), nullable=True)
    annee_id = Column(String(255), ForeignKey('annee.id_annee'))
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)
class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id_utilisateur = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    mot_de_passe = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)
    roles = relationship('UtilisateurRole', back_populates='utilisateur')

class Role(Base):
    __tablename__ = 'role'
    id_role = Column(String(255), primary_key=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)
    utilisateurs = relationship('UtilisateurRole', back_populates='role')

class UtilisateurRole(Base):
    __tablename__ = 'utilisateur_role'
    id_utilisateur_role = Column(String(255), primary_key=True)
    id_utilisateur = Column(String(255), ForeignKey('utilisateur.id_utilisateur'))
    id_role = Column(String(255), ForeignKey('role.id_role'))
    datajoutserver = Column(String(255), nullable=True)
    effacer = Column(String(255), nullable=True)
    utilisateur = relationship('Utilisateur', back_populates='roles')
    role = relationship('Role', back_populates='utilisateurs')
