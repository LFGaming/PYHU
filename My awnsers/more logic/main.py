## LOGICA

# Verander de vergelijkingsoperator zodat de print uitgevoerd wordt

# Voorbeeld:
x = 5
if x == 4: # 5 == 4 = False, dus de print wordt nu niet uitgevoerd
  print(x)

# Wordt:
x = 5
if x != 4: # 5 != 4 = True, dus nu wordt er wel geprint
  print(x)

z = 5
if not (z > 4):
  print(z)
  
if z != x:
  print(z)

if z + 2 < 3:
  print(z)

if z > 3 == 2:
  print(z)

## STRINGS

naam    = input('Wat is je naam? ')
salaris = int(input('Hoeveel heb je deze maand verdiend? '))
uurloon = int(input('Hoeveel krijg je per uur? '))

# > print nu met 'f'-strings  de naam van deze pesoon, hoeveel deze persoon verdiend heeft, het uurloon en hoeveel uren deze persoon dus gewerkt heeft.

# > Vraag een gebruiker in welk jaar deze persoon geboren is
# > Vraag ook welk jaar het nu is
# > Bereken hoe oud deze persoon is, en print zo vaak 'HOERA!' door middel van een f-string

# > Vraag een gebruiker om een woord in te typen
# > Vraag de gebruiker ook om een letter in te geven
# > Print of de gegeven letter in het woord voorkomt 

# Maak een super slecht wachtwoord programma.
# > Vraag een gebruiker om een wachtwoord in te stellen
# > Vraag een gebruiker om het wachtwoord te herhalen
# > Kijk of deze overeenkomen
# > Sla het wachtwoord op in een variabele

#%%
#! opdracht 1
naam    = input('Wat is je naam? ')
salaris = int(input('Hoeveel heb je deze maand verdiend? '))
uurloon = int(input('Hoeveel krijg je per uur? '))

f"Hallo, {naam}. Je verdient {salaris} met een uurloon van {uurloon}, dus je hebt {salaris/uurloon} gewerkt."
# %%
#! opdracht 2
geboren = int(input('wanneer ben je geboren? '))
datum = int(input('welk jaar is het nu? '))
i = datum - geboren
geweest = input('is je geboortedatum al geweest? ')
if geweest == 'ja':
    o = i 
else:
    o = i - 1

print(f"HOERA * {o}")
# %%
woord = input('vul een woord in: ')
letter = input('vul een letter in: ')

count = 0
  
for i in woord: 
    if i == letter: 
        count = count + 1
  
print(f"De letter {letter} komt {count} voor in {woord}") 
# %%
ww1 = input('vul wachtwoord in: ')
ww2 = input('herhaal wachtwoord: ')

if ww1 == ww2:
    ww3 = ww2
    print(ww3)
else:
    print('False')
# %%
