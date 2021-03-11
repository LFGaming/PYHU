# Bekijk je fizzbuzz van vorige week.
# Nu willen we fizzbuzz voor alle getallen van 1 tot en met 100 uitvoeren 
# Met input zou dit te lang duren ;)
# Schrijf dit nu met een loop, zodat dit automagisch gebeurt
#%%
for fizzbuzz in range(100):
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
	

# print alle even getallen vanaf 0 tot en met 42; gebruik hiervoor geen modulo! 

# Schrijf een loop die een driehoek van sterretjes print, zoals
# *
# * *
# * * *
# etc.
# Doe dit tot 10 sterretjes.

#%%

def pyramid(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
n = 10
pyramid(n)

# Laat je driehoek nu ook weer terug lopen.
# *
# * *
# (.. meer sterren ..)
# * *
# *
# Hint: gebruik twee for loops

#%%
#?
def pyramid(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
n = 10
pyramid(n)

def pyramid(p):
    myList = []
    for i in range(1,p+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
p = 11
pyramid(p)

# Voor een extra uitdaging bij deze opdracht kan je de driehoek ook zo maken (doe dit pas als je de rest af hebt. Let op: is erg lastig):
#   *
#  * *
# * * *

#%%
def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
n = 5
triangle(n)

# Schrijf nu je eigen max algoritme; zoek het grootste getal uit onderstaande lijst
# Je mag er vanuit gaan dat het kleinste getal nul is.
#
# Stappen:
# Maak een var_max met als waarde nul
# Loop over de lijst heen
# Als de waarde groter is dan var_max maak de variabele deze waarde
# 
# Check of jouw max overeenkomt met de max van de python functie max()

lijst = [1,3,4,1,123,0,5,1,32,1,1,3,5,1,12,3,101,10]
# %%
