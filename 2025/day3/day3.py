def check2(num,times):#tex 994592349234, 12 (2 för p1 och 12 för p2)
    voltage_list = [] #Voltages läggs från vänster till höger
    list = [int(x) for x in (str(num))] #1234->[1,2,3,4]
    for i in range(times):
        if((times-i)-1<=0): #Försöker hämta listan förutom de (times-i) sista elementen
            region =list #[:-0] blir alltid [] så en check måste finnas
        else: 
            region =list[:-(times-i)+1]  #Tar bort de sista (times-i) elementen
        voltage_list.append(max(region)) #Slänger in det största talet i den checkade regionen
        list = list[list.index(max(region))+1:] #Tar bort allt till vänster om det största talet
    return int("".join([str(x) for x in voltage_list]))#tex [9,2]->92

with open("2025/day3/day3.txt") as File:
    lines =[int(x) for x in File.read().split()]#Läser ut filen
    print("part1:",sum(list(map(lambda line:check2(line,2 ),lines))))
    print("part2:",sum(list(map(lambda line:check2(line,12),lines))))