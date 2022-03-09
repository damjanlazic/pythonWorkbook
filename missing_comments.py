"""
Exercise 161: Missing Comments
(Solved—44 Lines)
When one writes a function, it is generally a good idea to include a comment that
outlines the function’s purpose, its parameters and its return value. However, some-
times comments are forgotten, or left out by well-intentioned programmers that plan
to write them later but then never get around to it.
Create a python program that reads one or more Python source files and identifies
functions that are not immediately preceded by a comment. For the purposes of this
exercise, assume that any line that begins with def, followed by a space, is the
beginning of a function definition. Assume that the comment character, #, will be
the first character on the previous line when the function has a comment. Display the
names of all of the functions that are missing comments, along with the file name
and line number where the function definition is located.
The user will provide the names of one or more Python files as command line
parameters. If your program encounters a file that doesn’t exist or can’t be opened
then it should display an appropriate error message before moving on and processing
the remaining files.
"""

# get_filenames() prompts the user to eneter filenames and loads those names in a list
# returns a list of filenames entered by user
def get_filenames():
    fnames = []
    count = 1
    print("1.",end=" ")
    name = input("File name: ")
    while name != "":
        fnames.append(name)
        count = count+1
        print(count,end=" ")
        name = input("File name: ")
    return fnames

# check_comments(filename) @param: filename: name of file to be checked for comments
# returns dictionary: keys: names of functions with missing comments
# values: line numbers of function definitions
def check_comments(filename):
    fndict={}
    try:
        file = open(filename,"r")
        count = 0
        line = file.readline()
        if "#" not in line:
            comment = False
        else:
            comment = True
        while line != "":
            count = count + 1
            if "def " in line :
                if comment == False :
                    # skidamo ":" i "\n" sa kraja
                    funcN = line[4:len(line)-2]
                    fndict[funcN] = count
            if "#" not in line:
                comment = False
            else:
                comment = True
            line = file.readline()
    except:
        fndict["ERROR"]=-1
    file.close()
    return fndict

# main() prints out names of functions with missing comments in entered files
def main():
    files = get_filenames()
    for file in files:
        comment_info = check_comments(file)
        if comment_info != {}:
            if -1 in comment_info.values():
                print("File {} does not exist, or could not be opened".format(file))
            else:
                print("Missing comments in file {} :".format(file))
                for key in comment_info:
                    print("Function: {0} in line {1}".format(key, comment_info[key]))
        else:
            print("No missing comments in file: ", file)

main()  