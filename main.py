import tkinter as tk
from tkinter import *
from fractions import Fraction
import math

#git test 2 lol

def retrieve_input():
    global userInput, userInput2, userInput3
    userInput = (entry1.get())
    userInput2 = int(entry2.get())
    userInput3 = int(entry3.get())

    try:
        userInput = eval(userInput)
    except (NameError, SyntaxError):
        print("Invalid input for Input 1!")
        return

    p = userInput
    n = userInput2
    x = userInput3
    result = calculate_binomial_probability(p, n, x)
    result = (1000 * result) / 10
    result = round(result, 5)
    binomialResult.config(text=str(result) + "% is the exact chance of this happening!")

    # calculate the probability of getting <=x drops
    or_fewer_probability = sum(calculate_binomial_probability(p, n, i) for i in range(x + 1))
    or_fewer_probability = (1000 * or_fewer_probability) / 10
    or_fewer_probability = round(or_fewer_probability, 5)
    orFewerResult.config(text=str(or_fewer_probability) + "% is the chance of getting " + str(x) + " or fewer drops!")

    # calculate the chance of getting more than a certain number of drops
    more_than_probability = 100 - or_fewer_probability
    more_than_probability = round(more_than_probability, 5)
    moreThanResult.config(text=str(more_than_probability) + "% is the chance of getting more than " + str(x) + " drops!")

def calculate_binomial_probability(p, n, x):
    binomial_coefficient = math.comb(n, x)
    probability = binomial_coefficient * (p ** x) * ((1 - p) ** (n - x))
    return probability

root = tk.Tk()
root.geometry("400x300")
root.title("frewp's dry calculator")

message_label = tk.Label(root, text="Dry Calculator")
message_label.pack()

empty_space_frame = tk.Frame(root, height=10)
empty_space_frame.pack()

label1 = tk.Label(root, text="Probability (1/x):")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Attempts at drop:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Drops:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

button = tk.Button(root, text="Submit", command=retrieve_input)
button.pack()

empty_space_frame = tk.Frame(root, height=10)
empty_space_frame.pack()

results_label = tk.Label(root, text="Results:")
results_label.pack()

binomialResult = tk.Label(root)
binomialResult.pack()

orFewerResult = tk.Label(root)
orFewerResult.pack()

moreThanResult = tk.Label(root)
moreThanResult.pack()

root.mainloop()