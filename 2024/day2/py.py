def checklist(nums):
    differ =all(1<=abs(int(nums[i])-int(nums[i+1])) and 3>=abs(int(nums[i])-int(nums[i+1])) for i in range(len(nums)-1))
    asc = all(int(nums[i]) <= int(nums[i + 1]) for i in range(len(nums) - 1))
    desc =all(int(nums[i]) >= int(nums[i + 1]) for i in range(len(nums) - 1))
    return ((asc or desc) and differ)

with open("2024/day2/data.txt") as File:
    counter1 = 0
    counter2 = 0
    for row in File.read().split("\n"):
        nums = row.split()
        if(checklist(nums)):
            counter1+=1
            counter2+=1
        else:
            for i in range(len(nums)):
                if(checklist(nums[:i]+nums[i+1:])):
                    counter2+=1
                    break
print("part1:",counter1)
print("part2:",counter2)
