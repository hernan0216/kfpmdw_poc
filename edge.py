from typing import List, Optional
from pydantic import BaseModel

class Edge(BaseModel):
    """
    Represent an edge on a DAG representing a kubeflow pipelie
    """
    origin: str
    destiny: str
    port_name: Optional[str]
