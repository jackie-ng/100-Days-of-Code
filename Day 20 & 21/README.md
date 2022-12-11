# Slice Lists, Strings & Tuples in Python


- Basic usage of slices
- ```[start:stop]```
- ```[start:stop:step]```
- Extract from the end with a negative value
- Negative values for start and stop
- Negative values for step
- Slice object by slice()
- Assigning values by slices
- Slices for a list of lists
- Slices make shallow copy
- Slices for strings and tuples

## Basic usage of slices

```[start:stop]```

In a slice, the start position start and end position stop of the subsequence are written as ```[start:stop]```.

The range start <= x <stop is extracted. Note that the item at start is included, but the item at stop is not included.

```python
l = [0, 10, 20, 30, 40, 50, 60]

print(l[2:5])
# [20, 30, 40]
```

You can think of the positions (indices) for the slice as pointing between elements.

One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0.

```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
The above is an example for strings, but the same applies to lists, tuples, etc. The case of negative values is described later.

If ```start``` is omitted, the subsequence is extracted from the beginning, and if ```stop``` is omitted, the subsequence is extracted to the end. If both are omitted, all items are extracted.

```python
print(l[:3])
# [0, 10, 20]

print(l[3:])
# [30, 40, 50, 60]

print(l[:])
# [0, 10, 20, 30, 40, 50, 60]
```
Out of range
No error is raised if you specify a position that exceeds the number of items.
```python
print(l[2:10])
# [20, 30, 40, 50, 60]
```
If no item is selected
No error is raised if you specify start and stop that select no item. An empty list is returned.
```python
print(l[5:2])
# []

print(l[2:2])
# []

print(l[10:20])
# []
```
```[start:stop:step]```

In addition to the start position ```start``` and end position ```stop```, you can specify step as ```[start:stop:step]```.

For example, if step is set to 2, items at odd-numbered positions or even-numbered positions can be selected.
```python
print(l[::2])
# [0, 20, 40, 60]

print(l[1::2])
# [10, 30, 50]
```
Other examples:
```python
print(l[::3])
# [0, 30, 60]

print(l[2:5:2])
# [20, 40]
```
As in the previous examples, if ```step``` is omitted, it is set to 1.

## Extract from the end with a negative value
### Negative values for ```start``` and ```stop```
If ```start``` and ```stop``` are negative values, they are regarded as positions from the end.

The concept of the positions (indices) for the slice is restated below.
```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
print(l[3:-1])
# [30, 40, 50]

print(l[-2:])
# [50, 60]

print(l[-5:-2])
# [20, 30, 40]
```
### Negative values for ```step```
If ```step``` is a negative value, the items are selected in reverse order.

Items are selected from the position at ```start```. Note that unless ```start``` indicates a position after ```stop```, it will be empty.
```python
print(l[5:2:-1])
# [50, 40, 30]

print(l[2:5:-1])
# []
```
Other examples:
```python
print(l[-2:-5:-1])
# [50, 40, 30]

print(l[-2:2:-1])
# [50, 40, 30]

print(l[5:2:-2])
# [50, 30]
```
When ```step``` is a negative value, omitting ```start``` selects from the end, and omitting ```stop``` selects to the beginning. If both are omitted, all items are selected.

By omitting ```start``` and ```stop``` and setting step to -1, you can get a reversed object.

```python
print(l[:3:-1])
# [60, 50, 40]

print(l[3::-1])
# [30, 20, 10, 0]

print(l[::-1])
# [60, 50, 40, 30, 20, 10, 0]
```
You can also use ```reverse()``` and ```reversed()``` to reverse lists or strings, tuples, etc. See the following article for details.

Reverse a list, string, tuple in Python (reverse, reversed)

### Slice object by slice()
You can generate a slice object using the built-in function ```slice()```. If you want to repeatedly select the items at the same position, you only need to generate the slice object once.

Built-in Functions - ```slice(```) — Python 3.8.1 documentation
```slice(start, stop, step)``` is equivalent to ```start:stop:step```.
```python
sl = slice(2, 5, 2)
print(sl)
# slice(2, 5, 2)

print(type(sl))
# <class 'slice'>

print(l[sl])
# [20, 40]
```
If two arguments are specified, step is set to None. This is equivalent to start:stop.
```python
sl = slice(2, 5)
print(sl)
# slice(2, 5, None)

print(l[sl])
# [20, 30, 40]
```
If only one argument is specified, start and step are set to None. This is equivalent to : stop.
```python
sl = slice(2)
print(sl)
# slice(None, 2, None)

print(l[sl])
# [0, 10]
```
If all arguments are omitted, an error TypeError is raised. If you want to generate : with slice(), explicitly specify None.
```python
# sl = slice()
# TypeError: slice expected at least 1 arguments, got 0

sl = slice(None)
print(sl)
# slice(None, None, None)

print(l[sl])
# [0, 10, 20, 30, 40, 50, 60]
```
### Assigning values by slices
You can assign new values to the range selected by slices.

It does not matter if the number of items in the range selected by slicing does not match the number of items (= the length of object) to be assigned.
```python
l = [0, 10, 20, 30, 40, 50, 60]

l[2:5] = [200, 300, 400]
print(l)
# [0, 10, 200, 300, 400, 50, 60]

l[2:5] = [-2, -3]
print(l)
# [0, 10, -2, -3, 50, 60]

l[2:4] = [2000, 3000, 4000, 5000]
print(l)
# [0, 10, 2000, 3000, 4000, 5000, 50, 60]

l[2:6] = [20000]
print(l)
# [0, 10, 20000, 50, 60]
```
Note that specifying a scalar value on the right side will result in TypeError.
```python
# l[2:3] = 200
# TypeError: can only assign an iterable
```
If the right side is empty, the elements in the range selected by the slice will be deleted.
```python
l[1:4] = []
print(l)
# [0, 60]
```
It is also possible to specify an out-of-range or empty range for the assignment. The value on the right side is inserted at the specified position.
```python
l = [0, 10, 20, 30, 40, 50, 60]

l[100:200] = [-1, -2, -3]
print(l)
# [0, 10, 20, 30, 40, 50, 60, -1, -2, -3]

l[2:2] = [-100]
print(l)
# [0, 10, -100, 20, 30, 40, 50, 60, -1, -2, -3]
```
If the number of elements is not equal for the range where step is specified, an error ValueError is raised.
```python
l = [0, 10, 20, 30, 40, 50, 60]

l[1::2] = [100, 200, 300]
print(l)
# [0, 100, 20, 200, 40, 300, 60]

# l[1::2] = [100, 200]
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3

```
To add an element in the middle or at the end of the list, methods such as ```insert()``` and ```append()``` are provided. See the following article:

### Add an item to a list in Python (append, extend, insert)
Remove an item from a list in Python (clear, pop, remove, del)


### Slices for a list of lists
When applying a slice to a list of lists (= 2D list), inner lists are selected.
```python
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

print(l_2d[1:3])
# [[3, 4, 5], [6, 7, 8]]
```
To apply a slice to inner lists, use list comprehensions.

### List comprehensions in Python
```python
print([l[:2] for l in l_2d[1:3]])
# [[3, 4], [6, 7]]
```
If you want to get a column, you can transpose it.

### Transpose 2D list in Python (swap rows and columns)
```python
l_2d_t = [list(x) for x in zip(*l_2d)]
print(l_2d_t)
# [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]

print(l_2d_t[1])
# [1, 4, 7, 10]
```
Note that if you can use NumPy, it is easier to use NumPy to manipulate multi-dimensional arrays.

In NumPy, you can specify a slice for each dimension as [1:4, 2:5].

### Slices make shallow copy
Slice makes a shallow copy. For more information about shallow and deep copy, see the following article.

Shallow and deep copy in Python: ```copy()```, ```deepcopy()```
For example, in the case of a list whose elements are immutable objects, such as numbers, assigning the result obtained by slicing to a variable and updating the elements of the variable will not change the original object.
```python
l = [0, 10, 20, 30, 40, 50, 60]

l_slice = l[2:5]
print(l_slice)
# [20, 30, 40]

l_slice[1] = 300
print(l_slice)
# [20, 300, 40]

print(l)
# [0, 10, 20, 30, 40, 50, 60]
```
In the case of a list whose elements are mutable objects, such as lists and dictionaries, updating the elements will also change the original object.
```python
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

l_2d_slice = l_2d[1:3]
print(l_2d_slice)
# [[3, 4, 5], [6, 7, 8]]

l_2d_slice[0][1] = 400
print(l_2d_slice)
# [[3, 400, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 400, 5], [6, 7, 8], [9, 10, 11]]
```
In the above example, the list in the slice is updated, and the list in the original object is also changed. If the list in the original object is updated, the list in the slice is also changed.

To prevent this, import the copy module of the standard library and use ```deepcopy()```.
```python
import copy

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

l_2d_slice_deepcopy = copy.deepcopy(l_2d[1:3])
print(l_2d_slice_deepcopy)
# [[3, 4, 5], [6, 7, 8]]

l_2d_slice_deepcopy[0][1] = 400
print(l_2d_slice_deepcopy)
# [[3, 400, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
```

### Slices for strings and tuples
So far, we have shown examples of lists (list type), but slices can be used with other sequence objects such as strings str and tuples tuple as well.

However, str and tuple are immutable, so new values cannot be assigned.
```python
s = 'abcdefg'

print(s[2:5])
# cde

print(s[::-1])
# gfedcba

# s[2:5] = 'CDE'
# TypeError: 'str' object does not support item assignment

t = (0, 10, 20, 30, 40, 50, 60)

print(t[2:5])
# (20, 30, 40)

# t[2:5] = (200, 300, 400)
# TypeError: 'tuple' object does not support item assignment
```
