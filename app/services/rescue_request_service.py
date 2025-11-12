from sqlalchemy.orm import Session
from app.models.rescue_request import RescueRequest
from app.schemas.rescue_request import RescueRequestCreate, RescueRequestUpdate

class RescueRequestService:
    @staticmethod
    def get_all(db: Session):
        return db.query(RescueRequest).all()
    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(RescueRequest).filter(RescueRequest.id == id).first()
    @staticmethod
    def create(db: Session, data: RescueRequest):   
        new = RescueRequest(**data.model_dump())
        db.add(new)
        db.commit()
        db.refresh(new)
        return new
    @staticmethod
    def update(db: Session, id: int, data: RescueRequestUpdate):
        item = db.query(RescueRequest).filter(RescueRequest.id == id).first()
        if not item:
            return None
        for key, value in data.model_dump().items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item
    @staticmethod
    def delete(db: Session, id: int):
        item = db.query(RescueRequest).filter(RescueRequest.id == id).first()
        if not item:
            return None
        db.delete(item)
        db.commit()
        return item
