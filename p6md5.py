# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:58:11 2024

@author: appar
"""

import hashlib
# making a message
inputstring = "This is a message sent by a computer user."
# encoding the message using the library function
output = hashlib.md5(inputstring.encode())
# printing the hash function
print("Hash of the input string:")
print(output.hexdigest())
