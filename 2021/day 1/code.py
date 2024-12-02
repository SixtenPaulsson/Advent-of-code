file = open("2021/day 1/text.txt")
lines = file.readlines()
file.close()

raises = -1
start = 0

for i in range(len(lines)):
    lines[i] = int(lines[i].strip("\n"))
    if(lines[i]>start):
        raises+=1
    start = lines[i]



raises2 = -1
start2 = 0

for i in range(len(lines)-2):
    if(lines[i]+lines[i+1]+lines[i+2]>start2):
        raises2+=1
    start2 = lines[i]+lines[i+1]+lines[i+2]
    print(lines[i]+lines[i+1]+lines[i+2])

print("Part 1", raises,  "raises")
print("Part 2", raises2, "raises")