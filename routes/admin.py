from fastapi import APIRouter, Depends

from dependencies import require_role
from models import User, UserRole

router = APIRouter(prefix="/admin")

@router.get("/stats")
def get_stats(current_user: User = Depends(require_role(UserRole.ADMIN))):
    return {
        "message": "Секретная статистика админа",
        "admin_email": current_user.email
    }