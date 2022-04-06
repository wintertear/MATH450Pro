from matplotlib.pyplot import *
from numpy import *
from scipy import integrate
from scipy.integrate import odeint
from sympy import *
from scipy import linalg

pool = genfromtxt('test.txt',dtype='str')
rePool = pool
rePoolCount = 3

WR = 5
IR = 21
TR = 3
CP = ''
CC = ['' for x in range(WR)]
VC = ['' for x in range(WR)]
IC = ['' for x in range(IR)]
attempts = [[0 for x in range(TR)] for y in range(TR)]

def checkForCorrectChar(guess, sol):
    for i in range(WR):
        if guess[i] == sol[i]:
            CC[i] = guess[i]
        else:
            CC[i] = 0

def checkForValidChar(guess, sol):
    mark = 0
    for i in range(WR):
        for j in range(WR):
            if guess[i] == sol[j]:
                VC[mark] = guess[i]
                mark+=1

def checkForInvalChar(guess, sol):
    print('?')

def removeCand(rePool):
    print('?')

def resize(guess, sol, rePool):
    checkForCorrectChar(guess, sol)
    checkForValidChar(guess, sol)
    checkForInvalChar(guess, sol)

    removeCand(rePool)

def pick(rePool):
    print('?')

def main():
    for i in range(TR):
        for j in range(TR):
            rePool = pool
            guess = pool[i]
            sol = pool[j]

            if guess == sol:
                print("done")
                attempts[i][j] = 1
            else:
                resize(guess, sol, rePool)
                if pick(rePool) == sol:
                    print("done")
                    attempts[i][j] = 2
                else:
                    resize(guess, sol, rePool)
                    if pick(rePool) == sol:
                        print("done")
                        attempts[i][j] = 3
                    else:
                        resize(guess, sol, rePool)
                        if pick(rePool) == sol:
                            print("done")
                            attempts[i][j] = 4
                        else:
                            resize(guess, sol, rePool)
                            if pick(rePool) == sol:
                                print("done")
                                attempts[i][j] = 5
                            else:
                                resize(guess, sol, rePool)
                                if pick(rePool) == sol:
                                    print("done")
                                    attempts[i][j] = 6
    print(attempts)

