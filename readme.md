### Head First Python notes

##### Chapter 1 - Basics
- installing python 3, you'll get the python interperator, the python shell which is a REPL as well as the in built IDE called IDLE
- you start IDLE by just running idle and using the file menu you create a new file
- you press `F5` to save and run the application
- You can start the REPL by using the command `python3`
  - exit by using the `quit()` command
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
my_var = ''
if my_var == 'hello':
    pass
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
for ch in "hello this is a string":
  print(ch)

#over a fixed amount of times
for i in range(5):
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
- strings are defined with single quotes, double quotes and tripple quotes
- tripple quotes are used as `docstrings` to describe a function as a "standard"
- you can choose either single or double but you should be consistent
- you should check out Pep's (Pep8) to the style guide https://www.python.org/dev/peps/pep-0008/ also PEP 257 about docstrings
- booleans are `True` and `False` the capitalization is important there
- Every object in python can have a truth value associated with it (much like javascript)
- Objects are false when it is, `0`, `None`, empty string, empty data structure (list, tuple, map etc) everything else is true
- use the function `bool()` to create booleans `bool(0)`, `bool('')`, `bool({})` etc
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
- You can also use the built in function (BIF) `dict()` to create a dictionary
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
  - you can create sets with the BIF `set()`
  - they are faster than lists in terms of lookups as lists use sequential lookups
  - insertion order is not maintained
  - literal sets are created with a sequence of items, separated by commas around curly braces
  - sets provide maths like operations `difference`, `union`, `intersection`
  - you can convert a set into a list by using the `list()` function
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
  - can be created using the BIF `tuple()`
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
- `myOuterDict['outerKey']['innerDictKey']`


##### Chapter 4 - Functions and modules
- code resuse is done by using methods/functions, modules and the standard library
- functions are apart of modules and modules are part of the standard library
- functions are defined with the `def` keyword
- values are returned from functions using the `return` keyword
- function comments are created using the tripple String syntax `"""a comment goes here"""` and these are used to describe the function, much like javadoc - also known as a docstring
- one line comments are created using the hash `#` character
- functions can take zero or more parameters
- functions can have multiple return statements
- if you want to return more than one item, you can use the build in data structures or your own types
- after the function parenthesis, you must provide a colon `:`
- functions are known as `functions` when they are not defined within a class but within a class they are known as `methods`

```python
def this_is_a_function(argument1, argument2):
  """this is the standard way to define a function comment, eventhough tripple quotes return a multiline string"""
  #this is how you define a single line comment
  return argument1 #this is how to return a value
```
- as python treats everything as Objects, you do not need to declare the parameters types like in some languages
- To make things readable, you can use function annotations, these will indicate what functions take as argument types and what they return
- this helps the developer so that they do not need to read the functions code
- function argument annotations takes the form `...(argument:type)`
- the function return type annotation takes the form `...() -> type:`

```python
def this_is_a_function(argument1:str, argument2:str) -> str:
  """this is the standard way to define a function comment, eventhough tripple quotes return a multiline string"""
  #this is how you define a single line comment
  return argument1 #this is how to return a value

```
- The Python interperator doesn't use the types to validate your code
- You can define functions that take arguments that have default values when you dont provide the param
- if you call the following function like `my_function()` you will get  'the argument provided is: the default value'

```python
def my_function(argyment:str='my default value') ->str:
  return 'the argument provided is: ' + argument
```
- when calling a function with arguments, you typically use positional assignment
  - this means that the first provided argument maps to the first argument in the function etc
  - in other words, the order of the arguments matter
- python also support `keyword assignment` which means you can call the function with arguments in any order but you must state what argument should be assigned to which function argument

```python
def my_function(name:str, age:int) -> None:
  print(name + " is " + age)

my_function(age=7, name='Jenson')
```
- To define a module, you just create a python file with multiple functions defined
- To use the module, you need to import it using the `import` keyword but to import it the interpertor looks in the `search path`
- You must make sure that the module file only has function definitions and no calls to those functions. This is because when you import them, any invocation will be triggered
- The search path consists of 3 areas of a machine
  - The current working directory
  - site-packages location
    - this is where custom/third party packages
  - standard library locations
- Sometimes the second and third locations may be searched out of order
- To install a module into the site-packages, you need to build it into the correct format called a `distribution package`
  - To build you need to use the tool `setuptools` which comes with python 3.4
  - You need to do 3 things
    - The module file itself, the file that contains all the shared functions
    - Distribution description is required that contains information about your distribution package. this is a file called `setup.py` and lives in the same directory as your module file
    - it contains 2 lines the import of the tool and the invokation with 2 main properties, the name and the py_modules
    
```python
from setuptools import setup
setup(
name='vsearch',
version='1.0',
description='The Head First Python Search Tools',
author='HF Python 2e',
author_email='hfpy2e@gmail.com',
url='headfirstlabs.com',
py_modules=['vsearch'],
)
```
    - And lastly a `README.txt` that contains a description of what this module does. but this can be left empty
- With the 3 files in place, you can create the distribution with the following command on mac `python3 setyp.py sdist` sdist mean source distribution
- This will create a vsearch-1.0.tar.gz file in the dist directory
- To install this file into the site-packages, you will need to use `PIP` e.g. `python3 -m pip install vsearch-1.0.tar.gz`
- With it now installed in your site packages, the functions within it can be used in any python program we write
- To share, you can distribute the compressed file or you can push it to pythons central repo `PyPI` (pie-pee-eye) https://pypi.org/

- Function arguments
- Python supports whats is known as 'by-object-reference call semantics' which means it supports both call by value (copy sent to argument) and call by refernce.
- Depending on the value being sent, it'll choose one of the options
- If you send a `mutable` object, then `call-by-reference` is used 
  - So things like Lists, Sets and Dictionairies will be referenced, so changes to those within a method will change the original copy
- If you send an `immutable` object it'll use `call-by-value`
  - String, Integers and Tuples are copied to the functions

  - pytest is one of the most used testing frameworks
  - it has a plugin architecture
  - you can add the `pep8` plugin to test your code against pep8 compliance
  - You'll need to install pytest and the pip8 plugin using `pep`
  - `pip3 install pytest`
  - `pip3 install pytest-pep8`
  - To run pytest run `py.test` and to check a file for compliance use `py.test --pep8 FILENAME`


##### Chapter 5 - Webapp using Flask
- To use flask, you need to install flask into the environment using pip `pip3 search flask` and `pip3 install flask`
- You can use pypi.python.org to find modules that you can install
- to use flash, you use the `flask` module and import the `Flask` class `from flask import Flask`

```python
from flask import Flask
app = Flask(__name__)  #create an instance of Flash using the dunder name

@app.route('/') #decorator adds the homepage method with a GET route
def homepage() -> str:
    return 'hello'
app.run() #start the app
```
- By default, the route decorator uses the GET request method
- You can change this or even add more methods by providing the `methods` list attribute e.g. `@app.route('/', methods=['GET','POST'])
- You can have multiple decorators applied to a method (multiple app.routes using different urls)
- Start the application with the python3 command `python3 helloWorld.py
- The `app.run()` method call executes the application in a web container, you can add the `debug` attribute to allow for on the fly reload e.g. `app.run(debug=True)`
- templates and static folder need to be under the webapp directory
- templates directory holds the html while static typically has the css
- the webapp directory holds the python script with Flash definitions
- Flask templates use jinja2 which looks like mustache
- Jinja has a base template then other templates extend it filling out jinja2 directives with just content
- The following is the base.html

```html
<!doctype html>
<html>
    <head>
        <title>{{ the_title }}</title>
        <link rel="stylesheet" href="static/hf.css" />
    </head>
    <body>
        {% block body %}

        {% endblock %}
    </body>
</html>
```

```html
{% extends 'base.html' %}
{% block body %}
<h2>{{ the_title }}</h2>
<form method='POST' action='/search4'>
    <table>
        <p>Use this form to submit a search request:</p>
        <tr><td>Phrase:</td><td><input name='phrase' type='TEXT' width='60'></td></tr>
        <tr><td>Letters:</td><td><input name='letters' type='TEXT' value='aeiou'></td></tr>
    </table>
<p>When you're ready, click this button:</p>
<p><input value='Do it!' type='SUBMIT'></p>
</form>
{% endblock %}
```

- the content in the base template with the directives `{% block body %}` and `{% endblock %}` will be replaced by the inherited content
- To show html content, you'll need to have a method that returns `html` types and use the `render_template` method and provide it with the template and properties on the template that need to be replaced

```python
from flask import Flask, render_template
...
@app.route('/render')
def render_example() -> 'html':
    return render_template('firstPage.html', title='this is a dynamic title')
```

- To get posted form parameters you need to use the `request` object
- `from flask import Flask, request`
- The request object has the `form` object that supports bracket notation to get the submited values `request.form['param']`
- Decorated methods can return 'html', 'str' or http codes e.g. '302' for redirect
- To trigger a browser redirect, import the redirect method from the flask module and return the result of it `return redirect('/the_other_url')`
- When replying to a request, if the response has html tags, they may get ignored if they are invalid tags.
  - If you want these tags to be displayed, you would need to escape them
  - To escape html tags, you can use the escape function from the `flask` module

```python
from flask import Flask, escape

def some_endpoint(req:'flask_request', res:str) -> str:
  return escape("<blah>xxx</blah>")
```
- The flask request object contains may attributes and methods, you can use the `dir` function on those objects to get the objects attributes and methods
  - most of the time, you'd need to `form`, `user-agent` and `remote_addr` attributes on the request
- If your using a PAAS or something that will run you code, you may need to not call the running of the code (in this case the `app.run()`)
    - When your in this situation, you could choose to delete the `app.run()` line or do something better
    - Instead use the `dunder name` (__name__) method (the interpreator maintains the initialization and its value and its always the current namespace)
    - if you import a module with `__name__` its value will be the name of the module
- To selectively run the app depending on where you run it, you use the `dunder name dunder main` pattern

```python
if __name__ == '__main__':
  app.run()
```

##### Chapter 6 - Saving data
- To open a file on the filesystem, you use the `open` function, it takes 2 params, a filename and a mode (append/read only/write etc)
  - eg. `todos = open('myTodos.txt', 'a')`
  - You can assign the result of the open function call to a variable, which returns a filestream
  - You can write to the file using the `print` function with an additional 'file' parameter eg. print('my text to write', file=todos)
  - `print` also allows you to define the `end` character that's appended to the the value you supply. The default value is a new line character
  - `print` also allows you to define the `seperator` character between a list of strings eg. `print(str1, str2, str3, sep='|')`
  - To should close the filestream when your done or you could lose data `todo.close()`
  - If you do not provide a mode while opening a file, it's open it in the default readonly mode
  - while a variable is assigned to the filestream, you can use it to print each line of the file
  - The file is made in the same location (pwd) or the main function
```python
tasks = open('file.txt')

for task in tasks:
    print(task)
tasks.close()
```

- A better way of using files is to use the `with` statement

```python
with open('myTodos.txt') as todos:
    for todo in todos:
        print(todo, end='')
```

```python
with open('myTodos.txt') as todos:
    todo = todos.read() #can also use readlines() which reads all contents into a list
return todo
```
- The reason why this one is better is because using `with` automatically closes the filestream when you leave the suite
- The `with` statement conforms to something called to `context management protocol`
  - this allows python to manage the context within the suite allowing the interprator to automatically clean up by calling `close` for you
- When reading strings from a file that has been delimited, you can split the string to a list again using the strings `split` function eg. "string".split("|")
- jinja2 template to iterate over a list of lists

```html
{% extends base.html %}
    {% block body %}
        <h2> {{ title }}</h2>
        <table>
            <tr>
            {% for header in headers %}
                <th>{{ header }}</th>
            {% endfor %}
            </tr>
            {% for row in all_data %}
            <tr>
                {% for row_item in row %}
                <td>{{ row_item }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>

{% endblock %}
```

##### Chapter 7 - Using databases
- The DB-API is build into the standard library that allows you to connect and query a DB
- The DB-API is an abstraction above the DB driver that allows you to generically use any relational database without worry which one
- The MySql database driver needs to be install manually by downloading the driver and following the instructions to install it
- There are other DB drivers for MySql that you can also use
- Once Mysql is installed with the accompanying driver, you can connect to it using the `mysql.connector` and `cursor`

```python
import mysql.connector
dbconfig = {
    'host': 'localhost',
    'user': 'vserch',
    'password': 'mypassword',
    'database': 'vserdatabase',}
conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()
query = """show tables;"""
cursor.execute(query)
result = cursor.fetchall()
print(result)

#the result returned is always a list of tuples so it might be better to iterate and print each tuple
for row in result:
    print(row)
```
- The `**` syntax means that the variable provided gets expanded, in this case, the dict gets split into 4 different variables all being sent to the connect method
- When executing a query with a cursor, you have to retrieve the results using one of three methods
  - fetchone: returns one row of results
  - fetchmany: returns the specified rows of results
  - fetchall: returns all of the results 
- When writing a query that inserts, you would again use the execute method but write the insert with `data placeholders` and a set of values to replace them with

```python
import mysql.connector
my_creds = {'':'',} #fill this out

conn = mysql.connector.connect(**my_creds)
cursor = conn.cursor()
sql_insert = """insert into myTable (id, some_col, another_col) 
values
(%s, %s, %s)
"""
result = cursor.execute(sql_insert, (1, 'value1', 'value2'))
```
- By default, data is held in cache and doesn't always write to the table right away, to ensure that it gets written, you call the connections commit method `conn.commit()`
- Once you have finished querying, you should close your connection and cursor

```python
...
cursor.close()
conn.close()
```
- It would be ideal if we could use the `with x as var` syntax like when we were opening and processing files
  - Its possible to do this with databases/cursors but we'll need to use Classes
  
##### Chapter 8 - Classes
- To use the `with` syntax that manages resources you'll need to create classes
- Classes that implement the `Context Management Protocol` can hook into the `with` syntax
- Classes have `methods` and `attributes`
- Just like in other OOP, you instantiate instances of a class to create objects
- To create a class...

```python
class MyClassName:
    pass
```
- The `pass` keyword above is used in methods and classes to define a class/method that is empty. Without it, the interperator wouldn't know if you've ended the method correctly
- To instantiate an object from a class you call the class with parentheses

```python
class MyClass:
    pass

myVariable = MyClass()
anotherInstance = MyClass()
```
- By convention, functions should be named with lowercase and underscores while classes use camel case, this is so that you can tell at a glance if your calling a class or function
- Methods are called using dot notation followed by the method name and brackets
- When you call a method, the interperator inverts it to call the method on the class with the instance as a parameter

```python
class MyClassName:
    pass

a = MyClassName()
a.callMethod()
#this gets converted to the following but no one really writes code this way
MyClassName.callMethod(a)
```
- this means that every method you define MUST have at least one parameter, with that first parameter being the class type and must be called `self`
- This means that self is always assigned the variable value automatically
- If you don't define the method with the mandatory param, the interperator will error
- The keyword `self` is just like the keyword `this` from other languages

```python
class MyCounter:
    def inc(self) -> None:
        self.value += self.increaments
```
- Just like in other OOP languages, methods have scopes, so any variable defined within the method will be destroyed when out of scope
- So you must use the self param to store/access object attributes
- Variables need to be initialized before you can use them
- In Python the interpretor deals with instanciation while the `__init__` dunder init function deals with initialization
- All classes automatically inherit from the Object class where a lot of dunder functions reside.
  - These dunder functions provide hooks into a classes standard behaviour
  - These can be overridden
  - methods such as the `__eq__`, `__ge__` are like the Java equals method/greater than
  - The dunders from the Object class are also known as `the magic methods`
  - Object properties/attributes can be accessed directly without getters/setters - its like they are public
- The `__init__` function is what is typically the Constructor of a class
- An example of the `__init__` that intializes class attributes
```python
class MyIncClass:
    def __init__(self, start: int=0, step: int=1) -> None :
        self.value = start
        self.step = step
    def inc(self) -> None :
        self.value += self.step

a = MyIncClass(0, 10)
a.inc()
```

- This example shows a class with an dunder init that takes two params or these can be ignored and default values are provided
- The BIF `type()` can be used on an object to get the object type information
- Other BIF's are `id()` and `hex()` which returns the memory address id of an object, and a hex presentation of a number
- When you print an object, it'll run the `__repr__` dunder (which is just like the toString() method) which prints the class name and memory hex address
  - Override this dunder if you want something more nicer

```python
def __repr__(self) -> str:
  str(self.value)
```

##### Chapter 9 - With statement
- To be a class that adheres to the `Context management protocol` you must provide two methods
  - `__init__` dunder init is optional but with all classes, its used to initialize class properties. this runs before anything
  - `__enter__` dunder enter runs before you enter the `with` suite, this can (but doesn't have to) return a value. this runs right after init
  - `__exit__` dunder exit runs once you exit the `with` suite or when an exception occurs within the suite



