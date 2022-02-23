import random

import arcade


def main():
    our_colors = [arcade.color.LAVENDER, arcade.color.BLUE, arcade.color.GREEN,
                  arcade.color.BOSTON_UNIVERSITY_RED, arcade.color.ORANGE,
                  arcade.color.ALIZARIN_CRIMSON, arcade.color.ARSENIC,
                  arcade.color.ATOMIC_TANGERINE, arcade.color.YELLOW]
    arcade.open_window(800, 800, "bringing together the last few weeks")
    rectangleFile = open("recfile.txt", 'r')
    all_lines = rectangleFile.readlines()
    arcade.start_render()
    for line in all_lines:
        rec_data = line.split(",")
        center_x = int(rec_data[0])
        center_y= int(rec_data[1])
        width=int(rec_data[2])
        height=int(rec_data[3])
        color = random.choice(our_colors)
        rectangle=arcade.create_rectangle(center_x,center_y,width,height, color)
        rectangle.draw()

    arcade.finish_render()
    arcade.run()


main()
