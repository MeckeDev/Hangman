# importing needed Frameworks
import eel


# initializing EEL 
eel.init('ui')


class Game:


    # initialsing the Game-Variables
    def __init__(self):

        self.is_running = False     # to check if the Game is running or not
        self.word = ""              # setting the Word (default= Empty) like: "secret"
        self.hint = ""              # used to show the Word with * like: s*cr*t
        self.letters = ""           # list of all used Letters like: ['s','c', 'r', 't', 'o', 'z']
        self.guessed = []           # Array of guessed Word like: ['s', '*', 'c', 'r', '*', 't']
        self.mistakes = 0           # counts the wrong guessed Letters
        self.score = 0              # will be calculated based on speed and wrong guesses


    # starting the Game
    def start(self):
        self.is_running = True


    # stopping the Game
    def stop(self):
        self.is_running = False


    # Guessing a Letter
    def guess(self, letter):

        # if the Letter is not in the Word add 1 to the mistakes
        if letter not in self.word.lower():
            self.mistakes += 1

        # checking each Letter in the Word if it's the guessed Letter
        for i in range(len(self.word)):

            if self.word[i].lower() == letter.lower():
                self.guessed[i] = letter.lower()

        # clearing the Hint
        self.hint = ""

        # filling the Hint with all guessed Letters
        for i in self.guessed:
            self.hint += i

        if '*' not in self.guessed:
            self.stop()


    # setting the Word
    def set_word(self, word):

        self.word = word

        # creating an Array with * for each Letter
        for i in self.word:
            self.guessed.append('*')

# just some Lines of testing Stuff
# ##### #
g = Game()
g.set_word("Test")
g.guess("e")
g.guess("s")
g.guess('t')

print(g.is_running)
# ##### #

# starting EEL
eel.start('index.html')