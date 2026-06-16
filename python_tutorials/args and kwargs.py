def example_function(*args, **kwargs):
    print("args:", args)      # tuple
    print("kwargs:", kwargs)  # dict

example_function(1, 2, 3, name="Alice", age=25, city="New York")

def add(a=3, b=2):
    print(a + b)
add()
add(10)           
# add(10, 5)        #
# add(a=10)     
add(b=5)          
# add(a=10, b=5)    
# add(10, b=5)
# add(b=5, 10)       
add(10, b=5)      #
# add(a=10, a=20)