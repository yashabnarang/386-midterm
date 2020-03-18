import pygame as pg


# Vector Class
class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __rmul__(self, k: float):
        return Vector(k * self.x, k * self.y)

    def __mul__(self, k: float):
        return self.__rmul__(k)

    def __truediv__(self, k: float):
        return self.__rmul__(1.0 / k)

    def __neg__(self):
        self.x *= -1
        self.y *= -1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def test():  # feel free to change the test code
        v = Vector(x=5, y=5)
        u = Vector(x=4, y=4)
        print('v is {}'.format(v))
        print('u is {}'.format(u))
        print('u plus v is {}'.format(u + v))
        print('u minus v is {}'.format(u - v))
        print('ku is {}'.format(3 * u))
        print('-u is {}'.format(-1 * u))


# Class Ship
class Ship:
    def __init__(self, game, vector=Vector()):
        self.game = game
        self.surface = game.screen
        self.velocity = vector
        self.surface_rect = game.screen.get_rect()
        self.image = pg.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.lasers = pg.sprite.Group()

    def center_ship(self):  # Use this at the start of the game to center
        self.rect.midbottom = self.surface_rect.midbottom

    def fire(self):
        # self.lasers.fire()
        pass

    def remove_lasers(self):
        self.lasers.remove()

    def move(self):
        r, v = self.rect, self.velocity
        if v == Vector():
            return
        r.left += v.x
        r.top += v.y
        self.game.limit_on_screen(r)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()


def main():
    Vector.test()
