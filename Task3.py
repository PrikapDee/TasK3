#PAT3
#ques 1 create 2 list which is having all even number and one is having all odd numbers
list1=[10,501,22,100,999,87,351]
#new list to store even numbers
list2=[] 
#new list to store odd numbers
list3=[] 
for i in list1:
    if i%2==0:
        list2.append(i)

    else:
        list3.append(i)


print("list of even no.:", list2)
print("list of odd no:", list3)


# Pat3 ques no2 to count primer number and create a new list of prime numbers
list=[10,501,22,37,100,999,87,351]
#new list which will contain prime number
list_prime=[]
for i in list:
  list_prime.append(i)
  for j in range(2,i):
    
     if i%j==0:
       list_prime.remove(i)
       break
print("list of Prime number:",list_prime ,"\ncount of prime number in list:",len(list_prime))

#Pat 3 ques3 fine happy number from list given
#function to calculate square root of digits
def numSquareSum(n): 
    square_sum = 0
    while n:
        digit = n % 10
        square_sum += digit * digit
        n //= 10
    return square_sum
#function to check happy number is or not  
def isHappyNumber(num):                                                                                                                          
    seen_numbers = set()
    while True:
        num = numSquareSum(num)
        if num == 1:
            return True
        if num in seen_numbers:
            return False
        seen_numbers.add(num)


list1=[10,501,22,100,999,87,351] 
hapynumberlist=[]
for i in list1:
    if isHappyNumber(i):
       hapynumberlist.append(i)
print("list of happy number:",hapynumberlist)
     

#pat3 ques 4 write  a program to fin sum of the first and last digit of an integer
#take a input  from user
int_n=input("enter any integer") 
#convert it to string
number=str(int_n)  
#first index value of string and convert it to integer
first_digit=int(number[1]) 
# last index value of string and cnvert it to integer 
last_digit=int(number[-1]) 
#addition
sum_of_digit=first_digit + last_digit 
print("sum of first and last digit:",sum_of_digit)

#pat 3 ques 5 find no of ways to ditribute managoes to each student in gyi class

def binomial_coefficient(m, n):
    res = 1
 
    if n > m - n:
        n = m - n
 
    for i in range(0, n):
        res *= (m - i)
        res /= (i + 1) 
 
    return res
 
# helper function for generating no of ways
# to distribute m mangoes amongst n people
def calculate_ways(n, m):
 
    # not enough mangoes to be distributed    
    if n<m:
        return 0
 
    # ways  -> (m + n-1)C(m-1)
    ways = binomial_coefficient(m + n-1, m-1)
    return int(ways)
 




#Pat3 ques 6 write a program to find duplicates in 3 list
#List 1
L1=[3,5,6,9,1] 
#list 2
L2=[9,5,2] 
# List 3
L3=[5,2,4] 
#new blank list
L5=[] 
#contantate 3 list to make one list
L5= L1 + L2 + L3 
print(L5)
#to show duplicate list
duplicateList=[]

for i in L5:
    # condition to find duplicates
    if L5.count(i)>1 and i not in duplicateList: 
        duplicateList.append(i)


print("duplicate list :",duplicateList)




#pat3 ques7 python program to find the first non-repeating elements in a given list of integers
list1=[2,2,4,5,7,8,4,7,0]
#convert list into set
set2=set(list1)
#then convert set to list
list2=list(set2) 
#new list will be without non repeating integers.
list2  

# pat3 ques 8 write a python program to find the minium element rated in sorted list
List1=[24,67,89,23,45]
List1.sort() #apply sort function on list1
print("minmium rated element:", List1[0])


#Pat3 ques 9 :writea python program to find the triplets in list whose sum equal to 59

list1=[10,20,30,9] 
#find the length of list
n=len(list1) 
#blank list for result
list_trplts=[] 


for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if list1[i]+list1[j]+list1[k]==59: 
                list_trplts.append(list1[i]) 
                list_trplts.append(list1[j])
                list_trplts.append(list1[k])
print("sum of triplets equal to 59:",list_trplts)


#Pat3 ques 10 sublist whose sum should be zero
list=[4,2,-3,1,6]
#calculate length of List
n=len(list)
# new list to store result 
sublist=[]  
for i in range(n):
    for j in range(i+1,n):
        for K in range(j+1,n):
            if (list[i]+list[j]+list[K]==0): 
                sublist.append(list[i])
                sublist.append(list[j])
                sublist.append(list[k])
print("sum of sublist whose sume equal to zero:",sublist)
       

