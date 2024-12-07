def check(goal,terms,current=0,ops=""):
    if(len(terms)==0):
        return goal==current
    add  = check(goal,terms[1:],current+int(terms[0]),ops)
    mult  = check(goal,terms[1:],current*int(terms[0]),ops)
    if("&" in ops): 
        concat = check(goal,terms[1:],int(str(current)+str(terms[0])),ops)
        return add or mult or concat
    return add or mult

with open("2024/day7/day7.txt") as File:
    a = File.read().split("\n")
    h = [x.split(":") for x in a]
    d = [(x[0],x[1].split()) for x in h]
    checked = list(filter(lambda x:check(int(x[0]),x[1][1:],int(x[1][0])),d))
    checked2 = list(filter(lambda x:check(int(x[0]),x[1][1:],int(x[1][0]),"&"),d))
    check_sum = lambda y:sum(map(lambda x:int(x[0]),y))
    print("part1:",check_sum(checked))
    print("part2:",check_sum(checked2))