text=input("enter the word:")
longest=0
for words in text.split():
    if len(words)>longest:
        longest=len(words)
        longestword=words
print("the longrst word is",longestword,"with length",len(longestword))
        
