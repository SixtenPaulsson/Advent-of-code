def check_trail(coord,val,txt):
    print(coord,txt[coord[0]][coord[1]])
    visited = set()
    if(val=="9"):
        print(coord,"999")
        return coord
    for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
        if(coord[0]+a in range(len(txt)) and coord[1]+b in range(len(txt[0]))):
            print(val,(coord[0]+a,coord[1]+b),txt[coord[0]+a][coord[1]+b],"check")
            if(txt[coord[0]+a][coord[1]+b] == str(int(val)+1)):
                #print("ja")
                visited.update(check_trail((coord[0],coord[1]+1),str(int(val)+1),txt))
            #else:
                #print("nej")
    print(visited)

    return visited
    #print(coord)

with open("2024/day10/day10.txt") as File:
    visit = set()
    text = File.read().split("\n")
    for i in range(len(text)):
        for i2 in range(len(text[i])):
            if(text[i][i2]=="0"):
                visit.update(check_trail((i,i2),"0",text))
                input("ny")
                
    print(visit)
            #print(text[i][i2])