#fyi
#part 1 är fett bra enligt mig
#(förutom att det är en while true loop, kan bli bättre)
#part 2 är väldigt oeffektiv dock
#kollar igenom varenda . i filen och försöker sätta en # på den
#går att göra en bättre algorithm

def check(matrix,pos):
    #mängd på tuple av besökta platser
    visited = set()
    #kollar hur många gånger varenda ställe blivit stannat på (part2)
    visit_times = {}
    #Hållen man kan kolla (north,east mm)
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    #Dit man kollar just nu
    current = moves[0]
    direction = "#"
    #main loopen, brukade vara en while true men gjorde den så här
    while "#" in direction:
        #Hämtar index på den "viktiga" ändringen man kollar mot
        #tex North alltså (-1,0) betyder att det ba är -1 som ändrar på position
        #0 blir då imp
        imp = 1-current.index(0)
        #hämtar rangen åt riktningen man kollar mot, tex att det är 60 punkter väst tex
        ran =range([pos[imp]+1,len(matrix)-pos[imp]][max([current[imp],0])])
        #hämtar alla saker åt håller man kollar mot
        direction =[matrix[(current[0]*i)+pos[0]][(current[1]*i)+pos[1]] for i in list(ran)]
        #out of bounds check
        if("#" in direction):
            #.index ger error ifall # inte finns så if behövs
            next_obs = direction.index("#")
            #Hämtar coords på obstaceln
            obs_pos = pos[0]+next_obs*current[0],pos[1]+next_obs*current[1]
            #skillnad på gubbens pos och 
            change =abs(pos[0]-obs_pos[0]),abs(pos[1]-obs_pos[1])
            
            #hämtar och slänger in alla besökta coords i mängden
            visited_xy =[((current[0]*i)+pos[0],(current[1]*i)+pos[1]) for i in range(max(change))]
            visited.update(visited_xy)

            #updaterar ens pos
            pos = obs_pos[0]-current[0],obs_pos[1]-current[1]
            
            #för part2 (mycket mer effektiv kod finns)
            #ifall man har besökt 5 gånger måste man va i loop
            visit_times[pos] = visit_times.get(pos,0)+1
            if(visit_times[pos]==5):
                #print("loop")
                #ettan betyder att det är loop
                return visited,1
            
            #änder riktning
            current= moves[(moves.index(current)+1)%4]
        #ifall man blir out of bounds
        else:
            visited.update([((current[0]*i)+pos[0],(current[1]*i)+pos[1]) for i in list(ran)])
    return visited,0


with open("2024/day6/day6.txt") as File:
    m1= File.read().split("\n")
    pos = [(index, row.index("^")) for index, row in enumerate(m1) if "^" in row][0]
    p1 = check(m1,pos)[0]
    print("part 1:",len(p1))
    #part 2 kod
    #antal sätt att få loops
    #sätter ba ut obs på passerade ställen i p1
    #extremet jävla långsamt dock
    disp = 0
    for x in p1:
        disp+=check(m1[:x[0]]+[m1[x[0]][:x[1]]+"#"+m1[x[0]][x[1]+1:]]+m1[x[0]+1:],pos)[1]
    print("part 2:",disp)

