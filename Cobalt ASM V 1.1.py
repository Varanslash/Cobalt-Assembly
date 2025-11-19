registers = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0,
    "R5": 0,
    "R6": 0,
    "R7": 0,
}

strings = {
    "S0": " ",
    "S1": " ",
    "S2": " ",
    "S3": " ",
    "S4": " ",
    "S5": " ",
    "S6": " ",
    "S7": " ",
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
loop_count = 0
value = 0

while True:
    if function == True:
        if loop_count > 0:
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
        userinput = [soddom.split() for soddom in code.split(":") if soddom.strip()]
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
                    text = file.read().replace("\n", ":")
                
                # convert to list of commands
                userinput = [cmd.split() for cmd in text.split(":") if cmd.strip()]

                function = True
        lines.append(instruction)