
# A = Rock     = X
# B = Paper    = Y
# C = Scissors = Z
#
# Rock = 1
# Paper = 2
# Scissors = 3
#
# Lose = 0
# Win = 6
# Tie = 3

with open('puzzle2_input.txt') as fh:
    score = 0
    for line in fh:
        prev_score = score
        round = str.strip(line).split(' ')
        if round[0] == 'A':             # Opp plays A
            if round[1] == 'X':         # A vs X
                score += 3 + 1
            elif round[1] == 'Y':       # A vs Y
                score += 6 + 2
            elif round[1] == 'Z':       # A vs Z
                score += 0 + 3
        elif round[0] == 'B':           # Opp plays B
            if round[1] == 'X':         # B vs X
                score += 0 + 1
            elif round[1] == 'Y':       # B vs Y
                score += 3 + 2
            elif round[1] == 'Z':       # B vs Z
                score += 6 + 3
        elif round[0] == 'C':           # Opp plays C
            if round[1] == 'X':         # C vs X
                score += 6 + 1
            elif round[1] == 'Y':       # C vs Y
                score += 0 + 2
            elif round[1] == 'Z':       # C vs Z
                score += 3 + 3
        else:
            print("Bad Things happened!!")
        
#        print(round[0],'vs',round[1], '-- Score is',(score - prev_score))

    print("Total Score:",score)