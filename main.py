import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
 
o1, o2, o3 = 4, 17, 27
i1, i2 = 16, 20
GPIO.setup(o1, GPIO.OUT)
GPIO.setup(o2, GPIO.OUT)
GPIO.setup(o3, GPIO.OUT)
GPIO.setup(i1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(i2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def triangle(pin):
  pwm = GPIO.PWM(pin, 100)
  pwm.start(0)
  for dc in range(51):
    pwm.ChangeDutyCycle(2* dc)
    sleep(0.01)
  for dc in reversed(range(50)):
    pwm.ChangeDutyCycle(2*dc)
    sleep(0.01)
  pwm.stop()

GPIO.add_event_detect(i1, GPIO.RISING, callback=triangle(o2), bouncetime=100)
GPIO.add_event_detect(i2, GPIO.RISING, callback=triangle(o3), bouncetime=100)

try:
  while True:
    GPIO.output(o1, 0)
    sleep(0.5)
    GPIO.output(o1, 1)
    sleep(0.5)
except KeyboardInterrupt:
  print("\nExiting")
except Exception as e:
  print("\ne")
GPIO.cleanup()
