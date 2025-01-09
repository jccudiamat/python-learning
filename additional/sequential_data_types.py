#These are ones that are ordered in a defined sequence.

#String
text = "Order matters!" #elements in sequential data types can be accessed via their indexes
print(text[1])
print(text[-1])
#Indexes are measures of position. All elements within a sequence start in index 0.

#The index used must be valid:
print(text[14]) #IndexError: str index out of range

#Strings are also immutable data type which means that the characters cannot be changed.

#Most python objects(boolens, integers, floats, strings, and tuples) are immutable.
text[13] = '.'#TypeError: 'str' object does not support item assignment


