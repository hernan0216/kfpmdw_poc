
from typing import List, Optional
from pydantic import BaseModel
from models import Component, Edge

class Dag(BaseModel):
    """
    Represent DAG representing a kubeflow pipelie
    """
    components: List[Component] = []
    edges: List[Edge] = []
