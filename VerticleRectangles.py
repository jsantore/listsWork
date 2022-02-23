import random

import arcade

def main():
    our_colors = [arcade.color.BLACK, arcade.color.BLUE, arcade.color.GREEN,
                  arcade.color.BOSTON_UNIVERSITY_RED, arcade.color.ORANGE,
                  arcade.color.ALIZARIN_CRIMSON, arcade.color.ARSENIC,
                  arcade.color.ATOMIC_TANGERINE, arcade.color.YELLOW]
    arcade.open_window(700, 700, "Drawing Vertical Rectangles")
    arcade.set_background_color(arcade.color.LAVENDER)
    data_file = open('data.txt', 'r')
    all_lines = data_file.readlines()
    arcade.start_render()
    arcade.draw_text(all_lines[0], 200, 650, arcade.color.ALLOY_ORANGE, 20)
    rest_of_the_lines = all_lines[1:]
    x_loc = 100
    y_loc = 350
    for line in rest_of_the_lines:
        split_line = line.split(':')
        size = int(split_line[1])
        this_color = random.choice(our_colors)
        block = arcade.create_rectangle(x_loc,y_loc,75, size*2,this_color)
        block.draw()
        x_loc = x_loc+75



    arcade.finish_render()
    arcade.run()

main()