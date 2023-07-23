from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, Sequence, DateTime
from sqlalchemy.sql import func
from ..db_setup import Base
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email_id = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=False), server_default = text('now()'))
