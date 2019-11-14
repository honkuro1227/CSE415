# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#the input string.
 #It should compute the wordlist and mapped_wordlist values 
 #at the beginning of the function body instead of 
 #receiving those as inputs as in Shrink3.py. 
 #Second, instead of printing out its response, your respond function should return it as a string. 
 #This will allow the other agent to receive it as input in the joint-dialog program.

# Shrink3.py
# A conversational "doctor" simulation modelled loosely
# after J. Weizenbaum's ELIZA.
# This Python program goes with the book "The Elements of Artificial
# Intelligence".
# This version of the program runs under Python 3.x.

# Steven Tanimoto
# (C) 2012.
#MEMORY FEATURE, CYCLE FEATURE, and RANDOM-CHOICE feature
from re import *
from random import choice
wordList=["Say more","I am listening","...","Could you speak again","I cannot help you"]
defaultend=["Anything else?","Glad to help you","If you have any problem, I will try to help you!"]
NgwordsList=["stupid","idiot","useless","fuck","terrible"]
foodList=["Dumpling","Ramen","Spaghetti","Salman","Icecream"]
positive=["good","nice","yummy","delicious"]
VerbList=["is","tastes","looks"] 
bverbdo=["is","was","were","are","do","does","did","am"]
wver=["when","why","how","who","where"]
Memory=[]
Mapped_answer={"is":"am","was":"was","were":"was","are":"am"}
Mapped_wordList= {'i':'you', 'I':'you', 'me':'you','you':'i',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}
payment=None
paymentcontrol=0
countelse=0
noinput_time=0
count=0
def introduce():
    introduction="My name is Miku, and I am M-Mobile supporter.\nI was programmed by Hung Lo.\nIf you don't like the way I deal, contact him at honkuro@uw.edu\nHow can I help you?"
    return introduction
def respond(theInput):
    #record payment and function introduce part
    global payment
    global paymentcontrol
    global countelse
    global noinput_time
    global count
    global countpayment
    #1MEMORY FEATURE:
    if(theInput!=''):
        Memory.append(theInput)
    current_word_detect=split(" ",theInput)
    #print(current_word_detect)
    #todo fifteen rules for respond and five different when face same text        
    #2 MEMORY FEATURE rule:remember recent 5 sentences over than 5 pop out
    if(len(Memory)>5):        
        Memory.pop(0)
    #3 no Input
    if (theInput==''):
        noinput_time=noinput_time+1
        #RANDOM-CHOICE feature&& CYCLE FEATURE
        return choice(["please say something","Are you alright?","Are you still online?"])+" This is "+str(noinput_time)+" time you do not respond!"
    #4 check payment
    if any(x=="check" for x in current_word_detect):
        if any(x=="payment" for x in current_word_detect):
            rec="your recent payment is: "
            #5 check whether pay or not
            if (payment!=None):
                return rec+str(payment)
            else:
                #RANDOM-CHOICE feature
                return choice(["no recent payment record","you do not make any payment"])
    #6 make payment
    if (any(x=="make" for x in current_word_detect)):
        if(any(x=="payment" for x in current_word_detect)):
            paymentcontrol=1
            return "How much you want to pay ?"
    #7 enter the payment and check int or not
    if (paymentcontrol==1):
        try:
            payment = float(theInput)
            paymentcontrol=0
            return "success"+choice(defaultend)
        except ValueError:
            #RANDOM-CHOICE feature
            return choice(["That's not an number! ","Try again"])

    #8 default respond for too short sentence
    if(len(current_word_detect)<3 and countelse==1):    
        return choice(wordList)+" I cannot understand what \""+theInput+"\" mean."+choice(wordList)
    #9 1st and 2nd person solution
    if(countelse==1 and len(current_word_detect)>2):  
        if current_word_detect[0:2]==['you','are']:
            current_word_detect.pop(0)
            current_word_detect.pop(0)
            result=' '.join(current_word_detect)            
            return 'Why you think I am '+result
        if  current_word_detect[0:2]==['I','am']:
            current_word_detect.pop(0)
            current_word_detect.pop(0)
            result=' '.join(current_word_detect)            
            return 'what make you are '+result
        else:
            choice(["I cannot understand!","This is not my business","Try to tell other"])
    #10 bandAuxiliary verb
    if (current_word_detect[0].lower() in bverbdo):
        Subject=''
        verb=''
        ans=["Yes, ","No, "]
        for x in current_word_detect:
            if (x.lower() in Mapped_wordList):
                try:
                    Subject=Mapped_wordList[x]
                except:
                    Subject=x 
        try:
            verb=Mapped_answer[current_word_detect[0].lower()]
        except:
            verb=current_word_detect[0].lower()
        if (choice(range(10))%2==0):
            return ans[0]+Subject+" "+verb
        else:
            return ans[1]+Subject+" "+verb+" not"
    #11 check repeat rapid ||cycle feature
    if(Memory[len(Memory)-1]==Memory[len(Memory)-2] and len(Memory)>1):
        return choice(["Can you say something new?","You mention that before","Stop giving me same response!"])
    #12 mission describe
    if(countelse==0):
        countelse=1
        return "\nI could do these for you:\nmake payments\ncheck payment status\nif the problem is not on the list, please type other! \nPlease tell me what you want to do today"
    #13  #RANDOM-CHOICE feature pick recent conversation 
    if (len(Memory)>4):
        randpickconversa=split(" ",choice(Memory))
        for x in range(len(randpickconversa)):
            try:
                randpickconversa[x] = Mapped_wordList[randpickconversa[x]]
            except KeyError:
                a=0
        result=' '.join(randpickconversa)
        return "I am interested that why you say\""+result+"\" before?"
    #14 say byebye
    if match('bye',theInput.lower()):
        return "see you"
     #15 out of rule: talk about food||cycle feature
    else :
        return "My favorite food is "+choice(foodList)+" because it "+choice(VerbList)+" "+choice(positive)
    #rule introduce and tend user function
    
def agentName():
    name="Miku"
    return name
"""
def Miku():
    print(introduce())
    while True:  
        current_speaking=""
        the_input = input('TYPE HERE:>> ')
        #loop control
        if match('bye',the_input.lower()):
            print ("see you")
            break
        current_speaking=respond(the_input)
        print(current_speaking)
    return

Miku() # Launch the program.
"""