
length = 99
rows = []

def getScenicScore(val:int, x_index:int, y_index:int):
    # Is it visible from either Left or Right, or Up or Down, of the index?
    # If It is visible from any direction, it's visible
    global rows
    global length

    scores = []

    # Left Direction (reversed)
    tree_count = 0
    for c in reversed(range(0, x_index)):
        if rows[y_index][c] < val:
            tree_count += 1
        else:
            tree_count += 1
            break
    scores.append(tree_count)

    # Right Direction
    tree_count = 0
    for c in range(x_index + 1,length):
        if rows[y_index][c] < val:
            tree_count += 1
        else:
            tree_count += 1
            break
    scores.append(tree_count)
    
    # Up direction (reversed)
    tree_count = 0
    for r in reversed(range(0, y_index)):
        if rows[r][x_index] < val:
            tree_count += 1
        else:
            tree_count += 1
            break
    scores.append(tree_count)

    # Down Direction
    tree_count = 0
    for r in range(y_index + 1, length):
        if rows[r][x_index] < val:
            tree_count += 1
        else:
            tree_count += 1
            break
    scores.append(tree_count)

    print("  Scores:", scores)            
    score = 1
    for s in scores:
        score *= s
    return score
    
with open('puzzle8_input.txt') as fh:

    for line in fh:
        line = str.strip(line)
        row = []
        for i in range(len(line)):
            row.append(int(line[i]))
        rows.append(row)

    print("Column Length:", len(rows), " Row Length:", len(rows[0]))

    high_score = 0
    for r in range(length):
        for c in range(length):
            print("Get Score for:",rows[r][c])
            cur_score = getScenicScore(rows[r][c], c, r)
            print("Score:",cur_score)
            print("---------------------------------------")
            if cur_score > high_score:
                high_score = cur_score
    print("High Score:", high_score)
