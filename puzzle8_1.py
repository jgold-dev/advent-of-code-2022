
length = 99
rows = []

def isValVisible(val:int, x_index:int, y_index:int):
    # Is it visible from either Left or Right, or Up or Down, of the index?
    # If It is visible from any direction, it's visible
    global rows
    global length

    # Is it visible by row?
    is_visible = True
    for c in range(0, x_index):
#        print("Is Val Visible by Row?", val, "vs", rows[y_index][c])
        if rows[y_index][c] >= val:
            is_visible = False
    if is_visible:
        return True

    is_visible = True
    for c in range(x_index + 1,length):
#        print("Is Val Visible by Row?", val, "vs", rows[y_index][c])
        if rows[y_index][c] >= val:
            is_visible = False
    if is_visible:
        return True
    
    # Is it visible by column?
    is_visible = True
    for r in range(0, y_index):
#        print("Is Val Visible by Column?", val, "vs", rows[r][x_index])
        if rows[r][x_index] >= val:
            is_visible = False
    if is_visible:
        return True

    is_visible = True
    for r in range(y_index + 1, length):
#        print("Is Val Visible by Column?", val, "vs", rows[r][x_index])
        if rows[r][x_index] >= val:
            is_visible = False
    if is_visible:
        return True
            
    return False
    
with open('puzzle8_input.txt') as fh:

    for line in fh:
        line = str.strip(line)
        row = []
        for i in range(len(line)):
            row.append(int(line[i]))
        rows.append(row)

    print("Column Length:", len(rows), " Row Length:", len(rows[0]))

    visible_count = 0
    for r in range(length):
        if r == 0 or r == (length-1):
            visible_count += length
            continue
        for c in range(length):
            if c == 0 or c == (length-1):
                visible_count += 1
                continue
#            print("Is Val Visible?",rows[r][c])
            if isValVisible(rows[r][c], c, r):
#                print("True")
                visible_count += 1
#            else:
#                print("False")
#            print("-----------------------------------")
    print("# of visible:", visible_count)
