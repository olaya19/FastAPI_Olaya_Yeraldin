from datetime import datetime, timedelta

from jose import jwt

SECRET_KEY = "secreto_super_seguro"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
