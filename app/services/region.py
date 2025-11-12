from sqlalchemy.orm import Session
from app.models.region import Region
from app.schemas.region import RegionCreate, RegionUpdate

def get_all(db: Session):
    return db.query(Region).all()

def get_by_id(db: Session, id: int):
    return db.query(Region).filter(Region.id == id).first()

def create(db: Session, data: RegionCreate):
    new = Region(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def update(db: Session, id: int, data: RegionUpdate):
    item = get_by_id(db, id)
    if not item:
        return None
    for key, value in data.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, id: int):
    item = get_by_id(db, id)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item
