
def add_one(x):
    x += 1
    return x 

my_var = 2

print("Before calling add_one:", my_var)

count = 0
while count < 3:
    my_var = add_one(my_var)
    count += 1

print("After calling add_one:", my_var)
