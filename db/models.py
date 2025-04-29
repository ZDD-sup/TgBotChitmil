from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base

class UserChitmil(Base):
    __tablename__ = "user_chitmil"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, nullable=False)
    what_allow = Column(String, nullable=False)
    day_name = Column(String, nullable=False)
    period = Column(Integer, nullable=False)
    increase = Column(Boolean, default=False)
