from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.region import RegionCreate, RegionUpdate, RegionResponse
from app.services import region

router = APIRouter(prefix="/region", tags=["Region"])

@router.get("/", response_model=list[RegionResponse])
def get_all(db: Session = Depends(get_db)):
    return region.get_all(db)

@router.get("/{id}", response_model=RegionResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = region.get_by_id(db, id)
    if not item:
        raise HTTPException(404, "Region not found")
    return item

@router.post("/", response_model=RegionResponse)
def create(data: RegionCreate, db: Session = Depends(get_db)):
    return region.create(db, data)

@router.put("/{id}", response_model=RegionResponse)
def update(id: int, data: RegionUpdate, db: Session = Depends(get_db)):
    item = region.update(db, id, data)
    if not item:
        raise HTTPException(404, "Region not found")
    return item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = region.delete(db, id)
    if not item:
        raise HTTPException(404, "Region not found")
    return {"message": "Deleted successfully"}
