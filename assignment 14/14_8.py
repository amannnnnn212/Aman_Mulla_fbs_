# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

str="eat tea tan ate nat bat"
words = str.split(" ")

sorted_words = []
res = []

for w in words:
    wrd = ''.join(sorted(w))
    sorted_words.append(wrd)

# print(sorted_words)

for i in range(len(sorted_words)):
    grp = []
    for j in range(i+1,len(sorted_words)):
        if sorted_words[i] == sorted_words[j]:
            grp.append(words[i])
            grp.append(words[j])
    if grp:   # append only if grp is not empty
        res.append(grp)

print(res)