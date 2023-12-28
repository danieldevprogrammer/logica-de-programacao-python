# Ex. 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3..
# É importante lembrar de instalar a biblioteca pygame pip3 install pygame
import pygame
pygame.init()

pygame.mixer.music.load('#021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
