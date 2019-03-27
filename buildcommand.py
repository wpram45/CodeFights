import json
from collections import OrderedDict

new_json={}
temp={}

def build(new_temp):
    for k in new_temp:
                
        v=new_temp[k]
                
        if isinstance(v,int) or isinstance(v,float):
            new_temp[k]=0
        if isinstance(v,str):
            new_temp[k]=""
        if isinstance(v,list):
            new_temp[k]=[]
        if isinstance(v,dict):
            build(v)

def buildCommand(jsonFile):

    jsonObject = json.loads(jsonFile)
    
    for key in jsonObject:
        value=jsonObject[key]
        
        if isinstance(value,dict):
            #print("1",temp)
            new_temp=value
            for k in new_temp:
                
                v=new_temp[k]
                
                if isinstance(v,int):
                    new_temp[k]=0
                if isinstance(v,str):
                    new_temp[k]=""
                if isinstance(v,list):
                    new_temp[k]=[]
                if isinstance(v,dict):
                    build(v)
                    
                
          #  print("zzzz",new_temp)
            new_json[key]=new_temp
            
            
            
            
            
        elif isinstance(value,int) or isinstance(value,float):
            
            new_json[key]=0
        elif isinstance(value,list):
            new_json[key]=[]
            
        elif isinstance(value,str):
            new_json[key]=""
        #print(key,value)
            
        
    #print(new_json)  
    #print("---")
    #build(new_json)
                
    print("new_json",new_json)
    
    return json.dumps(new_json)