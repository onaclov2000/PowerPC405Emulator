import registers
import router
import memory
import controller
while(1):
   var = raw_input("Enter command: ")
   command = var.split()
   print command
   if (command[0] in router.instruction):
      if (len(command) > 1):
         operand = command[1].split(",")
         router.instruction[command[0]](operand)
      else:
         router.instruction[command[0]]()
      memory.SRAM[controller.pc] = var
      print "===================================================================="
      print "Registers"
      print registers.gp  
      print "===================================================================="
      print "===================================================================="
      print "SRAM"
      print memory.SRAM[0:200]
      print "===================================================================="
   else:
      if (command[0] in router.control):
         if (len(command) > 1):
            operand = command[1].split(",")
            router.control[command[0]](operand)
         else:
            router.control[command[0]]()
      else:
         print "Command does not exist"
   
   
