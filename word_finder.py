import os, sys

def hasMatchInLine(line,keyword):
	return line.find(keyword) >= 0

def hasMatchInFile(filepath,keyword):
    try:
        with open(filepath, "r") as my_file:
            for line in my_file: 
                if hasMatchInLine(line,keyword):
                   return True
    except UnicodeDecodeError:
        return False
    return False

def recursiveFind(path,keyword):
    list = []
    for root, subdirs, files in os.walk(path):
        for name in files:
            filepath = os.path.join(root, name)
            if hasMatchInFile(filepath,keyword):
                list.append(filepath)
    
    return list


def find(path,keyword):
    if os.path.isfile(path):
        if hasMatchInFile(path,keyword):
            print(os.path.abspath(path))
    elif os.path.isdir(path):
        matches = recursiveFind(path,keyword)
        for match in matches:
            print(os.path.abspath(match))
    else:
        print("Incorrect file or directory.")

#main function
path = "."
keyword = "TODO"
if len(sys.argv) == 3:
    path = sys.argv[1]
    keyword = sys.argv[2]
find(path, keyword)
