from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, Sequence, DateTime
from sqlalchemy.sql import func
from ..db_setup import Base

class User(Base):
    __tablename__ = "todo"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    user_id = Column(Integer, unique=False, index=True, nullable=False)
    todo_name = Column(String, unique=True, index=True, nullable=False)
    todo_desc = Column(Text, unique=True, nullable=False)
    priority = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
