

# This code is attempt to crack a vigionare cipher

# Knowns:


# Key is between 10 and 20 characters long
# Sum of squares of frequencies for each letter is ~ .65 for english text
# Input string is 600 characters long

#data derived from http://www.data-compression.com/english.html
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}


f=file('blackhat_1.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]

# check frequencies at start for kicks
def get_sum_freqs_squared(input_text):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(input_text.count(chr(ascii)))/len(input_text)

    sum_freqs_squared = 0.0
    for ltr in normal_freqs:
        sum_freqs_squared += normal_freqs[ltr]*frequency[ltr]
    
    return sum_freqs_squared

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

print(get_sum_freqs_squared(text))


print("Original Text: " + text)

for key_length in range(10, 21):


    strings_to_test = []

    
    # create a substring to test of every 'nth' letter

    print("For key_length " + str(key_length))
    for index in range(0, key_length):
        string_to_test = ""
        for index2 in range(index, 600, key_length):
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

            freq = get_sum_freqs_squared(newText)

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

    freq = get_sum_freqs_squared(newText)
    print(freq)


