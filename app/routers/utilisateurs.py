import datetime
from fastapi import APIRouter, HTTPException, Depends, status, utils
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt
from jwt import PyJWTError  # Import PyJWTError explicitly
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/utilisateurs",
    tags=["utilisateurs"]
)

# Configuration JWT
SECRET_KEY = "50bfb42481d3b4a81e353dcb1f094e88f70e43d80c5f5d8a313f546c2619998d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/utilisateurs/login")

def authenticate_user(db: Session, username: str, password: str):
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.username == username).first()
    if not utilisateur or not utils.verify_password(password, utilisateur.hashed_password):
        return False
    return utilisateur

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except PyJWTError:  # Correctly handle PyJWTError
        raise credentials_exception
    user = db.query(models.Utilisateur).filter(models.Utilisateur.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/signup", response_model=schemas.Utilisateur)
def create_utilisateur(utilisateur: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    hashed_password = utils.get_password_hash(utilisateur.password)
    db_utilisateur = models.Utilisateur(**utilisateur.dict(), hashed_password=hashed_password)
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    utilisateur = authenticate_user(db, form_data.username, form_data.password)
    if not utilisateur:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": utilisateur.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.Utilisateur)
def read_utilisateurs_me(current_user: schemas.Utilisateur = Depends(get_current_user)):
    return current_user
