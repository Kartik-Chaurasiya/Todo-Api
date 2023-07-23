from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, Sequence, DateTime
from sqlalchemy.sql import func
from ..db_setup import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    todo_name = Column(String, unique=True, nullable=False)
    todo_desc = Column(Text, nullable=False)
    priority = Column(Integer, default=1, nullable=False)
    complete_by = Column(Date, server_default=func.now())
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=False), nullable =False, server_default = text('now()'))
    updated_at = Column(DateTime(timezone=False), nullable =False, onupdate=func.now())
    user = relationship("User")
