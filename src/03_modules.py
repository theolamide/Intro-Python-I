"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for x in sys.argv:
    print("Argument", x)
    # Checking the length here. I am not sure what we are supposed to be doing here really.
    print(len(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
print("This computer is running on Windows", sys.getwindowsversion()[0])

# Print out the version of Python you're using:
# YOUR CODE HERE
print("I am running this current version of python:", sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("This is the process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("This is the working directory of this file:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Login of the user logged in:", os.getlogin())
