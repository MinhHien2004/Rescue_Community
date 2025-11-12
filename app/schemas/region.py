from pydantic import BaseModel

class RegionBase(BaseModel):
    name: str
    parent_id: int | None = None

class RegionCreate(RegionBase):
    pass

class RegionUpdate(RegionBase):
    pass

class RegionOut(RegionBase):
    id: int

    class Config:
        orm_mode = True

class RegionResponse(RegionBase):
    id: int

    class Config:
        from_attributes = True