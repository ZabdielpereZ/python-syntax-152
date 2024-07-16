# week 1 day 1 lecture
# This is a comment
# Usiing a # allows you to write a comment in your code that will not be run. python and VS code will ignore it

# Our first line of code 
print("hello world!")


# this is a variable with a string stored in it 
# A string is a date type used for storing text
first_words = "hello world!"

print(first_words)

# Here is a string with single quotes. It is still a string data type
new_string = 'I can also use single qoutes' 

# Escape character \ allows us to still use single qoutes inside of a single qoutes string
example = 'I can\'t use single qoute\'s inside of single qoute\'s'
print (example)

# Concatenating strings together - combine multiple strings together
string1 = "this is"
string2 = "super cool!"

# Concatenated multiple strings together and stored them in a new variable 
concat = string1 + string2
print(concat)

# Concatenated two strings together using a + sign
print(string1 + string2)

print(string1 + " " + string2) # Concatenated with a "space string" added in

print(string1, string2) # Concatenated with a comma , will automatically add a space between my strings 

# Docstring - a multiline string 

### Incorrect format for a doc string (a multi line string)
# another_string = "
# Line1
# line2
# line3 
# "
 
 # Initiate a docstring with triple qoutes, either single ''' or double """
doc = ''' 
Enter 1 to continue
Enter 2 to go back 
Enter 3 to figure it all out '''

print(doc)

# Python reads code from the top to the bottom, we've defined the variable doc, if we redefine the data stored there, then our print function will print that piece of data 
doc = "this is a new thing"

print(doc)

# Unpacking - we can define multiple pieces of data at once, and unpack them positionally into their own variable(places in memory)
first, middle, last = "Travis", "Cline", "Peck"
print(middle)

print(first, middle, last)

# Never create a variable with a reseved word
 
# global = "this"
# if = "that"
# 
# Global and if are both words that are already reserved for something else in python
 
# print = "something here"
# print(print)   