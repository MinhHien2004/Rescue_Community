from fastapi import APIRouter, Depends, HTTPException, status
from app.services.rescue_request_service import RescueRequestService
from app.schemas.rescue_request import RescueRequestOut, RescueRequestCreate, RescueRequestUpdate
from sqlalchemy.orm import Session
from app.dependencies import get_db

router = APIRouter(prefix="/rescue_request", tags=["rescue_request"])

@router.get("/", response_model=list[RescueRequestOut])
def get_all(db: Session = Depends(get_db)):
    return RescueRequestService.get_all(db)

@router.get("/{id}", response_model=RescueRequestOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = RescueRequestService.get_by_id(db, id)
    if not item:
        raise HTTPException(404, "Category not found")
    return item

@router.post("/", response_model=RescueRequestOut)
def create(data: RescueRequestCreate, db: Session = Depends(get_db)):
    return RescueRequestService.create(db, data)

@router.put("/{id}", response_model=RescueRequestOut)
def update(id: int, data: RescueRequestUpdate, db: Session = Depends(get_db)):
    item = RescueRequestService.update(db, id, data)
    if not item:
        raise HTTPException(404, "Category not found")
    return item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = RescueRequestService.delete(db, id)
    if not item:
        raise HTTPException(404, "Category not found")
    return {"message": "Deleted successfully"}
