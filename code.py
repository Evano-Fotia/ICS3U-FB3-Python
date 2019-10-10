#!/usr/bin/env python3

# Created by Evano Fotia
# Created on Sept 2019
# Pibadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

sprites = []


def main():
    # this function sets the background
    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    alien = stage.sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)
    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    if keys & ugame.K_X:
        # print("A")
        pass
    if keys & ugame.K_O:
        # print("B")
        pass
    if keys & ugame.K_start:
        # print("k_start")
        pass
    if keys & ugame.K_start:
        # print("K_start")
        pass
    if keys & ugame.K_Right:
        ship.move(ship.x - 1, ship.y)
        pass
    if keys & ugame.K_left:
        ship.move(ship.x - 1, ship.y)
        pass
    if keys & ugame.K_Up:
        ship.move(ship.x, ship.y + 1)
        pass

    game.reader_sprites(sprites)
    game.tick() wait until refresh rate finishes

    if __name__ == "__main__":
        main()
