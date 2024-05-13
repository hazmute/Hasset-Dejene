def search_number(arr, num):
    count = arr.count(num)
    return count

arr = []
n = int(input("Enter the length of the array: "))
for i in range(n):
    num = int(input("Enter number {}: ".format(i+1)))
    arr.append(num)

search_num = int(input("Enter a number to be searched: "))
count = search_number(arr, search_num)

if count > 0:
    print("{} appears {} time(s) in the array.".format(search_num, count))
else:
    print("{} does not appear in the array.".format(search_num))
	



