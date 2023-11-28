def to_int(input):
    if not input:
        return 0

    result = 0
    negative = False
    started = False

    for char in input:
        if char == ' ' and not started:
            continue
        elif char == '-' and not started:
            negative = True
        elif char.isdigit():
            result = result * 10 + int(char)
            started = True
        else:
            break

    if negative:
        result = -result

    result = max(-2**31, result)
    result = min(2**31 - 1, result)

    return result

input_str = ""
output = to_int(input_str)
print(output)

input_str = "  -42 abc"
output = to_int(input_str)
print(output)

input_str = "42 abcd"
output = to_int(input_str)
print(output)

input_str = "abcd ?!== 42"
output = to_int(input_str)
print(output)

input_str = "-9128347230032"
output = to_int(input_str)
print(output)

input_str = "42-10abcd"
output = to_int(input_str)
print(output)

input_str = "0042"
output = to_int(input_str)
print(output)
