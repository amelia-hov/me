"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will print the words in order because it is in a list.
some_words = ["what", "does", "this", "line", "do", "?"] 
# It printed everything in order but with as a single word. 

# It will print every word one by one after every run.
for word in some_words:
    print(word)
#It printed everything word by word

# x replaces the word 'word' and is now represented as 'x' and will show every word word by word.  
for x in some_words:
    print(x)
# It will do the same thing by doing it word by word. 

# It will print all the words
print(some_words)
# It printed the list of words ["what", "does", "this", "line", "do", "?"] 

# len() means that there is a number indication between the brackets therefore it was say that the number in lens will be greater than 3
if len(some_words) > 3:
    print("some_words contains more than 3 words")
# It showed that some_words contains more than 3

# the yellow brackets means that there is nothing in the brackets.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """

# the yellow brackets will then show "print(platform.uname())" which means that the yellow bracket up in useful function is this code below.
    print(platform.uname())
# platform refers to the computer and the data and where it is being saved. 

# finally output and should load the terminal and show all the info. 
usefulFunction()
