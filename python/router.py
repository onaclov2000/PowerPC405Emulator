import instructions
import controller
instruction = {'add': instructions.add,
               'stb': instructions.stb,
               'xor': instructions.xor}
control = {'li':controller.li,
               '.org': controller.org}

