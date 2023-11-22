# def my_functions(some_argument):
#   do this with some_argument
#   then do this
#   finally do this

# my_functions(123)

# function with outputs

def format_name(f_name, l_name):
    name1 = f_name.title()
    name2 = l_name.title()
    return f"{name1} {name2}"


print(format_name("angela", "yu"))


# function with outputs
# return statement
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    name1 = f_name.title()
    name2 = l_name.title()
    return f"{name1} {name2}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
