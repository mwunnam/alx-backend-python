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
'->' tells the return value
'a: int, b: int' This is declaring the parameters with their types

_Complex Types_
You can you use it for more complex types like list, dictionaries and custom types
You will have to import List, Dict, Tuple, Optional from typing
```python
from typing import List, Dict, Tuple, Optional


numbers: List[int] = [1, 2, 3, 4, 5]
prersion: Dict[str, str] = {'name'= 'Michael', 'age': '30'}
condinates: Tuple[int, int] = (10, 20)

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

_Union_
This is to indicate that a value can be of several type. This is useful when a parameter or a retrn value can be of multiple types.
```Javascript
from typing import Union

def example_function(x: Union[int, str]) -> None:
	if isinstance(x, int);
		print(f"x is an interger: {x}")
	elif ininstace(x, str):
		print(f"x is a string: {x}")
```

_Union_
This provides a way for you to indicate that a value of a parameter can be of several type.
_syntax_
```python
x: Union[type1, type2]
```
_example 1_
```python
def add(x: Union[int, float]) -> float
	return x + 20
```
_example 2_
```python
def check_value(condition: bool) -> Union[int, None]
	if condition:
		return 42
	else:
		return None
```

_Callable_
Thi is to indicate that a parameter or a return value should be a function.
This i useful if you want to indicate that a variable should be a function with a specified type and return type.
This is in the 'typing modulel'

_syntax_
```Python
from typing import Callable
Callable[[arg1_type, arg2_type, ...], return_type]
```

_example function parameters_
```python
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
	return func(a, b)

def add(x: int, y: int) -> int:
	return x + y

def multiply(x: int, y: int) -> int:
	return x * y

# Usage
print(apply_function(add, 2, 3))
print(apply_function(multiply, 2, 3))
```

_example return a Callable_
```python
from typing import Callable

def make_adder(addend: int) -> Callable[[int], int]:
	def adder(value: int) -> int:
		return value + addend
	return adder

add_5 = make_adder(5)
print(add_5(10))  // output: 15
```
_explanation_
1. when you do add_5 =make_adder(5)
	add_5 will have the value of adder function
	add_5 will now act as a function which can take an int type
2. When you do print(add_5(10)).
	10 now becomes the 'value' in the adder function and and the return an int which will be 15




