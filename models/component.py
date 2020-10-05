from typing import List, Optional
import secrets
from pydantic import BaseModel

class Component(BaseModel):
    """
    Represent a lightweight kubeflow Component
    """
    id: str = secrets.token_hex(12)
    name: Optional[str]
    description: Optional[str]
    base_url: Optional[str]
    packages: List[str] = []
    code: Optional[str]
