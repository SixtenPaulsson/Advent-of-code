def check2(list,times):
    voltage_list = []
    for i in range(times):
        if((times-i)-1<=0): #Försöker hämta listan förutom de (times-i) sista elementen
            region =list #[:-0] blir alltid [] så en check måste finnas
        else: 
            region =list[:-(times-i)+1] 
        voltage_list.append(max(region))
        list = list[list.index(max(region))+1:] #Slänger in det största talet i den checkade regionen
    return int("".join([str(x) for x in voltage_list]))#tex [9,2]->92

with open("2025/day3/day3.txt") as File:
    lines =[int(x) for x in File.read().split()]#Läser ut filen
    int_s = lambda x : [int(x) for x in (str(x))] #1234->[1,2,3,4]
    print("part1:",sum(list(map(lambda x :check2(int_s(x),2 ),lines))))
    print("part2:",sum(list(map(lambda x :check2(int_s(x),12),lines))))