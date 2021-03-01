# Dit hoef je niet te snappen!
#     _ _ _     _                  _          _           
#  __| (_) |_  (_)___    __ _  ___| |__   ___(_)_ __ ___  
# / _` | | __| | / __|  / _` |/ _ \ '_ \ / _ \ | '_ ` _ \ 
#| (_| | | |_  | \__ \ | (_| |  __/ | | |  __/ | | | | | |
# \__,_|_|\__| |_|___/  \__, |\___|_| |_|\___|_|_| |_| |_|
#                       |___/                             
#
from random import randint, seed
from string import ascii_lowercase

seed(42)
list(map(lambda z: (globals().update(z), z)[1], map(lambda z: {z: randint(~-True,2<<2|2)}, ascii_lowercase)))
