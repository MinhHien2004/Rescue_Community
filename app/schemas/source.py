from pydantic import BaseModel

class SourceBase(BaseModel):
    url: str
    name: str

class SourceCreate(SourceBase):
    pass

class SourceOut(SourceBase):
    id: int

    class Config:
        orm_mode = True
