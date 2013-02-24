import instructions
import controller
instruction = {'add': instructions.add,
               'and': instructions.pand,
               'stb': instructions.stb,
               'sth': instructions.sth,
               'stw': instructions.stw,
               'xor': instructions.xor}
control = {'li':controller.li,
               '.org': controller.org}

