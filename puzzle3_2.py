with open('puzzle3_input.txt') as fh:

    group_count = 0
    groups = {}
    group_list = []
    group_iter = 0
    for line in fh:
        line = str.strip(line)
        group_list.append(line)
        group_iter += 1

        if group_iter == 3:
            groups[group_count] = group_list
            group_list = []
            group_count += 1
            group_iter = 0

#    print(groups)

    sum = 0
    for key in groups.keys():
        common_item_type = list(set(groups[key][0]).intersection(set(groups[key][1])).intersection(set(groups[key][2])))
        
        if len(common_item_type) != 1:
            print("ERROR: More than 1 Common Item Type Found!")
        else:
            print("Common Item Type:", common_item_type)

            ascii_val = ord(common_item_type[0])
            if ascii_val >= 97:
                val = ascii_val - 96
            else:
                val = ascii_val - 38
            sum += val

    print("Total =",sum)