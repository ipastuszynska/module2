# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:16:50 2018

@author: iza
"""

import SimpleBundlePurchase_v1
#test one 
balance = 20
password = "ilikecats"
SimpleBundlePurchase_v1.checkPasscode(password, balance)

#test two
balance = 5
password = "ilikecats"
SimpleBundlePurchase_v1.checkPasscode(password, balance)

#test three
balance = 20
password = "ilikecats"
SimpleBundlePurchase_v1.checkPasscode(password, balance)

from SimpleBundlePurchase_v1 import DataBundlePurchase
# Test calls to program:
print 'TEST-EXAMPLE 1'
#database input, you will still need to check user pin
result = DataBundlePurchase('1234',34.55)
print '---------\nRESULT:', result
print '-' * 50, '\n'
print 'TEST-EXAMPLE 2'
result = DataBundlePurchase('2345',22.00)
print '---------\nRESULT:', result
print '-' * 50, '\n'
print 'TEST-EXAMPLE 3'
result = DataBundlePurchase('3456',17.55)
print '---------\nRESULT:', result