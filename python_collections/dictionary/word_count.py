text="hello hai hello hai hello"
words=text.split(" ") # ['hello','hai','hello','hai','hello']
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
# to print the word that is highest repeating
print(max(dict,key=dict.get)) # dict.get is used to access the value directly so that highest word can printed based on the value
#sorting
print(sorted(dict,key=dict.get,reverse=True))
