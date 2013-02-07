import registers
pc = 0

def org(param):
   pc = int(param[0])
def li (params):
   rD = params[0]
   rA = params[1]
   registers.gp[rD] = rA
