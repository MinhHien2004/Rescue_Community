from fastapi import FastAPI
from app.routers import rescue_request, category, region, source
from app.db.database import Base, engine
import uvicorn
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(rescue_request.router)
app.include_router(category.router)
app.include_router(region.router)
app.include_router(source.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)