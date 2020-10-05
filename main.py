from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from models import Component, Edge

app = FastAPI()


@app.get("/components/structure")
def read_structure():
    """
    Return the component structure.
    TODO: return something like Component.__annotations__ in oder to load the strucrure from class.
    """
    return {"base_url": "string", "packages": "List[string]", "code": "string"}


@app.get("/components/{component_id}")
def read_component(component_id: int, q: Optional[str] = None):
    """
    Read the component object value given an id.
    """
    return {"component_id": component_id, "q": q}


@app.put("/components/{component_id}")
def update_component(component_id: int, component: Component):
    """
    Update a component
    """
    return {"component_name": component.name, "component_id": component_id}


@app.post("/components/")
def create_component(component: Component):
    """
    Create a new component
    """
    return component

@app.post("/edges/")
def create_edge(edge: Edge):
    """
    Create and edge
    """
    return edge
