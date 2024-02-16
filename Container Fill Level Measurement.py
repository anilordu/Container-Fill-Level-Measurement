import drivers
import RPi.GPIO as GPIO
import time
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 18
ECHO = 17
buzzerPin = 4
button = Button(15)
display = drivers.Lcd()

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)

buzzTime = 0.5
buzzDelay = 2
derinlik = 0

while True:
    if button.is_pressed:
        GPIO.output(TRIG, False)
        print ("Derinlik Olculuyor...")
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            derinlik = pulse_duration * 17150 - 0.5
            derinlik = round(derinlik, 2)
            
        display.lcd_display_string ("Derinlik", 1)
        display.lcd_display_string ("{}cm".format(derinlik), 2)
        sleep(2)
        display.lcd_clear()
        sleep(2)
    
    else:
        display.lcd_display_string (" Derinlik Olcumu", 1)
        display.lcd_display_string ("  BUTONA BASIN", 2)
        sleep(2)
        display.lcd_clear()
        sleep(2)
        
        
    while derinlik != 0:
        GPIO.output(TRIG, False)
        print ("Olculuyor...")
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            bos_alan = pulse_duration * 17150 - 0.5
            bos_alan = round(bos_alan, 2)
            dolu_alan = derinlik - bos_alan
        
        if dolu_alan <= derinlik:
            oran = dolu_alan * 100 / derinlik
            oran = round(oran, 2)
            
            if oran < 2:
                oran = 0
            
            if oran > 75:
                GPIO.output(buzzerPin, True)
                sleep(buzzTime)
            
            display.lcd_display_string ("Doluluk Orani", 1)
            display.lcd_display_string ("%{}".format(oran), 2)
            sleep(2)
            GPIO.output(buzzerPin, False)
            sleep(buzzTime)
            display.lcd_clear()
            sleep(2)
            
        if button.is_pressed:
            break 