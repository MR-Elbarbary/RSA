from sympy import randprime

# the 2 prime numbers p and q and they are private 
p = randprime(10**(256-1), 10**256 - 1)
q = randprime(10**(256-1), 10**256 - 1)
while p == q:
    q = randprime(10**(256-1), 10**256 - 1)

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
            return phi_n + y
        return y



# the n is public
n = p * q

# the m is private
m = (p-1)*(q-1)

# the e is public
e = 65537
d = mod_inverse(e,m)


print("n",n)
print("m",m)
print("p",p)
print("q",q)
print("d:",d)