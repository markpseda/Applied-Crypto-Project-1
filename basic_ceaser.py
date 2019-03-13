#original = "hvwgw gqozz srobv wghcf wqozq wdvsf psqoi gswhw gpfcy sbhbl"
original = "sahyk iapkp daben opzwu kbpda naopk bukqn hebau"

def tryCeasarShift(text, offset):
    #print("text: " + text)
    #print("offset: " + str(offset))
    newSentence = ""

    for character in text:
        local_offset = offset
        if(character != ' '):
            newChar = character
            while local_offset > 0:
                if(newChar == 'z'):
                    newChar = 'a'
                else:
                    newChar = chr(ord(newChar) + 1)
                local_offset -= 1
        else:
            newChar = ' '
        newSentence += newChar
    return newSentence

for i in range(1, 26):
    print(str(i) + ": ")
    print(tryCeasarShift(original, i))