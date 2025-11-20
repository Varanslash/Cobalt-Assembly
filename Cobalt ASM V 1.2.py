registers = {
    "r0": 0,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
}

strings = {
    "s0": " ",
    "s1": " ",
    "s2": " ",
    "s3": " ",
    "s4": " ",
    "s5": " ",
    "s6": " ",
    "s7": " ",
}

routines = {

}

loops = {

}

ifelse = {
    
}

stack = []

lines = []

function = False
generalflag = False
loopflag = True
loop_count = 0
value = 0

while True:
    if function == True:
        if loop_count > 0 and loopflag == True:
            userinput = loops[loopname]
            loop_count -= 1
        else:
            try:
                userinput = routines[name]
                function = False
            except NameError:
                function = False
                pass
    else:
        code = input()
        userinput = [soddom.split() for soddom in code.split("\n") if soddom.strip()]
    for instruction in userinput:
        match instruction:
            case ["xor", reg1, reg2, dest] if reg1 in registers and reg2 in registers and dest in registers:
                registers[dest] = registers[reg1] ^ registers[reg2]
            case ["ora", reg1, reg2, dest] if reg1 in registers and reg2 in registers and dest in registers:
                registers[dest] = registers[reg1] | registers[reg2]
            case ["and", reg1, reg2, dest] if reg1 in registers and reg2 in registers and dest in registers:
                registers[dest] = registers[reg1] & registers[reg2]
            case ["not", reg1, dest] if reg1 in registers and dest in registers:
                registers[dest] = ~registers[reg1]
            case ["prt", reg] if reg in strings:
                print(strings[reg])
            case ["prn", reg] if reg in registers:
                print(registers[reg])
            case ["sav", reg, *string] if reg in strings:
                strings[reg] = " ".join(string)
            case ["reg", reg]:
                registers.update({reg: 0})
            case ["str", reg]:
                strings.update({reg: " "})
            case ["add", reg1, value] if reg1 in registers and value.isnumeric():
                registers[reg1] += int(value)
            case ["sub", reg1, value] if reg1 in registers and value.isnumeric():
                registers[reg1] -= int(value)
            case ["mov", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg2] = registers[reg1]
            case ["mul", reg1, value] if reg1 in registers and value.isnumeric():
                registers[reg1] *= int(value)
            case ["div", reg1, value] if reg1 in registers and value.isnumeric():
                registers[reg1] //= int(value)
            case ["mod", reg1, value] if reg1 in registers and value.isnumeric():
                registers[reg1] %= int(value)
            case ["psh", reg] if reg in registers:
                stack.append(registers[reg])
            case ["pop", reg] if reg in registers:
                if stack:
                    registers[reg] = stack.pop()
            case ["sar", reg1]:
                routines.update({reg1: []})
                name = reg1
            case ["sro", reg1, *string] if reg1 in routines:
                routines[reg1].append(string)
            case ["run", reg1] if reg1 in routines:
                userinput = routines[reg1]
                function = True
            case ["lop", reg1]:
                loops.update({reg1: []})
                loopname = reg1
            case ["lro", reg1, *string] if reg1 in loops:
                loops[reg1].append(string)
            case ["lup", reg1, value] if reg1 in loops:
                userinput = loops[reg1]
                loop_count = int(value)
                function = True
            case ["tru"]:
                generalflag = True
            case ["fal"]:
                generalflag = False
            case ["fif", func1, func2]:
                if generalflag == True:
                    userinput = routines[func1]
                    name = func1
                    function = True
                else:
                    userinput = routines[func2]
                    name = func2
                    function = True
            case ["rif", func1, func2, value]:
                if generalflag == True:
                    userinput = routines[func1]
                    name = func1
                    function = True
                else:
                    userinput = loops[func2]
                    name = func2
                    loop_count = int(value)
                    function = True
            case ["lif", func1, value1, func2, value2]:
                if generalflag == True:
                    userinput = routines[func1]
                    name = func1
                    loop_count = int(value1)
                    function = True
                else:
                    userinput = loops[func2]
                    name = func2
                    loop_count = int(value2)
                    function = True
            case [";"]:
                continue
            case ["lod", filename]:
                with open(filename, "r") as file:
                    text = file.read().replace("\n", "\n")
                userinput = [cmd.split() for cmd in text.split("\n") if cmd.strip()]
                function = True
            case ["brk", value, rout]:
                if loop_count < int(value):
                    loop_count = 0
                    loopflag = False
                    userinput = routines[rout]
            case ["rst"]:
                loopflag = True
            case ["frk"]:
                function = False
            case ["adt", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg1] += registers[reg2]
            case ["sut", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg1] -= registers[reg2]
            case ["mut", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg1] *= registers[reg2]
            case ["dit", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg1] //= registers[reg2]
            case ["mot", reg1, reg2] if reg1 in registers and reg2 in registers:
                registers[reg1] %= registers[reg2]
            case ["cmp", reg1, reg2] if reg1 in registers and reg2 in registers:
                if registers[reg1] == registers[reg2]:
                    generalflag = True
                else:
                    generalflag = False
            case ["smp", reg1, reg2] if reg1 in registers and reg2 in registers:
                if registers[reg1] != registers[reg2]:
                    generalflag = True
                else:
                    generalflag = False
            case ["fmp", reg1, reg2] if reg1 in registers and reg2 in registers:
                if registers[reg1] < registers[reg2]:
                    generalflag = True
                else:
                    generalflag = False
            case ["gmp", reg1, reg2] if reg1 in registers and reg2 in registers:
                if registers[reg1] > registers[reg2]:
                    generalflag = True
                else:
                    generalflag = False
            case ["cmv", reg, value] if reg in registers and value.isnumeric():
                if registers[reg] == int(value):
                    generalflag = True
                else:
                    generalflag = False
            case ["fmv", reg, value] if reg in registers and value.isnumeric():
                if registers[reg] < int(value):
                    generalflag = True
                else:
                    generalflag = False
            case ["gmv", reg, value] if reg in registers and value.isnumeric():
                if registers[reg] > int(value):
                    generalflag = True
                else:
                    generalflag = False
            case ["smv", reg, value] if reg in registers and value.isnumeric():
                if registers[reg] != int(value):
                    generalflag = True
                else:
                    generalflag = False
            case ["inc", reg] if reg in registers:
                registers[reg] += 1
            case ["dec", reg] if reg in registers:
                registers[reg] -= 1
            case ["shl", reg1, dest] if reg1 in registers and dest in registers:
                registers[dest] = registers[reg1] << 1
            case ["shr", reg1, dest] if reg1 in registers and dest in registers:
                registers[dest] = registers[reg1] >> 1
            case ["rhl", reg1] if reg1 in registers:
                registers[reg1] = (registers[reg1] << 1)
            case ["rhr", reg1] if reg1 in registers:
                registers[reg1] = (registers[reg1] >> 1)
            case ["csh"]:
                exit()
        lines.append(instruction)