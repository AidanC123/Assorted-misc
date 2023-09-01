#open dictionary text file
with open("dictionary.txt", "r") as dic:
    corpus = dic.readlines()
dic.close()

corpus[len(corpus)-1] = corpus[len(corpus)-1] + '\n'

#global due to laziness, some needing to exist between individual cryptogram words
formatwords = []
savedwords = []
inputletter = []
markletters = []
markletters2 = []
endword = []
endcorpus = []
firstword = []
checkme = []
letters = []

while 0 != 1:
    cryptogram = input("Enter cryptogram: ")
    cryptowords = cryptogram.split()
    key = [[],[]]
    #for each word as input, run program
    for z in range(len(cryptowords)):
        #if word in dictionary equal to entered word, add to savedwords
        for word in corpus:
            if len(word)-1 == len(cryptowords[z]):
                savedwords.append(word.strip())
                
        for letter in cryptowords[z]:
            inputletter.append(letter)
            
        #create key based on structure of word
        for letter in cryptowords[z]:
            key[0].append(letter)
        for v in range(len(cryptowords[z])):
            key[1].append(v)
        
        markletters = inputletter
        
        #for first word, go over each letter and set to number, also update key with numbers
        if(cryptowords[0] == cryptowords[z]):
            a = 0
            for letter in markletters:
                a = a + 1
                for x in range(len(markletters)):
                    if letter == markletters[x]:
                        markletters[x] = a
            key[1] = markletters
        else:
            #for words that aren't the first word, issues here
            for v in range(len(cryptowords[0])):
                checkme.append(key[0][v])
            for letter in markletters:
                for otherletter in checkme:
                    if letter == otherletter:
                        #most notable unfinished part
                        #only uncommented because of indenting issue
                        key[1][key[0].index(letter)]
                        
        #uncomment print(key) below to see key and understand more of the code
        #print(key)   
                
        #for each word in savedwords, do process similar to above, giving numbers to letters
        for savedword in savedwords:
            b = 0
            markletters2 = []
            for letter in savedword:
                markletters2.append(letter)
            for letter in savedword:
                b = b + 1
                for x in range(len(savedword)):
                    if letter == savedword[x]:
                        markletters2[x] = b
            endword.append(markletters2)
        endcorpus.append(endword)
        endcorpus = endcorpus[0]
        
        #check if structure the same as cryptogram, then add to another list
        z = 0
        for word in endcorpus:
            if markletters == word:
                formatwords.append(savedwords[z])
            z = z + 1
        
        print(len(formatwords))
        print(formatwords)
        formatwords = []
        savedwords = []
        inputletter = []
        markletters = []
        markletters2 = []
        endword = []
        endcorpus = []
        firstword = []

    #enter a single space to exit (" ") (in case you wanted to run the word "exit", etc.)
    if (cryptogram[0] == " "):
        break
    
    #Didnt want to have to check each letter and try it against every other letter until a
    #word was found, so I tried to be clever. But I couldn't finish, it can only really run
    #one word at a time. Had issue making it run with two of the same letters, and inputing
    #two words at the same time. Can run with two letters but can't do two words.
    #I Underestimated how much time it would take to change it to make it work with 2 words
    #when words are done separately they work thou (as they would if they were a cryptogram
    #by themselves