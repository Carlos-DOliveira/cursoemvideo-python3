''' 021 Faça um programa em Python que abra e reproduza o áudio de um arq MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


# não deu, pq o pygame não instalou