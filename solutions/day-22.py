from _getinput import *

# --- Day 22: Monkey Market ---

data = getinput('22', example=True)
numbers = list(map(int, data))

def mix(new_secret, secret):
    return new_secret ^ secret

def prune(new_secret):
    return new_secret % 16777216

def sequence(secret):
    old_secret = secret
    new_secret = secret * 64
    new_secret = mix(new_secret, old_secret)
    new_secret = prune(new_secret)

    old_secret = new_secret
    new_secret = new_secret // 32
    new_secret = mix(new_secret, old_secret)
    new_secret = prune(new_secret)

    old_secret = new_secret
    new_secret = new_secret * 2048
    new_secret = mix(new_secret, old_secret)
    new_secret = prune(new_secret)

    return new_secret

total = 0
for secret in numbers:
    for _ in range(2000):
        secret = sequence(secret)
    total += secret

print(total)