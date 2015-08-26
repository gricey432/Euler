hundred = "hundred"
ten = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teen = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
one = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
and_s = "and"

def int_to_string(n):
    string = ""
    hundreds = n / 100
    tens = (n % 100) / 10
    ones = (n % 10)

    if hundreds:
        string += one[hundreds] + hundred
        if tens or ones:
            string += and_s

    if tens == 1 and ones == 0:
        string += ten[tens]
    elif tens == 1:
        string += teen[ones]
        return string
    else:
        string += ten[tens]

    string += one[ones]
    return string

length = 0
for n in range(1, 1000):
    length += len(int_to_string(n))

# Special case for one thousand
length += len("one") + len("thousand")

print length
        
