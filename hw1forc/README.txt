Name - Aidan Conley
Email - aidancon@udel.edu
Assignment 1: Stock Market QA System

Programming language: Python with Perl wrapper

Every file:
README - Contains information and program and how to run it.
hw1.py - Actual program itself, can take user input or a file of questions, and if they pertain to the article, it can also answer them. 
hw1.pl - Perl wrapper to run hw1.py 
test.txt - The article itself
inputtest.txt - A file of questions that can be run when added as the second argument

Supporting files:
Libraries: sys, re, nltk

NLP tools used:
from re: match, search
from nltk: tokenize (by word and by sentence), stopwords, pos_tag

How it works: Run the Perl code to begin (perl hw1.pl); there can be 1 or 2 arguments following this, the first being the stock article (mandatory) the second being a file of questions (non-mandatory). If you added the file of questions, the program runs and terminates itself. If you didn't, the program asks you for questions that should be typed in. When given a question relating to the article, the program returns an answer. The program will keep asking for questions until you enter "exit" as a question, after which it terminates. More detailed explanation can be found commented in the python file itself.

Features (limitations):
Known issues include problems with S&Q (hardcoded in), problems with IBM, and form 1 questions ("rise or fall") aren't implemented in the best way, though the right answer usually comes through. Form 1 questions also don't provide a source. 