
elves = {}
elf_count = 0
# Read in file
with open('puzzle1_input.txt') as fh:
    
    item_count = 0
    cal_sum = 0
    for line in fh:
        if str.strip(line) == '':
            elves[elf_count] = (item_count, cal_sum)
            elf_count += 1
            item_count = 0
            cal_sum = 0
        else:
            item_count += 1
            cal_sum += int(line)

print("# of Elves:", len(elves))
most_cal_elf = 0
most_cals = 0
cal_counts = []
for key in elves.keys():
    cal_counts.append(elves[key][1])
    if elves[key][1] > most_cals:
        most_cals = elves[key][1]
        most_cal_elf = key

# Finds all duplicates
unique_cal_count = set(cal_counts)
print("Unique Cal Vals:", len(unique_cal_count))
duplicates = [number for number in cal_counts if cal_counts.count(number) > 1]
print(duplicates)

# print("Elf:", most_cal_elf, "Cals:", most_cals)
#for key in elves.keys():
#    print(elves[key][1])
