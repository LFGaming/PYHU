# Extra uitdagingen:

# Een palindroom is een woord dat van voor naar achter en andersom exact hetzelfde is, zoals 'legovogel'. 
# > Vraag een gebruiker met input om een woord, en controleer of het een palindroom is. Wat voorbeelden: racecar, otto, maandnaam, legermeetsysteemregel, kook.
# > Let op: Python ziet kleine letters en hoofdletters als verschillende letters, maar voor een palindroom maakt dat niet uit.
# > Extra: Het kan eventueel ook met zinnen: 'Ai, de media', 'Er is daar nog onraad, Sire', let er dan op dat spaties niet meetellen.

#%%
# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
# Driver code
s = input()
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# Bubblesort is een simpel sorteeralgoritme waarbij je steeds door een lijst loopt, naar twee elementen tegelijk kijkt en deze omwisselt als ze niet op de juiste volgorde staan:

# [0,1,5,3,2,6] # Staan goed
#  ^ ^
# [0,1,5,3,2,6] # Staan goed
#    ^ ^
# [0,1,5,3,2,6] # Staan niet goed
#      ^ ^
# [0,1,3,5,2,6] # Verwisseld
#      ^ ^
# [0,1,3,5,2,6] # Staan ook niet goed
#        ^ ^
# [0,1,3,2,5,6] # Verwisseld
#        ^ ^
# [0,1,3,2,5,6] # Staan goed, einde van pass
#          ^ ^ 
# Hierna begint de loop opnieuw, totdat er na een 'pass' (een cycle) niets meer veranderd is.
# > Implementeer je eigen Bubble sort. Laat een lijst vullen d.m.v. input óf d.m.v. random getallen (hiervoor moet je even Googlen hoe je dat moet doen)

# %%
#! bubble sort

import random
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(0, 100), 10)
print(randomlist)

def bubbleSort(arr): 
	n = len(arr) 

	for i in range(n-1): 
		for j in range(0, n-i-1): 

			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = randomlist 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 

# %%
