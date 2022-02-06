import turtle
import turtle as t
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)

dict = []

for i in all_state:
    if i in guessed_states:
        continue
    else:
        dict.append(i)

new_data = pd.DataFrame(dict)
new_data.to_csv("states_to_learn.csv")