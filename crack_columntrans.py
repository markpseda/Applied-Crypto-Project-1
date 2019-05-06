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
print()

best_fittness = 0
best_text = ""
best_key_length = 0

for key_length in range(8, 11):

    columns = [""]*(key_length)

    index = 0

    print("Text Length: ")
    print(len(text))
    print(len(text) // key_length)
    colLength = len(text) // key_length
    for i in range(0, key_length):
        columns[i] += text[index: index + colLength]
        index+= colLength
    
    snippedText = text[index:]

    newIndex = 0
    for c in snippedText:
        columns[newIndex] += c
        index = index + 1 % key_length

    print("Columns: ****************")
    print(columns)
    print("*************************")
    print(len(columns))
    columnOrder = range(0, key_length)

    fails = 0

    local_best_fittness = 0
    local_best_text = ""

    before_text_1 = ""
    for i in range(0, len(columns[0])):
        for colVal in columnOrder:
            if(i < len(columns[colVal])):
                before_text_1 += columns[colVal][i]

    print("=============")
    print(before_text_1)
    print("=============")

    while(fails < 10000):

        before_text = ""

        for i in range(0, len(columns[0])):
            for colVal in columnOrder:
                if(i < len(columns[colVal])):
                    before_text += columns[colVal][i]

        before_fittness = fittness.getFitness(before_text)

        #print(columnOrder)

        random_1 = random.randrange(0, key_length)
        random_2 = random.randrange(0, key_length)

        temp = columnOrder[random_1]

        columnOrder[random_1] = columnOrder[random_2]
        columnOrder[random_2] = temp

        #print(columnOrder)
        after_text = ""

        for i in range(0, len(columns[0])):
            for colVal in columnOrder:
                if(i < len(columns[colVal])):
                    after_text += columns[colVal][i]

        after_fittness = fittness.getFitness(after_text)

        if(after_fittness > before_fittness):
            local_best_fittness = after_fittness
            local_best_text = after_text
            fails = 0
            print(columnOrder)
        else:
            fails += 1
            # swap back if failed
            temp = columnOrder[random_1]
            columnOrder[random_1] = columnOrder[random_2]
            columnOrder[random_2] = temp
    
    print("-----------------")
    print(local_best_text)
    print("-----------------")

    if(local_best_fittness > best_fittness):
        best_fittness = local_best_fittness
        best_text = local_best_text
        best_key_length = key_length

print(best_key_length)
print(best_fittness)
print(best_text)
