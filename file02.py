# példák bejáró ciklusra:

# egy for ciklus, ami végigmegy egy lista minden elemén:

gyumolcsok:list[str] = ['alma', 'körte', 'banán', 'kiwi']

for gyumi in gyumolcsok:
    print(f'\t - a {gyumi} az egy gyümölcs a listából')

karakterlanc:str = 'bableves'

for karakter in karakterlanc:
    print(f'{karakter}', end='  ')
print()
for n in range(1, 11):
    print(f'{n}^2 = {n**2}')