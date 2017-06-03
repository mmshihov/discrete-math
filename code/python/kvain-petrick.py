#перебор всех вариантов минимизации булевых функций n-аргументов

def getSdnf(vector, n):
    sdnf = []
    argCount = 1 << n
    arg = 0
    while (arg < argCount):
        if ((vector >> arg) & 1):
            sdnf.append(getConstituent(arg, n))
        arg = arg + 1
    return sdnf
    
def getConstituent(arg, n):
    i = 0
    constituent = ""
    while (i < n):
        constituent = "{0}".format((arg >> i) & 1) + constituent
        i = i + 1
    return "#" + constituent

def isInvalid(arg):
    return arg[0:1] == "&"

def markAsInvalid(arg):
    return "&" + arg[1:]
    
def isChecked(arg):
    return arg[0:1] == "!"

def checkArg(arg):
    return "!" + arg[1:]

def glueArgs(arg1, arg2, n):
    rarg = "#"
    i    = 0
    diff = 0
    while (i < n):
        var1 = arg1[i+1:i+2]
        var2 = arg2[i+1:i+2]
        if   (var1 == "0" and var2 == "0"):
            rarg = rarg + "0"
        elif (var1 == "0" and var2 == "1"):
            rarg = rarg + "*"
            diff = diff + 1
        elif (var1 == "1" and var2 == "0"):
            rarg = rarg + "*"
            diff = diff + 1
        elif (var1 == "1" and var2 == "1"):
            rarg = rarg + "1"
        elif (var1 == "*" and var2 == "*"):
            rarg = rarg + "*"
        else:
            rarg = rarg + "?"
            diff = diff + 2
        i = i + 1
    if (diff == 1):
        return rarg
    return markAsInvalid(rarg)
    
def isListContainArg(dnf, arg):
    for item in dnf:
        if (arg == item):
            return True
    return False
    
def kvain(vector, n):
    sdnf = getSdnf(vector, n)
    tdnf = []
    
    while len(sdnf) > 0:
        dnf = []
        i = 0
        while (i < len(sdnf) - 1):
            j=i+1
            while (j < len(sdnf)):
                arg = glueArgs(sdnf[i], sdnf[j], n)
                if (not isInvalid(arg)):
                    if (not isListContainArg(dnf, arg)):
                        dnf.append(arg)
                    sdnf[i] = checkArg(sdnf[i])
                    sdnf[j] = checkArg(sdnf[j])
                j = j + 1
            i = i + 1
        i = 0
        while (i < len(sdnf)):
            if (not isChecked(sdnf[i])):
                tdnf.append(sdnf[i])
            i = i + 1
        sdnf = dnf
    return tdnf

#покрытие импликантой impli конституэнты consti
def isCover(impli, consti, n):
    i=0
    while (i < n):
        argConsti = consti[i+1:i+2]
        argImpli  = impli[i+1:i+2]
        if (argImpli == "1" or argImpli == "0"):
            if (argImpli != argConsti):
                return False
        i = i + 1
    return True

def isSymInList(sym, list):
    for elem in list:
        if (sym == elem):
            return True
    return False

def isEats(dizWho, dizWhom):
    for sym in dizWho:
        if (not isSymInList(sym, dizWhom)):
            return False
    return True
    
def petrickConditon(sdnf, dnf, n):
    knfs = []
    for consti in sdnf:
        knf = []
        i = 0
        while (i < len(dnf)):
            if (isCover(dnf[i], consti, n)):
                knf.append(i)
            i = i + 1
        knfs.append(knf)
    return knfs

def petrickTransformCondition(condition):
    copy = []
    for list in condition:
        copy.append(list)
    for list in condition:
        i = 0
        isItWasEat = False
        while (i < len(copy)):
            if (isEats(list, copy[i])):
                copy[i:i+1] = []
                isItWasEat = True
            else:
                i = i + 1
        if (isItWasEat):
            copy.append(list)
    return copy
    
def decart(list):
    indexes  = []
    cortages = []
    
    for el in list:
        indexes.append(0)
    
    i = 0
    isOverflow = False
    while (not isOverflow and i < len(indexes)):
        i = 0
        cortage = []
        while (i < len(indexes)):
            impli = list[i][indexes[i]]
            if (not isSymInList(impli, cortage)):
                cortage.append(impli)
            i = i + 1
        cortages.append(cortage)
        i = 0
        while (i < len(indexes)):
            indexes[i] = indexes[i] + 1
            if (indexes[i] < len(list[i])):
                break
            else:
                indexes[i] = 0
                i = i + 1
                if (i >= len(indexes)):
                    isOverflow = True
    return cortages
        

def petrick(sdnf, dnf, n):
    condition = petrickConditon(sdnf, dnf, n)
    return petrickTransformCondition(condition)

    
def calcDecartPower(list):
    r = 1
    for item in list:
        r = r * len(item)
    return r

def IsPreferred(vector, n):
    i = 0
    vectorLength = (1 << n)
    oneValuesCount = (vectorLength >> 1)
    mask = (1 << (vectorLength - 1))
    while (mask != 0):
        if (vector & mask):
            i = i + 1
        mask = (mask >> 1)
    return (i == oneValuesCount)
    
    
n = 5
maxTdnfCount = 9
maxVector    = 1 << (1 << n)
vector       = 0
while (vector < maxVector):
    if (IsPreferred(vector, n)):
        covers = petrick(getSdnf(vector, n), kvain(vector, n), n)
        decartPower = calcDecartPower(covers)
        if ((0 < decartPower) and (decartPower < maxTdnfCount)):
            print("vector=", vector)
            print(getSdnf(vector, n))
            print(kvain(vector, n))
            print(covers)
            print(decart(covers))
            print("-----------------------------------------------")
    vector = vector + 1
    
