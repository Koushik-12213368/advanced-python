'''str1=input("enter the value:")
str2=input("enter the value:")
if id(str1)==id(str2):
    print("the strings have same id")
else:
    print("the strings don't have same id") 



a,b=input("enter a value:"),input("enter a value:")
c,d=id(a),id(b)
print(c,d)'''

'''str=input("Enter a string: ")
upper=0
lower=0
digit=0

for i in str:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper=upper+1
    elif(i.isdigit()):
        digit=digit+1
    
        
        

print("The lower case letters:",lower)
print("The upper case letters:",upper)
print("The digit in the string:",digit)'''

'''s="lovely professional university"
print(s[::-1])
print(s[-2:-7])
print(s[-7:-2])'''

'''x=input("enter a string")
y=input("enter a string")
print("the id of x is:",id(x))
print("the id of y is :",id(y))
if x>y:
    print("x is greater than y")
elif x<y:
    print("x is smaller than y")
else:
    print("x is equal to y")'''

'''name=input("enter name:")
surname=input("enter surname:")
sno=input("enter sno:")
data="the name of candidate is {0} surname is {1} and sno is {2}"
print(data.format(name,surname,sno))

name=input("enter name:")
surname=input("enter surname:")
sno=input("enter sno:")
data="the name of candidate is {} and surname is {} and sno is {}"
print(data.format(name,surname,sno))'''



'''s="auditor69"
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())'''

'''s="   Auditor"
print(s.isupper())
print(s.islower())
print(s.isspace())'''

'''a,b,c,d,e=1,2,3,4,5
print(a,b,c,d,e)
print(a,b,c,d,e,sep="#")'''

'''s="A paragraph (from Ancient Greek παράγραφος (parágraphos) 'to write beside') is a self-contained unit of discourse in writing dealing with a particular point or idea. Though not required by the orthographic conventions of any language with a writing system, paragraphs are a conventional means of organizing extended segments of prose."
print(s.endswith("prose"))
print(s.startswith("A"))
print(s.find("Greek"))
print(s.find("auditor"))
print(s.rfind("o"))
print(s.count("A"))
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.replace("Greek","Sanskrit"))'''



'''s="hello"          #1
a=s[0]*2
b=s[1]*2
c=s[2]*2
d=s[3]*2
e=s[4]*2
op="{}{}{}{}{}"
print(op.format(a,b,c,d,e))'''


'''s1=input("enter a string")            #2
s2=input("enter a string")
if len(s1)<len(s2):
    op="{}{}{}"
    print(op.format(s1,s2,s1))
else:
    ip="{}{}{}"
    print(ip.format(s2,s1,s2))'''

'''s=input()                                   #3
if s.startswith("python"):
    print("True")
elif s.endswith("programming"):
    print("True")
else:
    print("False")'''


'''s=input()                        #4
a=s[0:6]*5
print(a)'''
#str=input("str:")
#result=""
#for i in str:
 #   result=result+2*i
#print("result:",result)


def Punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    print(string)
 
string = input("enter a string")
Punctuation(string)





