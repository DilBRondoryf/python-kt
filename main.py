from fastapi import FastAPI, Depends

from dependencies import get_current_user
from models import User
from routes.auth import router as auth_router
from routes.admin import router as admin_router
from dependencies import require_role, UserRole


app = FastAPI()
app.include_router(auth_router)
app.include_router(admin_router)

@app.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/moderate")
def moderate_page(current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.MODERATOR))):
    return {
        "message": "Страница модератора",
        "user_email": current_user.email    
    }