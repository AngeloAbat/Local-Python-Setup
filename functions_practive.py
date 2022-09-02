def hello():
    print("Hello World!")

def pack(x, y, z):
    print((x, y, z))

pack("Test1", "Test2", "Test3")

def eat_lunch(x):
    counter = 1

    for i in x:
        if counter == 1:
            print("First I eat", i)
        else:
            print("Next I eat", i)
        counter += 1

    if counter == 1:
        print('My lunchbox is empty!')


eat_lunch(["Apple", "Apple"])