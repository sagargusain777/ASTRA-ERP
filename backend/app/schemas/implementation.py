from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ImplementationCreate(BaseModel):
    #Basic info
    title:str
    module:str
    sap_version:Optional[str] = None
    difficulty:str
    tags: Optional[str] = None

    #Bussiness Context
    bussiness_scenario : Optional[str] = None
    functional_context : Optional[str] = None

    #Technical flow
    
    architecture_flow :Optional[str] = None
    table_used  : Optional[str] = None
    bapi_used  : Optional[str] = None

    #Working Code
    full_code : Optional[str] = None

    #Debug Performance
    common_errors :Optional[str] = None
    debug_guide : Optional[str] = None
    performance_notes : Optional[str] = None

    #LLM Instruction
    system_prompt : Optional[str] = None


class ImplementationOut(BaseModel):
    id : str
    title : str
    module : str
    sap_version : Optional[str] = None
    difficulty : str
    tags : Optional[str]= None
    bussiness_scenario: Optional[str] = None
    functional_context: Optional[str] = None
    architecture_flow: Optional[str] = None
    table_used: Optional[str] = None
    bapi_used: Optional[str] = None
    full_code: Optional[str] = None
    common_errors: Optional[str] = None
    debug_guide: Optional[str] = None
    performance_notes: Optional[str] = None
    system_prompt: Optional[str] = None
    created_by : str
    created_at : datetime

    model_config = {"from_attributes": True}




