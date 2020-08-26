# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:49:24 2020

@author: vasil
"""

i = 0 

from fractions import Fraction 
import random

table_numerator = [2,3,4,5,6,7,8,9,10]
table_denominator = [4,6,8,10,12,46,49,50]



while i<5:
        
    d_num = random.choice(table_numerator)
    d_dem = random.choice(table_denominator)
    
    answer = float((Fraction(d_num,d_dem)))
    print(answer)
    
    n_N = input("please give the NUMENATOR of the fraction's %s/%s simpliest form: \n" %(d_num,d_dem))
    n_D =  input("please give the DENOMINATOR of the fraction's %s/%s simpliest form: \n" %(d_num,d_dem))
    ratio1 = (n_N/n_D)
    ratio2 = float(ratio1)
    
    if ratio2 == answer:
        print("You got the asnwer correct!")
    else:
        print("Wrong answer, please retry!")
    i += 1