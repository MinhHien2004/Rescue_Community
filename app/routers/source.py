from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.source import SourceOut, SourceCreate
from app.services.source_service import SourceService
from app.dependencies import get_db

router = APIRouter(prefix="/source", tags=["source"])

@router.get("/", response_model=list[SourceOut])
def get_all_sources(db: Session = Depends(get_db)):
    return SourceService.get_all(db)

@router.get("/{source_id}", response_model=SourceOut)
def get_source_by_id(source_id: int, db: Session = Depends(get_db)):
    source = SourceService.get_by_id(db, source_id)
    if not source:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Source not found")
    return source

@router.post("/", response_model=SourceOut, status_code=status.HTTP_201_CREATED)
def create_source(source_in: SourceCreate, db: Session = Depends(get_db)):
    return SourceService.create(db, source_in)

@router.delete("/{source_id}", response_model=SourceOut)
def delete_source(source_id: int, db: Session = Depends(get_db)):
    source = SourceService.delete(db, source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source
@router.put("/{source_id}", response_model=SourceOut)
def update_source(source_id: int, source_in: SourceCreate, db: Session = Depends(get_db)):
    source = SourceService.update(db, source_id, source_in)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source
