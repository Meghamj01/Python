

def foo(**kwargs):
    for key, values in kwargs.items():
        print("{}:{}".format(key,values))
        
foo(huda="female", ziyad ="male", john = "male")

