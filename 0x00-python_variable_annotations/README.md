## 0x00.Python-Variable Annotations

This is a way of explicitly stating the data type of a variable.
This helps in debugging, readability, and assist with the type checking
It does not enforce the type at runtime though.
```python
# without variable annotation
x = 10
y = 'Hellow'

# with variable annotation
x: int = 10
y: str = 'Hello'

```
_Syntax_:
	<variable_name>: <variable_type> = <value_of_variable>

_Function Annotations_
You can use this to seet the type of the parameters, and the return type
```Python
def greetings(name: str) -> str:
	return f"Hello, {name}"

def sum(a: int, b: int) -> int:
	return a + b
```

_Complex Types_
You can you use it for more complex types like list, dictionaries and custom types
You will have to import List, Dict, Tuple, Optional from typing
```python
from typing import List, Dict, Tuple, Optional


numbers: List[int] = [1, 2, 3, 4, 5]
prersion: Dict[str, str] = {'name'= 'Michael', 'age': '30'}
condinates: tuple[int, int] = (10, 20)

# Optional type for values that could be none
def find_item(items: List[str], key: str) -> Optional[str]:
	for item in items:
		if item == key:
			return item
	return None
```
Optional : This is used when the function can either return something or None


_Type Aliases_
```python
from typing import Dict
ScoreMap = Dict[str, int]

sores: ScoreMap = {'Alice': 90, 'Bob': 78'}

# Functiont to add a new score

def add_score(scores: ScoreMap, name: str, score: int) -> None:
	score[name] = score

def get_score(scores: ScoreMap, name: str) -> int:
	return sorces.get(name, 0)

```
