def mario(level):
    #method 1
    if level==1:
        return 1
    elif level %10==0:
        return 0
    else:
        return mario(level//100)+mario(level//10)

    #method 2
    if level<10:
        return 1
    elif level%100==0:
        return 0
    elif level% 100<=10:
        return mario(level//10)
    else:
        return mario(level//100)*2