import random
from tkinter import Tk, Label, Entry, StringVar

# Initialize main window
window = Tk()
window.title("Probability Switch Test")
window.geometry("400x110")
window.resizable(False, False)

# StringVars to hold win counts
kept_win_count = StringVar(value="0")
switched_win_count = StringVar(value="0")

# Entry field for number of simulations
simulation_input = Entry(window)

# Labels for display
Label(window, text="Wins (Kept Original Choice):").place(x=30, y=10)
Label(window, textvariable=kept_win_count, font=("Arial", 12)).place(x=220, y=10)

Label(window, text="Wins (Switched Choice):").place(x=30, y=40)
Label(window, textvariable=switched_win_count, font=("Arial", 12)).place(x=220, y=40)

Label(window, text="Number of Simulations:").place(x=30, y=75)
simulation_input.place(x=190, y=75)


def simulate_monty_hall(event):
    original_wins = 0
    switch_wins = 0

    try:
        num_trials = int(simulation_input.get())
    except ValueError:
        kept_win_count.set("Invalid")
        switched_win_count.set("Input")
        return

    for _ in range(num_trials):
        # Prize is behind one of the 3 doors
        prize_door = random.randint(0, 2)
        player_initial_choice = random.randint(0, 2)

        # Host opens a door that's not the prize and not the player's choice
        possible_doors_to_open = [
            door for door in range(3)
            if door != prize_door and door != player_initial_choice
        ]
        host_reveals = random.choice(possible_doors_to_open)

        # Player switches to the remaining unopened door
        final_choice = [
            door for door in range(3)
            if door != player_initial_choice and door != host_reveals
        ][0]

        if player_initial_choice == prize_door:
            original_wins += 1
        elif final_choice == prize_door:
            switch_wins += 1

    # Update result labels
    kept_win_count.set(str(original_wins))
    switched_win_count.set(str(switch_wins))


# Bind Enter key to trigger simulation
simulation_input.bind("<Return>", simulate_monty_hall)
window.mainloop()
