import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup([8,10,12,16], gpio.OUT, initial=gpio.LOW)
gpio.setup([11,13,15,29,31,33,35,37], gpio.IN, pull_up_down = gpio.PUD_DOWN)

def atuar1(peca):
    if peca[0:2] == True and peca[3] == False:
        print("Peca grande nao metalica")
        time.sleep(0.5)
        gpio.output(8,gpio.HIGH)
        gpio.wait_for_edge(33, gpio.RISING)
        gpio.output(8, gpio.LOW)

   ''' elif peca[0] == True and peca[3] == True and peca[1] == False:
        print("Peca pequena metalica")
        time.sleep(1)
        gpio.output(10,gpio.HIGH)
        gpio.wait_for_edge(35, gpio.RISING)
        gpio.output(10, gpio.LOW)
    
    elif peca[0,1] == True and peca[3] == False and peca[2] == False:
        print("Peca media metalica")
        time.sleep(1.5)
        gpio.output([12,16],[gpio.HIGH,gpio.LOW])
        gpio.wait_for_edge(37, gpio.RISING)
        gpio.output([12,16], [gpio.LOW,gpio.HIGH])'''

    else:
        print('Peca nao selecionada')



while True:
    f1 = False
    f2 = False
    f3 = False
    i1 = False
    c1 = False
    if gpio.input(11) == 1:
        f1 = True
    if gpio.input(13) == 1:
        f2 = True
    if gpio.input(15) == 1:
        f3 = True
    if gpio.input(29) == 1:
        i1 = True
    if gpio.input(31) == 1:
        c1 = True
    
  
    peca = [f1, f2, f3, i1, c1]
  
    if peca[4] == True:

      atuar1(peca)

    peca = 0
    
