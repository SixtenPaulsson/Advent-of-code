def check(matrix,pos):
    visited = set()
    visit_times = {}
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    current = directions[0]
    in_path = "#"
    while "#" in in_path:
        imp = 1-current.index(0)
        ran =range([pos[imp]+1,len(matrix)-pos[imp]][max([current[imp],0])])
        in_path =[matrix[(current[0]*i)+pos[0]][(current[1]*i)+pos[1]] for i in list(ran)]
        if("#" in in_path): #kommer träffa #
            next_obs =in_path.index("#")
            obs_pos = pos[0]+next_obs*current[0],pos[1]+next_obs*current[1]
            pos_diff =abs(pos[0]-obs_pos[0]),abs(pos[1]-obs_pos[1])
            visited.update([((current[0]*i)+pos[0],(current[1]*i)+pos[1]) for i in range(max(pos_diff))])
            pos = obs_pos[0]-current[0],obs_pos[1]-current[1]
            visit_times[pos] = visit_times.get(pos,0)+1
            if(visit_times[pos]==5):
                return visited,1
            current= directions[(directions.index(current)+1)%4]
        else: #out of bounds
            visited.update([((current[0]*i)+pos[0],(current[1]*i)+pos[1]) for i in list(ran)])
    return visited,0

with open("2024/day6/day6.txt") as File:
    m1= File.read().split("\n")
    pos = [(index, row.index("^")) for index, row in enumerate(m1) if "^" in row][0]
    p1 = check(m1,pos)[0]
    print("part 1:",len(p1))
    p1.remove(pos)
    change_index =lambda y1,y2,y3:y3[:y1]+[y3[y1][:y2]+"#"+y3[y1][y2+1:]]+y3[y1+1:]
    disp = sum(list(map(lambda x:check(change_index(x[0],x[1],m1),pos)[1],p1)))
    print("part 2:",disp)