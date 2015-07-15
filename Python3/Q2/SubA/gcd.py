def gcd(m,n):
    return m if n==0 else gcd(n,m%n)

def lcm(m,n):
    return m*n//gcd(m,n)
