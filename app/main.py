from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.component import Component
from app.edge import Edge
from app.dag import Dag
import pdb

app = FastAPI()

"""TODO: implement multitenancy for Dags cration."""
DEFAULT_DAG = Dag()


@app.get("/components/schema")
def read_shema():
    """TODO: return something like Component.__annotations__."""
    return {
        "name": "string",
        "description": "string",
        "base_image": "string",
        "packages": ["string"],
        "source": ["string"],
    }


@app.post("/components/")
def create_component(component: Component):
    """Create a new component."""
    DEFAULT_DAG.components.append(component)
    return component


@app.post("/edges/")
def create_edge(edge: Edge):
    """Create and edge."""
    DEFAULT_DAG.edges.append(edge)
    return edge

@app.get("/pipelines")
def read_dag():
    return DEFAULT_DAG

@app.get("/pipelines/deploy")
def deploy_dag():
    """Deploy dag as a kubeflow pipeline on kubernetes."""
    try:
        DEFAULT_DAG.compile()
    except (NotImplementedError) as error:
        return {"error": "NotImplentedError" + str(error)}
