set=[]


def implies(a,b):
    if a and not b:
        return 0
    else:
        return 1
    
def iff(a,b):
    if a==b:
        return 1
    else:
        return 0



def CreateExpression(op1 , operation, op2):
    exp=[]
    exp.extend([op1,operation,op2])
    return exp
    
    
def EvalualteExpression(expression):
    
    if isinstance(expression[0],list):
        
        expression[0]=EvalualteExpression(expression[0])
        
    if isinstance(expression[2],list):
        expression[2]=EvalualteExpression(expression[2])
    
    if expression[1]=='&':
        x=expression[0] and expression[2]
        
    
    elif expression[1]=='||':
        x=expression[0] or expression[2]
        
    
    elif expression[1]=='->':
        x=implies(expression[0] , expression[2])
        
    
    elif expression[1]=='<->':
        x=iff(expression[0],expression[2])
        
    return x
        
        
            
    
# e=CreateExpression([0,'&',[1,'->',0]],'||',[0,'||',1])

# print(e)

# print("result:")


# print(EvalualteExpression(e))

    