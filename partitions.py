# A utility function to print an
# array p[] of size 'n'
def printArray(p, n):
    for i in range(0, n):
        print(p[i], end = " ")
    print()
 
def printAllUniqueParts(n):
    p = [0] * n     # An array to store a partition
    k = 0         # Index of last element in a partition
    p[k] = n     # Initialize first partition
                 # as number itself
 
    # This loop first prints current partition,
    # then generates next partition.The loop
    # stops when the current partition has all 1s
    while True:
         
            # print current partition
            printArray(p, k + 1)
 
            # Generate next partition
 
            # Find the rightmost non-one value in p[].
            # Also, update the rem_val so that we know
            # how much value can be accommodated
            rem_val = 0
            while k >= 0 and p[k] == 1:
                rem_val += p[k]
                k -= 1
 
            # if k < 0, all the values are 1 so
            # there are no more partitions
            if k < 0:
                print()
                return
 
            # Decrease the p[k] found above
            # and adjust the rem_val
            p[k] -= 1
            rem_val += 1
 
            # If rem_val is more, then the sorted
            # order is violated. Divide rem_val in
            # different values of size p[k] and copy
            # these values at different positions after p[k]
            while rem_val > p[k]:
                p[k + 1] = p[k]
                rem_val = rem_val - p[k]
                k += 1
 
            # Copy rem_val to next position
            # and increment position
            p[k + 1] = rem_val
            k += 1
 
# Driver Code
print('All Unique Partitions of 3')
printAllUniqueParts(3)
 
print('All Unique Partitions of 4')
printAllUniqueParts(4)
 
print('All Unique Partitions of 5')
printAllUniqueParts(5)

print('All Unique Partitions of 6')
printAllUniqueParts(6)

print('All Unique Partitions of 7')
printAllUniqueParts(7)

print('All Unique Partitions of 8')
printAllUniqueParts(8)

print('All Unique Partitions of 9')
printAllUniqueParts(9)

print('All Unique Partitions of 10')
printAllUniqueParts(10)

print('All Unique Partitions of 11')
printAllUniqueParts(11)

print('All Unique Partitions of 12')
printAllUniqueParts(12)
