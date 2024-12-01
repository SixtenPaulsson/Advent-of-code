with open("2024/day1/data.txt") as File:
    list1,list2 = [],[]
    for row in File.read().split("\n"):
        nums = row.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
list1.sort()
list2.sort()
summa1 = sum(map(lambda x,y: abs(x-y) , list1, list2))
summa2 = sum(map(lambda x: x*list2.count(x) , list1))
print("Part 1:",summa1)
print("Part 2:",summa2)