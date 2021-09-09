def fact(x:int):
    if x ==0:
        return 1
    return x*fact(x-1)

    print(fact(5))