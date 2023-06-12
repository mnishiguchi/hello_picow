from machine import Pin, Timer

timer = Timer()
led = Pin("LED", Pin.OUT)

blink = lambda timer: led.toggle()
timer.init(freq = 1, mode = Timer.PERIODIC, callback = blink)