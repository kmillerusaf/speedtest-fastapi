from sqlalchemy import Column, Integer, String

from database import Base

class SpeedTestResultStats(Base):
    __tablename__ = "Speedtest"
    
    id = Column(Integer, primary_key=True, index=True)
    public_ip = Column(String)
    download = Column(Integer)
    upload = Column(Integer)
    ping = Column(Integer)
    server_name = Column(String)
    server_id = Column(String)
    timestamp = Column(String)
