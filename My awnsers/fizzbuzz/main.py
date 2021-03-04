# Vraag de gebruiker om een getal in te voeren
# Zorg ervoor dat je dit ook echt als getal kunt gebruiken

# Als het getal deelbaar is door 3:     print fizz
# Als het getal deelbaar is door 5:     print buzz
# Als het getal deelbaar is door 3 & 5: print fizz én buzz
# Anders print je het getal

# Voorbeeld:
# Gebruiker geeft het getal 12 in
# 12 is deelbaar door 3 (12/3 = 4), dus 'fizz' wordt geprint
# 12 is niet deelbaar door 5 (12/5 = 2.4), dus 'buzz' wordt niet geprint
# Omdat 12 deelbaar is door 3 hoeft het getal zelf niet geprint te worden.

# Voor de getallen 1 t/m 5:
# 1 -> 1
# 2 -> 2
# 3 -> 'fizz'
# 4 -> 4
# 5 -> 'buzz'

#%%
x = int(input('number: '))
i = x % 3
o = x % 5

if i == 0:
    print('fizz')
elif o == 5:
    print('buzz');
elif i == 0 and o == 0:
    print('fizzbuzz');
else:
    print(x);

# %%
#! For loop
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	
#%%
#! Working
x = int(input('number: '))

if (x%3 == 0) and (x%5 == 0):
    print("FizzBuzz")
elif (x%5 == 0):
    print("Buzz")
elif (x%3 == 0):
    print("Fizz")
else:
    print(x)
# %%
