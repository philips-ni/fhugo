def convertWord(s):
    if s == "":
        return s
        # rule 5
    if s[-1] in ['!', ",", "."]:
        return convertWordCore(s[:-1]) + s[-1]
    else:
        return convertWordCore(s)

def getVowelIndex(s):
    for i,val in enumerate(s):
	# rule 7, if "u" is part of "qu" don't treat it as vowel
        if val in "aeiouAEIOU" and (i > 0 and s[i-1:i+1] != "qu"):
	    return i
    return -1

def convertWordCore(s):
    # rule 3
    if s[0] in "aeiouAEIOU":
	ret = s + "way"
    else:
	vowelIndex = getVowelIndex(s)
	if vowelIndex == -1:
	    ret = s + "ay"
	else:
	    # rule 4 and 1
	    if s[0].isupper():
		# rule 6
		ret = s[vowelIndex:].capitalize() + s[:vowelIndex].lower() + "ay"
	    else:
		ret = s[vowelIndex:] + s[:vowelIndex] + "ay"
    return ret


def convertSentence(s):
    words = []
    word = ""
    convertedWords = []
    for c in s:
	if c in [",", "!"]:
	    words.append(word + c)
	    word = ""
	elif c == " ":
	    words.append(word)
	    word = ""
	else:
	    word += c
	if word != "":
	    words.append(word)
            # rule 2
    for word in words:
	convertedWords.append(convertWord(word))
    return " ".join(convertedWords)

inputs = ["Hello world", "Hello,world!", "eat apples", "bybye", "quickly and quietly", "ququi"]
for input in inputs:
    print("{} -> {}".format(input, convertSentence(input)))
