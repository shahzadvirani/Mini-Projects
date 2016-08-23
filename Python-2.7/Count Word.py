'''
program that will count the number of
times a chosen word occurs in a string
'''

def count_word(a,b):  #a represents the word. b represent the sentence.

    #method 1:
    #result=b.split()  #the sentence is converted to a list with each word being a seperate element
    #print ("The word '" + a + "' occurs " + str(result.count(a)) + " times in the sentence.")

    #method 2:
    num = 0  #number of occurences
    for word in b.split():  #loop through each word of the sentence
        if word == a:
            num += 1
    print ("The word '" + a + "' occurs " + str(num) + " times in the sentence.")

my_word=raw_input("Enter a word: ")
my_sentence=raw_input("Enter a sentence: ")

count_word(my_word,my_sentence)

