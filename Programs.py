import keyword

print("Well come to Python Program")

print(keyword.kwlist)

a=10
b=20
c=5
x= a if a<b else b
print(x)

y=a if a<b and a<c else b if b<c else c
print(y)

#while loop print 1 to 10
x=1
while x<=10:
    print(x)
    x=x+1

# sum of numbers
'''n=eval(input("Enter the number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
    print("The sum of number",i," is",sum)'''

'''name=""
while name!='Basavanagouda':
    name = input("Enter the name")
print("Thanks for the Confirmation")'''

# transfers statement
# print odd number between 0 to 9 using continue statement
for i in range(10):
    if i%2==0:
        continue
    print(i)

#reading multiple value in single line
'''a,b=[int(x) for x in input("Enter 2 numbers").split(',')]
print(a+b)'''

'''a,b,c=[float(x) for x in input("Enter 3 numbers").split()]
print(a+b+c)'''

#write a function to check given number is even or odd.
'''def odd_even(n):
    if n%2==0:
        print('Even number')
    else:
        print('odd Number')

odd_even(100)'''

# Write a function to find factorial of a number
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result

print(fact(10))

#function after varibale length argument with key word
def f1(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)

f1("a","b",n1=100)

#**kwarguments
def display(**kwargs):
    for key,value in kwargs.items():
        #print(k,"=",v)
        print("%s == %s"%(key,value))

display(n1=100,n2=400,n3=500, n4="basava")

#recursive Function
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(10))

def countdown(num):
    while num>0:
        yield num
        num=num-1
    return num

values=countdown(4)
for value in values:
    print(value)


words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)

num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[ i for i in num1 if i not in num2]
print(num3)

num3=[ i for i in num1 if i  in num2]
print(num3)

words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)

#Write a program to display unique vowels present in the given word?
vovels =['a','e','i','o','u']
word="learning"
print(words)
found=[]

for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)

print(found)

#Write a program to take a tuple of numbers from the keyboard and print its sum and average?
'''t=eval(input("Enter the numbers"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
print("The sum of value is",sum)
print("The Average value is ", sum/l)'''

#write a program to eliminate duplicates present in the list?
#1st approach
'''l=eval(input("Enter the list"))
s=set(l)
print(s)'''

#2nd approch
l=[10,20,30,40,50,40,50]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

#Write a program to print different vowels present in the given word?
'''word=input("Enter the words")
s=set(word)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The voles present in the given", word,"are ",d)'''

#Write a program to enter name and percentage marks in a dictionary and display information on the screen
'''rec={}
n=int(input("Enter the number of students"))
i=1
while i<=n:
    name=input("Enter the student name")
    marks=input("Enter the marks in %")
    rec[name]=marks
    i=i+1
for x in rec:
    print(x,rec[x])'''

#Write a program to take dictionary from the keyboard and print the sum of values?
d={100:100,200:200,300:300}
s=sum(d.values())
print(s)

#Write a program to find number of occurrences of each letter present in the given string?
'''words=input("Enter the words")
d={}
for x in words:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occured in",v,"these many times")'''

#Write a program to find number of occurrences of each vowel present in the given string?
'''words=input("Enter the words")
vovels={'a','e','i','o','u'}
d={}
for x in words:
    if x in vovels:
        d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occured in",v,"these many times")'''

#dectionary comprehension
d={x:2*x for x in range(1,10)}
print(d)

#Write a program to accept some string from the keyboard and display its characters by
# index wise(both positive and nEgative index)
'''s=input("Enter the string")
i=0
for x in s:
    print("the charector present in +ve index is",i,"and -ve index is",i-len(s),"is",x)
    i=i+1'''

#write a program to access the string in both forward and backward direction
'''s='Basavanagouda'
n=len(s)
i=0
#forward
while i<n:
    print(s[i],end='')
    i=i+1
#backword
i=-1
print(".............................")
while i>=-n:
    print(s[i],end='')
    i=i-1

print("..............")
for x in s[::-1]:
    print(x)
'''
#write a program to reverse a string
'''s='Basavanagouda'
print(s[::-1])
print("".join(reversed(s)))
i=-1
n=len(s)
while i>=-n:
    print(s[i],end='')
    i=i-1
'''

#Program to reverse order of words
'''s="learning python is very easy"
l=s.split()
print(l)
l1=[]
i=len(l)
print(i)
i=len(l)-1
print(i)
while i>=0:
    l1.append(l[i])
    i=i-1
print(l1)
output="".join(l1)
print(output)'''


#Q3. Program to reverse internal content of each word.
'''s="Learning python is very easy"
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
print(l1)
op="".join(l1)
print(op)'''

#Write a program to print characters at odd position and even position for the given String?
s="Basavanagouda"
#1st way
'''print("charector at even position",s[::2])
print("charector at odd position",s[1::2])
'''
#2nd way
'''i=0
while i<len(s):
    print(s[i],end="")
    i=i+2
print("...........")

i=1
while i<len(s):
    print(s[i],end="")
    i=i+2'''

#write a program to merge 2 strings
'''s1="basavana"
s2='gouda'
output=""
i,j=0,0

while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)'''

#Q6. Write a program to sort the characters of the string and first alphabet symbols followed by numeric values
#input: B4A1D3 Output: ABD134
'''s="B4A1D3"
s1=s2=output=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)'''

#Q7. Write a program for the following requirement
#input: a4b3c2 output: aaaabbbcc
'''s="a4b3c2"
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)'''

#Q8. Write a program to perform the following activity
#input: a4k3b2 output:aeknbd

'''s="a4k3b2"
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)'''

#Q9. Write a program to remove duplicate characters from the given input string?
#input: ABCDABBCDABBBCCCDDEEEF output: ABCDEF
'''input="ABCDABBCDABBBCCCDDEEEF"
l=[]
for x in input:
    if x not in l:
        l.append(x)
print(l)
output="".join(l)
print(output)'''

#Q10. Write a program to find the number of occurrences of each character present in the given String?
#input: ABCABCABBCDE output: A-3,B-4,C-3,D-1,E-1
'''input="ABCABCABBCDE"
d={}
for x in input:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1

print(d)
for k,v in d.items():
    print(k,"==",v)'''


#check given number ifs +ve ,-ve or zero

'''x=10
if x>0:
    print("positive")
elif x==0:
    print("zero")
else:
    print("negative")'''

#checkgiven number is even or odd
'''x= int(input("Enter the numbers"))

if x%2==0:
    print("{0} is even number".format(x))
else:
    print("{0} is not a even number".format(x))'''

#write a program to print leap year
'''x=1900

if x%4==0:
    if x%100==0:
        if x%400==0:
            print(x,"is a leap year")
        else:
            print(x,' is not a leap years')
    else:
        print(x, ' is not a leap years')
else:
    print(x, 'is not a leap years')'''

#write a program to find the largest number in the given program
'''i=100
j=200
c=300

#1 way using if condition
if i>j and i>c:
    print(i, "is greater than j and c")
elif j>c:
    print(j,"is greater than i and c")
else:
    print(c,"is greater than i and j")

#another way usinf for loop.

x=i if i>j and i>c else j if j>c else c
print(x)'''

#write a program to check given number is prime or not
'''num=5
if x>1:
    for i in range(2,num):
        if num%i== 0:
            print(num,"is not a prime a number")
            print(i, "times",num//i,"is ",num)
            break
    else:
        print("is a prime number")
'''
#print all prime numbers in a interval
'''x=100
y=200
for x1 in range(x,y+1):
    if x1>1:
        for i in range(2,x1):
            if x1%i==0:
                break
        else:
            print(x1)'''
#write a program to factorial of a number
num=4
fact1=1
if num==0:
    print("factorial is 1")
elif num<0:
    print("sorry not a factorial number")
else:
    for i in range(1,num+1):
        fact1=fact1*i
    print(fact1)


#write a program to display multiplication table
num=12

for i in range(1,11 ):
    print(num ,"x",i,"=",num*1)

#write a program to print fibonacci series
'''n=int(input("enter the number"))
n1,n2=0,1
count=0
if n<=0:
    print('please enter positive number')
elif n==1:
    print("the fibonacci series of n is",n1)
else:
    print("fibonaci sequence")
    while count<n:
        print(n1)
        nth=n1+n2
        n1 = n2
        n2=nth
        count=count+1
'''

#write a program to print amstrong number
'''num=153

sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num==sum:
    print("yes")
else:
    print("no")'''

#calender mode

'''import calendar
year=int(input("Enter the year"))
month=int(input("enter the month"))

print(calendar.month(year,month))'''


#cube of a number
number=3
cub=number*number*number
cub1=number**3
print(cub, cub1)

#write a program to print electricity bill

'''units=int(input("Enter the units which you consumed"))
if units<50:
    amount=units*2.26
    supercharge=25
elif (units<=100):
    amount=130+(units-50)*3.25
    supercharge=35
elif (units<=200):
    amount=130+162.5+(units-100)*5.35
    supercharge=45
else:
    amount=130+162.5+526+(units-200)*8.25
    supercharge=75

total=amount+supercharge
print(total)'''

#write a program to print simple intrest
'''import math
P=float(input('Enter the amount'))
T=float(input("Entr the time frame"))
r=float(input("Enter the rate of intrest"))

SI=P*T*r/100

print(SI)
'''

#compound interest
import math
P=float(input('Enter the amount'))
T=float(input("Entr the time frame"))
r=float(input("Enter the rate of intrest"))

CI_future=P*math.pow((1+r/100),T)
CI=CI_future-P

print(CI)


