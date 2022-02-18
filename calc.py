import math as m
import numpy as np 
import tkinter as tk 
import statistics
import matplotlib as mplt
import pandas as pd
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b
def square(x):
    return x*x
def squareroot(x):
    return m.sqrt(x)
def random(x):
    return m.random(x)

a=int(input("Enter a random number a="))
b=int(input("Enter a random number b="))
x=int(input("Enter x"))
print(sub(a,b),add(a,b),mul(a,b),div(a,b))
print(square(x),squareroot(x),random(x))
