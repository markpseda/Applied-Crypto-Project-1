
import random
import urllib2

import fittness
# This code is attempt to crack a substitution cipher


# Was solved using a hill climb; the only shot-gunning was re-running the program

#data derived from http://www.data-compression.com/english.html
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}


f=file('blackhat_1.txt','r')
lines = [l.strip() for l in f] # should just be one
text = lines[0]

fails = 0

while(fails < 10000):
    flip1 = random.randrange(0, 26)
    flip2 = random.randrange(0, 26)

    before_fittness = fittness.getFitness(text)
    #print(chr(97 + flip1))
    #print(chr(97 + flip2))
    temp_text = text.replace(chr(97 + flip1), '~')
    temp_text = temp_text.replace(chr(97 + flip2), chr(97 + flip1))
    temp_text = temp_text.replace('~', chr(97 + flip2))

    after_fittness = fittness.getFitness(temp_text)

    if(after_fittness > before_fittness):
        print("improvement!")
        print(after_fittness)
        text = temp_text
        fails = 0
    else:
        fails += 1

print(text)



# very close:
close = "shecouldnotezvlaininsomanygordsbutshefeltthatthoseghovrevareforalltheemerkenciesoflifebeforehandmayejuivthemselwesattheezvenseofpoyitisafairewenhandednobleadpustmentofthinksthatghilethereisinfectionindiseaseandsorrogthereisnothinkinthegorldsoirresistiblycontakiousaslaukhterandkoodhumournooneisuselessinthisgorldretortedthesecretarygholikhtenstheburdenofitforanyoneelselewerakeisewerythinkgasghatiusedtosaydontbekintovrytillyouhawekotthelonkarmonyoursidehavvyaretheythatheartheirdetractionsandcanvutthemtomendinkbutthecloudnewercomesinthatjuarterofthehoriqonfromghichgegatchforitdesvairhasitsogncalms"

close = close.replace('z', '~')
close = close.replace('x', 'z')
close = close.replace('~', 'x')

close = close.replace('v', '~')
close = close.replace('p', 'v')
close = close.replace('~', 'p')

close = close.replace('g', '~')
close = close.replace('w', 'g')
close = close.replace('~', 'w')

close = close.replace('q', '~')
close = close.replace('j', 'q')
close = close.replace('~', 'j')

close = close.replace('g', '~')
close = close.replace('v', 'g')
close = close.replace('~', 'v')

close = close.replace('k', '~')
close = close.replace('g', 'k')
close = close.replace('~', 'g')

close = close.replace('j', '~')
close = close.replace('k', 'j')
close = close.replace('~', 'k')

close = close.replace('k', '~')
close = close.replace('z', 'k')
close = close.replace('~', 'z')

print(close)

# Now we have the final solution:
# Blackhat_1.txt:
# shecouldnotexplaininsomanywordsbutshefeltthatthosewhoprepareforalltheemergenciesoflifebeforehandmayequipthemselvesattheexpenseofjoyitisafairevenhandednobleadjustmentofthingsthatwhilethereisinfectionindiseaseandsorrowthereisnothingintheworldsoirresistiblycontagiousaslaughterandgoodhumournooneisuselessinthisworldretortedthesecretarywholightenstheburdenofitforanyoneelseleverageiseverythingwaswhatiusedtosaydontbegintoprytillyouhavegotthelongarmonyoursidehappyaretheythatheartheirdetractionsandcanputthemtomendingbutthecloudnevercomesinthatquarterofthehorizonfromwhichwewatchforitdespairhasitsowncalms