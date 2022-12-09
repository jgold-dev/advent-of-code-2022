with open('puzzle4_input.txt') as fh:

    count = 0
    for line in fh:
        line = str.strip(line)
        pair = line.split(',')

        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')

        start1 = int(elf1[0])
        end1 = int(elf1[1])

        start2 = int(elf2[0])
        end2 = int(elf2[1])

        if (start1 <= start2 and end1 >= start2) or (start2 <= start1 and end2 >= start1):
            count += 1

print("Overlap in Range:", count)