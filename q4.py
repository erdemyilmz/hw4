def is_harshad(n):
    digittotal = 0
    for element in str(n):
        digittotal += int(element)
    if n%digittotal == 0:
        return True   
    return False

def is_double_harshad(n):
    digittotal = 0
    for element in str(n):
        digittotal += int(element)
    reserve_n = n
    if is_harshad(n):
        reserve_n = reserve_n // digittotal
        seconddigittotal = 0
        for element in str(reserve_n):
            seconddigittotal += int(element)
        if reserve_n % seconddigittotal == 0:
            return True       
    return False

def find_double_harshad(start, end):
    new_start = start if start<end else end
    new_end = end if start<end else start
    n = new_start
    mylist = []
    while n<=new_end:
        if is_double_harshad(n):
            mylist.append(n)
        n+=1
    return mylist

while True:
    val1 = input("Enter your number: ")
    if val1.isdigit() and int(val1) > 0:
        n1 = int(val1)
        break
    print("Invalid input")

while True:
    val2 = input("Enter your number: ")
    if val2.isdigit() and int(val2) > 0:
        n2 = int(val2)
        break
    print("Invalid input")
    
print(find_double_harshad(n1, n2))
    



































    