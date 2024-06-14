# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:54:39 2024

@author: appar
"""

def mod_exp(base, exp, modulus):
    """Computes (base^exp) % modulus efficiently using modular exponentiation."""
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % modulus
        exp = exp >> 1  # exp = exp // 2
        base = (base * base) % modulus  # Square the base
    return result

def diffie_hellman_key_exchange(p, g, a, b):
    # Step 2: Alice computes A = g^a mod p
    A = mod_exp(g, a, p)
    
    # Step 3: Bob computes B = g^b mod p
    B = mod_exp(g, b, p)
    
    # Step 4: Alice and Bob exchange A and B over an insecure channel
    # They can compute the shared secret key K
    K1 = mod_exp(B, a, p)  # Bob computes K1 = A^b mod p
    K2 = mod_exp(A, b, p)  # Alice computes K2 = B^a mod p
    
    assert K1 == K2
    return K1

# User input for prime modulus (p), base (g), secret integers a, and b
p = int(input("Enter the prime modulus (p): "))
g = int(input("Enter the base (g): "))
a = int(input("Enter Alice's secret integer (a): "))
b = int(input("Enter Bob's secret integer (b): "))

# Perform Diffie-Hellman key exchange
shared_key = diffie_hellman_key_exchange(p, g, a, b)
print("Shared Secret Key:", shared_key)