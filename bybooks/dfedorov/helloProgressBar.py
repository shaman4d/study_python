from time import sleep  
from random import random  
from clint.textui import progress  
if __name__ == '__main__':
    for i in progress.bar(range(100)):
        sleep(random() * 0.2)

    for i in progress.dots(range(100)):
        sleep(random() * 0.2)