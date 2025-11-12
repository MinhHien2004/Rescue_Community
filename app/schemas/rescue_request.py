from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RescueRequestBase(BaseModel):
    category_id: int
    title: str
    location: Optional[str] = None
    content: Optional[str] = None
    map_link: Optional[str] = None
    status: Optional[str] = None
    source_id: Optional[int] = None
    posted_time: Optional[str] = None
    created_date: Optional[datetime] = None
    image: Optional[str] = None
    urgency_score: Optional[float] = None
    reliability_score: Optional[float] = None
    contract: Optional[str] = None
    post_url: Optional[str] = None
    region_id: Optional[int] = None

class RescueRequestCreate(RescueRequestBase):
    pass

class RescueRequestUpdate(RescueRequestBase):
    pass
class RescueRequestOut(RescueRequestBase):
    id: int

    class Config:
        orm_mode = True
