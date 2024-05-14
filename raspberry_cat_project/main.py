from machine import Pin, SoftI2C, UART
import time
from rpi_motors import Car
from ultrasonic import UltrasonicSensor
import simple_uartClass 
import rpi_lcd1602
import json


class IR(object):
    
    def __init__(self, ir1, ir2,ir3):
        
        self.ir1 = Pin(ir1,Pin.IN,0)
        self.ir2 = Pin(ir2,Pin.IN,0)
        self.ir3 = Pin(ir3,Pin.IN,0)
        
    def update(self,ir1,ir2,ir3):
        
        self.ir1 = Pin(ir1,Pin.IN,0)
        self.ir2 = Pin(ir2,Pin.IN,0)
        self.ir3 = Pin(ir3,Pin.IN,0)

def run():
    
    #if(receiver.is_stop() == True):
     #   print("stop")
      #  return
    ir = IR(4, 5, 6)
    car = Car()
    #car.stop()
    ultrasonic = UltrasonicSensor(3, 2)
                    
            
    print("distance244: ", ultrasonic.distance())    
         
    if ultrasonic.distance() <= 10:   
        print("distance2: ", ultrasonic.distance())
        car.stop()
        time.sleep(1)
        car.move_side_capitan_salami(40)
        time.sleep(0.5)
        car.stop()
        time.sleep(1)
        car.move(27)
        time.sleep(1.5)
        car.stop()
        time.sleep(1)
        while(ir.ir3.value() != 0):
            car.move_side_capitan_salami(-25)
        
    else:
        
        print("IR1: ", ir.ir1.value())
        print("IR2: ", ir.ir2.value())
        print("IR3: ", ir.ir3.value()) #cuando IR3 es 1 y loshay que girar derecha
        #time.sleep_ms(100)
        #ir.update(4,5,6)
        
        if ir.ir3.value() == 1:
            if ir.ir1.value() == 1:
                # IR3 y IR1 es 1, palante
                print("Palante")
                car.move(30)
            else:
                # solo IR3 es 1, derecha
                print("Derecha")
                car.stop()
                car.move_side_coke(30)
        else:
            if ir.ir1.value() == 1:
                if ir.ir2.value() == 1:
                    # IR1 y IR2 es 1, izquierda
                    print("Izquierda")
                    car.stop()
                    car.move_side_coke(-30)
                else:
                    # solo IR1 es 1, izquierda
                    print("Izquierda")
                    car.stop()
                    car.move_side_coke(-30)
            else:
                # todos 0, palante
                print("Palante")
                car.move(30)
        
# def run():
#     if ir.ir1.value() == 0 and ir.ir2.value() == 0 and ir.ir3.value() == 0:
#         if ultrasonic.distance() <= 10:
#             print("distance2: ", ultrasonic.distance())
#             car.stop()
#             time.sleep(1)
#             car.move_side_capitan_salami(40)
#             time.sleep(0.5)
#             car.stop()
#             time.sleep(1)
#             car.move(25)
#             time.sleep(1.7)
#             car.stop()
#             time.sleep(1)
#             while(ir.ir3.value() != 0):
#                 car.move_side_capitan_salami(-27)
#                 time.sleep(1)
#                 car.move_side_coke(-27)
#                 time.sleep(0.5)
#         else:
#             print("IR1: ", ir.ir1.value())
#             print("IR2: ", ir.ir2.value())
#             print("IR3: ", ir.ir3.value()) 
#             
#             if ir.ir3.value() == 1:
#                 if ir.ir1.value() == 1:
#                     print("Palante")
#                     car.move(25)
#                 else:
#                     print("Derecha")
#                     car.stop()
#                     car.move_side_coke(25)
#             else:
#                 if ir.ir1.value() == 1:
#                     if ir.ir2.value() == 1:
#                         print("Izquierda")
#                         car.stop()
#                         car.move_side_coke(-25)
#                     else:
#                         print("Izquierda")
#                         car.stop()
#                         car.move_side_coke(-25)
#                 else:
#                     print("Palante")
#                     car.move(25)
#     else:
#         car.stop()
    
def start():
    ir = IR(4, 5, 6)
    car = Car()
    #car.stop()
    ultrasonic = UltrasonicSensor(3, 2)
    uart = UART(0, baudrate=115200)
    
    print("sensors")
    
    lcd = rpi_lcd1602.LCD(SoftI2C(sda=Pin(20), scl=Pin(21)))
    lcd.clear()
    lcd.puts("Bye", 1, 0)
    car.stop()
    while True:
        
        if uart.any():
            line = uart.readline()
            obj = json.loads(line)
            if 'command' in obj:
                if obj['command'] == 'start':
                    print("start")
                    while True:
                        if uart.any():
                            line = uart.readline()
                            obj = json.loads(line)
                            if 'command' in obj:
                                if obj['command'] == 'stop':
                                    print("stop")
                                    car.stop()
                                    break
                        run()
                
                
        time.sleep_ms(50)
