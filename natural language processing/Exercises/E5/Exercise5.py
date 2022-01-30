# Islam md Shariful 1720601
# MOHAMED MOUBARAK MOHAMED MISBAHOU MKOUBOI 1820705

import re
import os
import numpy as np
#os.chdir('D:\Sem 5\NLP\Exercise 5')

biDict = {}
triDict = {}


def ngram():
    with open('text-ngram.dat', 'r') as rflie:
        infile = rflie.readlines()

    bifile = open("bigram.dat", "w")
    trifile = open("trigram.dat", "w")

    sent = sent = [s for s in infile[0].split(".")]
    test_sentence = 'Natural language processing addresses fundamental questions at the intersection of human languages and computer science'
    v = 0
    for line in sent:
        # Bi_code
        for j in range(len(line.split())-1):
            biag = line.split()[j]+" "+line.split()[j+1]

            # biDict: creating dictionary for all bigrams in training file
            if biag not in biDict:
                biDict[biag] = 1
            else:
                biDict[biag] += 1

            bifile = open("bigram.dat", "a")
            bifile.write(str(biag)+"\n")
            bifile.close()

        # tri_code
        for k in range(len(line.split())-2):
            trifile = open("trigram.dat", "a")
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            if tri not in triDict:
                triDict[tri] = 1
            else:
                triDict[tri] += 1

            trifile.write(str(tri)+"\n")
            trifile.close()

    # test_dict: creating dictionary for all bigrams in testing sentence
    test_dict = {}
    for j in range(len(test_sentence.split())-2):
        words = test_sentence.split(
        )[k]+" "+test_sentence.split()[k+1]+" "+test_sentence.split()[k+2]
        if words not in test_dict:
            test_dict[words] = 1
        else:
            test_dict[words] += 1

    # Calculate probability of each c in test sentence
    probabilty_tri = []
    for key in test_dict:
        if key not in triDict:
            probabilty_tri.append(0)
        else:
            probabilty_tri.append(triDict[key]+1/biDict[key]+v)

    print('probability list: ', probabilty_tri)

    # Calculate the probability of the whole test sentence
    prob_sentence = np.sum(probabilty_tri)
    print('Probability of the whole test sentence: ', prob_sentence)


def print_dict(dict):  # function to print particular dictionary
    for level, value in dict.items():
        print(level, ':', value)


# probability calculaton
ngram()
# call the function
print("Dictionary: ")
print_dict(triDict)
