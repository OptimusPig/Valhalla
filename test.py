#!/usr/bin/python
#  -*-coding: UTF-8-*-
import time
import support
from Phone import Pots

money = 2000
flag =False
name="luren"
if name =="python":
	flag =True
	print"welcome boss"
else:
	print name

num =5
if num ==3:
	print "boss"
elif num ==2:
	print "user"
elif num ==1:
	print "worker"
elif num<0:
	print "error"
else:
	print "roadman"
count=0
while (count<9):
	print "The count is:",count
	count+=1

for letter in "Python":
	print "the letter is:",letter

fruits =["banana","apple","mango"]
for index in range(len(fruits)):
	print "当前水果:",fruits[index]

print "a",3.43e93,19+2.3j,"xyz"
localtime = time.asctime(time.localtime(time.time()))
print localtime
total=1
def sum(arg1,arg2):
	total =arg1+arg2
	print total
	return total 
total=sum(1,2)
print total
support.print_func("Zara")
support.print_func2("Zara")

def printinfo(arg1,*vartuple):
	print "output:"
	print arg1
	for var in vartuple:
		print var
	return;
printinfo(10)
printinfo(70,60,50)
def AddMoney():

	global money
	money = money +1
print money
AddMoney()
print money
Pots()

