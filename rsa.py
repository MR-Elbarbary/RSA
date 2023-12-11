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
        return y
    

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus  # Ensure base is within the modulus range

    while exponent > 0:
        # If the least significant bit of exponent is 1, multiply the result by base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Move to the next bit of the exponent
        exponent //= 2

        # Square the base (equivalent to moving to the next bit)
        base = (base * base) % modulus

    return result



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


t = (m-110000)
print("t",t)

c = mod_exp(t, e, n)

r = mod_exp(c, d, n)

print("c",c)
print("t",r)

if t == r:
    print("TRUE")
else:
    print("FALSE")