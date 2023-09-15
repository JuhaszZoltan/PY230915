# import random
# rnd:int = random.randint(0, 9)
# print(rnd)
# while "a világ" == "a világ":
#     print(f'{random.randint(100, 999)}', end=' ')

# from random import randint

# rnd:int = randint(0, 9)
# print(rnd)

# while "a világ" == "a világ":
#     print(f'{randint(100, 999)}', end=' ')

from random import randint as veletlen

rnd:int = veletlen(0, 9)
print(rnd)

while "a világ" == "a világ":
    print(f'{veletlen(100, 999)}', end=' ')