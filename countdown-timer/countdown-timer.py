import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
print("Welcome to Countdown Timer")
print("Enter the time:-")

hours = int(input("Enter hours : "))
minutes = int(input("Enter minutes : "))
seconds = int(input("Enter seconds : "))

total_time = hours * 3600 + minutes * 60 + seconds
pygame.mixer.music.play(loops=-1)
time.sleep(total_time)

print("TIME'S UP!")
pygame.mixer.music.stop()

sound = pygame.mixer.Sound("audio2.mp3")
sound.play(loops=-1)
print("Press CTRL + C to Stop")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTimer stopped.")
    sound.stop()
    pygame.mixer.quit()
