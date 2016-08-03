# -*- coding: utf-8 -*- 
import sys 
from cpsProviders import Providers as cps 
import simplejson as json 
if len(sys.argv) > 1 and sys.argv[1] == '1': 
    loop = True 
else: 
    loop = False 
comments = True 
def exit(): 
    sys.exit(0) 
def switch(option): 
    switch={1:'default_customer',2:'customer',3:'client'} 
    if option > len(switch.keys()): 
        raise Exception() 
    return switch[option] 
    
def returnJson(): 
    if comments: print('1: Default customer\n2: Full customer\n3: Client to register\n0: Exit\n:',end='') 
    try: 
        option = int(input()) 
        if not option: exit() 
        out = getattr(cps.all(), switch(option))() 
        jsonObj = json.dumps(out, indent = True, ensure_ascii=False, encoding="utf-8") 
        if comments : print(jsonObj) 
    except ValueError: 
        print('Please enter an integer') 
    #except Exception: 
        #print('Jesteś debilem') 
        
returnJson() 
while loop: 
	returnJson() 
