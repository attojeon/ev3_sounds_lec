#!/usr/bin/env python3
from ev3dev2.led import Leds 
from ev3dev2.sound import Sound  
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.sensor import INPUT_1,INPUT_2, INPUT_3, INPUT_4
import time 

sound = Sound()
song = (
    ('D4', 'e3'),      # intro anacrouse
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),       # meas 1
    ('D5', 'h'),
    ('C5', 'e3'),      # meas 2
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 3
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 4
    ('B4', 'e3'),
    ('C5', 'e3'),
    ('A4', 'h.'),
)

sound.play_song(song)


'''
Sound: play_song

'''
