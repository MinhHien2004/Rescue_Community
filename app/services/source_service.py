from sqlalchemy.orm import Session
from app.models.source import Source
from app.schemas.source import SourceCreate

class SourceService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Source).all()

    @staticmethod
    def get_by_id(db: Session, source_id: int):
        return db.query(Source).filter(Source.id == source_id).first()

    @staticmethod
    def create(db: Session, source_in: SourceCreate):
        db_source = Source(**source_in.dict())
        db.add(db_source)
        db.commit()
        db.refresh(db_source)
        return db_source

    @staticmethod
    def delete(db: Session, source_id: int):
        source = db.query(Source).filter(Source.id == source_id).first()
        if source:
            db.delete(source)
            db.commit()
        return source
    @staticmethod
    def update(db: Session, source_id: int, source_in: SourceCreate):
        source = db.query(Source).filter(Source.id == source_id).first()
        if source:
            for key, value in source_in.dict().items():
                setattr(source, key, value)
            db.commit()
            db.refresh(source)
        return source
