def collaz(n):

    if n == 1:
        # print("at base")
        return 0

    if n % 2 == 0:
        # print ("at number: ", str(n))
        n = n/2
        return collaz(n) + 1
    
    elif n % 2 != 0:
        # print ("at number: ", str(n))
        n = (n*3) + 1
        return collaz(n) + 1

print (collaz(5))
