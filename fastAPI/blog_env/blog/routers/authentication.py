from datetime import datetime, timedelta,timezone
import os
from typing import Optional
from jose import jwt
from dotenv import load_dotenv
from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext


from blog import models,schemas
from blog.database import get_db


router=APIRouter(
    tags=["Authentication"]
)




def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    load_dotenv()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user=db.query(models.UserModel).filter(models.UserModel.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found",
                            headers={"WWW-Authenticate":"Bearer"})
    
    if not pwd_context.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    
    acess_token_expires=timedelta(minutes=60)
    access_token=create_access_token(data={"sub":user.email},expires_delta=acess_token_expires)
    # return_user = schemas.ShowUser(email=user.email, username=user.username)
    # return {"user":return_user,
    #         "access_token":access_token,
    #         "token_type":"bearer"}
    return {"email": user.email, 
            "username": user.username,
              "access_token": access_token, 
              "token_type": "bearer"}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception
    user = db.query(models.UserModel).filter(models.UserModel.email == email).first()
    if user is None:
        raise credentials_exception
    # token_data=schemas.TokenData(email=email)

    return user


@router.post("/logout", status_code=status.HTTP_200_OK)
def logout_user():
    response = {"message": "User logged out successfully"}
    return response


# // Example code in JavaScript to handle the logout request
# fetch('/logout', {
#   method: 'POST',
#   headers: {
#     'Content-Type': 'application/json',
#     // Include the authentication token if required
#     'Authorization': `Bearer ${token}`
#   }
# })
# .then(response => {
#   if (response.ok) {
#     // Clear the user details from sessionStorage
#     sessionStorage.removeItem('user');
#     console.log('User logged out successfully');
#   }
# })
# .catch(error => {
#   console.error('Error logging out:', error);
# });


