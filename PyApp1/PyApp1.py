"""1st python program"""
try:
    x = 0
    if x:
     print(f"hello x = {x}")
    else:
     str = r"we want to see this \n change of line..."
     print(str)
    lst = ["Chris","Orton","Jurek"]
    print(len(lst))
    print(lst)
    for index in range(len(lst)):
        print(lst[index])

    dict = {"key1": 1,"key2":2}
    dict["key3"]= "New"
    print(dict["key1"])
    print(dict["key2"])
    del dict["key2"]
    print(dict)
except Exception:
    print("Exception occured")


