def recursion(number):
    # Recursive function calls itself until a condition is reached.
    if number == 1:     # Our recursion stop.
        return number   # The result of the function (5+4+3+2+1).
    # We add the current number to the sum continually,
    # while subtracting 1 from the number we use as counter.
    return number + recursion(number-1)

""" SOME MORE EXAMPLES """
def gcd(high, low):
    if low == 0:
        return high
    return gcd(low, high%low)

def lcm(low, high):
    return int(low / gcd(low, high)) * high

if __name__ == "__main__":
    print("Example function:        ", recursion(5))
    print("Greatest Common Divisor: ", gcd(98, 56))
    print("Least Common Multiple:   ", lcm(15, 20))


