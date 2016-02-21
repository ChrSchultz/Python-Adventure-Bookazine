
import os as Os
import sys as Sys
import random as Random
import time as Time
class Adventure():
    
   
    
    def __init__(self):
        self.name = input("what is your name warrior?")
        
    def setup(self):
        print (self.name)
        self.__q = input(self.name +" do you want to start the with a saved game?(y|n)\n")
        if (self.__q == 'y'):
            fname = "adventure-" + self.name
            fobj = open(fname, "r")
            self.HP = int(fobj.read(2))
            fobj.seek(3)
            self.MP = int(fobj.read(2))
            print ("\nDaten gelesen")
            fobj.close()
        else:
            self.HP = Random.randint(5,20)
            self.MP = Random.randint(5,20)
            
            
            
            
    
    def north(self):
        print ("To go to north press 'n' followed by 'enter'")
    def east(self):
        print ("To go to east, press 'e' followed by 'enter'")
    def south(self):
        print ("To go tosouth, press 's' followed by 'enter'")

    def west(self):
        print("To go to west, press 'w' followed by 'enter'")
        
    def load(self):
    	fname = "adventure-" + self.name
    	fobj = open(fname, "r")
    	self.HP = int(fobj.read(2))
    	fobj.seek(3)
    	self.MP = int(fobj.read(2))
    	print ("\nDaten gelesen")
    	fobj.close()
    def save(self):
        #ts=time.strftime("%Y%b%d-%H%M%S")
        fname="adventure-" +self.name
        fobj=open(fname, "w")
        if (fobj):
            fobj.write(str(self.HP) +";"+ str(self.MP))
            fobj.close()
            print ("Spielstand gespeichert")
        else:
            print ("konnte Datei nicht anlegen")


    def villager(self):
        #This will create a randomly named Villager to interact with
        
        
        #Below is a list, we can store lots of things in a list and then retrieve them later.
        _responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
        _npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
        #Shuffle will shuffle the list contents into a random order.
        Random.shuffle(_npcnamechoice)
        npcname = _npcnamechoice[0]
        print ("[",npcname,":] Hello, my name is ",npcname,", Would you like to talk to me?", "(j|n)",sep="" )
        Random.shuffle(_responses)
        response=_responses[0]
        print ("Press y to talk to the villager")
        if input() == "y":
            print ("["+npcname+":] " ,response)
        else:
            print("[",npcname,":] Goodbye", sep=" ")

   
        
        
