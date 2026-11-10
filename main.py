from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from dependencies import get_current_user, require_role
from models import User, UserRole
from routes.auth import router as auth_router
from routes.admin import router as admin_router

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(admin_router)

@app.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/moderate")
def moderate_page(current_user: User = Depends(require_role(UserRole.ADMIN))):
    return {
        "message": "Страница модератора",
        "user_email": current_user.email    
    }