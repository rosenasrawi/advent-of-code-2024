from _getinput import *

# --- Day 9: Disk Fragmenter ---

data = getinput('09', example=False)

def checksum_block(data):

    num, files = 0, []

    for i,n in enumerate(data):
        
        if i % 2 == 0:
            files += [str(num)] * int(n)
            num += 1
        else:
            files += ['.'] * int(n)

    empty = [i for i,n in enumerate(files) if n == '.']

    while empty:

        if files[-1] == '.':
            files.pop()
            empty.pop()
            continue

        num = files.pop()
        id = empty.pop(0)
        files[id] = num

    return sum(i * int(n) for i, n in enumerate(files))

def checksum_files(data):

    num, files = 0, []

    for i,n in enumerate(data):
        
        if i % 2 == 0:
            files.append([str(num)] * int(n))
            num += 1
        else:
            if int(n) > 0:
                files.append(['.'] * int(n))

    empty = [i for i,n in enumerate(files) if '.' in n]
    numbers = [i for i,n in enumerate(files) if '.' not in n]

    while numbers:

        num_id = numbers.pop()
        num = files[num_id]

        for space_id in empty:

            if space_id > num_id:
                break

            space = files[space_id]

            if len(space) == len(num):

                files[space_id] = num
                files[num_id] = space

                torem = empty.index(space_id)
                empty.pop(torem)

                break

            if len(space) > len(num):

                space1 = space[:len(num)]
                space2 = space[len(num):]

                files[space_id] = num
                files[num_id] = space1
                files.insert(space_id+1, space2)

                empty = [e + 1 if e >= space_id else e for e in empty]
                numbers = [n+1 if n >= space_id+1 else n for n in numbers]

                break

    files = [i for f in files for i in f]

    return sum(i * int(n) for i, n in enumerate(files) if n != '.')

print('Part 1:', checksum_block(data))
print('Part 2:', checksum_files(data))