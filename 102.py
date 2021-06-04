#!/usr/bin/env python3
from ev3dev2.led import Leds 
from ev3dev2.sound import Sound  
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.sensor import INPUT_1,INPUT_2, INPUT_3, INPUT_4
import time 


sound = Sound()
sound.play_file('/home/robot/sounds/Activate.wav')

# 폴더의 파일목록 가져오는 방법
import glob 
wav_files = glob.glob('/home/robot/sounds/*.wav')
print(wav_files)

for w in wav_files:
    sound.play_file(w)
    time.sleep(0.5)


'''
Sound: sound.play_file()

'''
