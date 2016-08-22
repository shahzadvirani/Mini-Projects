'''
Program that uses a list to create a new
list that only contains even numbers from
the original list (using list comprehension).
'''

a = [None]*10  #list initialization

for x in range(0,10):  #loop to populate the list with values
    a[x]=int(raw_input("Enter element for position " + str(x) + " in the list: "))

new_list=[element for element in a if (element%2==0)]  #list comprehension

print ("\nThe list of even numbers is: ")
print new_list