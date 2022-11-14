# Made by 0sir1ss @ https://github.com/0sir1ss/Carbon
# Modified by Mcall for SCA-ML
import ast, re, random, io, tokenize, os, sys, platform, math

is_windows = True if platform.system() == "Windows" else False

maxThreads = 100
errorFiles = 0
goodFiles = 0



if is_windows:
    os.system("title Carbon @ github.com/0sir1ss/Carbon")

def clear():
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

def pause():
    if is_windows:
        os.system(f"pause >nul")
    else:
        input()

def leave():
    try:
        sys.exit()
    except:
        exit()

def error(error):
    print(red(f"        [>] Error: {error}"), end="")
    pause(); clear(); leave()

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded

def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

def remove_docs(source):
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out

def do_rename(pairs, code):
    for key in pairs:
        code = re.sub(fr"\b({key})\b", pairs[key], code, re.MULTILINE)
    return code

def rename(filename: str):
    with open(filename, "r") as file:
        code = file.read()
        code = remove_docs(code)
        parsed = ast.parse(code)

    funcs = {
        node for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    classes = {
        node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
    }
    args = {
        node.id for node in ast.walk(parsed) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
    }
    attrs = {
        node.attr for node in ast.walk(parsed) if isinstance(node, ast.Attribute) and not isinstance(node.ctx, ast.Load)
    }
    for func in funcs:
        if func.args.args:
            for arg in func.args.args:
                args.add(arg.arg)
        if func.args.kwonlyargs:
            for arg in func.args.kwonlyargs:
                args.add(arg.arg)
        if func.args.vararg:
            args.add(func.args.vararg.arg)
        if func.args.kwarg:
            args.add(func.args.kwarg.arg)

    pairs = {}
    used = set()
    for func in funcs:
        if func.name == "__init__":
            continue
        iteration = 0
        newname = "functionToken " + str(iteration) + " "
        while newname in used:
            iteration += 1
            newname = "functionToken " + str(iteration)
        used.add(newname)
        pairs[func.name] = newname

    for _class in classes:
        iteration = 0
        newname = "ClassToken " + str(iteration)
        while newname in used:
            iteration += 1
            newname = "ClassToken " + str(iteration)
        used.add(newname)
        pairs[_class.name] = newname

    for arg in args:
        if (arg == 'f'):
            newname = "F"
            used.add(newname)
            pairs[arg] = newname
        elif (arg == 'F'):
            newname = "f"
            used.add(newname)
            pairs[arg] = newname
        else:
            iteration = 0
            newname = "argTokens " + str(iteration)
            while newname in used:
                iteration += 1
                newname = "argTokens " + str(iteration)
            used.add(newname)
            pairs[arg] = newname

    for attr in attrs:
        iteration = 0
        newname = "attrToken" + str(iteration)
        while newname in used:
            iteration += 1
            newname = "attrToken" + str(iteration)
        used.add(newname)
        pairs[attr] = newname

    string_regex = r"('|\")[\x1f-\x7e]{1,}?('|\")"

    original_strings = re.finditer(string_regex, code, re.MULTILINE)
    originals = []

    for matchNum, match in enumerate(original_strings, start=1):
        originals.append(match.group().replace("\\", "\\\\"))

    placeholder = os.urandom(16).hex()
    code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

    for i in range(len(originals)):
        for key in pairs:
            originals[i] = re.sub(r"({.*)(" + key + r")(.*})", "\\1" + pairs[key] + "\\3", originals[i], re.MULTILINE)

    while True:
        found = False
        code = do_rename(pairs, code)
        for key in pairs:
            if re.findall(fr"\b({key})\b", code):
                found = True
        if found == False:
            break


    replace_placeholder = r"('|\")" + placeholder + r"('|\")"
    for original in originals:
        code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)

    return code

def codeSimiliarizer(data):
    code = rename(data)
    return code

def searchFiles(path, fileformats):
    filesToDo = []
    for root, dirs, files in os.walk(path):
        for file in files:
            for fileformat in fileformats:
                if file.endswith(fileformat):
                    #code to generate a list of paths of files to generate logs for
                    filesToDo.append(os.path.join(root, file))
    return filesToDo

def searchFileName(path, fileName):
    filesToDo = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == fileName:
                #code to generate a list of paths of files to generate logs for
                filesToDo.append(os.path.join(root, file))
    return filesToDo

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
        
        
def tothread(file):
    global goodFiles
    global errorFiles
    try:
        data = codeSimiliarizer(file)
        #write data to .pysimp file
        path = file
        path = path.strip(".txt")
        goodFiles = goodFiles + 1
        with open(path + ".pysimp", "w") as file:
            file.write(data)
            file.close()
    except:
        print("Error + " + file +  "Sucessful Files" + str(goodFiles) + "\r")
        errorFiles =+ 1

def mainForDatabase(dirtocheck):
    filesToSimplify = []
    
    #get sub directories
    filePathsToSimplify = searchFileName(dirtocheck, '0.txt')

    for fileNumb in range(len(filePathsToSimplify)):
        if fileNumb == 0:
            filesToSimplify = searchFiles(filePathsToSimplify[fileNumb].strip('0.txt'),'.txt')
        else:
            filesToSimplify = filesToSimplify + (searchFiles(filePathsToSimplify[fileNumb].strip('\\0.txt'),'.txt'))
    import threading
    import time
    for file in filesToSimplify:
        print (file)
        printProgressBar(filesToSimplify.index(file), len(filesToSimplify), prefix = 'Progress:', suffix = 'Complete', length = 50)
        t= threading.Thread(target=tothread, args=(file,))
        while (threading.active_count() > maxThreads):
            time.sleep(.1)
        t.start()
    print("error ratio: " + str(errorFiles/len(filesToSimplify)))

        
def main():
    import argparse
    #get arguments from command line
    parser = argparse.ArgumentParser(description='Simplify python code')
    parser.add_argument('path', metavar='path', type=str, help='path to file or directory')
    parser.add_argument('-f', '--file', action='store_true', help='path is a file')
    parser.add_argument('-dc', '--databasecheck', action='store_true', help='path is datacollector database')       
    args = parser.parse_args()
    if args.databasecheck:
        mainForDatabase()
    elif args.file:
        data = codeSimiliarizer(args.path)
        #write data to .pysimp file
        path = args.path
        path = path.strip(".txt")
        with open(path + ".pysimp", "w") as file:
            file.write(data)
            file.close()
    elif os.path.isdir(args.path):
        filesToSimplify = searchFiles(args.path, '.py')
        for file in filesToSimplify:
            data = codeSimiliarizer(file)
            #write data to .pysimp file
            path = file
            path = path.strip(".py")
            with open(path + ".pysimp", "w") as file:
                file.write(data)
                file.close()
        
        

        
        
        
        
        
    
    
    
main()
#mainForDatabase()
