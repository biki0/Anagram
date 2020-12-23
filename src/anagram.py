# Bikash Khatiwoda

import random
import tkinter as tk

# class for user input
class User_Words:

    def __init__(self, user_input=""):
        self.u = user_input
        self.u = input("Enter a word to find its anagram or q to quit: ")

    def get_input(self): # returning user's input
        return self.u

# class for randomly picking a word from the file
class Random_Word:
    def __init__(self):
        self.rand_line = "..." # default value

    def get_word(self):
        return self.rand_line # returning rand_line

    def roll(self):
        my_file = open("words.txt").read().splitlines()  # puts all the words in a list
        self.rand_line = random.choice(my_file)  # picks a random word from the list

# class for GUI
class GUI:
    def __init__(self):
        main_window = tk.Tk()
        main_window.geometry("500x300") # size of the window
        main_window.title("Random Word")# title
        main_window.configure(background="black") # background color of the window
        self.rand_word = Random_Word() # calling our Word class
        self.label1 = tk.Label(main_window, text=self.rand_word.get_word(), width=20, bg="black", fg="white")
        self.label1.pack()

        # button when clicked on will randomly show a word
        but1 = tk.Button(main_window, text="roll", width=6, command=self.button_pressed) # calling button pressed function
        but1.pack()

        main_window.mainloop()

    # function that is a command for button
    def button_pressed(self):
        self.rand_word.roll() # calling roll function from Random Word class
        self.label1.config(text=self.rand_word.get_word()) # connecting label to get word which returns a word

def dictionary(file):

    # sorting each line of the file
    # looking through each line in file
    for x in file:
        # finding what letters are in by stripping
        x = x.strip()

        # sorting in alphabetical order and joins which returns a string
        i = "".join(sorted(x))

        # adding each line to the dictionary by its key
        if i in dic:  # if it is in dic
            g = dic.get(i)  # getting i from dic
            dic[i] = x + ", " + g  # adding to dic as value
        else:
            dic[i] = x  # if i is not in dic then x is value

    return dic # returning dic

# returns list of anagrams of word user inputted from the dictionary
def getting_anagram(y):

    # sorting y (y is user input) in alphabetical order and joining it together
    i = "".join(sorted(y))
    x = dictionary(file) # calling dictionary function
    val = x.get(i) # getting i (i is users input) from the dictionary, getting value of i
    return val # returning val

# this function saves the inputs of user's
# a method that takes an object of a class as a parameter
def saving(word_of_user):
    saving_inputs = []
    saving_inputs.append(word_of_user.get_input()) # a list of object that saves user's input

    return saving_inputs

# this function will loop
def loop(word_of_user):

    while word_of_user.get_input() != "q": # keeps on looping till user inputs q

        print("Anagram for " + "(" + word_of_user.get_input().upper() + ")" + " are: ")
        r = getting_anagram(word_of_user.get_input()) # calling getting anagram function
        print(r) # printing getting anagram function
        print("\n")

        # asking user again on what they want to do
        # calling user input class
        word_of_user = User_Words()
        saving_inputs.append(word_of_user.get_input()) # list of object that saves user's input
        together = l + saving_inputs # joining the first and other words user entered
        together.sort() # sorting entered word

        new_file = open("anagram_words.txt", "w")  # creating a new file
        new_file.write(str(together) + "\n")  # writing the list of word user entered to the file
        new_file.close() # closing file

        # if user input q then following will happen
        if word_of_user.get_input() == "q":
            print("You quit")
            new_file2 = open("anagram_words.txt", "r") # opening file for reading
            ls1 = new_file2.readline() # reading what is on the file

            print("Here are all of your inputs: " + str(ls1)) # printing the entered words that was saved in the file

dic = {} # creating a dictionary
file = open("words.txt", "r") # opening words file
file.readline() # reading each line in file

# calling User Word class (user input)
word_of_user = User_Words()
l = saving(word_of_user) # calling saving function
saving_inputs = [] # creating list to save inputs

calling_loop = loop(word_of_user) # calling loop function


# calling GUI class
# opens a window that has a button, pressing the button will show random words
# words are from the file
my_gui = GUI()
print(my_gui)

