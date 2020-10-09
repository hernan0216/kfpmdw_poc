from typing import List, Optional, Union
from pydantic import BaseModel
from uuid import UUID

class Component(BaseModel):
    """
    Represent a lightweight kubeflow Component
    """
    id: Union[int, str, UUID]
    name: Optional[str]
    description: Optional[str]
    base_image: Optional[str]
    packages: List[str] = []
    source: List[str] = []
