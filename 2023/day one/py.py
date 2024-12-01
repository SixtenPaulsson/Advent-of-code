
def firstdig(line):
    if (line[0].isnumeric()):
        return int(line[0])
    return firstdig(line[1:(len(line))])
def seconddig(line):
    if (line[len(line)-1].isnumeric()):
        return int(line[len(line)-1])  
    return seconddig(line[0:(len(line)-1)])
def replaceNr(line):
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    return line

file = open("data.txt", "r")
värde=0
for x in file:
    line=replaceNr(x)
    print(line)
    värde=värde+(firstdig(line)*10+seconddig(line))
    print(värde)
file.close()
print(värde)