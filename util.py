#holds all the commands accesable by the terminal

def dnd_help():
    instructions = {"help" : "returns this list", "random" : "creates a random character sheet"}
    command_spacing = "          "
    instruction_spacing = "                                                                  "
    print('\n+------------+--------------------------------------------------------------------+')
    for command in list(instructions.keys()):
        print(f'| {command}{command_spacing[len(command)-1:len(command_spacing)-1]} | {instructions[command]}{instruction_spacing[len(instructions[command])-1:len(instruction_spacing)-1]} |')
    print('+------------+--------------------------------------------------------------------+\n')
