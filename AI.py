

import time
import random
from colors import red, green, blue

def jokes(different):
    jk = ""
    jokes = "How does the blonde try to kill a worm?","What did the DNA say to the other DNA?"
    
    for i in range(different):
        jk = jk + random.choice(jokes)
    print(jk)
    return jk

    

print("You can say, Tell me a joke. \nWhats the weather like?\nand ask anything about me. \nSo go ahead, ")
while True:
    userInput = input("Ask me anything.  ").lower()
    if userInput.startswith(("hi","hello")):
        print("Hello")
    elif userInput in ['Whats the wether?', 'Whats the wether like?', 'what is the wether']:
        print("i dont know")
    elif userInput in ['tell me a joke.','whats a funny joke?']:
    
    
        print("How does a blonde try to kill a worm?")
        time.sleep(3)
        print("By burrying it alive")
        print("Ha ha ahahaha that was a good one!")
    
    elif userInput in ['Tell me a joke','Tell me a fat joke.''Tell me a fat joke.''tell me a fat joke']:
        print("no never")
        
    elif userInput in ['tell me a joke.']:
        print("ok")
        
    elif userInput in ['tell me a joke']:
        print("What did the DNA say to the other DNA?")
        time.sleep(3)
        print("Do these genes make my butt look fat.")
    elif userInput in ['What are you','What do you do?','what do you do','what are you?','what are you']:
        print("I am a work in progress AI made by Aaron Gadeken, i can answer basic questions, and tell you things you would want to know.")
        
    
    else:
        print("I did not understand what you said")
  
