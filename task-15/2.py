# read the number of test cases
num_test_cases = int(input())

# loop through each test case
for i in range(num_test_cases):
  # read the value of n for each test case
  n = int(input())

  # initialize the fibonacci sequence with the first two terms
  fib = [1, 2]

  # initialize the sum to 0
  sum = 0

  # loop until the next term in the fibonacci sequence exceeds n
  while fib[-1] + fib[-2] <= n:
    # add the next term in the fibonacci sequence
    fib.append(fib[-1] + fib[-2])

  # loop through the fibonacci sequence and add the even-valued terms to the sum
  for i in fib:
    if i % 2 == 0:
      sum += i

  print(sum) # print the sum

        
        
    
