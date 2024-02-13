from machine import Pin
import time
from rpi_motors import Car




class IR(object):
    def __init__(self, ir1, ir2,ir3):
        self.ir1 = Pin(ir1,Pin.IN,0)
        self.ir2 = Pin(ir2,Pin.IN,0)
        self.ir3 = Pin(ir3,Pin.IN,0)
        
    def update(self,ir1,ir2,ir3):
        self.ir1 = Pin(ir1,Pin.IN,0)
        self.ir2 = Pin(ir2,Pin.IN,0)
        self.ir3 = Pin(ir3,Pin.IN,0)
        
        
    
if __name__ == "__main__":
    ir = IR(4,5,6)
    car = Car()
    while(True):
        print("IR1: ", ir.ir1.value())
        print("IR2: ", ir.ir2.value())
        print("IR3: ", ir.ir3.value()) #cuando IR3 es 1 y loshay que girar derecha
        time.sleep_ms(100)
        ir.update(4,5,6)
        
        if ir.ir3.value() == 1:
            if ir.ir1.value() == 1:
                # IR3 y IR1 es 1, palante
                print("Palante")
                car.move(25)
            else:
                # solo IR3 es 1, derecha
                print("Derecha")
                car.stop()
                car.move_side_coke(40)
        else:
            if ir.ir1.value() == 1:
                if ir.ir2.value() == 1:
                    # IR1 y IR2 es 1, izquierda
                    print("Izquierda")
                    car.stop()
                    car.move_side_coke(-40)
                else:
                    # solo IR1 es 1, izquierda
                    print("Izquierda")
                    car.stop()
                    car.move_side_coke(-40)
            else:
                # todos 0, palante
                print("Palante")
                car.move(25)


        
            
        
        
            
        

    
    

