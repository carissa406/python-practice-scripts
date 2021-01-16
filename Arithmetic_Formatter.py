problems = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
solution = True

def arithmetic_arranger(problems, solution=False):
  #cannot have more than 5 problems
  if len(problems) > 5:
      return "Error: Too many problems."

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

  #can only do addition and subtraction
  prob = 0
  for prob in splitnums:
      if prob[1] != "+" and prob[1] != "-":
          return "Error: Operator must be '+' or '-'."

  #for each problem, convert the numbers into integers, else, leave the operator
  #as a string
  for list in splitnums:
          for nums in list:
              try:
                  intproblems.append(int(nums))
              except:
                  if nums == '+' or nums == '-':
                    intproblems.append(nums)
                  else:
                      return "Error: Numbers must only contain digits."
  #print(intproblems)
  
  #print error for only int numbers allowed
  for num in intproblems:
      if type(num) == int:
          continue
      elif type(num) == str:
          continue
      else:
          return "Error: Numbers must only contain digits."

  #print error that number cannot be more than four digits
  for list in splitnums:
      for num in list:
          if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."
          else:
              continue
 

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
  completeddashes = completeddashes[:-4]

  #separating the first, second, and last lines to be printed
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
  completedfirst = completedfirst[:-4]

  completedsecond =""
  i=0
  for space in secondspaces:
      completedsecond += operator[i]  + (secondspaces[i])*" " + lastele[i]+"    "
      i+=1
  completedsecond = completedsecond[:-4]

  #print(completedfirst)
  #print(completedsecond)
  #print(completeddashes)

  #calculate the solution
  solutionslist = []
  x = 0
  y = 0
  i = 0
  for num in intproblems:
      if type(intproblems[i]) == str:
          x = intproblems[i-1]
          y = intproblems[i+1]
          if intproblems[i] == '+':
                  solutionslist.append(str(x + y))
          else:
                  solutionslist.append(str(x - y))
          i+=1
      else:
          i+=1
          continue

  #print(solutionslist)

  #create the strings to be printed for the solutions
  solutionspaces =[]
  i=0
  for num in solutionslist:
      solutionspaces.append(totalspaces[i] - len(num))
      i+=1
    
  completedsolutions =""
  i=0
  for space in solutionspaces:
      completedsolutions += solutionspaces[i]*" " + solutionslist[i]+ "    "
      i+=1
  completedsolutions = completedsolutions[:-4]

  if solution == True:
      print(completedsolutions)

  arranged_problems = completedfirst + "\n" + completedsecond + "\n" + completeddashes

  #final return statement
  if solution == True:
      arranged_problems += "\n" + completedsolutions

  return arranged_problems



print(arithmetic_arranger(problems, solution))