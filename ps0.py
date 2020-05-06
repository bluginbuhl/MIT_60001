#!/usr/bin/env python3
# encoding: utf-8

from numpy import log2

# Prompt the user for an x and y value
x = int(input("Enter number x: "))

y = int(input("Enter number y: "))

# Print the value of x**y
print("{}^{} = ".format(x, y) + str(x**y))

# Print the value of log_2(x)
log_result = log2(x)
print("log_2({}) = {:.2f}".format(x, log_result))
