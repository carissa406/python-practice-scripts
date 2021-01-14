problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


splitnums=[]
intproblems=[]
sortedproblems = []

#split the numbers and operators away from each other, now have a list of lists
#with each list in the list containing each individual problem, strings
for i in problems:
    splitnums.append(i.split())
print(splitnums)

#for each problem, convert the numbers into integers, else, leave the operator
#as a string
for list in splitnums:
        for nums in list:
            try:
                intproblems.append(int(nums))
            except:
                intproblems.append(nums)
print(intproblems)

#for each problem, sort the problem by length of character, with the largest
#character at the end of the list, each character is a string
for list in splitnums:
        sortedproblems.append(sorted(list, key=len))
print(sortedproblems)

fourspaces = "    "
spaces = []

#the number of lines required to separate the problem from the solution
for list in sortedproblems:
    spaces.append(len(list[-1] + "  "))
print(spaces)

firstele = []
operator = []
lastele = []

for list in splitnums:
    #print((" ")*spaces[list] - len(list[0]))
    firstele.append(list[0])
print(firstele)

for list in splitnums:
    operator.append(list[1])
print(operator)

for list in splitnums:
    lastele.append(list[2])
print(lastele)


first_line = '{:>4}    {:>4}    {:>4}    {:>4}'.format(firstele[0], firstele[1], firstele[2], firstele[3])
second_line = '{:>4}    {:>4}    {:>4}    {:>4}'.format(operator[0] + lastele[0], operator[1] + lastele[1], operator[2] + lastele[2], operator[3] + lastele[3])
print(first_line)
print(second_line)
#problem1 = "32 + 432"
#intproblem1 = []
#finalintproblem1 =[]

#justnums = problem1.split()
#print(justnums)

#for i in justnums:
    #try:
        #intproblem1.append(int(i))
    #except:
        #intproblem1.append(i)
#print(intproblem1)