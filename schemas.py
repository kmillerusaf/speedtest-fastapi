from pydantic import BaseModel

class NodeInfo(BaseModel):
    nodename: str
    public_ip: str

class ResultStats(BaseModel):
    download: int
    upload: int
    ping: int
    timestamp: str
    server: dict
    client: dict

    class Config:
        orm_mode = True

class GetResultStats(BaseModel):
    id: int
    public_ip: str
    download: int
    upload: int
    ping: int
    timestamp: str
    server_name: str
    server_id: str

    class Config:
        orm_mode = True
