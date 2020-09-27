from sqlalchemy.orm import Session

import models, schemas

def create_result(db: Session, 
        info: schemas.NodeInfo, result: schemas.ResultStats):
    db_result = models.SpeedTestResultStats(
            public_ip=result.client["ip"],
            download=int(result.download / 1000000),
            upload=int(result.upload / 1000000), 
            ping=result.ping, 
            server_name=result.server["name"], 
            server_id=result.server["id"],
            timestamp=result.timestamp)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


def get_result(db: Session, result: int):
    return db.query(models.SpeedTestResultStats).filter(models.SpeedTestResultStats.id == result).first()

def all_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SpeedTestResultStats).offset(skip).limit(limit).all()
