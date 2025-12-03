def filter_wrong(text,rules):
    sp = text.split(",")
    
    for i in range(len(sp)):
        #Kollar ifall saken är med på regelbrytarlistan
        if(len([a for a in rules.get(sp[i],[]) if a in sp[i+1:]])!=0):
            #print(len(sp),len([a for a in rules[sp[i]] if a in sp[i+1:]]))
            return False
    return True

def fix(sp,rules):
    print(sp)
    print("hej")
    for a in sp:
        
        print(a,rules.get(a,[]))
    return sp
 
with open("2024/day5/day5.txt") as File:
    rules, updates =[x.split("\n") for x in File.read().split("\n\n")]
    rule_list = {}
    for rule in rules:
        a = rule.split("|")
        rule_list[a[1]]=rule_list.get(a[1],[])+[a[0]] 
    #Tar bort sakerna som bryter mot reglerna
    valid = filter(lambda x: filter_wrong(x, rule_list), updates)
    false = filter(lambda x: not filter_wrong(x, rule_list), updates)
    print("asdd",list(false))
    print("asd",list(map(lambda x: x, false)))
    fixed = list(map(lambda x:fix(x.split(","),rule_list),list(false)))
    print(fixed)
    #print(fix(list(false.spl),rule_list))
    #Summerar mitten på de som är kvar
    sum = sum(list(map(lambda x:int(x.split(",")[(len(x.split(","))-1)//2]),valid)))
    print("part1:",sum)