def makeChange(n):
    """
    The function below will:
    - Obtain the input n 
    - Iterate over the possible number of quarters, dimes, nickels, and pennies
    - Add each valid combination to a set
    - Return the set containing all unique combinations
    """
    result = set()
    for quarters in range(n // 25 + 1):
        for dimes in range((n - quarters * 25) // 10 + 1):
            for nickels in range((n - quarters * 25 - dimes * 10) // 5 + 1):
                pennies = n - quarters * 25 - dimes * 10 - nickels * 5
                result.add((quarters, dimes, nickels, pennies))
    return result


n = 10
print(makeChange(n))
