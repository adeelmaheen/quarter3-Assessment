def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

if __name__ == "__main__":
    result1 = in_range(5, 1, 10) 
    print(result1) 
    result2 = in_range(5, 5, 10)
    print(result2)
    result3 = in_range(5, 1, 4)
    print(result3)