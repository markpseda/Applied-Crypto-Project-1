
from Crypto.Util.number import *

import random
import urllib2

import fittness
# This code is attempt to crack a hill 2x2 cipher




#data derived from http://www.data-compression.com/english.html
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}


f=file('blackhat_4.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]



def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))


print("Original Text: " + text)


# inverse of 2x2
# [ a, b, c, d] = (1/ ad - bc) [d, -b, -c, a]

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def invertMatrix(a, b, c, d, modulus):
    first_term = (a * d) % modulus
    second_term = (b * c) % modulus
    determinant = (first_term - second_term) % modulus
    if(GCD(determinant, modulus) != 1):
        return False
    else:
        inverse_determinant = inverse(determinant, modulus)
        new_a = (inverse_determinant * d) % modulus
        new_b = (inverse_determinant * -b) % modulus
        new_c = (inverse_determinant * -c) % modulus
        new_d = (inverse_determinant * a) % modulus
        return [new_a, new_b, new_c, new_d]


# For every possible matrix 2x2 in Z 26

bestScore = 0
bestLetters = [0,0,0,0]
bestText = ""

for a in range(0,26):
    print("Done through: " + str(a))
    for b in range(0,26):
        for c in range(0,26):
            for d in range(0,26):
                result = invertMatrix(a, b, c, d, 26)
                
                if result != False:
                    copy_text = text
                    decrypted_text = ""
                    while(len(copy_text) > 0):
                        # snip off four characters at a time
                        if(len(copy_text) < 2):
                            padding = 2 - len(copy_text)
                            next_snip = copy_text[:len(copy_text)]
                            next_snip += "a"*padding
                            copy_text = []
                        else:
                            next_snip = copy_text[:2]
                            copy_text = copy_text[2:]
                        
                        #print(next_snip)
                        a1 = ord(next_snip[0]) - ord('a')
                        b1 = ord(next_snip[1]) - ord('a')

                        new_a = (a1*result[0] + b1*result[1]) % 26
                        new_b = (a1* result[2] + b1*result[3]) % 26

                        
                        decrypted_text += chr(ord('a') + new_a) + chr(ord('a') + new_b)
                        # + chr(ord('a') + new_b) chr(ord('a') + new_c) chr(ord('a') + new_d)
                    
                    fit = fittness.getFitness(decrypted_text)

                    if(fit > bestScore):
                        bestScore = fit
                        print(bestScore)
                        bestLetters = [a,b,c,d]
                        bestText = decrypted_text
                        print(bestText)




print(bestLetters)
print(bestText)
print(bestScore)

                        
                        


# For writeup:

# was multipling wrong, was final nail in the coffin.
# used this to tune my fitness function.
# Satisfying to solve.

# Best solution:
# Matrix: [3, 24, 21, 21]
# Fitness: 955 looking at first 50 most common words 
# Text:
# itisafairevenhandednobleadjustmentofthingsthatwhilethereisinfectionindiseaseandsorrowthereisnothingintheworldsoirresistiblycontagiousaslaughterandgoodhumourihavelearnednottothinklittleofanyonesbeliefnomatterhowstrangeitmaybeihavetriedtokeepanopenmindanditisnottheordinarythingsoflifethatcouldcloseitbutthestrangethingstheextraordinarythingsthethingsthatmakeonedoubtiftheybemadorsanebyundueprofundityweperplexandenfeeblethoughtanditispossibletomakeevenvenusherselfvanishfromthefirmanentbyascrutinytoosustainedtooconcentratedortoodirectadifferenceoftasteinjokesisagreatstrainontheaffections





# Check if inverse exists