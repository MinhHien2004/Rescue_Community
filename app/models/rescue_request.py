from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class RescueRequest(Base):
    __tablename__ = "rescue_request"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    title = Column(String, nullable=False)
    location = Column(String, nullable=True)
    content = Column(String, nullable=True)
    map_link = Column(String, nullable=True)
    status = Column(String, nullable=True)
    source_id = Column(Integer, ForeignKey("source.id"))
    posted_time = Column(String, nullable=True)  # Hoặc DateTime nếu sau này muốn chuẩn hóa
    created_date = Column(DateTime, default=datetime.utcnow)
    image = Column(String, nullable=True)
    urgency_score = Column(Float, nullable=True)
    reliability_score = Column(Float, nullable=True)
    contract = Column(String, nullable=True)
    post_url = Column(String, nullable=True)
    region_id = Column(Integer, ForeignKey("region.id"))
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)

    category = relationship("Category")
    source = relationship("Source")
    region = relationship("Region")
