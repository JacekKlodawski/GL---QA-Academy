import random
from subprocess import Popen, PIPE, STDOUT
import sys


p = Popen([sys.executable, 'tictactoe.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, encoding='utf-8', shell=True)
characters = list(map(chr, range(0, 123)))
while True:
    myinput = random.choice(characters)
    stdout, stderr = p.communicate(myinput)
    print(stdout)

