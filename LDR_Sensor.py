import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LDR_PIN = 27

def setup_ldr_pin():
  GPIO.setup(LDR_PIN,GPIO.IN)

def read_ldr_intensity():
  ldr_value = GPIO.input(LDR_PIN)
  return ldr_value

def calculate_light_intensity(ldr_value):

  if ldr_value < 1:
    return "Very Bright"
  else:
    return "Low"

def main():
  try:
    setup_ldr_pin()

    while True:
      ldr_intensity = read_ldr_intensity()
      intensity_level = calculate_light_intensity(ldr_intensity)
      print("LDR Intensity ",ldr_intensity)
      print("Intensity Level ",intensity_level)

      if ldr_intensity == GPIO.LOW:
        print("Light is On : High")
      else:
        print("Light is Off : Low")
        time.sleep(1)
  except KeyboardInterrupt:
    GPIO.cleanup()
if __name__ == "__main__":
  main()