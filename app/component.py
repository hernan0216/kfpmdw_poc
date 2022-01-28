import pdb
from typing import List, Optional, Union
from pydantic import BaseModel
from uuid import UUID
import maps

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

    def __hash__(self):
        """Hasheable object in order to use as a DiGraph node."""
        return hash(maps.FrozenMap.recurse(self.dict()))

    def __eq__(self, other):
        return self.__hash__ == other.__hash__
