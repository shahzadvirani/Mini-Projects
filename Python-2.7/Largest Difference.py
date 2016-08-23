'''
Program that will take a list of integers
and output the difference between the
smallest and the largest element
'''

def big_diff(listx):  #function definition
    smallest=9999999999
    largest=0

    for i in listx:
        if (i<smallest):
            smallest=i
        elif (i>largest):
            largest=i

    return (largest-smallest)

integer_list=[None]*5  #list initialization

for x in range(0,5):  #list population
    integer_list[x]=int(raw_input("Enter value for position " + str(x) +": "))

print ("\nThe largest difference is:")
print big_diff(integer_list)

