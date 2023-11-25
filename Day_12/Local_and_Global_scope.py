# Local Scope
"""
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

"""

# Example
# A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

# Example
# Function Inside Function
"""
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

"""

# Example
# The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
"""
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
    
"""

# Example
# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
    print(x)

myfunc()

print(x)

# Modify Global Variable
"""
If you use the global keyword, the variable belongs to the global scope:
    
    """

# Example
# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300

myfunc()

print(x)