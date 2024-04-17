import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

sound_pin = 18
led_pin = 17
GPIO.setup(sound_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

clap_count = 0
def main():
  global clap_count
  try:
    while True:
      if GPIO.input(sound_pin):
        clap_count +=1
        print("Clap Detected ! Count: ",clap_count)
        if clap_count % 2 == 1:
          GPIO.output(led_pin,GPIO.HIGH)
          print("LED ON")
        else:
          GPIO.output(led_pin,GPIO.LOW)
          print("LED OFF")
        time.sleep(1)
  except KeyboardInterrupt:
    GPIO.cleanup()

if __name__ == "__main__":
  main()