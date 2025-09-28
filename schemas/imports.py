from bson import ObjectId
from pydantic import GetJsonSchemaHandler
from pydantic import BaseModel, EmailStr, Field,model_validator
from pydantic_core import core_schema
from datetime import datetime,timezone
from typing import Optional,List,Any
from enum import Enum
import time

class UserRoleBody(BaseModel):
    name:str
    description:str
    
class UserRoles(Enum):
    remote_engineer=UserRoleBody(name="remote_engineer",description="Full system access incl. remote control, video feeds")
    safety_officer= UserRoleBody(name="safety_officer",description="Sensor monitoring, worker tracking, incident reporting")
    maintenance_tech=UserRoleBody(name="maintenance_tech",description="Equipment health, predictive maintenance")
    operator_viewer=UserRoleBody(name="operator_viewer",description="Read-only dashboards")	
    
class UserRolesBase(str,Enum):
    remote_engineer="remote_engineer"
    safety_officer="safety_officer"
    maintenance_tech="maintenance_tech"
    operator_viewer="operator_viewer"
    
    
    

    
