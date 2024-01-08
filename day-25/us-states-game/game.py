import pandas
import turtle


class Game:
    def __init__(self):
        self.states = pandas.read_csv("50_states.csv")
        self.guessed_states = []
        self.score = 0
        self.title = "Guess the state"
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        image = "blank_states_img.gif"
        self.screen.addshape(image)
        self.turtle = turtle.Turtle()
        self.turtle.shape(image)

    def increase_score(self):
        self.score += 1
        self.title = f"{self.score}/50 States"
        self.screen.title(self.title)

    def check_answer(self, answer):
        # Check if guess in 50 states
        match = self.states[self.states["state"] == answer]
        if not match.empty and match.state.item() not in self.guessed_states:
            # Write correct guesses onto map
            self.write_state(match)
            # Record correct guesses in a list
            self.guessed_states.append(match.state.item())
            # Keep track of score
            self.increase_score()
            self.screen.title("POTATO")

    def save_states_to_learn(self):
        missing_states = []
        for state in self.states.state.to_list():
            if state not in self.guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")

    def ask(self):
        answer_state = self.screen.textinput(title=self.title,
                                             prompt="What's another state's name?").title()
        if answer_state == 'Exit':
            self.save_states_to_learn()
            turtle.bye()
        self.check_answer(answer_state)

    @staticmethod
    def write_state(state):
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state.x), int(state.y))
        new_turtle.write(state.state.item())
