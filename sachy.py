import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
arcade.finish_render()
arcade.run()