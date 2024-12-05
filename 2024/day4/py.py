def xmas(coord,list):
    checkers =[(x,i) for x in range(-1,2) for i in range(-1,2)]
    checkers.remove((0,0))
    counter=0
    for x in checkers:
        g = "X"
        for i in range(1,4):
            c =x[0]*i+coord[0],x[1]*i+coord[1]
            if(0 <= c[0] < len(list) and 0 <= c[1] < len(list[0])):
                g+=list[c[0]][c[1]]
        if(g=="XMAS"):
            counter+=1        
    return counter     

with open("2024/day4/day4.txt") as File:
    coords = File.read().split("\n")
    count,count2 = 0,0
    for i in range(len(coords)):
        for y in range(len(coords[i])):
            if(coords[i][y]=="X"):
                count+=xmas((i,y),coords)
            if(coords[i][y]=="A"):
                if(0 < i < len(coords)-1 and 0 < y < len(coords[0])-1):
                    a1,a2 = coords[i-1][y-1],coords[i+1][y+1]
                    b1,b2 = coords[i-1][y+1],coords[i+1][y-1]
                    b="".join(a1+a2+b1+b2)
                    count2+=int(b in ["SMSM","SMMS","MSMS","MSSM"])
print("part1:",count)
print("part2:",count2)