from typing import Optional
from numpy import ndarray, DtypeType, ShapeType

# if you add to this set of functions,
#   please also add them to RandomState() below
def rand(*args: int) -> ndarray[float]: ...
def randn(*args: int) -> ndarray[float]: ...
def ranf(*args: int) -> ndarray[float]: ...
def random(size: ShapeType=None) -> float: ...
def randint(low: int, high: int=None, size: ShapeType=None, dtype: DtypeType=int) -> ndarray[int]: ...

# if you add to this set of functions,
#   please also add them to the top-level module above
class RandomState:
    def __init__(self, seed: Optional[int] = None) -> None: ...
    def rand(self, *args: int) -> ndarray[float]: ...
    def randn(self, *args: int) -> ndarray[float]: ...
    def ranf(self, *args: int) -> ndarray[float]: ...
    def random(self, size: ShapeType=None) -> float: ...
    def randint(self, low: int, high: int=None, size: ShapeType=None, dtype: DtypeType=int) -> ndarray[int]: ...
