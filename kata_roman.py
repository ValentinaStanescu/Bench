'''Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) 
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.'''

def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    year = 0
    pre = 0
    for i in roman:
        print(f"i={i}: {int(symbols.get(i))}")
        if pre < int(symbols.get(i)) and pre != 0:
            year = year  + int(symbols.get(i)) - 2*pre
        else:
            year = year  + int(symbols.get(i))
        print (year)
        pre = int(symbols.get(i))
    return year
print(solution("MMMCMXCIX"))
