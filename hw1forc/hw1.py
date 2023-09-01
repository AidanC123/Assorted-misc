#!/c/Python39/env python

import sys
import re
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#In case I need them

#nltk.download('averaged_perceptron_tagger')

financial_article, qa_filename = sys.argv[1], sys.argv[2] if len(
    sys.argv) > 2 else None

print("The financial article is '" + financial_article + "'")
print("The qa filename " + ("is '" + qa_filename +
      "'" if qa_filename else "has not been provided"))

###########################################################################
#Synonyms of words that coincide with positive stock increases 
synonym_rise = ["rise", "climb", "rose", "increase", "grow", "boost", "grew", "acclerate", "advance", "up", "raise", "hike", "surge", "improve", "growth", "progress", "climb", "open"]

#Synonyms of words that coincide with negative stock decreases
synonym_fall = ["fall", "lose", "plunge", "plunged", "drop", "down", "close", "closed", "fell", "sank"]

#Synonyms of words that coincide with possible future increases/decreases
badwords = ["future", "could"]

#Synonyms of words that coincide with closing of markets
syn_close = ["close", "closed", "shut"]

#Synonyms of words that coincide with opening of markets
syn_open = ["open", "opened"]

#The given text file being opened
filetxt = open(sys.argv[1],"r")
text = filetxt.read()

#function to evaluate questions asked or given by file
def questionEval(userinput):
    #empty lists that will be filled with positive/negative words in question
    posiwords = []
    negawords = []
    otherwords = []
    #Also seen in main function, works to end program
    if(userinput == "exit" or userinput == "EXIT" or userinput == "Exit"):
        quit()
    #Checks what "form" question was enter; different questions, different answers
    form = 0
    if re.match(r"^Did.*\?$",userinput):
        form = 1
    if re.match(r"^How\smuch.*\?$",userinput):
        form = 2
    if re.match(r".*open.*",userinput) or re.match(r".*close.*",userinput):
        form = 3
    #Checks question for pronouns, saves them
    final_input = nltk.pos_tag(userinput.split())
    for word,pos in final_input:
        propernouns = [word for word,pos in final_input if pos == 'NNP']
        userinput = userinput.lower()
    #Removes "?" marks, also adds postive and negative words in question to 
    #positive and negative lists
    for word in final_input:
        if (word[0].replace('?', '') in synonym_rise):
            posiwords.append(word[0].replace('?', ''))
        elif (word[0].replace('?', '') in synonym_fall):
            negawords.append(word[0].replace('?', ''))
        else:
            otherwords.append(word[0].replace('?', ''))
    #Checks whether question is positive ("rises") or negative ("falls") or neither
    posi_nega = 0
    if (posiwords > negawords):
        posi_nega = 1
    elif (posiwords < negawords):
        posi_nega = -1
    return(form,propernouns[0],posi_nega)

#function to evaluate article
def articleEval(text, form, propernoun, posi_nega):
    #Simplifies and cleans up text of article
    sentences = text.strip()
    words = nltk.word_tokenize(text)
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_words = []
    for word in words:
        if word.casefold() not in stop_words:
            filtered_words.append(word)
    final_words = nltk.pos_tag(filtered_words)
    #For form 1; checks words in text if the are positive or negative, and uses 
    #this information to return an answer
    textgood = 0
    textbad = 0
    for word in final_words:
        if (word[0].replace('?', '') in synonym_rise):
            textgood = textgood + 1
        elif (word[0].replace('?', '') in synonym_fall):
            textbad = textbad + 1
    if (form == 1):
        if textgood > textbad:
            return "It rose"
        if textgood < textbad:
            return "It fell"
        else:
            return "No information available"
    #For form 2; checks each line in text, then searches for pre-found pronouns and
    #adds to a new list of sentences that the pronoun was found in
    if (form == 2):
        pronountext = []
        finaltext = []
        complete = []
        forallNNP = []
        sentences = sentences.split("\n")
        for line in sentences:
            if re.search(propernoun, str(line)):
                pronountext.append(line)
                for line in pronountext:
                #Checks pre found posi_nega score, to decide which group of 
                #synonyms to use to sort thru again
                    if posi_nega < 0:
                        for word in synonym_fall:
                            if re.search(word, str(line)):
                                #skips if line already added
                                if any(line in text for text in finaltext):
                                    pass
                                else:
                                #creates final text to be used
                                    finaltext.append(line)
                    #Like above example, just for positive synonym set
                    if posi_nega > 0:
                        for word in synonym_rise:
                            if re.search(word, str(line)):
                                if any(line in text for text in finaltext):
                                    pass
                                else:
                                    finaltext.append(line)
        #Save actual values (will be used ahead)
        numbers = []
        #check to see if anything has been found yet, if not ends and returns no answer
        if not finaltext:
            return "No answer available"
        print("Source: " + finaltext[0])
        for line in finaltext:
            words = nltk.word_tokenize(line)
            words = nltk.pos_tag(words)
            forallNNP = words
            #Another checker of positivity (rise vs fall)
            if posi_nega < 0:
                #Effectively sorts looking for numbers, and adds the number if the word before it is a negative synonym
                for index, word in enumerate(words):
                    if (index+1 < len(words) and index - 1 >= 0):
                        if word[1] == "CD":
                            if any(words[index-1][0] in text for text in synonym_fall):
                                numbers.append(word[0])
            if posi_nega > 0:
                #Does same but for positive
                for index, word in enumerate(words):
                    if (index+1 < len(words) and index - 1 >= 0):
                        if word[1] == "CD":
                            if any(words[index-1][0] in text for text in synonym_rise):
                                numbers.append(word[0])
        #Had to be hard coded, in the text when tokenize it came back as 'S' '&' 'P'and I realized too late. Also happens in form 3
        if not numbers:
            return "No answer available"
        allNNP = ["S&P"]
        #Decides which of the numbers found should be used for which given pronoun
        for word,pos in forallNNP:
            if pos == "NNP":
                allNNP.append(word)
        trueindex = int(allNNP.index(propernoun)/2)
        if len(allNNP) >= 6:
            return numbers[trueindex]
        else:
            return numbers[0]

    #For form 3; like form 2, but differences will be noted
    if (form == 3):
        pronountext = []
        finaltext = []
        complete = []
        forallNNP = []
        sentences = sentences.split("\n")
        for line in sentences:
            if re.search(propernoun, str(line)):
                pronountext.append(line)
                for line in pronountext:
                    if posi_nega < 0:
                        for word in syn_close:
                            if re.search(word, str(line)):
                                if any(line in text for text in finaltext):
                                    pass
                                else:
                                    finaltext.append(line)
                    if posi_nega > 0:
                        for word in syn_open:
                            if re.search(word, str(line)):
                                if any(line in text for text in finaltext):
                                    pass
                                else:
                                    finaltext.append(line)
        numbers = []
        if not finaltext:
            return "No answer available"
        print("Source: " + finaltext[0])
        for line in finaltext:
            #tokenization is slightly adapted
            words = nltk.word_tokenize(line)
            forallNNP = nltk.pos_tag(words)
            if posi_nega < 0:
                for index, word in enumerate(words):
                    #Has to check more, previous word and the word after
                    if (index+1 < len(words) and index - 1 >= 0):
                        if word == "at" or word == "to":
                            if any(words[index-1] in text for text in syn_close):
                                numbers.append(words[index+1])
                            if words[index-1][0].isnumeric():
                                numbers.append(words[index+1])
            if posi_nega > 0:
                for index, word in enumerate(words):
                    #Does same for positive
                    if (index+1 < len(words) and index - 1 >= 0):
                        if word == "at":
                            if any(words[index-1] in text for text in syn_open):
                                numbers.append(words[index+1])
                            if words[index-1][0].isnumeric():
                                numbers.append(words[index+1])
        if not numbers:
            return "No information available"
        #Hardcode as mentioned before
        allNNP = ["S&P"]
        for word,pos in forallNNP:
            if pos == "NNP":
                allNNP.append(word)
        trueindex = int(allNNP.index(propernoun)/2)
        if len(allNNP) >= 6:
            return numbers[trueindex]
        else:
            return numbers[0]

#Controller function, takes input, runs through both questionEval then through articleEval
def answer(userinput):
    form, propernoun,posi_nega = questionEval(userinput)
    answer = articleEval(text, form, propernoun, posi_nega) 
    print(answer)

#main function, runs everything; also controls what user sees
def main():
    start = 1
    if(qa_filename == None):
        #For user input by hand
        while start == 1:
            val = input("Ask a question: ")
            if (val == "exit" or val == "EXIT" or val == "Exit"):
                start = 0
                break
            answer(val)
            filetxt.close()
    else:
        #For file input
        if(qa_filename!= None):
            fileinput = open(qa_filename, "r")
            textinput = fileinput.read()
            filequestion = textinput.strip()
            for i in re.split("\n", filequestion):
                print(answer(i))

if __name__ == "__main__":
    main()
