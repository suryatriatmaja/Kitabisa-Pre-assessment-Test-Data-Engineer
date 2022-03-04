#=========================================== task 1 ====================================================#
# Find first N prime number, and print the result
# Input: 4
# Output : 2, 3, 5, 7

input = 4
# bilangan prima harus lebih besar dari 1
x = 1
y = 0
num_x = 0
list_data_final = []
while y <= x:
    x=x+1
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                # print(x, "bukan bilangan prima")
                # print(i, "kali", x//i, "=", x)
                break
        else:
            # print(x,"adalah bilangan prima")
            list_data_final.append(x)
            num_x = num_x+1
    if num_x == input:
        print(str(list_data_final).replace("[","").replace("]",""))
        break

#=========================================== task 2 ====================================================#

# Sort and combine these 2 lists and print the result
# Input 1: 4,3,6,5,1,2
# Input 2: F,C,D,B,A
# Output : [1:A],[2:B],[3:C],[4:D],[5:F],[6:NULL]

input_1 = '4,3,6,5,1,2'
input_1 = input_1.split(',')
list_input_1 = []
for x in input_1:
    list_input_1.append(int(x))
list_input_1.sort()

input_2 = 'F,C,D,B,A'
input_2 = input_2.split(',')
list_input_2 = []
for x in input_2:
    list_input_2.append(str(x))
list_input_2.sort()

x = 0
while x < len(list_input_1):
    try:
        print('['+str(list_input_1[x])+':'+str(list_input_2[x])+'],', end="")
    except:
        print('['+str(list_input_1[x])+':NULL]')
    x = x + 1


