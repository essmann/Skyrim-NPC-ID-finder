
from bs4 import BeautifulSoup


import requests
import time

list = []
def mainx():
    
    
    variable = 1

    found = False
    
    npc = input("Type an NPC name to get its constituent base ID: " + " ")
    while True:
        
        if(found==False and variable==30):
            print("Error: Couldn't find NPC")
            found = True
            variable = 1
            npc = input("Type an NPC name to get its constituent base ID: " + " ")
        
        if(variable==1):
            url = "https://skyrimcommands.com/npcs/"
            variable+=1
            data = requests.get(url)
            soup = BeautifulSoup(data.text, "html.parser")

            tags = soup.findAll("td")
            
            for tag in tags:
                index = tags.index(tag)
                
                    
                
                if(tag.text==npc):
                    id = (tags[index+1]).text
                    print(npc +":" + " " + " " + id)
                    found = True
                    variable = 1
                    
                    
                    
                    mainx()
                    
        
            
            
        else:
            url = "https://skyrimcommands.com/npcs/{}".format(variable)
            variable+=1
            data = requests.get(url)
            soup = BeautifulSoup(data.text, "html.parser")

            tags = soup.findAll("td")
            for tag in tags:
                index = tags.index(tag)
                
                
                if(tag.text==npc):
                    id = (tags[index+1]).text
                    list.append("{}:{}".format(npc,id))
                    
                    found = True
                    variable = 1
                    print(npc +":" + " " + " " + id)
                    
                    print(list)
                   
                        
                    
                    
                    mainx()
                   
                    
               
            print(url)
            
mainx()
    
        