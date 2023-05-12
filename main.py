#factorial function call by itself
"""def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result=fact(5)
print(result)"""
#lambda function (also known as anonymous function)
#it works same as function but it is anonymous it can be understood by using them in filter and map functions
"""f=lambda a:a*a
result=f(5)
print(result)"""

#use of lambda function,filter,map,reduce functions
#filter function is going to filter the list according to the condition of function
#map function is going to map the condion in funtion to all the numbers in the list
#reduce is going to reduce the list according to the given function and give the answer
"""from functools import reduce 
nums=[2,3,5,6,7]
evens=list(filter(lambda a:a%2==0,nums))
doubles=list(map(lambda a:a*a,nums))
sum=reduce(lambda a,b:a+b,nums)
print(nums)
print(evens)
print(doubles)
print(sum)"""
#creating  a module and calling the functions from that module using import function
"""import calc
a=calc.add(3,5)
print(a)"""

#usage of class and its methods and calling them and  __init__ (constructor)
"""class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("this is init constructor")
    def config(self):
        print("this is called from class",self.cpu,self.ram)

com1=computer("intel",8)
com2=computer("ryzen",16)#calling anotehr object from one object
com1.config()#way calling the function in the class using object
com2.config()"""
"""class student:
    def __init__(self,m1,m2,m3):
        
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1=student(2,4,6)
print(s1.avg())"""

#inheritance multilevel
"""
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
a1=A()
a1.feature1()
class B(A):          #it is way of inheriting A class to B class
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
b1=B(A)
b1.feature3()
b1.feature1()

class C(B):            #A to B to C multilevel  ,A and B to C multiple
    def feature5(self):
        print("feature 3 is working")
c1 = C()
c1.feature3()
"""
#inheritance multiple
"""
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
a1=A()
a1.feature1()
class B():   
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
b1=B()
b1.feature3()

class C(A,B):              #,A and B to C multiple inheritance
    def feature5(self):
        print("feature 5 is working")
c1 = C()
c1.feature3()
c1.feature1()
c1.feature5()"""

#inheritance in constructor multilevel
""""
class A:
    def __init__(self):
        print("class A init")
    def feature1(self):
        print("feature 1 is working")

class B(A):
    def __init__(self):
        super().__init__() #way of calling constructor of the super clas
        print("class B init")
    def feature2(self):
        print("feature 3 is working")
b1=B()
b1.feature2()"""

#constructor inheritance multiple
"""class A:
    def __init__(self):
        print("class A init")
    def feature1(self):
        print("feature 1 is working")

class B():
    def __init__(self):
        print("class B init")
    def feature2(self):
        print("feature 2 is working")

class C(A,B):
    def __init__(self):
        super().__init__()#according to method resolutin order it will
                            # start from left so constructor of A will be called
        print("class c init")
    def feature3(self):
        print("feature 3 is working")

c1=C()
"""
#methode overloading
#in python we don't have method over loading concept
#but we can use the default parameters to over come method overloadimg
#in one class if we have two methods of same name it is clled method overloading
""""
class A:
    def sum(self,a,b,c=0):#like this we can implement method overloading
        return a+b+c

a1=A()
print(a1.sum(2,3))"""

#multithreading
"""
from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=hello()
t2=hi()
t1.start()
sleep(0.5)
t2.start()

"""

#file handling in python
"""
f=open('mydata','r')#used for open ad read
f1=open('abc','w')#used for open and write
f=open('hello','a')#used for update data(append)

for data in f:
    f1.write(data)"""
















