# goal of this package is to implement all functions that the PPC405 uses.
import registers
import memory

def add (params):
   rD = params[0]
   rA = registers.gp[params[1]]
   rB = registers.gp[params[2]]
   registers.gp[rD] = int(rA)+int(rB)
def adddot(rD, rA, rB):
   print "Not Implemented"
def addo(rD, rA, rB):
   print "Not Implemented"
def addodot(rD,rA,rB):
   print "Not Implemented"   
def addc(rD,rA,rB):
   print "Not Implemented"
def addcdot(rD,rA,rB):
   print "Not Implemented"
def addco(rD,rA,rB):
   print "Not Implemented"
def addcodot(rD,rA,rB):
   print "Not Implemented"
def adde(rD,rA,rB):
   print "Not Implemented"
def addedot(rD,rA,rB):
   print "Not Implemented"
def addeo(rD,rA,rB):
   print "Not Implemented"
def addeodot(rD,rA,rB):
   print "Not Implemented"
def addi(rD,rA,SIMM):
   print "Not Implemented"
def addic(rD,rA,SIMM):
   print "Not Implemented"
def addicdot(rD,rA,SIMM):
   print "Not Implemented"
def addis(rD,rA,SIMM):
   print "Not Implemented"
def addme(rD,rA):
   print "Not Implemented"
def addmedot(rD,rA):
   print "Not Implemented"
def addmeo(rD,rA):
   print "Not Implemented"
def addmeodot(rD,rA):
   print "Not Implemented"
def addze(rD,rA):
   print "Not Implemented"
def addzedot(rD,rA):
   print "Not Implemented"
def addzeo(rD,rA):
   print "Not Implemented"
def addzeodot(rD,rA):
   print "Not Implemented"
def pand(params):
   rA = params[0]
   rS = registers.gp[params[1]]
   rB = registers.gp[params[2]]
   registers.gp[rA] = int(rS) & int(rB)
def panddot(rA,rS,rB):
   print "Not Implemented"
def pandc(rA,rS,rB):
   print "Not Implemented"
def pandcdot(rA,rS,rB):
   print "Not Implemented"
def pandidot(rA,rS,UIMM):
   print "Not Implemented"
def pandisdot(rA,rS,UIMM):
   print "Not Implemented"
def b(target):
   print "Not Implemented"
def ba(target):
   print "Not Implemented"
def bl(target):
   print "Not Implemented"
def bla(target):
   print "Not Implemented"
def bc(BO,BI,target):
   print "Not Implemented"
def bca(BO,BI,target):
   print "Not Implemented"
def bcl(BO,BI,target):
   print "Not Implemented"
def bcla(BO,BI,target):
   print "Not Implemented"
def bcctr(BO,BI):
   print "Not Implemented"
def bcctrl(BO,BI):
   print "Not Implemented"
def bclr(BO,BI):
   print "Not Implemented"
def bclrl(BO,BI):
   print "Not Implemented"
#def cmp(crfD,0,rA,rB):
   print "Not Implemented"
#def cmpi(crfD,0,rA,SIMM):
   print "Not Implemented"
#def cmpl(crfD,0,rA,rB):
   print "Not Implemented"
#def cmpli(crfD,0,rA,UIMM):
   print "Not Implemented"
def cntlzw(rA,rS):
   print "Not Implemented"
def cntlzwdot(rA,rS):
   print "Not Implemented"
def crpand(crbD,crbA,crbB):
   print "Not Implemented"
def crpandc(crbD,crbA,crbB):
   print "Not Implemented"
def creqv(crbD,crbA,crbB):
   print "Not Implemented"
def crnpand(crbD,crbA,crbB):
   print "Not Implemented"
def crnpor(crbD,crbA,crbB):
   print "Not Implemented"
def crpor(crbD,crbA,crbB):
   print "Not Implemented"
def crporc(crbD,crbA,crbB):
   print "Not Implemented"
def crxpor(crbD,crbA,crbB):
   print "Not Implemented"
def dcba(rA,rB):
   print "Not Implemented"
def dcbf(rA,rB):
   print "Not Implemented"
def dcbi(rA,rB):
   print "Not Implemented"
def dcbst(rA,rB):
   print "Not Implemented"
def dcbt(rA,rB):
   print "Not Implemented"
def dcbtst(rA,rB):
   print "Not Implemented"
def dcbz(rA,rB):
   print "Not Implemented"
def dccci(rA,rB):
   print "Not Implemented"
def dcread(rD,rA,rB):
   print "Not Implemented"
def divw(rD,rA,rB):
   print "Not Implemented"
def divwdot(rD,rA,rB):
   print "Not Implemented"
def divwo(rD,rA,rB):
   print "Not Implemented"
def divwodot(rD,rA,rB):
   print "Not Implemented"
def divwu(rD,rA,rB):
   print "Not Implemented"
def divwudot(rD,rA,rB):
   print "Not Implemented"
def divwuo(rD,rA,rB):
   print "Not Implemented"
def divwuodot(rD,rA,rB):
   print "Not Implemented"
def eieio():
   print "Not Implemented"
def eqv(rA,rS,rB):
   print "Not Implemented"
def eqvdot(rA,rS,rB):
   print "Not Implemented"
def extsb(rA,rS):
   print "Not Implemented"
def extsbdot(rA,rS):
   print "Not Implemented"
def extsh(rA,rS):
   print "Not Implemented"
def extshdot(rA,rS):
   print "Not Implemented"
def icbi(rA,rB):
   print "Not Implemented"
def icbt(rA,rB):
   print "Not Implemented"
def iccci(rA,rB):
   print "Not Implemented"
def icread(rA,rB):
   print "Not Implemented"
def isync():
   print "Not Implemented"
def lbz(rD,drA):
   print "Not Implemented"
def lbzu(rD,rA,rB):
   print "Not Implemented"
def lbzux(rD,rA,rB):
   print "Not Implemented"
def lbzx(rD,rA,rB):
   print "Not Implemented"
def lha(rD,drA):
   print "Not Implemented"
def lhau(rD,drA):
   print "Not Implemented"
def lhaux(rD,rA,rB):
   print "Not Implemented"
def lhax(rD,rA,rB):
   print "Not Implemented"
def lhbrx(rD,rA,rB):
   print "Not Implemented"
def lhz(rD,drA):
   print "Not Implemented"
def lhzu(rD,drA):
   print "Not Implemented"
def lhzux(rD,rA,rB):
   print "Not Implemented"
def lhzx(rD,rA,rB):
   print "Not Implemented"
def lmw(rD,drA):
   print "Not Implemented"
def lswi(rD,rA,NB):
   print "Not Implemented"
def lswx(rD,rA,rB):
   print "Not Implemented"
def lwarx(rD,rA,rB):
   print "Not Implemented"
def lwbrx(rD,rA,rB):
   print "Not Implemented"
def lwz(rD,drA):
   print "Not Implemented"
def lwzu(rD,drA):
   print "Not Implemented"
def lwzux(rD,rA,rB):
   print "Not Implemented"
def lwzx(rD,rA,rB):
   print "Not Implemented"
def macchw(rD,rA,rB):
   print "Not Implemented"
def macchwdot(rD,rA,rB):
   print "Not Implemented"
def macchwo(rD,rA,rB):
   print "Not Implemented"
def macchwodot(rD,rA,rB):
   print "Not Implemented"
def macchws(rD,rA,rB):
   print "Not Implemented"
def macchwsdot(rD,rA,rB):
   print "Not Implemented"
def macchwso(rD,rA,rB):
   print "Not Implemented"
def macchwsodot(rD,rA,rB):
   print "Not Implemented"
def macchwsu(rD,rA,rB):
   print "Not Implemented"
def macchwu(rD,rA,rB):
   print "Not Implemented"
def machhw(rD,rA,rB):
   print "Not Implemented"
def machhws(rD,rA,rB):
   print "Not Implemented"
def machhwsu(rD,rA,rB):
   print "Not Implemented"
def machhwu(rD,rA,rB):
   print "Not Implemented"
def maclhw(rD,rA,rB):
   print "Not Implemented"
def maclhws(rD,rA,rB):
   print "Not Implemented"
def maclhwsu(rD,rA,rB):
   print "Not Implemented"
def mcrf(crfD,crfS):
   print "Not Implemented"
def mcrxr(crfD):
   print "Not Implemented"
def mfcr(rD):
   print "Not Implemented"
def mfdcr(rD,DCRN):
   print "Not Implemented"
def mfmsr(rD):
   print "Not Implemented"
def mfspr(rD,SPRN):
   print "Not Implemented"
def mftb(rD,TBRN):
   print "Not Implemented"
def mtcrf(CRM,rS):
   print "Not Implemented"
def mtdcr(DCRN,rS):
   print "Not Implemented"
def mtmsr(rS):
   print "Not Implemented"
def mtspr(SPRN,rS):
   print "Not Implemented"
def mulchw(rD,rA,rB):
   print "Not Implemented"
def mulchwu(rD,rA,rB):
   print "Not Implemented"
def mulhhw(rD,rA,rB):
   print "Not Implemented"
def mulhhwu(rD,rA,rB):
   print "Not Implemented"
def mulhw(rD,rA,rB):
   print "Not Implemented"
def mullhw(rD,rA,rB):
   print "Not Implemented"
def mulhwu(rD,rA,rB):
   print "Not Implemented"
def mulli(rD,rA,SIMM):
   print "Not Implemented"
def mullw(rD,rA,rB):
   print "Not Implemented"
def npand(rA,rS,rB):
   print "Not Implemented"
def neg(rD,rA):
   print "Not Implemented"
def nmacchw(rD,rA,rB):
   print "Not Implemented"
def nmacchws(rD,rA,rB):
   print "Not Implemented"
def nmachhw(rD,rA,rB):
   print "Not Implemented"
def nmachhws(rD,rA,rB):
   print "Not Implemented"
def nmaclhw(rD,rA,rB):
   print "Not Implemented"
def nmaclhws(rD,rA,rB):
   print "Not Implemented"
def npor(rA,rS,rB):
   print "Not Implemented"
def por(rA,rS,rB):
   print "Not Implemented"
def porc(rA,rS,rB):
   print "Not Implemented"
def pori(rA,rS,UIMM):
   print "Not Implemented"
def poris(rA,rS,UIMM):
   print "Not Implemented"
def rfci():
   print "Not Implemented"
def rfi():
   print "Not Implemented"
def rlwimi(rA,rS,SH,MB,ME):
   print "Not Implemented"
def rlwinm(rA,rS,SH,MB,ME):
   print "Not Implemented"
def rlwnm(rA,rS,rB,MB,ME):
   print "Not Implemented"
def sc():
   print "Not Implemented"
def slw(rA,rS,rB):
   print "Not Implemented"
def sraw(rA,rS,rB):
   print "Not Implemented"
def srawi(rA,rS,SH):
   print "Not Implemented"
def srw(rA,rS,rB):
   print "Not Implemented"
def stb(params):
   rS = params[0]
   base = params[1].split("(")
   EA =  int(base[0]) + int(registers.gp[base[1].split(")")[0]])
   memory.SRAM[EA] = registers.gp[rS]
   #store in memory
def stbu(rS,drA):
   print "Not Implemented"
def stbux():
   print "Not Implemented"
def stbx():
   print "Not Implemented"
def sth():
   rS = params[0]
   base = params[1].split("(")
   EA =  int(base[0]) + int(registers.gp[base[1].split(")")[0]])
   memory.SRAM[EA] = registers.gp[rS]
def sthbrx():
   print "Not Implemented"
def sthu():
   print "Not Implemented"
def sthux():
   print "Not Implemented"
def sthx():
   print "Not Implemented"
def stmw():
   print "Not Implemented"
def stswi():
   print "Not Implemented"
def stswx():
   print "Not Implemented"
def stw():
   rS = params[0]
   base = params[1].split("(")
   EA =  int(base[0]) + int(registers.gp[base[1].split(")")[0]])
   memory.SRAM[EA] = registers.gp[rS]
def stwbrx():
   print "Not Implemented"
def stwcxdot():
   print "Not Implemented"
def stwu():
   print "Not Implemented"
def stwux():
   print "Not Implemented"
def stwx():
   print "Not Implemented"
def subf():
   print "Not Implemented"
def subfc():
   print "Not Implemented"
def subfe():
   print "Not Implemented"
def subfic():
   print "Not Implemented"
def subfme():
   print "Not Implemented"
def subfze():
   print "Not Implemented"
def sync():
   print "Not Implemented"
def tlbia():
   print "Not Implemented"
def tlbre():
   print "Not Implemented"
def tlbsx():
   print "Not Implemented"
def tlbsync():
   print "Not Implemented"
def tlbwe():
   print "Not Implemented"
def tw():
   print "Not Implemented"
def twi():
   print "Not Implemented"
def wrtee():
   print "Not Implemented"
def wrteei():
   print "Not Implemented"
def xor(params):
   rA = params[0]
   rS = registers.gp[params[1]]
   rB = registers.gp[params[2]]
   registers.gp[rA] = int(rS) ^ int(rB)
def pxori():
   print "Not Implemented"
def xporis():
   print "Not Implemented"

