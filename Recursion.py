def TowerOfHanoi(n, from_peg, to_peg, other_peg):
    global c
    c += 1
    if n==1:
        print(f'Move disk 1 : {from_peg} ---> {to_peg}')
        return

    TowerOfHanoi(n-1, from_peg, other_peg, to_peg)
    print(f'Move disk {n} : {from_peg} ---> {to_peg}')
    TowerOfHanoi(n-1, other_peg, to_peg, from_peg)

c = 0
TowerOfHanoi(7, 'A', 'B', 'C')

print(c)