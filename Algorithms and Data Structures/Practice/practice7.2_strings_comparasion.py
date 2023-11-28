s = "abc"
t = "abdd##c"
stack = []
for char in t:
    if char != '#':
        stack.append(char)
    elif stack:
        stack.pop()
print(stack)
print(''.join(stack))
print(s)
print(t)
print('YES' if ''.join(stack) == s else 'NO')