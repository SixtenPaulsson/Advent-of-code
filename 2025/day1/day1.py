with open("2025/day1/day1.txt") as File:
    list =[int(x) for x in File.read().replace("L","-").replace("R","").split()]
    
    current_num=50
    p2 = 0
    list2 = []
    for i in range(len(list)):
        

        print(current_num,list[i],list[i]//100)
        
        range_modulo = list[i] % 100
        p2 += (current_num + range_modulo) // 100 + list[i] // 100


            
            


        current_num=(current_num+list[i])%100
        list2.append(current_num)

    



    #print(list2)
    print("Part1:",list2.count(0))
    print("Part2:",p2)