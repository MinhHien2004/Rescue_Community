from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Source(Base):
    __tablename__ = "source"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
