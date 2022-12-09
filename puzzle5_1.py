with open('puzzle5_input.txt') as fh:

    # Read until we get a 1
    for line in fh:
        line = str.strip(line)

        if line[0] == '1':
            fh.readline()
            break

    # Create stacks
    stack1 = ['J','H','G','M','Z','N','T','F']
    stack2 = ['V','W','J']
    stack3 = ['G','V','L','J','B','T','H']
    stack4 = ['B','P','J','N','C','D','V','L']
    stack5 = ['F','W','S','M','P','R','G']
    stack6 = ['G','H','C','F','B','N','V','M']
    stack7 = ['D','H','G','M','R']
    stack8 = ['H','N','M','V','Z','D']
    stack9 = ['G','N','F','H']
    stacks = []
    stacks.append(stack1)
    stacks.append(stack2)
    stacks.append(stack3)
    stacks.append(stack4)
    stacks.append(stack5)
    stacks.append(stack6)
    stacks.append(stack7)
    stacks.append(stack8)
    stacks.append(stack9)

    # print(stacks)
    for line in fh:
        line = str.strip(line)

        moves = int(line[5:line.index('f')-1])
        from_stack_i = int(line[line.index('f')+5:line.index('t')-1])
        to_stack_i = int(line[line.index('t')+3:].strip())

        from_stack = stacks[from_stack_i - 1]
        to_stack = stacks[to_stack_i - 1]

        for m in range(moves):
            crate = from_stack.pop()
            to_stack.append(crate)

    top_crate_str = ""
    for s in stacks:
        top_crate_str += s[len(s) - 1]

    print(top_crate_str)