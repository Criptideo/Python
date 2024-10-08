#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#para isso vamos usar o módulo pygame

import pygame 
pygame.init() #iniciar o módulo pygame
pygame.mixer.music.load("audio/Explosion Loud Sound Warning Subspace Tripmine Roblox (1).mp3")
pygame.mixer.music.play()
pygame.event.wait()