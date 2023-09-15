x:int = 1
lsz:int = 0
while x <= 10000000:
    print(f"2^{lsz} := {x}")
    lsz += 1
    x *= 2

jelszo:str = "password123"
proba:str = ''
while proba != jelszo:
    proba = input('kérem a jelszót: ')
    if proba != jelszo: print('nyyyeeeeeeeem....')
print("navégre!")