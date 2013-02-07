import registers
import router
router.instruction['add'](31,2,3)
print registers.gp[0]
print registers.gp[1]
#check out of range
#print registers.gp[32]
