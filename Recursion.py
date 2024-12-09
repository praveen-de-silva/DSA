# --------------
# Tower Of Hanoi
# --------------

def TowerOfHanoi(n, from_peg, to_peg, other_peg):
    global c
    c += 1
    if n==1:
        print(f'Move disk 1 : {from_peg} ---> {to_peg}')
        return

    TowerOfHanoi(n-1, from_peg, other_peg, to_peg)
    print(f'Move disk {n} : {from_peg} ---> {to_peg}')
    TowerOfHanoi(n-1, other_peg, to_peg, from_peg)


##TowerOfHanoi(3, 'A', 'B', 'C')

# ---
# GCD
# ---

def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)

##print(gcd(24,144))


# ---------
# Factorial
# ---------

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

##print(fact(3))


# ---------
# nth Power
# ---------

##def nPow(x, n):
##    if n==0:
##        return 1
##    return x * nPow(x, n-1)

def nPow(x, n):
    if n==0:
        return 1
    if n%2:
        return x * (nPow(x, n//2))**2
    return (nPow(x, n//2))**2
        

##print(nPow(2, 600))


# -------
# Fib seq
# -------

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1) + fib(n-2)
        

print(fib(22))

# -----------
# Max of List
# -----------

def maxOfList(arr):
    size = len(arr)

    if size==0:
        return None
    if size==1:
        return arr[0]
    if size==2:
        if arr[0]>arr[1]:
            return arr[0]
        return arr[1]

    mid = len(arr)//2
    L_max = maxOfList(arr[:mid])
    R_max = maxOfList(arr[mid:])
    return maxOfList([L_max, R_max])
