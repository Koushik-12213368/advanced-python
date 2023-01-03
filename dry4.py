#def factorial(n):
 #   fact=1

  #  for i in range(1, n+1):
   #     fact=fact*i
    #return fact     

#n=int(input("Please enter any number to find factorial: "))

#result=factorial(n)

#print(result)

#def fact(n):             #2nd type (recurtion)
    #if n==0:
    #    return 1
    #else:
     #   return n*fact(n-1)
#n=int(input("enter any number:"))
#print(fact(n)

#def printnumber(num):
 #   if (num>=1):
  #      print(num,end=" ")
   #     printnumber(num+1)
#num=int(input("enter a number:"))
#print("the first n numbers are:")
#printnumber(num)

#def rev(n):
    #if n==1:
   #     print(1)
  #  else:
  #      print(n)
 #       rev(n-1)
#n=int(input("enter any number:"))
#rev(n)

#number=int(input("enter integer value"))   #the reverse question thst csme in daily test
#reverse_number=0
#while(number>0):
 #   remainder=number%10
  #  reverse_number=(reverse_number*10)+remainder
   # number=number//10
#print("the reverse number is :{}".format(reverse_number))

def display(name,age):#positional arg
    print("name is=",name,"age is=",age)
    display('j',25)
    display(40,'s')

#display("john")
display(age=34,name="abc") #keyword arg


#Default Argument
def display(a,b=10,c=20):
    print("a=",a,"b=",b,"c=",c)

display(15)
display(50,c=30)
display(c=80,a=25,b=35)

#Arbitrary Arguments, *args
def my_function(*n):
for i in n:
print(i)

my_function(1,3,5)
my_function(-2.3,3.4,'a',2,4)
    
        
