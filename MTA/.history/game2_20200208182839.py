import pygame as pg
import random as r

pg.init()
pg.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (54,198,83)
blue = (30,144,255)

screen caption = "snake2"
screen_widgth = 1000
screen_height = 500
box_width = 990
box_height = 400
snake_x = 100
snake_y = 150
food_x = r.randint(0,box_width)
food_y = r.randint(0,box_height)



