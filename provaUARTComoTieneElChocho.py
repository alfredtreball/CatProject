import simple_uartClass
from BLE import BLESimplePeripheral
import bluetooth
import time


def main():
    #uart_esp32 = simple_uartClass.UartClass(1, tx_pin=1, rx_pin=3)
    #sender = simple_uartClass.UartClass(1,1,3)
    ble = bluetooth.BLE()
    blueLola = BLESimplePeripheral(ble)
    
    
    def on_rx(rx_data):
            print(rx_data)
            if rx_data == b'start':
                print("start")
                sender.send_command("start")
                
            else:
                sender.send_command("stop")
    
    blueLola.on_write(on_rx)

    while True:
        time.sleep_ms(100)
#         if blueLola.is_connected():
#             #blueLola.on_write(on_rx)
#             #print("Curiosity kill the cat, all well!!!")
#             time.sleep_ms(1000)
#         # Define UART connections for Raspberry Pi and ESP32
#              # UART 1 for ESP32, TX: GPIO1, RX: GPIO3
        


