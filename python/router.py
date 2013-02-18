import instructions
import controller
instruction = {'add': instructions.add,
               'and': instructions.pand,
               'stb': instructions.stb,
               'xor': instructions.xor}
control = {'li':controller.li,
               '.org': controller.org}

