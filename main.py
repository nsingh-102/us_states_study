import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
all_states = data.state.to_list()
game_is_on = True

answer_state = screen.textinput(title="Guess the State", prompt="Whats another states name?")
answer_state_caps = answer_state.title()

while game_is_on:

    if answer_state_caps in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        user_state_info = data[data.state == answer_state_caps]
        user_state_x = int(user_state_info.x)
        user_state_y = int(user_state_info.y)
        t.goto(user_state_x, user_state_y)
        t.write(answer_state_caps)
        if not answer_state_caps in guessed_states:
            guessed_states.append(answer_state_caps)

    if len(guessed_states) == 50:
        game_is_on = False
        g = turtle.Turtle()
        g.penup()
        g.hideturtle()
        g.write("You guessed all the states. You Win", align="center", font=("Arial", 24, "normal"))
        break

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another states name?")
    answer_state_caps = answer_state.title()

    if answer_state_caps == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_missed.csv")
        break



#you can also do data.state.to_list() to make it into a list