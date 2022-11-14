import ast, re, random, io, tokenize, os, sys, platform, math
argTokens 21 = True if platform.system() == "Windows" else False
if argTokens 21:
    os.system("title Carbon @ github.com/0sir1ss/Carbon")
def functionToken 0():
    if argTokens 21:
        os.system("cls")
    else:
        os.system("clear")
def functionToken 3():
    if argTokens 21:
        os.system(F"pause >nul")
    else:
        input()
def functionToken 5():
    try:
        sys.exit()
    except:
        exit()
def argTokens 24(argTokens 24):
    print(argTokens 51(F"        [>] Error: {argTokens 8Tokens 24}"), end="")
    functionToken 3(); functionToken 0(); functionToken 5()
def argTokens 51(argTokens 23):
    os.system(""); faded = ""
    for argTokens 44 in argTokens 23.splitlines():
        argTokens 30 = 250
        for argTokens 29 in argTokens 44:
            argTokens 30 -= 5
            if argTokens 30 < 0:
                argTokens 30 = 0
            argTokens 6 += (F"\033[38;2;255;{argTokens 30};0m{argTokens 29}\033[0m")
        argTokens 6 += "\n"
    return argTokens 6
def functionToken 4(argTokens 23):
    os.system(""); faded = ""
    for argTokens 44 in argTokens 23.splitlines():
        argTokens 30 = 0
        for argTokens 29 in argTokens 44:
            argTokens 30 += 3
            if argTokens 30 > 255:
                argTokens 30 = 255
            argTokens 6 += (F"\033[38;2;0;{argTokens 30};255m{argTokens 29}\033[0m")
        argTokens 6 += "\n"
    return argTokens 6
def functionToken 10(argTokens 23):
    os.system(""); faded = ""
    argTokens 30 = 10
    for argTokens 44 in argTokens 23.splitlines():
        argTokens 6 += (F"\033[38;2;0;{argTokens 30};255m{argTokens 36argTokens 9ne}\033[0m\n")
        if not argTokens 30 == 255:
            argTokens 30 += 15
            if argTokens 30 > 255:
                argTokens 30 = 255
    return argTokens 6
def functionToken 2(argTokens 23):
    os.system("")
    argTokens 6 = ""
    argTokens 7 = False
    for argTokens 44 in argTokens 23.splitlines():
        argTokens 51 = 40
        for argTokens 29 in argTokens 44:
            if argTokens 7:
                argTokens 51 -= 3
            else:
                argTokens 51 += 3
            if argTokens 51 > 254:
                argTokens 51 = 255
                argTokens 7 = True
            elif argTokens 51 < 1:
                argTokens 51 = 30
                argTokens 7 = False
            argTokens 6 += (F"\033[38;2;{argTokens 8Tokens 51};0;220m{argTokens 29}\033[0m")
    return argTokens 6
def functionToken 8(argTokens 45):
    argTokens 10 = io.StringIO(argTokens 45)
    argTokens 12 = ""
    argTokens 1 = tokenize.INDENT
    argTokens 13 = -1
    argTokens 48 = 0
    for argTokens 3 in tokenize.generate_tokens(argTokens 10.readline):
        argTokens 42 = argTokens 3[0]
        argTokens 31 = argTokens 3[1]
        argTokens 35, argTokens 16 = argTokens 3[2]
        argTokens 17, argTokens 5 = argTokens 3[3]
        if argTokens 35 > argTokens 13:
            argTokens 48 = 0
        if argTokens 16 > argTokens 48:
            argTokens 12 += (" " * (argTokens 16 - argTokens 48))
        if argTokens 42 == tokenize.COMMENT:
            pass
        elif argTokens 42 == tokenize.STRING:
            if argTokens 1 != tokenize.INDENT:
                if argTokens 1 != tokenize.NEWLINE:
                    if argTokens 16 > 0:
                        argTokens 12 += argTokens 31
        else:
            argTokens 12 += argTokens 31
        argTokens 1 = argTokens 42
        argTokens 48 = argTokens 5
        argTokens 13 = argTokens 17
    argTokens 12 = '\n'.join(argTokens 36 for argTokens 36 in argTokens 12.splitlines() if argTokens 36.strip())
    return argTokens 12
def functionToken 1(argTokens 49, argTokens 18):
    for argTokens 27 in argTokens 49:
        argTokens 18 = re.sub(fr"\b({argTokens 27})\b", argTokens 49[argTokens 27], argTokens 18, re.MULTILINE)
    return argTokens 18
def functionToken 7(argTokens 28: str):
    with open(argTokens 28, "r") as argTokens 4:
        argTokens 18 = argTokens 4.read()
        argTokens 18 = functionToken 8(argTokens 18)
        argTokens 34 = ast.parse(argTokens 18)
    argTokens 26 = {
        argTokens 11 for argTokens 11 in ast.walk(argTokens 34) if isinstance(argTokens 11, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    argTokens 47 = {
        argTokens 11 for argTokens 11 in ast.walk(argTokens 34) if isinstance(argTokens 11, ast.ClassDef)
    }
    argTokens 33 = {
        argTokens 11.id for argTokens 11 in ast.walk(argTokens 34) if isinstance(argTokens 11, ast.Name) and not isinstance(argTokens 11.ctx, ast.Load)
    }
    argTokens 22 = {
        argTokens 11.argTokens 43 for argTokens 11 in ast.walk(argTokens 34) if isinstance(argTokens 11, ast.Attribute) and not isinstance(argTokens 11.ctx, ast.Load)
    }
    for argTokens 50 in argTokens 26:
        if argTokens 50.argTokens 33.argTokens 33:
            for argTokens 8 in argTokens 50.argTokens 33.argTokens 33:
                argTokens 33.add(argTokens 8.argTokens 8)
        if argTokens 50.argTokens 33.kwonlyargs:
            for argTokens 8 in argTokens 50.argTokens 33.kwonlyargs:
                argTokens 33.add(argTokens 8.argTokens 8)
        if argTokens 50.argTokens 33.vararg:
            argTokens 33.add(argTokens 50.argTokens 33.vararg.argTokens 8)
        if argTokens 50.argTokens 33.kwarg:
            argTokens 33.add(argTokens 50.argTokens 33.kwarg.argTokens 8)
    argTokens 49 = {}
    argTokens 32 = set()
    for argTokens 50 in argTokens 26:
        if argTokens 50.name == "__init__":
            continue
        argTokens 15 = 0
        argTokens 2 = "functionToken" + argTokens 15
        while argTokens 2 in argTokens 32:
            argTokens 15 += 1
            argTokens 2 = "functionToken" + argTokens 15
        argTokens 32.add(argTokens 2)
        argTokens 49[argTokens 50.name] = argTokens 2
    for argTokens 40 in argTokens 47:
        argTokens 15 = 0
        argTokens 2 = "ClassToken" + argTokens 15
        while argTokens 2 in argTokens 32:
            argTokens 15 += 1
            argTokens 2 = "ClassToken" + argTokens 15
        argTokens 32.add(argTokens 2)
        argTokens 49[argTokens 40.name] = argTokens 2
    for argTokens 8 in argTokens 33:
        argTokens 15 = 0
        argTokens 2 = "argToken" + argTokens 15
        while argTokens 2 in argTokens 32:
            argTokens 15 += 1
            argTokens 2 = "argToken" + argTokens 15
        argTokens 32.add(argTokens 2)
        argTokens 49[argTokens 8] = argTokens 2
    for argTokens 43 in argTokens 22:
        argTokens 15 = 0
        argTokens 2 = "attrToken" + argTokens 15
        while argTokens 2 in argTokens 32:
            argTokens 15 += 1
            argTokens 2 = "attrToken" + argTokens 15
        argTokens 32.add(argTokens 2)
        argTokens 49[argTokens 43] = argTokens 2
    argTokens 25 = r"('|\")[\x1f-\x7e]{1,}?('|\")"
    argTokens 38 = re.finditer(argTokens 25, argTokens 18, re.MULTILINE)
    argTokens 46 = []
    for argTokens 41, argTokens 39 in enumerate(argTokens 38, start=1):
        argTokens 46.append(argTokens 39.group().replace("\\", "\\\\"))
    argTokens 37 = os.urandom(16).hex()
    argTokens 18 = re.sub(argTokens 25, F"'{placehoargTokens 36der}'", argTokens 18, 0, re.MULTILINE)
    for argTokens 9 in range(len(argTokens 46)):
        for argTokens 27 in argTokens 49:
            argTokens 46[argTokens 9] = re.sub(r"({.*)(" + argTokens 27 + r")(.*})", "\\1" + argTokens 49[argTokens 27] + "\\3", argTokens 46[argTokens 9], re.MULTILINE)
    while True:
        argTokens 0 = False
        argTokens 18 = functionToken 1(argTokens 49, argTokens 18)
        for argTokens 27 in argTokens 49:
            if re.findall(fr"\b({argTokens 27})\b", argTokens 18):
                argTokens 0 = True
        if argTokens 0 == False:
            break
    argTokens 14 = r"('|\")" + argTokens 37 + r"('|\")"
    for argTokens 19 in argTokens 46:
        argTokens 18 = re.sub(argTokens 14, argTokens 19, argTokens 18, 1, re.MULTILINE)
    return argTokens 18
argTokens 20 = F"""
                                  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
                                 /$$__  $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$| $$$ | $$
                                | $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$
                                | $$      | $$$$$$$$| $$$$$$$/| $$$$$$$ | $$  | $$| $$ $$ $$
                                | $$      | $$__  $$| $$__  $$| $$__  $$| $$  | $$| $$  $$$$
                                | $$    $$| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$\  $$$
                                |  $$$$$$/| $$  | $$| $$  | $$| $$$$$$$/|  $$$$$$/| $$ \  $$
                                 \______/ |__/  |__/|__/  |__/|_______/  \______/ |__/  \__/
        {functionToken 2(F"[>] Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_argTokens 9nFo[2]}")}
"""
functionToken 0()
print(functionToken 10(argTokens 20))
while True:
    argTokens 4 = input(functionToken 2("        [>] Enter the python file you wish to obfuscate [script.py] : ") + "\033[38;2;148;0;230m")
    if not os.path.exists(argTokens 4):
        print(argTokens 51("        [!] Error : That file does not exist"), end="")
    else:
        break
argTokens 18 = functionToken 7(argTokens 4)
with open(F"{argTokens 8Tokens 4[:-3]}-obf.py", "w") as F:
    F.write(argTokens 18)
print(functionToken 4(F"        [>] Code has been successfully obfuscated @ {argTokens 8Tokens 4[:-3]}-obf.py"), end="")
functionToken 3(); functionToken 0(); functionToken 5()