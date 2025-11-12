from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('region.id'), nullable=True)
    name = Column(String, nullable=False)
