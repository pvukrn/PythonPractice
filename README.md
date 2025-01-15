# 1.	Data Types:
### Numeric Types:
•	int: Integer values, e.g., 42
•	float: Floating-point values, e.g., 3.14
•	complex: Complex numbers, e.g., 3+4j
### Sequence Types:
•	str: String, a sequence of characters, e.g., "Hello, World!"
•	list: Ordered, mutable collection, e.g., [1, 2, 3, 4]
•	tuple: Ordered, immutable collection, e.g., (1, 2, 3, 4)
### Mapping Type:
•	dict: Collection of key-value pairs, e.g., {"name": "Alice", "age": 25}
### Set Types:
•	set: Unordered collection of unique elements, e.g., {1, 2, 3}
•	frozenset: Immutable version of a set, e.g., frozenset([1, 2, 3])
### Boolean Type:
•	bool: Boolean values, True or False
### Binary Types:
•	bytes: Immutable sequence of bytes, e.g., b'hello'
•	bytearray: Mutable sequence of bytes, e.g., bytearray(b'hello')
•	memoryview: Allows memory access without copying, e.g., memoryview(b'hello')
### None Type:
•	NoneType: Represents the absence of a value, e.g., None
### Mutable vs Immutable Types
•	Mutable: Objects that can be changed after creation. Examples: list, dict, set
•	Immutable: Objects that cannot be changed after creation. Examples: int, float, str, tuple
Understanding this distinction is crucial, as it affects how data is passed around in your programs and how efficiently your code runs.
### Type Hints and Annotations
Type hints provide a way to specify the expected data types of function arguments and return values. This is especially useful for improving code readability and for tools like linters and IDEs to provide better support.
### Custom Data Types with NamedTuple and dataclass
For more structured and readable code, you can create your own data types using NamedTuple or dataclass.
### Type Conversion and Casting
Python provides functions to convert one data type to another, also known as type casting.
### Abstract Base Classes (ABCs)
ABCs allow you to define abstract types and enforce that derived classes implement particular methods.
### Type Checking at Runtime
You can use the isinstance() function to check the type of an object at runtime, which is helpful for dynamic type checks.
### Memory Management and Garbage Collection
Python uses automatic garbage collection to manage memory, but understanding how memory is allocated and deallocated can help you write more efficient programs. The gc module provides tools to interact with the garbage collector.
## Inbuilt Methods for List, Dictionary and String:
```markdown
str.lower(): Converts all characters to lowercase.
str.upper(): Converts all characters to uppercase.
str.capitalize(): Capitalizes the first character of the string.
str.title(): Converts the first character of each word to uppercase.
str.strip([chars]): Removes leading and trailing characters (space by default).
str.replace(old, new[, count]): Replaces occurrences of a substring with another substring.
str.split([sep[, maxsplit]]): Splits the string at the specified separator and returns a list of substrings.
str.join(iterable): Joins elements of an iterable with the string as a separator.
str.find(sub[, start[, end]]): Returns the lowest index of the substring if found, otherwise returns -1.
str.count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of the substring.
str.startswith(prefix[, start[, end]]): Returns True if the string starts with the specified prefix.
str.endswith(suffix[, start[, end]]): Returns True if the string ends with the specified suffix.
dict.keys(): Returns a view object containing the dictionary's keys.
dict.values(): Returns a view object containing the dictionary's values.
dict.items(): Returns a view object containing the dictionary's key-value pairs.
dict.get(key[, default]): Returns the value for the specified key if it exists, otherwise returns the default value.
dict.update([other]): Updates the dictionary with the key-value pairs from another dictionary or iterable.
dict.pop(key[, default]): Removes the specified key and returns its value. If the key is not found, returns the default value.
dict.popitem(): Removes and returns the last key-value pair as a tuple.
dict.clear(): Removes all key-value pairs from the dictionary.
dict.copy(): Returns a shallow copy of the dictionary.
dict.setdefault(key[, default]): If the key is in the dictionary, returns its value. If not, inserts the key with the specified default value.
list.append(x): Adds an item to the end of the list.
list.extend(iterable): Extends the list by appending elements from the iterable.
list.insert(i, x): Inserts an item at a given position.
list.remove(x): Removes the first item from the list whose value is equal to x.
list.pop([i]): Removes and returns the item at the given position.
list.clear(): Removes all items from the list.
list.index(x[, start[, end]]): Returns the index of the first item whose value is equal to x.
list.count(x): Returns the number of times x appears in the list.
list.sort(key=None, reverse=False): Sorts the items of the list in place.
list.reverse(): Reverses the elements of the list in place.
list.copy(): Returns a shallow copy of the list.
```
## Time Complexity:
Time complexity essentially measures how the runtime of an algorithm scales with the size of the input. It's a way to understand how fast or slow an algorithm performs. Here are the main concepts in simple language:
1.	Constant Time (O(1)): The runtime does not change with the size of the input. It's always the same. Example: accessing an element in a list by index.
2.	Logarithmic Time (O(log n)): The runtime increases logarithmically as the input size increases. Example: binary search in a sorted list.
3.	Linear Time (O(n)): The runtime increases linearly with the size of the input. Example: looping through all elements in a list.
4.	Linearithmic Time (O(n log n)): The runtime increases more than linearly but less than quadratically. Example: efficient sorting algorithms like Merge Sort and Quick Sort.
5.	Quadratic Time (O(n^2)): The runtime increases quadratically with the size of the input. Example: nested loops, such as checking all pairs in a list.
6.	Exponential Time (O(2^n)): The runtime doubles with each addition to the input size. Example: solving the Fibonacci sequence recursively without memorization.
### Implementation of dict and set: 
cpython/Objects/dictobject.c at main · python/cpython, 
cpython/Objects/setobject.c at main · python/cpython
## Mutability and Immutability from Memory angle: 
Mutable objects are objects that can be modified after creation without changing their identity. Examples: list, dict, set. In memory, when you modify a mutable object, the object retains its original memory location. Mutable Objects are efficient for frequent modifications. Since they don’t create new copies when altered, they save memory and reduce the overhead.
Example: Appending multiple items to a list.
Immutable objects are objects that cannot be altered once created. Examples: int, float, str, tuple. In memory, modifying an immutable object results in the creation of a new object with a different memory location. Immutable Objects are Safer and simpler to use when you need to ensure that the data won’t change, such as using keys in a dictionary.
Example: Tuples used as dictionary keys.
Reference Counting and Garbage Collection
•	Python uses reference counting and garbage collection to manage memory.
•	For mutable objects, since modifications don't lead to new objects, reference counts don't frequently change.
•	For immutable objects, frequent creation and deletion can trigger garbage collection more often, especially in memory-intensive applications.

