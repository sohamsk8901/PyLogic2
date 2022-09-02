

from logic import CreateExpression
from logic import EvalualteExpression
def PlaceValue(expression,key,value):
    
    if isinstance(expression[0],list):
        
        PlaceValue(expression[0],key,value)
        
    if isinstance(expression[2],list):
        PlaceValue(expression[2],key,value)
        
    if expression[0]==key:
        expression[0]=value
    
    if expression[2]==key:
        expression[2]=value
        
# e=CreateExpression(['myvalue','&',1],'||','val2')
# print(e)
# PlaceValue(e,'myvalue',1)

# PlaceValue(e,'val2',1) 
# print(e)
# print("result="+str(EvalualteExpression(e)))
    
    
    
    
    
    
    
    
    
    