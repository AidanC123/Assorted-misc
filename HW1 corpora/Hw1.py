
import re
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.lm import Laplace
stop_words = set(stopwords.words('english'))
    
def unigram_bigram(text):
    unigram = []
    bigram = []
    wordcount = 0
    sentence = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(sentence)
    for word in words:
        wordcount = wordcount + 1
        if (word == 's'):
            words.remove(word)
    unigram.extend(list(ngrams(words, 1)))
    bigram.extend(list(ngrams(words, 2)))  
    return unigram, bigram, wordcount

def main():
    textfile1 = open("corpora1.txt",encoding = "latin-1")
    textfile2 = open("corpora2.txt",encoding = "latin-1")
    text1 = textfile1.read()
    text2 = textfile2.read()
    textfile1.close()
    textfile2.close()
    unigram, bigram, wordcount = unigram_bigram(text1)
    unigramfreq = nltk.FreqDist(unigram)
    bigramfreq = nltk.FreqDist(bigram)
    print(wordcount)
    print(unigramfreq.most_common(10))
    print("Frequency of being in article")
    for word,amount in unigramfreq.most_common(10):
        print(amount/wordcount)
    print(bigramfreq.most_common(10))
    print("Frequency of being in article")
    for word,amount in bigramfreq.most_common(10):
        print(amount/wordcount)
    add1smooth = nltk.LaplaceProbDist(bigramfreq)
    print("Appearances of sentence fragments")
    print(add1smooth.prob(("the","godfather")))
    print(add1smooth.prob(("his","daughter")))
##################################################################
    print("####################################################################")
    unigram, bigram, wordcount = unigram_bigram(text2)
    unigramfreq = nltk.FreqDist(unigram)
    bigramfreq = nltk.FreqDist(bigram)
    print(wordcount)
    print(unigramfreq.most_common(10))
    print("Frequency of being in article")
    for word,amount in unigramfreq.most_common(10):
        print(amount/wordcount)
    print(bigramfreq.most_common(10))
    print("Frequency of being in article")
    for word,amount in bigramfreq.most_common(10):
        print(amount/wordcount)
    add1smooth = nltk.LaplaceProbDist(bigramfreq)
    print("Appearances of sentence fragments")
    print(add1smooth.prob(("the","godfather")))
    print(add1smooth.prob(("his","daughter")))
    
if __name__ == "__main__":
    main()