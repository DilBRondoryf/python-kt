from fastapi import FastAPI, Depends

from dependencies import get_current_user
from models import User
from routes.auth import router
from security import oauth2_scheme


app = FastAPI()
app.include_router(router)

@app.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return current_user