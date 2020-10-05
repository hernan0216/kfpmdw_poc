
from typing import List, Optional
from pydantic import BaseModel
from models import Component

class Edge(BaseModel):
    """
    Represent an edge on a DAG representing a kubeflow pipelie
    """
    origin: Component
    destiny: Component
    port_name: Optional[str]
