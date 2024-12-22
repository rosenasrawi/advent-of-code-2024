from _getinput import *

# --- Day 22: Monkey Market ---

data = getinput('22', example=False)
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

seqs = []
total = 0
for secret in numbers:
    new_seq = []
    for _ in range(2000):
        secret = sequence(secret)
        new_seq.append(int(str(secret)[-1]))
    total += secret
    seqs.append(new_seq)

for i, n in enumerate(numbers):
    seqs[i].insert(0, n)

all_scores = {}

for seq in seqs:

    scores = {}
    
    for slide in range(len(seqs[0])-5):
        nums = seq[slide:slide+5]
        difs = tuple([nums[i+1]-nums[i] for i in range(4)])
        score = seq[slide+4]

        if difs not in scores:
            scores[difs] = score

    for key in scores:
        if key in all_scores:
            all_scores[key] += scores[key]
        else:
            all_scores[key] = scores[key]

print('Part 1:', total)
print('Part 2:', max(all_scores.values()))