with open('puzzle3_input.txt') as fh:

    sum = 0
    for line in fh:
        line = str.strip(line)
        mid = int(len(line)/2)
        comp1 = line[0:mid]
        comp2 = line[mid:]

        comp1_arr = []
        for i in range(len(comp1)):
            comp1_arr.append(comp1[i])

        comp2_arr = []
        for i in range(len(comp2)):
            comp2_arr.append(comp2[i])

        dupe = list(set(comp1_arr).intersection(set(comp2_arr)))

        if len(dupe) != 1:
            print("ERROR: More than 1 Dupe Found!")
        else:
            val = 0
            ascii_val = ord(dupe[0])
            if ascii_val >= 97:
                val = ascii_val - 96
            else:
                val = ascii_val - 38
            sum += val

    print("Total =",sum)
