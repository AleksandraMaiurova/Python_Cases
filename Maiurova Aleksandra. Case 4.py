for x in range (1,101):
    if x%7 == 0 and x%5 == 0:
            print (x, "бинго")
    elif x%7 == 0:
            print (x, "x7")
    elif x%5 == 0:
            print (x, "x5")
    else:
        print(x)