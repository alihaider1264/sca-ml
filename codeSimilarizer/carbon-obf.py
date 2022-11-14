import ast, re, random, io, tokenize, os, sys, platform, math
IlIIIIIIIlIllII = True if platform.system() == "Windows" else False
if IlIIIIIIIlIllII:
    os.system("title Carbon @ github.com/0sir1ss/Carbon")
def lIlIIIIlIlIIlIllIl():
    if IlIIIIIIIlIllII:
        os.system("cls")
    else:
        os.system("clear")
def llllIllIIllIl():
    if IlIIIIIIIlIllII:
        os.system(lIIllllIIlIlIIlIIIlI"pause >nul")
    else:
        input()
def IlIIIIIIlllIIlIII():
    try:
        sys.exit()
    except:
        exit()
def llllIlllllIIIllIIl(llllIlllllIIIllIIl):
    print(lIIIIIlll(lIIllllIIlIlIIlIIIlI"        [>] Error: {llllIlllllIIIllIIlIIllIIllllIIIlIlIl}"), end="")
    llllIllIIllIl(); lIlIIIIlIlIIlIllIl(); IlIIIIIIlllIIlIII()
def lIIIIIlll(IlllIIlIl):
    os.system(""); faded = ""
    for lIIIIlIIllllllllI in IlllIIlIl.splitlines():
        IIIlIIlIllIII = 250
        for lIlIIIlIIlIllIIllll in lIIIIlIIllllllllI:
            IIIlIIlIllIII -= 5
            if IIIlIIlIllIII < 0:
                IIIlIIlIllIII = 0
            IllllIlIIIlIIIIlll += (lIIllllIIlIlIIlIIIlI"\033[38;2;255;{IIIlIIlIllIII};0m{lIlIIIlIIlIllIIllllIIllIIllllIIIlIlIl}\033[0m")
        IllllIlIIIlIIIIlll += "\n"
    return IllllIlIIIlIIIIlll
def IIIIIIll(IlllIIlIl):
    os.system(""); faded = ""
    for lIIIIlIIllllllllI in IlllIIlIl.splitlines():
        IIIlIIlIllIII = 0
        for lIlIIIlIIlIllIIllll in lIIIIlIIllllllllI:
            IIIlIIlIllIII += 3
            if IIIlIIlIllIII > 255:
                IIIlIIlIllIII = 255
            IllllIlIIIlIIIIlll += (lIIllllIIlIlIIlIIIlI"\033[38;2;0;{IIIlIIlIllIII};255m{lIlIIIlIIlIllIIllllIIllIIllllIIIlIlIl}\033[0m")
        IllllIlIIIlIIIIlll += "\n"
    return IllllIlIIIlIIIIlll
def IlIlIIIlllIllIlIIII(IlllIIlIl):
    os.system(""); faded = ""
    IIIlIIlIllIII = 10
    for lIIIIlIIllllllllI in IlllIIlIl.splitlines():
        IllllIlIIIlIIIIlll += (lIIllllIIlIlIIlIIIlI"\033[38;2;0;{IIIlIIlIllIII};255m{lIIIIlIIllllllllIIllIIllllIIIlIlIlI}\033[0m\n")
        if not IIIlIIlIllIII == 255:
            IIIlIIlIllIII += 15
            if IIIlIIlIllIII > 255:
                IIIlIIlIllIII = 255
    return IllllIlIIIlIIIIlll
def IIIlIllIIlIIlIlIIl(IlllIIlIl):
    os.system("")
    IllllIlIIIlIIIIlll = ""
    IIlllllIllllI = False
    for lIIIIlIIllllllllI in IlllIIlIl.splitlines():
        lIIIIIlll = 40
        for lIlIIIlIIlIllIIllll in lIIIIlIIllllllllI:
            if IIlllllIllllI:
                lIIIIIlll -= 3
            else:
                lIIIIIlll += 3
            if lIIIIIlll > 254:
                lIIIIIlll = 255
                IIlllllIllllI = True
            elif lIIIIIlll < 1:
                lIIIIIlll = 30
                IIlllllIllllI = False
            IllllIlIIIlIIIIlll += (lIIllllIIlIlIIlIIIlI"\033[38;2;{lIIIIIlll};0;220m{lIlIIIlIIlIllIIllllIIllIIllllIIIlIlIl}\033[0m")
    return IllllIlIIIlIIIIlll
def IIIIlIIlllIIIIIll(IIlllIII):
    IIIlllIIIIll = io.StringIO(IIlllIII)
    IllIIIlIllllIIlIlII = ""
    IlIIIlIIllIl = tokenize.INDENT
    lIlIIIIlllIlII = -1
    lIlIlllIIIl = 0
    for llIlllIII in tokenize.generate_tokens(IIIlllIIIIll.readline):
        IllIIIIIlllIIllIlI = llIlllIII[0]
        IIllIllIIlIIllIlIl = llIlllIII[1]
        llIIllIIIlII, IIIlIIllllIlllIIIl = llIlllIII[2]
        lIIllllIlIlIlIIlIll, llIlllIlI = llIlllIII[3]
        if llIIllIIIlII > lIlIIIIlllIlII:
            lIlIlllIIIl = 0
        if IIIlIIllllIlllIIIl > lIlIlllIIIl:
            IllIIIlIllllIIlIlII += (" " * (IIIlIIllllIlllIIIl - lIlIlllIIIl))
        if IllIIIIIlllIIllIlI == tokenize.COMMENT:
            pass
        elif IllIIIIIlllIIllIlI == tokenize.STRING:
            if IlIIIlIIllIl != tokenize.INDENT:
                if IlIIIlIIllIl != tokenize.NEWLINE:
                    if IIIlIIllllIlllIIIl > 0:
                        IllIIIlIllllIIlIlII += IIllIllIIlIIllIlIl
        else:
            IllIIIlIllllIIlIlII += IIllIllIIlIIllIlIl
        IlIIIlIIllIl = IllIIIIIlllIIllIlI
        lIlIlllIIIl = llIlllIlI
        lIlIIIIlllIlII = lIIllllIlIlIlIIlIll
    IllIIIlIllllIIlIlII = '\n'.join(lIIllIIllllIIIlIlIl for lIIllIIllllIIIlIlIl in IllIIIlIllllIIlIlII.splitlines() if lIIllIIllllIIIlIlIl.strip())
    return IllIIIlIllllIIlIlII
def IIIlIlIlllII(IIlIlllIlIllII, IllIlIIlI):
    for IIlllIIIlI in IIlIlllIlIllII:
        IllIlIIlI = re.sub(fr"\b({IIlllIIIlI})\b", IIlIlllIlIllII[IIlllIIIlI], IllIlIIlI, re.MULTILINE)
    return IllIlIIlI
def llIIllIlllIIllIlll(llllllIlllI: str):
    with open(llllllIlllI, "r") as IIIIllIIIlIlllll:
        IllIlIIlI = IIIIllIIIlIlllll.read()
        IllIlIIlI = IIIIlIIlllIIIIIll(IllIlIIlI)
        IIllIIllIIllIlIIII = ast.parse(IllIlIIlI)
    IlllIIIIIlIIl = {
        lIlllIlIlIlllIIIll for lIlllIlIlIlllIIIll in ast.walk(IIllIIllIIllIlIIII) if isinstance(lIlllIlIlIlllIIIll, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    llIllllII = {
        lIlllIlIlIlllIIIll for lIlllIlIlIlllIIIll in ast.walk(IIllIIllIIllIlIIII) if isinstance(lIlllIlIlIlllIIIll, ast.ClassDef)
    }
    IIIlIllIIIlllIll = {
        lIlllIlIlIlllIIIll.id for lIlllIlIlIlllIIIll in ast.walk(IIllIIllIIllIlIIII) if isinstance(lIlllIlIlIlllIIIll, ast.Name) and not isinstance(lIlllIlIlIlllIIIll.ctx, ast.Load)
    }
    IlIIIlIlIIl = {
        lIlllIlIlIlllIIIll.llIlIIllIIllIIll for lIlllIlIlIlllIIIll in ast.walk(IIllIIllIIllIlIIII) if isinstance(lIlllIlIlIlllIIIll, ast.Attribute) and not isinstance(lIlllIlIlIlllIIIll.ctx, ast.Load)
    }
    for IIIlllIlllIlIll in IlllIIIIIlIIl:
        if IIIlllIlllIlIll.IIIlIllIIIlllIll.IIIlIllIIIlllIll:
            for lIIlIllllIII in IIIlllIlllIlIll.IIIlIllIIIlllIll.IIIlIllIIIlllIll:
                IIIlIllIIIlllIll.add(lIIlIllllIII.lIIlIllllIII)
        if IIIlllIlllIlIll.IIIlIllIIIlllIll.kwonlyargs:
            for lIIlIllllIII in IIIlllIlllIlIll.IIIlIllIIIlllIll.kwonlyargs:
                IIIlIllIIIlllIll.add(lIIlIllllIII.lIIlIllllIII)
        if IIIlllIlllIlIll.IIIlIllIIIlllIll.vararg:
            IIIlIllIIIlllIll.add(IIIlllIlllIlIll.IIIlIllIIIlllIll.vararg.lIIlIllllIII)
        if IIIlllIlllIlIll.IIIlIllIIIlllIll.kwarg:
            IIIlIllIIIlllIll.add(IIIlllIlllIlIll.IIIlIllIIIlllIll.kwarg.lIIlIllllIII)
    IIlIlllIlIllII = {}
    lllllIllIlIIlIlI = set()
    for IIIlllIlllIlIll in IlllIIIIIlIIl:
        if IIIlllIlllIlIll.name == "__init__":
            continue
        IlllllIlIlllI = 0
        llIllIlIIIlIlIIlll = "functionToken" + str(IlllllIlIlllI)
        while llIllIlIIIlIlIIlll in lllllIllIlIIlIlI:
            IlllllIlIlllI += 1
            llIllIlIIIlIlIIlll = "functionToken" + str(IlllllIlIlllI)
        lllllIllIlIIlIlI.add(llIllIlIIIlIlIIlll)
        IIlIlllIlIllII[IIIlllIlllIlIll.name] = llIllIlIIIlIlIIlll
    for IIllllIIIIIIllllIIlI in llIllllII:
        IlllllIlIlllI = 0
        llIllIlIIIlIlIIlll = "ClassToken" + str(IlllllIlIlllI)
        while llIllIlIIIlIlIIlll in lllllIllIlIIlIlI:
            IlllllIlIlllI += 1
            llIllIlIIIlIlIIlll = "ClassToken" + str(IlllllIlIlllI)
        lllllIllIlIIlIlI.add(llIllIlIIIlIlIIlll)
        IIlIlllIlIllII[IIllllIIIIIIllllIIlI.name] = llIllIlIIIlIlIIlll
    for lIIlIllllIII in IIIlIllIIIlllIll:
        if (lIIlIllllIII == 'f'):
            continue
        IlllllIlIlllI = 0
        llIllIlIIIlIlIIlll = "argToken" + str(IlllllIlIlllI)
        while llIllIlIIIlIlIIlll in lllllIllIlIIlIlI:
            IlllllIlIlllI += 1
            llIllIlIIIlIlIIlll = "argToken" + str(IlllllIlIlllI)
        lllllIllIlIIlIlI.add(llIllIlIIIlIlIIlll)
        IIlIlllIlIllII[lIIlIllllIII] = llIllIlIIIlIlIIlll
    for llIlIIllIIllIIll in IlIIIlIlIIl:
        IlllllIlIlllI = 0
        llIllIlIIIlIlIIlll = "attrToken" + str(IlllllIlIlllI)
        while llIllIlIIIlIlIIlll in lllllIllIlIIlIlI:
            IlllllIlIlllI += 1
            llIllIlIIIlIlIIlll = "attrToken" + str(IlllllIlIlllI)
        lllllIllIlIIlIlI.add(llIllIlIIIlIlIIlll)
        IIlIlllIlIllII[llIlIIllIIllIIll] = llIllIlIIIlIlIIlll
    IIIIIllIlllIll = r"('|\")[\x1f-\x7e]{1,}?('|\")"
    llIllIlIIIIlI = re.finditer(IIIIIllIlllIll, IllIlIIlI, re.MULTILINE)
    IlIlllIIIIllllIIll = []
    for lIIllIIllIIlI, IIlIIIllIIIlllIIl in enumerate(llIllIlIIIIlI, start=1):
        IlIlllIIIIllllIIll.append(IIlIIIllIIIlllIIl.group().replace("\\", "\\\\"))
    IIlIIIlllIllllIllIIl = os.urandom(16).hex()
    IllIlIIlI = re.sub(IIIIIllIlllIll, lIIllllIIlIlIIlIIIlI"'{IIlIIIlllIllllIllIIlIIllIIllllIIIlIlIl}'", IllIlIIlI, 0, re.MULTILINE)
    for IIIlllIllIIIl in range(len(IlIlllIIIIllllIIll)):
        for IIlllIIIlI in IIlIlllIlIllII:
            IlIlllIIIIllllIIll[IIIlllIllIIIl] = re.sub(r"({.*)(" + IIlllIIIlI + r")(.*})", "\\1" + IIlIlllIlIllII[IIlllIIIlI] + "\\3", IlIlllIIIIllllIIll[IIIlllIllIIIl], re.MULTILINE)
    while True:
        lIllllIIIIIlIIIll = False
        IllIlIIlI = IIIlIlIlllII(IIlIlllIlIllII, IllIlIIlI)
        for IIlllIIIlI in IIlIlllIlIllII:
            if re.findall(fr"\b({IIlllIIIlI})\b", IllIlIIlI):
                lIllllIIIIIlIIIll = True
        if lIllllIIIIIlIIIll == False:
            break
    lllIIIIIIIIIll = r"('|\")" + IIlIIIlllIllllIllIIl + r"('|\")"
    for IlIllIlIIlIII in IlIlllIIIIllllIIll:
        IllIlIIlI = re.sub(lllIIIIIIIIIll, IlIllIlIIlIII, IllIlIIlI, 1, re.MULTILINE)
    return IllIlIIlI
IIllIlIIIl = lIIllllIIlIlIIlIIIlI"""
                                  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
                                 /$$__  $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$| $$$ | $$
                                | $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$
                                | $$      | $$$$$$$$| $$$$$$$/| $$$$$$$ | $$  | $$| $$ $$ $$
                                | $$      | $$__  $$| $$__  $$| $$__  $$| $$  | $$| $$  $$$$
                                | $$    $$| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$\  $$$
                                |  $$$$$$/| $$  | $$| $$  | $$| $$$$$$$/|  $$$$$$/| $$ \  $$
                                 \______/ |__/  |__/|__/  |__/|_______/  \______/ |__/  \__/
        {IIIlIllIIlIIlIlIIl(lIIllllIIlIlIIlIIIlI"[>] Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_IIIlllIllIIIlIIllIIllllIIIlIlIlnlIIllllIIlIlIIlIIIlIo[2]}")}
"""
lIlIIIIlIlIIlIllIl()
print(IlIlIIIlllIllIlIIII(IIllIlIIIl))
while True:
    IIIIllIIIlIlllll = input(IIIlIllIIlIIlIlIIl("        [>] Enter the python file you wish to obfuscate [script.py] : ") + "\033[38;2;148;0;230m")
    if not os.path.exists(IIIIllIIIlIlllll):
        print(lIIIIIlll("        [!] Error : That file does not exist"), end="")
    else:
        break
IllIlIIlI = llIIllIlllIIllIlll(IIIIllIIIlIlllll)
with open(lIIllllIIlIlIIlIIIlI"{IIIIllIIIlIlllllIIllIIllllIIIlIlIl[:-3]}-obf.py", "w") as lIIllllIIlIlIIlIIIlI:
    lIIllllIIlIlIIlIIIlI.write(IllIlIIlI)
print(IIIIIIll(lIIllllIIlIlIIlIIIlI"        [>] Code has been successfully obfuscated @ {IIIIllIIIlIlllllIIllIIllllIIIlIlIl[:-3]}-obf.py"), end="")
llllIllIIllIl(); lIlIIIIlIlIIlIllIl(); IlIIIIIIlllIIlIII()