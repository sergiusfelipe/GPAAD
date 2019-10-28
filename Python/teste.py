import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup([8,10,12,16], gpio.OUT, initial=gpio.LOW)
gpio.setup([11,13,15,29,31,33,35,37], gpio.IN, pull_up_down = gpio.PUD_DOWN)

def atuar1(peca):
    if peca[0,2] == True && peca[3] == False:
        print("Peca grande nao metalica")
        time.sleep(0.5)
        gpio.output(8,gpio.HIGH)
        gpio.wait_for_edge(33, gpio.RISING)
        gpio.output(8, gpio.LOW)

    elif peca[0] == True && peca[3] == True && peca[1] == False:
        print("Peca pequena metalica")
        time.sleep(1)
        gpio.output(10,gpio.HIGH)
        gpio.wait_for_edge(35, gpio.RISING)
        gpio.output(10, gpio.LOW)
    
    elif peça[0,1] == True && peca[3] == False && peca[2] == False:
        print("Peca media metalica")
        time.sleep(1.5)
        gpio.output([12,16],[gpio.HIGH,gpio.LOW])
        gpio.wait_for_edge(37, gpio.RISING)
        gpio.output([12,16], [gpio.LOW,gpio.HIGH])

    else:
        print('Peca nao selecionada')



while True:
    try:
        print("Iniciando...")
    if gpio.input(11) == 1:
        so1 = True
    else:
        so1 = False
    if gpio.input(13) == 1:
        so2 = True
    else:
        so2 = False
    if gpio.input(15) == 1:
        so3 = True
    else:
        so3 = False
    if gpio.input(29) == 1:
        si = True
    else:
        si = False
    if gpio.input(31) == 1:
        sc = True
    else:
        sc = False
    
  
    peca = [so1, so2, so3, si, sc]
  
    if peca[4] == True:

      atuar1(peça)

    peca = 0

    except (KeyboardInterrupt):
		    print “Saindo...”
		    gpio.cleanup()
		    exit()
    
