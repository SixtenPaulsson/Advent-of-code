from math import log10
def blink(stones,rule):
    st = []

    for x in stones:
        print(x,"är sak")
        if(rule.get(str(x),None)!=None):
            print(x,"blir",rule.get(str(x)),"dict")
            st+=rule.get(str(x))
        else:
            if(int(log10(x))+1)%2==0:
                sv = str(x)
                v1 = int(sv[:len(sv)//2])
                v2 = int(sv[len(sv)//2:])
                #mid = len(str(x))//2
                b=[v1,v2]
                print(x,"blir",v1,v2,"h")
            else:
                b=[x*2024]
                print(x,"blir",x*2024,"2024")
            rule[str(x)]=b
            st+=b
    print(stones)
    print(st)    
    return st,rule

with open("2024/day11/day11.txt") as File:
    stones = [int(x) for x in File.read().split()]
    fast = {"0":1}
    for i in range(5):
        #input()
        
        stones,fast = blink(stones,fast)
        #print(stones,fast)
        #print(i,len(stones),len(fast.keys()))
    print("part1",len(stones))