import pygame as pg
from sys import exit
pg.init()
screen = pg.display.set_mode((1000,800))
pg.display.set_caption('Pong Game')
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit() #for exiting game
            exit() #for exiting loop similar to break
    pg.display.update()
