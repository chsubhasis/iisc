def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    return gcd(b, a%b)

if gcd(26, 65) == 13:
    print("Works for 26, 65")
