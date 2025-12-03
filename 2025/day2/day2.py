def concat(x):
    return int(str(x)+str(x))

def check_wrong(a,b):
    if(len(str(a))==len(str(b)) and len(str(a))%2==1):
        #print("udda",a,b)
        return 0
    #räkna ut max
    min,max = 0,0
    if(len(str(b))%2==1):
        
        maxis=pow(10,len(str(b))-1)-1
        max = int(str(pow(10,len(str(b))-1)-1)[-len(str(maxis))//2:])
        #print(max)
    else:

        första = int(str(b)[0:len(str(b))//2])
        if(len(str(första))!=len(str(första-1))):
            print("fel")
        if(concat(första)<=b):
            max =första
        else: 
            max = första-1
        #print("max jämnt:",b,concat(första))
    #1000

    #Räkna ut min
    if(len(str(a))%2==1):
        min =pow(10,(len(str(a))-1)//2)
    else:
        #print("min jämnt:",a)
        första = int(str(a)[0:len(str(a))//2])
        print(första,concat(första),concat(första)>=a)
        if(len(str(första))!=len(str(första+1))):
            print("fel")
        if(concat(första)>=a):
            min =första
        else: 
            min = första+1



    #print("max,min",min,max)
    if(concat(min)>b or concat(max)<a):
        return 0
    
    return inter(min,max)

def inter(c,d):
    h = list(range(c,d+1))
    return sum([concat(x) for x in h])
    


with open("2025/day2/day2.txt") as File:
    intervalls =[[int(y) for y in x.split("-")] for x in File.read().split(",")]
    print(intervalls)
    wrong = list(map(lambda x :check_wrong(x[0],x[1]),intervalls))
    print(wrong)

    print("part 1:",sum(wrong))

    
    a = [sum([i for i in range(lo,hi+1) if(str(i) == str(i)[:len(str(i)) // 2] * 2)]) for lo,hi in intervalls]
    print(sum(a))
    b = []

    print("Part 2:", sum(
    sum(
        i for i in range(lo, hi + 1)
            if (s := str(i)) and (l := len(s)) and any(s == s[:l // q] * q for q in range(2, l + 1))
    ) for lo, hi in intervalls
))
