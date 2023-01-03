'''srt1="hello sir"
print("initial string:")
print(str1)
del str1
print("\ndeleting entire string")
print(str1)'''

'''a=int(input())
print(str(a)[2])
print(str(a)[1])
print(str(a)[0])
print(a//2)

a,b=int(input()),int(input())
a=a+b
op="a+=b: a= {} b= {}"
print(op.format(a,b))'''

'''def Convert(string):
	li = list(string.split(" "))
	return li

str1=input("enter string")
print(Convert(str1))'''

'''l=[10,abc,3.5,61]
a=int(input())
if a not in l:
    if a>=0 and a<len(l):
        print('''

'''list1=[10,20,40,50]
list2=["paabity","rabbity","scabbers","megha"]
mydict=dict(zip(list1,list2))
print(mydict)
a=int(input("enter the key you want to change:"))
b=input("enter the value you wanna change:")
mydict[a]=b
print(mydict)
print(sorted(mydict.items()))
mydict.popitem()
mydict.popitem()
print(mydict)'''

'''dict1={i:i+10 for i in range(1,11)}
print(dict1)'''

'''class sum:
    def __int__(self,x,y):
        self.a=x
        self.b=y
    def sum():
        print(self.a+self.b)
a=int(input())
b=int(input())
sum()'''

'''print("____hierarchial inheritance_____")
class superclass:
    x=int(input())
class subclass1(superclass):
    pass
class subclass2(superclass):
    pass
class subclass3(superclass):
    pass
a=subclass1()
b=subclass2()
c=subclass3()
print(a.x,b.x,c.x)


print("____multiple inheritance___")
class claculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def multiplication(self,a,b):
        return a*b;
class derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b;
d=derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))'''

f=open("radheradhe.txt","a")
a=input("enter value")
f.append("\n",a)
print(f)
