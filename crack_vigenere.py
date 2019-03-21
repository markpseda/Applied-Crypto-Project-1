

# This code is attempt to crack a vigionare cipher

# Knowns:


# Key is between 10 and 20 characters long
# Sum of squares of frequencies for each letter is ~ .65 for english text
# Input string is 600 characters long

import fittness

f=file('blackhat_1.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))



print("Original Text: " + text)


bestFit = 0
bestFit_text = ""
for key_length in range(10, 21):


    strings_to_test = []

    
    # create a substring to test of every 'nth' letter

    print("For key_length " + str(key_length))
    for index in range(0, key_length):
        string_to_test = ""
        for index2 in range(index, len(text), key_length):
            string_to_test += text[index2]
        #print(string_to_test)
        strings_to_test.append(string_to_test)
    
    print("Num strings: " + str(len(strings_to_test)))

    # for this substring, try all shift amounts and print the one that is closest match to .65 frequency
    

    key_test = []
    
    for string in strings_to_test:
        #print("String testing: " + string)
        possible_shifts = []

        best_shift = 0
        best_freq = 1
        for num_shift in range(1, 27):

            local_string = string
            newText = ""
            for character in local_string:
                local_offset = num_shift
                newChar = character
                while local_offset > 0:
                    if(newChar == 'z'):
                        newChar = 'a'
                    else:
                        newChar = chr(ord(newChar) + 1)
                    local_offset -= 1
                newText += newChar

            freq = fittness.get_sum_freqs_squared(newText)

            if(abs(freq - .065) < abs(best_freq - .065)):
               best_freq = freq
               best_shift = num_shift

        #print("Best shift and freqency:")
        #print(best_shift)
        #print(best_freq)

        key_test.append(best_shift)


    print(key_test)


    print("Trying it out!")

    newText = ""
    index = 0
    for c in text:
        index_mod = index % key_length
        newChar = shiftBy(c, key_test[index_mod])
        newText += newChar
        index += 1

    freq = fittness.get_sum_freqs_squared(newText)
    print(freq)

    fit = fittness.getFitness(newText)

    if(fit > bestFit):
        print("Best Fit: " + str(fit))
        bestFit = fit
        bestFit_text = newText


print("Best fit: " + str(bestFit))
print(bestFit_text)



