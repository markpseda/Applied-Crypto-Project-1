# For cracking column transposition

# This is blackhat_2 because this already had distribution of english text



import fittness
import random

f=file('blackhat_2.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]


print("Original Text: " + text)
print()

best_fittness = 0
best_text = ""
best_key_length = 0

# First runthrough, 16 was clearly the key length
for key_length in range(8, 10):

    columns = [""]*key_length

    index = 0
    for c in text:
        columns[index] += c
        index = (index+1) % key_length

    columnOrder = range(0, key_length)

    fails = 0

    local_best_fittness = 0
    local_best_text = ""
    while(fails < 1000):

        before_text = ""

        for colVal in columnOrder:
            before_text += columns[colVal]

        before_fittness = fittness.getFitness(before_text)

        print(columnOrder)

        random_1 = random.randrange(0, key_length)
        random_2 = random.randrange(0, key_length)

        temp = columnOrder[random_1]

        columnOrder[random_1] = columnOrder[random_2]
        columnOrder[random_2] = temp

        print(columnOrder)
        after_text = ""
        for colVal in columnOrder:
            after_text += columns[colVal]

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
    
    
    if(local_best_fittness > best_fittness):
        best_fittness = local_best_fittness
        best_text = local_best_text
        best_key_length = key_length

print(best_key_length)
print(best_fittness)
print(best_text)
