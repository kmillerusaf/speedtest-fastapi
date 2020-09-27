from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/get_result/{result}", response_model=schemas.GetResultStats)
def get_result(result: int, db: Session = Depends(get_db)):
    results = crud.get_result(db, result=result)
    return results

@app.get("/api/v1/all_results/", response_model=List[schemas.GetResultStats])
def all_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = crud.all_results(db, skip=skip, limit=limit)
    return results

@app.post("/api/v1/upload_result", status_code=201)
def create_result(
        info: schemas.NodeInfo, result: schemas.ResultStats, 
        db: Session = Depends(get_db)):
    return crud.create_result(db=db, info=info, result=result)
