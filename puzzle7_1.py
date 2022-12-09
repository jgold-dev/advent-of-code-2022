# Find the size of all directories (including subdirectories)
# Identify which ones are <= 100000.  This can also include the subdirectories
# Calculcate sum total size of all of those directories
#
# {directory: size}

sum_total = 0
max_disk = 70000000
min_free = 30000000
best_candidate_size = min_free #default to a high number to start

class Directory():
    def __init__(self, name, parent_name):
        self.name = name
        self.parent_name = parent_name
        self.children = []
        self.files = {}
        self.size = 0

def printTree(dir:Directory, level=0):
    pad = ""
    for i in range(level*2):
        pad += " "
    print(pad,dir.name, ":", dir.size)
    for child in dir.children:
        printTree(child, level + 1)

def calcTree(dir:Directory):
    for child in dir.children:
        calcTree(child)
        if child.size <= 100000:
            global sum_total
            sum_total += child.size

def searchTreeSizes(dir:Directory, magic_no):
    # Must be close and over (not under)
    for child in dir.children:
        searchTreeSizes(child, excess)
        global best_candidate_size
        if child.size >= magic_no and child.size < best_candidate_size:
            best_candidate_size = child.size

def calculateFileSizes(dir:Directory):
    for child in dir.children:
        if child.size == 0:
            calculateFileSizes(child)
        dir.size += child.size

    for file,size in dir.files.items():
        dir.size += size

with open('puzzle7_input.txt') as fh:
    line = str.strip(fh.readline())
    root = Directory("/", None)
    current_dir = root
    prev_dirs = []
    for line in fh:
        line = str.strip(line)
        if line.startswith("$ cd"):
            name = line[5:]
            if name == "..":
                current_dir = prev_dirs.pop()
            else:
                prev_dirs.append(current_dir)
                current_dir = [dir for dir in current_dir.children if dir.name == name][0]
        elif line.startswith("dir"):
            child_dir = line[4:]
            current_dir.children.append(Directory(child_dir, current_dir.parent_name))
        elif ord(line[0]) >= 49 and ord(line[0]) <= 57:
            file = line.split(" ")
            current_dir.files[file[1]] = int(file[0])

    calculateFileSizes(root)

    excess = min_free - (max_disk - root.size)
    print("Need to clear:", excess)
    searchTreeSizes(root, excess)
    print("Best Candidate:", best_candidate_size)

#    printTree(root)
#    calcTree(root)
#    print(sum_total)
