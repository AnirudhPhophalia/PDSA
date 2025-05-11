def odd_one(L):
# ek dictionary bana sakte hai aur jis dtatatype wil be one that we will return
    p ={}
    for el in L:
        if type(el) not in p:
            p[type(el)]=0
        p[type(el)] +=1
        
    for key, value in p.items():
        if value == 1:
            return key.__name__
            
print(odd_one(eval(input().strip())))