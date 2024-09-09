# 0x03-Unittests_and_integration_tests

## Project on Unittests and Integrations Test

1.  To Know the difference between unit and interation test.
2.  Common testing patterns such as mocking, parametrizations and fixutres



## **Task 0**
*What is Mapping and Sequence*: They are abstract base classes that describe the
the expected types for nest_map.

*Mapping:* is a generic type that represents any object that supports
key-value access like dictionaries

*Sequence:* is a generic type that represents any objects represents an
ordered collectoin ex. list, tuple


**What is the access_nested_map used for**
This function is used to access a value deep within a nested dictionary by following a sequence of keys
- It starts with the outer outer dictionary (nested_map)
- Iterate over the path: Each key in the path sequence is used to access a level deeper in the dictionary
- It will then return the value obtained after following all keys in the path

**Parameterized**
It is a module in python which allows you to run a single test method multiple
times with different sets of parameters. Very helpful when you want to test the same
functionality with diffenrent conditions without writting separate codes of each case.
*How it works*: The @parameterized.expand decorator is used to pass multiple
set of parameters is used to run the test method independely.
1. import parameterized so that you can used the @parameterized.expand decorator
2. Define Test Cases, you define a list of tuple where each tuple contains the arguments that will be passed to the method. the tuples shold match the method's signature

1. import parameterized so that you can used the @parameterized.expand decorator
2. Define Test Cases, you define a list of tuple where each tuple contains the arguments that will be passed to the method. the tuples shold match the method's signature
1. import parameterized so that you can used the @parameterized.expand decorator
2. Define Test Cases, you define a list of tuple where each tuple contains the arguments that will be passed to the method. the tuples shold match the method's signature
1. import parameterized so that you can used the @parameterized.expand decorator
2. Define Test Cases, you define a list of tuple where each tuple contains the arguments that will be passed to the method. the tuples shold match the method's signature
3. Decorate the method, apply the @parameterized.expand decorator to the test method, pass the list to tuples as an argument to the decorator. This list will represent the different cases.
4. Run the test, the test method will executed once for each tuple in the list.
