# Annother attempt to crack vigenere, but by hill climing by changing random keys for a given length key

import fittness
import random

f=file('blackhat_3.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))



print("Original Text: " + text)




best_fittness = 0
best_text = ""
best_key_length = 0

# First runthrough, 16 was clearly the key length
for key_length in range(10, 20):
    key_length = 16
    print("Key Length: " + str(key_length))
    numFails = 0
    local_best_fittness = 0
    copy_text = text
    while(numFails < 5000):
        # which random key to change
        randKey = random.randrange(0, key_length)

        # what random amount to shift it by
        randShift = random.randrange(0, 26)

        before_fittness = fittness.getFitness(copy_text)

        temp_text = copy_text

        for i in range(0, len(temp_text), key_length):
            if(i + randKey + 1 < len(temp_text)):
                temp_text = temp_text[:i + randKey] + shiftBy(temp_text[i + randKey], randShift) + temp_text[i + randKey + 1:]
        after_fittness = fittness.getFitness(temp_text)

        if(after_fittness > before_fittness):
            print("Improvement!")
            print(str(after_fittness))
            copy_text = temp_text
            local_best_fittness = after_fittness
            numFails = 0
        else:
            numFails += 1
    
    if(local_best_fittness > best_fittness):
        best_fittness = local_best_fittness
        best_text = copy_text
        best_key_length = key_length

print(best_fittness)
print(best_key_length)
print(best_text)



# Got it easy!
# blackhat_3
# key length 16
# could get key pretty easily
# madnessingreatonesmustnotunwatchdgothelifeofeverymanisadiaryinwhichhemeanstowriteonestoryandwritesanotherandhishumblesthouriswhenhecomparesthevolumeasitiswithwhathevowedtomakeittimeisthegreatphysiciantisnotthedyingforafaiththatssohardmasterharryeverymanofeverynationhasdonethattisthelivinguptoitthatisdifficultthereisnosuchthingasunmixedevilamanwholoseshismoneygainsatleastexperienceandsometimessomethingbetterprejudicesitiswellknownaremostdifficulttoeradicatefromtheheartwhosesoilhasneverbeenloosenedorfertilisedbyeducationtheygrowtherefirmasweedsamongstonesmadnessingreatonesmustnotunwatchdgv