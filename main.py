# This is a sample Python script.
import math as m

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# VARIABLES///IF OR ELIF

# x = int(input("enter num"))
# z = m.pow(x,3)
# print(z)

# x = 7
#
# r = x % 2
#
# if r==0:
#     print("even")
# else:
#     print("odd")
#
# x = int(input("enter first num"))
# y = int(input("enter second num"))
# z = int(input("enter third num"))
#
# r = max(x,y,z)
#
# print(r)


# LOOP

# for i in range(1,500):
#     if m.pow(i,2) < 500:
#         print()


# for i in range(1,5):
#     for j in range(i,5):
#         print(j, end="")
#     print()

# str1="ABCD"
# str2="PQR"
# i=0
# while i < len(str1) :
#  for j in range(0,i+1):
#   print(str1[j],end=" ")
#  for k in range(i,len(str2)):
#   print(str2[k],end=" ")
#  i+=1
#  print()

from array import *
#
# vals = array("i",[2,3,4,5,6])
#
# for i in range(len(vals)):
#     if i == 2:
#         del vals[i]
#
# print(vals)


# nums = array("i",[2,3,4,5,6])
#
# for i in range (5):
#     print(nums[i])
#


# arr=array('i',[1,2,3,4,5])
# k=-len(arr)-1
# for i in range(-1,-6,-1):
#     print(arr[i])

# arr = array('i', [0, 1, 2, 3, 4])
#
# floor = m.floor(len(arr) / 2)
# l = len(arr)
#
# for i in range(floor):
#     x = arr[i]
#     arr[i] = arr[l-i-1]
#     arr[l-i-1] = x
#
# print(arr)


from numpy import *

# arr1 = array([85,8,76,4,10])
#
# arr2 =array([6,5,9,1,3])
#
#
# for i in range(len(arr1)):
#     k = arr1[i]+arr2[i]
#     print(k)
#
# hN = 0
# for i in range(len(arr1)):
#     if arr1[i] >= hN:
#         hN=arr1[i]
#
# print(hN)

# arr1=array([
# [1,2,3],
# [4,5,6]])
# arr2=arr1.reshape(3,2)
# arr3=ones((2,2))
# for i in range(2):
#     for j in range(2):
#         c=0
#         for k in range(3):
#             f=arr1[i][k]*arr2[k][j]
#             c=c+f
#         arr3[i][j]=c
# print(arr3)

# FUNCTION
# def myname():
#     names = []
#     for i in range(5):
#         k = input("Enter name")
#         names.append(k)
#     return names
#
# guestNames = myname()
#
#
# def nameCount(guestNames):
#     for i in guestNames:
#         if len(i)>5:
#             print(i)
#             print(len(i))
#
#
# nameCount(guestNames)
#


# FIBONACCI

# def fib(n):
#     a = 0
#     b = 1
#     if n<=0:
#         print("Invalid number")
#     elif n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#             if c<100:
#                 print(c)


#
# fib(100)
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# def main():
#   emoji=input("write anything?")
#   if ":(" in emoji:
#     emoji=emoji.replace(":(","🙂")
#     emote(emoji)
#   elif ":)" in emoji:
#     emoji=emoji.replace(":)","🙁")
#     emote(emoji)
#
#
#
#
# def emote(emoji):
#   print(emoji)
#
#
# main()

# def main():
#   dollars = dollars_to_float(input("How much was the meal? "))
#   percent = percent_to_float(input("What percentage would you like to tip? "))
#   tip = dollars * percent
#   print(f"Leave ${tip:.2f}")
#
#
# def dollars_to_float(d):
#   d = d.replace("$","")
#   return float(d)
#
# def percent_to_float(p):
#   z=p.replace("%","")
#   z = float(z)
#   return z/100
#
# main()


# greetings =input("greet?").lower().split()

# if (greetings[0][0]) == "h" and (greetings[0]) != "hello":
#   print("$20")
# elif (greetings[0]) == "hello":
#   print("$0")
# else:
#   print("$100")
#
# x = input("firstnumber? ")
# z = int(x[0])
# y = int(x[4])
#
# if x[2]=="+":
#     print(float(z + y))
# elif x[2]=="-":
#     print(float(z - y))
# elif x[2]=="*":
#     print(float(z * y))
# elif x[2]=="/":
#     print(round(z / y,1))

#
# def main():
#     time = input("time? ")
#     convert(time)
#


# def convert(time):
#     hours, minutes = time.split(":")
#     hours = float(hours)
#     minutes = float(minutes)
#     new_minutes = float(minutes/60)
#     new_time = hours + new_minutes
#
#     if new_time >= 7 and new_time <= 8:
#         print("breakfast time")
#     elif new_time >= 12 and new_time <= 13:
#         print("lunch time")
#     elif new_time >=18 and new_time <= 19:
#         print("dinner time")
#     else:
#         print("")
#
#
#
#
# if __name__ == "__main__":
#     main()


# x = input("camelCase? ")
#
# for char in x:
#     if char.isupper():
#         print("_",end="")
#
#         char = char.lower()
#
#     print(char, end="")


# money_allowed =(25,10,5)
# coke_price =50
# Amount_due = 0
# new_coin = 0
#
# while True:
#     coin = int(input("insert coin? "))
#     if coin in money_allowed:
#         new_coin = new_coin + coin
#         if coke_price > new_coin:
#             Amount_due = coke_price - new_coin
#             print("Amount_due: ", Amount_due)
#
#
#         elif coke_price < new_coin:
#             change_owed = new_coin - coke_price
#
#             print("Change_owed: ", change_owed)
#             break
#
#         else:
#             print("Amount_due: ", 0)
#             break
#     else:
#         Amount_due = coke_price-new_coin
#         print("Amount_due: ", Amount_due)
#         continue


#
# words = input("Tweets? ")
#
# vowels = ["a","e","i","o","u"]
#
# for word in words:
#     if word in vowels:
#         continue
#     print(word,end="")


#
# # def two_char(s):
# #     # Python program to count the number of characters in a string
# #     #
# #     # import re
# #     #
# #     # Given input
# #     # str_input = "geeksforgeeks !!$ is best 4 all Geeks 10-0"
# #     #
# #     # Counting alphabets in the string using regex and re.findall() function
# #     # count = len(re.findall('[a-zA-Z]', str_input))
# #     #
# #     # Printing the count of alphabets in the string
# #     # print("Count of Alphabets: ", count)
# #     #
# #     # res = sum(1 for c in test_str if c.isalpha())
# #     res = len([ele for ele in s if ele.isalpha()])
# #     if res >= 2:
# #
# #         return True
# #     else:
# #         return False
#
#
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     # checking if the plate number is greater than 6 or less than 2
#     if len(s) < 2 or len(s) > 6:
#         return False
#
#     # checking of the last number is numeric
#     if not s[-1].isnumeric():
#         return False
#     i = 0
#
#     # checking if first and second number is alphabet
#     if not s[0].isalpha() and not s[1].isalpha():
#         return False
#
#     # checking if the first number after alphabet is 0
#     while i < len(s):
#         if not s[i].isalpha():
#             if s[i] == "0":
#                 return False
#             else:
#                 break
#         i += 1
#
#     # checking if punctuation marks are in license plates
#     for c in s:
#         if c in [",", ".", "?", "|", "!", "''", " "]:
#             return False
#     return True
#
#
# main()


# Fruits = {
#     'apple': '130',
#     'avocado': '50',
#     'banana': '110',
#     'cantaloupe': '50',
#     'grapefruit': '60',
#     'grapes': '90',
#     'honeydew melon': '50',
#     'kiwifruit': '90',
#     'lemon': '15',
#     'lime': '20',
#     'nectarine': '60',
#     'orange': '80',
#     'peach': '60',
#     'pear': '100',
#     'pineapple': '50',
#     'plums': '70',
#     'strawberries': '50',
#     'sweet cherries': '100',
#     'tangerine': '50',
#     'watermelon': '80',
# }
#
# fruit = input("item: ").lower()
#
# if fruit in Fruits:
#     print(Fruits[fruit])


#      # some exercises
# name = input("name? ").split(" ")
#
# firstname, lastname = name
#
# for j in range(len(firstname)-1,-1,-1):
#     print(firstname[j], lastname[j],end="" )

# for k in range(len(lastname)-1, -1, -1):
#     print(lastname[k],end="")


# numbers = input("number? ").split(",")
# mylist=[]
#
# for i in numbers:
#    mylist.append(i)
# print(mylist)
#

# n = input("number? ")
# z=[n,n+n,n+n+n]
# c = 0
# for i in z:
#    c = c + int(i)
#
# print(c)

# print(print.__doc__)

# to check year and date and time
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
#
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 8, 11)
# delta = l_date - f_date
# print(delta.date)


# class students:
#
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height
#
#
#
# std=students("solomon","24","156")
# print(std.age)


# Linear search

# list=[4,3,12,34,56,77,89]
# n=int(input('enter a number'))
# for i in range(len(list)):
#     if list[i]==n:
#         print('found at pos',i+1)
#         break
# else:
#         print('not found')


# binary search

# pos = 0
#
# def search(list, n):
#     for i in range(len(list)):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#     return False
#
#
# list = [5, 8, 9, 7, 15, 6]
# n = 8
# if search(list, n):
#     print("Found at {}".format(pos+1))
# else:
#     print("Not found")


# bubble sort
# def sort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 #look here
#                 list[j],list[j+1] = list[j+1],list[j]
#
#
# nums = [4,7,3,6,2,3,1]
# sort(nums)
# print(nums)

# slection sort
# def sort(nums):
#     for i in range(len(nums)):
#         minpos = i
#         for j in range(i+1, len(nums)):
#
#             if nums[j] < nums[minpos]:
#                 minpos = j
#
#         nums[i], nums[minpos] = nums[minpos], nums[i]
#         print(nums)
#
#
# nums = [4, 7, 3, 6, 2, 3, 1]
# sort(nums)
# print(nums)


import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='bebejimjim08',database='pylearn')

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()
for i in result:
    print(i)




























