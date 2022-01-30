#This program demonstrates steps to extract n-grams and save it in a file
#An example of saving in a dictionary is shown for unigram only. Modify the file to suit the exercise
#Use math.log(a,base) to find the log likelihood for each trigram probability - base can ether be '10' or 'e' for n-grams 

import re
import os
import math

#You have to call this function in your interpreter or editor to use/activate it
def ngram():

    #change this to your working directory	
    #os.chdir("C:/Users/H P/OneDrive/Documents/Sem 1 2021_22/CSCI 4342/Exercise")
    os.chdir("C:/Users/ H P/Downloads")

    
    #creates an empty dictionary for unigrams   
    unigram = {}  
    
    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("unigram.dat","w") #unigram file
    bifile = open("bigram.dat","w") #bigram file
    trifile = open("trigram.dat","w") #trigram file  
    
    sent = [s for s in infile[0].split(".")]
   
    for line in sent:        
        for j in range(len(line.split())-1):
            uni = line.split()[j]
            
	    #example of storing frequency counts of unigrams in dictionary
            if uni not in unigram.keys():
            	unigram[uni] = 1
            else:
                unigram[uni] += 1

	    #store this in dictionary	
            bi = line.split()[j]+" "+line.split()[j+1]
            print(bi)

            unifile = open("unigram.dat","a")
            bifile = open("bigram.dat","a")            
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()

        for k in range(len(line.split())-2):
            trifile = open("trigram.dat","a")
   
	    #store this in dictionary         
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            trifile.write(str(tri)+"\n")
            trifile.close()

        print(unigram)


        
