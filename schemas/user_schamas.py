# Importing Libraries
from pydantic import BaseModel
from typing import Any, Optional

# Initializing
class check_user(BaseModel):
    username : str
    
