

words="apple come to apple asks banana how is papaya doing about apple"

word_dict= {}

for word in words.split():
	if word in word_dict:
		word_dict[word] +=1
	else:
		word_dict[word]=1
for word, count in sorted(dict.iteritems(word_dict), key=lambda k: k[0]):
	print "%s: %d\n"%(word, count)

print word_dict
	

