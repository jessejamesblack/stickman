from tkinter import *
import random
import time


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [
            PhotoImage(file="figure-L1.gif"),
            PhotoImage(file="figure-L2.gif"),
            PhotoImage(file="figure-L3.gif")
        ]
        self.images_right = [
            PhotoImage(file="figure-R1.gif"),
            PhotoImage(file="figure-R2.gif"),
            PhotoImage(file="figure-R3.gif")
        ]
        self.image = game.canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2


class PlateformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co2.x1 < co1.x1 < co2.x2) \
            or (co2.x1 < co1.x2 < co2.x2) \
            or (co1.x1 < co2.x1 < co1.x2) \
            or (co1.x1 < co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co2.y1 < co1.y1 < co2.y2) \
            or (co2.y1 < co1.y2 < co2.y2) \
            or (co1.y1 < co2.y1 < co1.y2) \
            or (co1.y1 < co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x2 >= co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 >= co2.x2:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co1.y1 >= co2.y2 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:
            return True
    return False


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Stickman race for the exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="background.gif")
        # self.bg2 = PhotoImage(file+"background2.gif")
        w = self.bg.width()
        h = self.bg.height()
        draw_background = 0
        for x in range(0, 5):
            for y in range(0, 5):
                if draw_background == 1:
                    self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
                    draw_background = 0
                else:
                    # self.canvas.create_image(x * w, y * h, image=self.bg2, anchor='nw')
                    draw_background = 1
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
platform1 = PlateformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10)
platform2 = PlateformSprite(g, PhotoImage(file="platform1.gif"), 150, 440, 100, 10)
platform3 = PlateformSprite(g, PhotoImage(file="platform1.gif"), 300, 400, 100, 10)
platform4 = PlateformSprite(g, PhotoImage(file="platform1.gif"), 300, 160, 100, 10)
platform5 = PlateformSprite(g, PhotoImage(file="platform2.gif"), 175, 350, 66, 10)
platform6 = PlateformSprite(g, PhotoImage(file="platform2.gif"), 50, 300, 66, 10)
platform7 = PlateformSprite(g, PhotoImage(file="platform2.gif"), 170, 120, 66, 10)
platform8 = PlateformSprite(g, PhotoImage(file="platform2.gif"), 45, 60, 66, 10)
platform9 = PlateformSprite(g, PhotoImage(file="platform3.gif"), 170, 250, 32, 10)
platform10 = PlateformSprite(g, PhotoImage(file="platform3.gif"), 230, 200, 32, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)

g.mainloop()
