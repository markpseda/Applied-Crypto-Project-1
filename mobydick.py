import urllib2, ssl

response = urllib2.urlopen("https://vip.udel.edu/crypto/mobydick.txt", context=ssl._create_unverified_context())
mobytext = response.read()

onlyletters = filter(lambda x: x.isalpha(), mobytext)
loweronly = onlyletters.lower()

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

print "Should be near .065 if plain: " + str(sum_freqs_squared)