def sum_of_multiples(n):
    multi =[]
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            multi.append(i)
    return sum(multi)

# Reading the number of test cases
t = int(input())

# Looping through all the test cases
for i in range(t):
    n = int(input())
    # Computing and printing the sum of multiples for each test case
    print(sum_of_multiples(n))
