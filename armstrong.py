#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:11:05 2023

@author: achintyarai
"""

num=int(input("Enter the number:"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+= digit**order
    temp//=10
if num==sum:
    print("Is a Armstrong Number")
else:
    print("Is a non armstrong number")