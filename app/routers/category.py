from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import category

router = APIRouter(prefix="/category", tags=["Category"])

@router.get("/", response_model=list[CategoryResponse])
def get_all(db: Session = Depends(get_db)):
    return category.get_all(db)

@router.get("/{id}", response_model=CategoryResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = category.get_by_id(db, id)
    if not item:
        raise HTTPException(404, "Category not found")
    return item

@router.post("/", response_model=CategoryResponse)
def create(data: CategoryCreate, db: Session = Depends(get_db)):
    return category.create(db, data)

@router.put("/{id}", response_model=CategoryResponse)
def update(id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    item = category.update(db, id, data)
    if not item:
        raise HTTPException(404, "Category not found")
    return item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = category.delete(db, id)
    if not item:
        raise HTTPException(404, "Category not found")
    return {"message": "Deleted successfully"}
