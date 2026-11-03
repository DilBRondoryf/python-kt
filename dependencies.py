from fastapi import Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from database import get_session
from models import User
from security import oauth2_scheme, SECRET_KEY


def get_current_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    payload = jwt.decode(token, SECRET_KEY)
    user_id = payload.get("sub")
    user = session.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="Пользователь не найден")

    return user
