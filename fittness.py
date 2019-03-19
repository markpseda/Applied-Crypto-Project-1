# This file is for functions related to finding the fitness of a piece of
# text (how close it is to written english)

import urllib2

import re

#data derived from http://www.data-compression.com/english.html
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

res = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
words = res.read().split()

def get_sum_freqs_squared(input_text):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(input_text.count(chr(ascii)))/len(input_text)

    sum_freqs_squared = 0.0
    for ltr in normal_freqs:
        sum_freqs_squared += normal_freqs[ltr]*frequency[ltr]
    
    return sum_freqs_squared

# higher is better
def getFitness(text):
    score = 0
    sfs = get_sum_freqs_squared(text)

    #closer to .065
    distance = abs(sfs - .065)

    # Anything closer than .04 is equally "good"
    if distance < .004:
        distance = .004

    # this will grow faster and faster as we approach .04 and then stop
    score += int(1 / distance)

    #print("Score from frequency: " + str(score))

    # only check for words if the sfs is close to english
    for word in words[:50]:
        num = len(re.findall(word, text))

        mult = 1

        # every letter makes a match twice as valuable to score
        if len(word) == 1:
            mult = .1
        else:
            mult = mult * 2**len(word)
        
        score += num*mult
    
    #print("Score with word count: " + str(score))
    #print(score)
    return score