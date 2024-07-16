#Assignment 2
'''
Write a Python function called max_num()to find the maximum of three numbers.
Write a Python function called mult_list() to multiply all the numbers in a list.
Write a Python function called rev_string() to reverse a string.
Write a Python function called num_within() to check whether a number falls in a given range.
    The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
    Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
    The function accepts the number n, the number of rows to print
    Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.'''

#silly, brute force way to find max of three numbers
def max_num_brute_force(num1=2, num2=3, num3=4):
    if num1>num2:
        if num1>num3:
            return num1
        else: return num3
    elif num2>num3:
        return num2
    else: return num3
#elegant and simple way to find max number
def max_num(num1=2, num2=3, num3=4):
    numList = [num1,num2, num3]
    return max(numList)
#multiply all numbers in a list
def mult_list(list=[1,2,3,4]):
    result = 1
    for i in range(len(list)):
        result*=list[i]
#reverse a string
def rev_string(string="test"):
    reversed = ''
    for i in range(len(string)):
        alt=i+1
        reversed = reversed + string[-alt]
    print(reversed)
#check if number is within range (inclusive)
def num_within(num1, num2, num3):
    if num2 <= num1 <= num3:
        return True
    else: return False
#Sweet pascal triangle function...using RECURSION!!
def pascal(rows):
  if rows == 0:
    return []  # Base case: Empty list for 0 rows
  elif rows == 1:
    print(1)  # Base case: Print the single 1 for 1 row
    return [[1]]

  # Get the previous row using recursion
  previous_row = pascal(rows - 1)
  current_row = [1]  # Start new row with 1

  # Generate the remaining elements of the list row based on previous row
  for i in range(1, rows - 1):
    #using the pascal math, add the "inside" values
    current_row.append(previous_row[i - 1] + previous_row[i])
  current_row.append(1)  # End new row with a 1

  # Print the current row by iterating through the list of values
  for num in current_row:
    print(f"{num}", end=" ") #the end=" " keeps new values on the same line to make it pretty
  print('')  # Move to next line after each row

  return current_row

pascal(12)