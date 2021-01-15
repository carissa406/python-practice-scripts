problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
solution = False

#--------------------------------------------------------
#cannot have more than 5 problems
#if len(problems) > 5:
    #return "Error: Too many problems."

#can only do addition and subtraction
#prob = 0
#for prob in problems:
    #if prob[1] != "+" or "-":
        #return "Error: Operator must be '+' or'-'"
    #else:
        #continue
#---------------------------------------------------------

splitnums=[]
intproblems=[]
sortedproblems = []

#split the numbers and operators away from each other, now have a list of lists
#with each list containing each individual problem, strings
for i in problems:
    splitnums.append(i.split())
#print(splitnums)

#for each problem, sort the problem by length of character, with the largest
#character at the end of the list, each character is a string
for list in splitnums:
        sortedproblems.append(sorted(list, key=len))
#print(sortedproblems)

#for each problem, convert the numbers into integers, else, leave the operator
#as a string
for list in splitnums:
        for nums in list:
            try:
                intproblems.append(int(nums))
            except:
                intproblems.append(nums)
#print(intproblems)

#------------------------------------------------------------------
#print error for only int numbers allowed
#for num in intproblems:
    #if type(num) == int
        #continue
    #else if type(num) == str
        #continue
    #else:
        #return "Error: Numbers must only contain digits."

#print error that number cannot be more than four digits
#for list in splitnums:
    #for num in list:
        #if len(num) > 4:
           # return "Error: Numbers cannot be more than four digits."
        #else:
            #continue
#------------------------------------------------------------------

totalspaces = []
dashes = []

#the number of lines required to separate the problem from the solution
for list in sortedproblems:
    totalspaces.append(len(list[-1] + "  "))
#print(totalspaces)
#printing the lines
for i in totalspaces:
    dashes.append("-"*i)
#print(dashes)
completeddashes =""
for i in dashes:
    completeddashes += i + "    "

firstele = []
operator = []
lastele = []
for list in splitnums:
    #print((" ")*spaces[list] - len(list[0]))
    firstele.append(list[0])
#print(firstele)
for list in splitnums:
    operator.append(list[1])
#print(operator)
for list in splitnums:
    lastele.append(list[2])
#print(lastele)

firstspaces = []
secondspaces = []
#storing the number spaces needed in the first and second lines of the 
#lines of numbers
i = 0
for ele in firstele:
    firstspaces.append(totalspaces[i] - len(ele))
    i += 1
#print(firstspaces)

i = 0
for ele in lastele:
    secondspaces.append(totalspaces[i] - len(ele) -1)
    i += 1
#print(secondspaces)

completedfirst =""
i=0
for space in firstspaces:
    completedfirst += firstspaces[i]*" " + firstele[i]+"    "
    i+=1

completedsecond =""
i=0
for space in secondspaces:
    completedsecond += operator[i]  + (secondspaces[i])*" " + lastele[i]+"    "
    i+=1

#print(completedfirst)
#print(completedsecond)
#print(completeddashes)

#return completedfirst + "\n" + completedsecond + "\n" + completeddashes

solutionslist = []
if solution == True:
    x = 0
    y = 0
    i = 0
    for num in intproblems:
        if type(intproblems[i+1]) == str:
            x = num
            y = intproblems[i+2]
            if intproblems[i+1] == '+':
                    solutionslist.append(x + y)
            else:
                    solutionslist.append(x - y)
        else:
            continue

print(solutionslist)