import pdb
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.component import Component
from app.edge import Edge
from app.dag import Dag
import pdb

app = FastAPI()

"""TODO: implement multitenancy for Dags cration."""
DEFAULT_DAG = Dag(name="one_session")


@app.get("/components/schema")
def read_shema():
    return Component.schema()


@app.post("/components/")
def create_component(component: Component):
    """Create a new component."""
    DEFAULT_DAG.add_component(component)
    return component


@app.post("/edges/")
def create_edge(edge: Edge):
    """Create and edge."""
    origin_cmp = DEFAULT_DAG.get_component(edge.origin)
    destiny_cmp = DEFAULT_DAG.get_component(edge.destiny)
    DEFAULT_DAG.add_edge(origin_cmp, destiny_cmp)
    return edge

@app.get("/pipelines")
def read_dag():
    return {"nodes": [node for node in DEFAULT_DAG.nodes()], "edges": [edge for edge in DEFAULT_DAG.edges()]}

@app.get("/pipelines/deploy")
def deploy_dag():
    """Deploy dag as a kubeflow pipeline on kubernetes."""
    try:
        DEFAULT_DAG.compile()
    except (NotImplementedError) as error:
        return {"error": "NotImplentedError" + str(error)}
