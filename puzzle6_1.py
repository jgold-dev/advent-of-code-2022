with open('puzzle6_input.txt') as fh:

    # Read until we get a 1
    for line in fh:
        line = str.strip(line)

    print(len(line))

    tmp_str = ""
    marker = 14
    for i in range(len(line)):
        tmp_str += line[i]
        if len(tmp_str) > marker:
            tmp_str = tmp_str[1:]

            tmp_set = set()
            for m in range(len(tmp_str)):
                tmp_set.add(tmp_str[m])

            if len(tmp_set) == marker:
                print("4 unique chars at",i+1)
                break