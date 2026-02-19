# Example 1: *args collects positional arguments into a tuple
def show_args(*args):
    print(args)


# Example 2: Sum of *args
def sum_args(*args):
    print(sum(args))


# Example 3: **kwargs collects keyword arguments into a dict
def show_name(**kwargs):
    print(kwargs["name"])


# Example 4: Safe access with get()
def show_age(**kwargs):
    print(kwargs.get("age", 0))


# Example 5: Keyword arguments (order does not matter)
def kids(child1, child2, child3):
    print("The youngest is " + child3)


show_args(1, 2, 3)
sum_args(4, 5, 6)
show_name(name="Ann")
show_age()
kids(child1="Emil", child2="Tobias", child3="Linus")