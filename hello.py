# import redis

# redis_host =  'localhost'
# redis_port = 6379

print("Starting the Python script...")


def display(a ,b):
    try:
        print("Entering the display function...")
        print("This is testing for Docker Using Python ")
        print(f"Sum of {a} and {b} is {a + b}")
        print(f"Product of {a} and {b} is {a * b}")
    except Exception as e:
        print(f"Error inside display function: {e}")

print("Before calling the display function...")
display(10, 20)
print("After calling the display function...")
    
    
