# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:16:41 2024

@author: appar
"""

def findMinX(num, rem, k): 
    x = 1; # Initialize result 
  
    # As per the Chinise remainder 
    # theorem, this loop will 
    # always break. 
    while(True): 
          
        # Check if remainder of  
        # x % num[j] is rem[j]  
        # or not (for all j from  
        # 0 to k-1) 
        j = 0; 
        while(j < k): 
            if (x % num[j] != rem[j]): 
                break; 
            j += 1; 
  
        # If all remainders  
        # matched, we found x 
        if (j == k): 
            return x; 
  
        # Else try next number 
        x += 1; 
  
# Driver Code 
num = [3, 4, 5]; 
rem = [2, 3, 1]; 
k = len(num); 
print("x is", findMinX(num, rem, k)); 