import logging



class ColorDual:
    def __init__(self, config):
        self.printer = config.get_printer()
        gcode.register_command("T0", self.t0, desc="Swap to T0")
        gcode.register_command("T1", self.t1, desc="Swap to T1")
        
        
    
    def debugger(self, gcmd, msg):
      gcmd.respond_info(msg)
    
    def t0(self, gcmd):
        self.debugger(gcmd, "t0 choosen")
        print(self.objects)
    
    def t1(self, gcmd):
        self.debugger(gcmd, "t1 choosen")


    def _handle_ready(self):
       pass

       
       
def load_config(config):
   return ColorDual(config)