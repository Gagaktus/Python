import enum
from database import Base, engine
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default=UserRole.USER.value, nullable=False)
    
Base.metadata.create_all(engine)
