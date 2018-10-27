import RPi.GPIO as G
import time

LedPin = 4 #pin4 for the LED
CapacitivePin = 18 #pin18 for he capacitive touch

def setup():
    G.setmode(G.BCM)
    G.setup(CapacitivePin, G.IN)
    G.setup(LedPin, G.OUT, initial=G.LOW)
    
    
def blink():
    while True:
        
        if G.input(CapacitivePin) == G.HIGH:
            G.output(LedPin, True)
        else:
            G.output(LedPin, False)
    
        #Sketch for just blink the LED
        #G.output(LedPin, G.HIGH)
        #time.sleep(1)
        #G.output(LedPin, G.LOW)
        #time.sleep(1)
        
def destroy():
    G.output(LedPin, G.LOW)
    G.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
        