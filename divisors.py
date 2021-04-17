def find_divisors(numList, inputNum):
   i = 1
   while i <= inputNum:
      if (inputNum % i) == 0:
         numList.append(i)
      i += 1
   
   return numList
