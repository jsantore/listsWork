import arcade

def main():
    arcade.open_window(500,500,"Quiz 2 Question")
    arcade.start_render()
    for x_location in range(0,500, 100):
        arcade.draw_line(x_location,0,x_location,500, arcade.color.YELLOW)
    arcade.finish_render()
    arcade.run()


main()