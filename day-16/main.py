# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('cyan')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable, MARKDOWN
table = PrettyTable()
table.set_style(MARKDOWN)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)