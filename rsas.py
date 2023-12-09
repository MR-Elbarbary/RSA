
from random import randrange

def isprime(n):
    i = 2
    while n >= i * i:
        if n % i == 0:
            return False
        i += 1
    return True

def gcs(e, m):
    if m % e == 0:
        return e
    else:
        return gcs(m % e, e)

def inv(e, m):
    d = 0.1
    while not isinstance(d, int):
        i = 1
        d = ((i * m) + 1) // e
    return d


def mod_inverse(e, phi_n):
    # Step 2: Extended Euclidean Algorithm
    d, x, y = extended_gcd(e, phi_n)
    
    # Step 3: Check GCD and Return
    if d != 1:
        # No modular inverse exists
        return None
    else:
        # Modular inverse exists, return x
        y = x % phi_n
        if y < 0:
            y = phi_n + y
            return y
        else:
            return y

def extended_gcd(a, b):
    # Base case
    if a == 0:
        return b, 0, 1
    
    # Recursive call
    d, x1, y1 = extended_gcd(b % a, a)
    
    # Compute x and y
    x = y1 - (b // a) * x1
    y = x1
    
    return d, x, y

# the 2 prime numbers p and q and they are private
p = randrange(10**(4-1), 10**4 - 1)
while not isprime(p):
    p = randrange(10**(4-1), 10**4 - 1)

q = randrange(10**(4-1), 10**4 - 1)
while not isprime(q):
    q = randrange(10**(4-1), 10**4 - 1)

n = p * q
m = (p - 1) * (q - 1)
e = randrange(10, 100)
while not isprime(e):
    e = randrange(10, 100)

d = mod_inverse(e, m)

#print("d:", d)

z = (6**e) % n
print("z:", z)

y = (z**d) % n
print("y:", y)