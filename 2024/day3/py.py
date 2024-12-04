import re
def mul(text):
    x = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", text)
    nums = list(map(lambda s: s[4:].strip("()").split(","),x))
    return sum(list(map(lambda s: int(s[0])*int(s[1]) ,nums)))
with open("2024/day3/day3.txt") as File:
    text = File.read()
    te = text.split("don't()")
    #a = ["" if(te[i].count("do()")==0) else te[i][te[i].index("do()"):] for i in range(1,len(te))]
    for i in range(1,len(te)):
        if(te[i].count("do()")==0):
            te[i]=""
        else:
            te[i]=te[i][te[i].index("do()"):]
    te="".join(te)
    print("Part1:",mul(text))
    print("Part2:",mul(te))