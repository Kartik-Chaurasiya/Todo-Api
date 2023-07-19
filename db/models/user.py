from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, Sequence, DateTime
from sqlalchemy.sql import func
from ..db_setup import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email_id = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
