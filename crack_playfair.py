# For cracking playfair
# For cracking column transposition

# This is blackhat_2 because this already had distribution of english text

# Cracked it!:

# unwelcometruthsarenotpopularnooneisuselessinthisworldretortedthesecretarywholightenstheburdenofitforanyoneelseihavealwaysthoughtthatawildanimalneverlookssowellaswhensomeobstacleofpronounceddurabilityisbetweenusapersonalexperiencehasintensifiedratherthandiminishedthatideawhenyouvelearnedtolaughatthethingsthatshouldbelaughedatandnottolaughatthosethatshouldntyouvegotwisdomandunderstandingrichgiftswaxpoorwhengiversproveunkindtobeconsciousthatyouareignorantisagreatsteptoknowledgethereismanyayoungcockerelthatwillstanduponadunghillandcrowabouthisfatherbywayofmakinghisownplumagetoshine


import fittness
import random

f=file('blackhat_2.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]


print(text)




# Function to generate 5x5 matrix using 10 passed in words

def generateMatrix(words):
    # words is an array with 10 words in it

    seed = "".join(words).replace('j','i')

    alpha = 'abcdefghiklmnopqrstuvwxyz'
    suffix = "".join( sorted( list( set(alpha) - set(seed) ) ) )
    seed_set = set()
    prefix = ""
    for letter in seed:
        if not letter in seed_set:
            seed_set.add(letter)
            prefix += letter
    key = prefix + suffix




# Function to get plaintext for a given 5x5 matrix


best_fittness = 0
best_text = ""
best_key_length = 0

fails = 0
while(fails < 10000):

    before_text = "a"

    before_fittness = fittness.getFitness(before_text)

    after_text = "a"

    after_fittness = fittness.getFitness(after_text)

    if(after_fittness > before_fittness):
        best_fittness = after_fittness
        best_text = after_text
        fails = 0
    else:
        fails += 1

print(best_fittness)
print(best_text)
