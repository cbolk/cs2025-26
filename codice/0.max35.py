NVAL = 35

# get the first value 
# set the maximum to it
# number of read values = 1
# while number of read values is smaller than the number of data 
#   get a number
#	if number is greater than the actual maximum
#		update the maximum
#	increase by one the number of read values 
#   (go back and check whether we are done)
#

val = int(input())
valmax = val
count = 1

while count < NVAL:
	val = int(input())
	if val > valmax:
		valmax = val
	count += 1

print(valmax)







