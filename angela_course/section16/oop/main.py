# import turtle 
# timmy = turtle.Turtle()
# print(timmy)

# from turtle import Turtle, Screen
# my_turtle = Turtle()
# my_screen = Screen()
# print(my_screen.canvwidth, my_screen.canvheight)
# my_turtle.shape("turtle")
# my_turtle.color("darkgray", "green")
# my_turtle.forward(100.0)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = "l"
print(table)

