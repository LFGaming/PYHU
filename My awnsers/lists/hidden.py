#   _____ ______ _    _ ______ _____ __  __
#  / ____|  ____| |  | |  ____|_   _|  \/  |
# | |  __| |__  | |__| | |__    | | | \  / |
# | | |_ |  __| |  __  |  __|   | | | |\/| |
# | |__| | |____| |  | | |____ _| |_| |  | |
#  \_____|______|_|  |_|______|_____|_|  |_|
# dit hoef je niet te snappen
from random import randint, seed
seed(42)
onze_lijst = [randint(0,0xFFFF) for _ in range(0b1100100)]