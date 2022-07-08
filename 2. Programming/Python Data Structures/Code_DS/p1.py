punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
fopen = open("words.txt","r")
# LEARNER CODE START HERE
punclist = list()
dictionary = dict()
wordlist = list()
#spliting punctuation string to get the list
for p in punctuations:
#now punclist is the list of words we have to ignaore
    punclist.append(p)
for lines in fopen:
    lines.rstrip()
    wordlist.append(lines)
print(wordlist)
