### Head First Python notes

##### Chapter 1 - Basics
- installing python 3, you'll get the python interperator, the python shell which is a REPL as well as the in built IDE called IDLE
- you start IDLE by just running idle and using the file menu you create a new file
- you press `F5` to save and run the application
- variables are defined without any keyword and assignment is done with an equals operator
- variable types are inferred by its initialized value

```python
this_is_a_variable = "hello"
```
- literal lists are defined using `[]`

```python
my_arr_of_numbers = [1, 2, 3, 4, 5]
```
- you don't need to end a statement with semi colons
- there is no main method
- blocks of code are called `suites` and you can have nested suites
- `suites` are defined without curly braces but with indentations and preceded by a colon `:`

```python
if my_var == 'hello'
```
- python comes with many `modules` that allow you to import functionality into an application
- these `modules` contain `submodules` or `functions` that can also be imported individually
- some of these packages are...
  - os
  - json
  - random
  - enum
  - datetime
  - sys
  - time
- you can use a package by using the keyword `from` at the top of a file
- do have something like a static import from java, you use the following syntax

```python
from os import getcwd
my_dir = getcwd()
print(my_dir)
```
- you dont need to do static imports, you can just import an entire module but you'll need to prefix the function with the module name
- these two import techniques are known as specific and non specific imports.
- if you always use specific imports you might end up with 2 different modules that have functions with the same name and therefore you'll get collision python wouldn't know what function to call when invoked

```python
import os
my_dir = os.getcwd()
print(my_dir)
```
- Using the python shell (REPL) you can use the `dir()` function to query things.
- To get a list of functions/attributes of a modules, you just call `dir(module_name)`
- note: in order to query it, you must first import it
- calling `dir()` with no args will list the current imported modules/functions

```python
>>>dir(random)
```
- To get more information about a module for a function, you can use the help function

```python
>>>help(os)
>>>help(getcwd)
```
- function calls are done with parentheses `()`
- attributes on objects are access directly with the dot notation
- python comes with the standard set of operators, <,>,<=,>=,==,!= and =
- `if` statements are defined as, don't forget the `:` and the indentation of the `suite`

```python
if var == 'x':
  print('the var is x')
elif var == 'y':
  print
```
- looping
  - you can loop using `for` and `while` loops
  - in general, there are 3 different type of for loops
    - loop across a list / array
    - iterate over a string
    - loop a set number of times
  - while looping you must remember to indent the suite and have a colon

```python
#over a list
for i in [1, 2, 3, 4, 5]:
  print(i)

#over a string
for ch in "hello this is a string"
  print(ch)

#over a fixed amount of times
for i in range(5)
  print('hello')
```
- range is actually a function that will return an array of integers from 1 to the number provided
- the range loop has a number of overloaded variants
```python
#basic fixed loop
for i in range(5):
  xxx
#loop starting from one number to the next, first number is inclusive the end number is exclusive
for i in range(10, 100)
#loop between 2 numbers with a step
for i in range(99, 1, -1)
```
- You can create a list by using in the `list` function

```python
list_of_five = list(range(5))
```

##### Chapter 2 - Lists
- variables are dynamic and they infer their types during initilization
- variables can be redefined to a different type
- there are numbers, strings, booleans and Objects
- booleans are `True` and `False` the capitalization is important there
- everything is basically an object (string, numbers, functions, modules)
- Python is `Object Based` and not purely `Object oriented`

```python
greeting = "hello"
greeting = 12334
```
- Python has 4 main collection types
  - lists - ordered and mutable, can dynamically grow
  - tuple - ordered list but immutable and static in size
  - dictionary - also known as map, hash etc key val pair
  - set - like java, non duplicate and un ordered
- Lists, unlike in java can hold anything, you can mix the types
  - you dont restrict the types during initialization
  - you can define a list with `[]`
  - literal lists are defined like `variable = [1, 2, 3]`
  - the `len()` function can be used to return the size of a list
  - `in` and `not in` are operators that can be used to check if a value is in or not in a list `if 'a' in ['a']:`
  - lists have some basic functions
    - `append` - to add an item
    - `remove` - remove a certain object from the list
    - `pop` - remove from the end or an index
    - `extend` - add a list to this list
    - `insert` - add at a certain index
    - `copy` - create a return a copy of the list
- when creating a list, if you assign a variable to that first variable, your basically creating a reference, NOT a copy to that list

```python
my_list = [1]
my_second_list = my_list
#both my_list and my_second_list point to the same list

my_third_list = my_second_list.copy()
```

- python support square bracket notation with lists `my_list[0]`
- you can also use negative numbers in the square brackets to iterate from the end of the list e.g. `my_list[-1]` will return the last object `my_list[-2]` second to last
- list the `range()` function, lists support the start, stop and step notation

```python
my_list = [1,2,3,4,5]
my_list[1:2:1] #start at index 1, stop at index 1 over 1 increments
```
- each value of the start, stop steps and be omitted and have default values
  - start, defaults to 0
  - stop, defaults to the last index
  - step defaults to 1

```python
my_list = [1,2,3,4,5]
my_list[:2:1] #start at index , stop at index 1 over 1 increments
```
- the step can actually be negative, doing so will iterate the list backwards
- you can use just the start and stop and it will behave like a slice
- slicing doesn't mutate the list, it just returns a copy of the values
- The `Manipulation character` is `*` and it multiplies the amount of things using a print `print("hello " * 3)`

##### Chapter 3 - Structured Data
- You can get input from the user via the terminal by using the function `input("prompt")`
- Using the function `type(var)` on a variable returns the class of that variable
- Dictionarys or dict's are just like java maps
- Dictionarys are key value stores that are unordered
- Literal dict's look like json

```python
my_dictionary =
{
'myKey1': 'blah',
'my_key_2': 'blahblah'
}
```
- An empty dictionary literal looks like `myVal = {}`
- Dictionary's support bracket notation for both accessing the values AND setting them

```python
my_dictionary['myKey1'] #prints out the value 'blah'
my_dictionary['my_key_2'] = 'some other value' #sets the value of that key
```
- There is no increment or decrement operators `myval++` or `myval--` you must use the `+=` or `-=` operators instead
- Iterating through a map with a for loop only iterates through the keys
- If you want to access the values too, you'll need to use the bracket notation

```python
myDict =
{
 'a': 1,
 'b': 2,
 'c': 3
}

for k in myDict:
  print('the key is:', k, 'and the value is', myDict[k])
```
- As Dict's are unordered, the ordering isn't preserved. If you want to iterate in a
known order, you and sort the keys before iterating in a for loop

```python
for k in sorted(mydict):
  print('the key is:', k, 'and the value is', myDict[k])
```
- An `items` is an alternative way to loop through a dict when you want both they key and values. You do so by using the `items()` method on the dict in a loop

```python
for k, v in sorted(myDict.items()):
  print('the key is:', k, 'and the value is', v)
```
- List lists, you can use the `in` (as well as the `not in`) operator to see if a map contains a key

```python
if 'a' in myMap:
  print('its in')
```
- The ternary operator `?:` is supported in python but has a different syntax

```python
x = 5 if y > 3 else 10
```
- Accessing a value of a key in a Dictionary will result in a `KeyError`
- When you have a scenario where you want to check if a key exists and if not create it, its so common that there are a number of ways to do it

```python
if 'myKey' in myMapCounters:
  myMapCounters['keyKey'] += 1 #increment if it exists
else:
  myMapCounters['myKey'] = 0  #initialize key and value if it doesn't exist

#You can shorten it by doing these 3 lines instead of 4
if 'myKey' not in myMapCounters:
  myMapCounters['myKey'] = 0

myMapCounters['myKey'] += 1

#its so common you can do it all in 2 lines using the setdefault() method
myMapCounters.setdefault('myKey', 0) #set a default value if the key isnt there
myMapCounters['myKey'] += 1
```
- Sets are data structures that dont allow duplicates
  - they are faster than lists in terms of lookups as lists use sequential lookups
  - insertion order is not maintained
  - literal sets are created with a sequence of items, separated by commas around curly braces
  - sets provide maths like operations `difference`, `union`, `intersection`
  - you can convert a set into a list by using the `list` function
```python
mySet = {'a value', 'another value', 'some other value'}
#sort hand if you want a set of individual characters from a String
anotherSet = set("this string will be split into individual characters")
```
- `union` combines two sets and return the combination without modifying the original 2
- `difference` returns a set that displays what is in the set you ran it on, compared to the provided set
- `intersection` returns a set that displays what is common in both sets

```python
evens = {2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
oneToTen = evens.union(odds) #combines both evens and odds

someEvens = {4, 6}

diff = evens.difference(someEvens) #will return set of 2, 8, 10 as they dont exist in someEvens
anotherDiff = someEvens.difference(evens) #will return empty set as evens contains all of someEvens

intersection = evens.intersection(someEvens) #returns a set of 4 and 6
```
- Tuples are a little like lists
  - they keep their insertion order
  - they are immutable
  - tuple literals are created with a sequences of items, separated by commas between parenthesis
  - one rule about making type literals is that `THERE MUST BE AT LEAST ONE COMMA`
  - so if you want a single valued tuple, add a comma to the end of the list
  - they support the same square bracket notation to access values at an index

```python
myTuple = (1,2,3,4,5)

myTuple[0] = 10 #this will throw an error

myOtherTyple = ("SINGLE VALUE TUPE",) #DONT FORGET THE COMMA AT THE END
```
- pprint is a module that stands for pretty print
  - its used to print out dictionarys nicer on the prompt

```python
import pprint

pprint.pprint(mydict)
```
- if you've got a dictionary in a dictionary, when you want to access the nested dictionary, you use the double square bracket notation
- `myOuterDict['outerKey']['innerDictKey']
