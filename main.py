#Variables store a single value
#Lists store multiple values
# <list name> = [<item>, <item>, <item>, ...]

#Empty list
myList = []



# Let's make a better list
newList = ["Alice", "Bob", "Chad", "Erin"]

print(newList)

#Important Note: Items are indexed starting at index 0.
#We can print individual elements.

print(newList[0]) #Should be Alice
print(newList[3]) #Should be Erin
#print(newList[4]) #Shouldn't work. Out of Range. 





#We can find the length of a list, or the number of elements in a list.

listLength = len(newList)
print(listLength) #Should be 4






#The following will print out all the elements in the list separately on new lines.
index = 0
while index < listLength:
  print(newList[index])
  index += 1











  


#Length function also works with STRINGS. It can find a string variable's length.
courseName = "CS177 - Python"

stringLength = len(courseName)
print(stringLength)
#Should be 14

#We can access individual characters of a string as well.
#For example:
print(courseName[0])


#We can build a while loop to build these strings one char at a time:
charIndex = 0

while charIndex < len(courseName):
  print(courseName[charIndex])
  charIndex += 1











#For Loops
# The name of the variable after "for" can be anything. I named it name, but it could be anything. 

for name in newList:

  print(name)






#We can again use it on strings. Char by char at a time. Letter could have been named anything. As long as the print uses the same variable name. 
for letter in courseName:

  print(letter)





#Nested For Loop
for name in newList:

  for letter in name:

    print(letter)






#Prime number check

def isPrime(n):

  if n == 1:
    return False

  # i takes in values from 2 to n-1
  for i in range(2, n):

    if n % i == 0:
      return False

  return True


print(isPrime(2)) #Should print true
print(isPrime(14)) #Should print false

    


for number in range(1, 101): #1 to 100

  if isPrime(number):
    print(number)





























