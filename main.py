from random import *
import string

pool = string.ascii_letters + string.digits
for char in 'Il1oO0':
    pool = pool.replace(char, '')


def generate_password(length):
    password = ''.join(sample(pool, length))
    while set(password).isdisjoint(set(string.digits)) or set(password).isdisjoint(set(string.ascii_lowercase)) or set(password).isdisjoint(set(string.ascii_uppercase)):
        password = ''.join(sample(pool, length))
    return password


def generate_passwords(count, length):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords


n = int(input())
m = int(input())
print(*generate_passwords(n, m), sep='\n')
