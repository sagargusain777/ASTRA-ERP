from uuid import uuid4
from sqlalchemy import Column , String , Integer , DateTime , Boolean ,ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Implementation(Base):
    __tablename__ = "implementations"

    #Primarykey
    id = Column(String,primary_key = True,index = True , default = lambda:str(uuid4()))
    #Basic Information
    title = Column(String(256),nullable = False , index = True)
    module = Column(String(72), nullable = False)
    sap_version = Column(String(50), nullable = True)
    difficulty = Column(String(20), nullable = False)
    tags = Column(String(500), nullable = False)

    #Bussiness Context

    bussiness_scenario = Column(Text , nullable = True)
    functional_context =  Column(Text, nullable = True)
    #Technical Flow 

    architecture_flow = Column(Text , nullable = True)
    table_used = Column(Text , nullable = True)
    bapi_used = Column(Text , nullable = True)
    #Working Code
    full_code = Column(Text , nullable = True)
    #Debug Performance
    common_errors = Column(Text, nullable=True)
    debug_guide = Column(Text, nullable=True)
    performance_notes = Column(Text, nullable=True)
    # LLM Instructions
    system_prompt = Column(Text, nullable=True)

    #Metadata
    created_by = Column(String,ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default = func.now())

    #Relationship
    creator = relationship("User",backref="implementations")
