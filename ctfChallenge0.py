from random import choice
alphabet = "abcdefghijklmnopqrstuvwxyz"

class Cipher:
    """
    A class defining a letter-wise cipher.
    Has a member variable for each letter, each variable should be a
    replacement string.
    Can handle multi-letter replacements, eg self.a = aaaa
    """
    def __init__(self):
        """
        Initialize all of the letters to be no-op replacements.
        """
        self.a = "a"
        self.b = "b"
        self.c = "c"
        self.d = "d"
        self.e = "e"
        self.f = "f"
        self.g = "g"
        self.h = "h"
        self.i = "i"
        self.j = "j"
        self.k = "k"
        self.l = "l"
        self.m = "m"
        self.n = "n"
        self.o = "o"
        self.p = "p"
        self.q = "q"
        self.r = "r"
        self.s = "s"
        self.t = "t"
        self.u = "u"
        self.v = "v"
        self.w = "w"
        self.x = "x"
        self.y = "y"
        self.z = "z"
        # I wanted to use self's builtin __dict__ for this too, but apparently
        # you can't write directly to it. I wonder why that might be...
        #self.__dict__ = alphaDict

    def encode(self, string):
        """
        Encode the input string.
        """
        out = ""
        string = string.lower()
        for letter in string:
            # This if check lets us avoid having members
            # for numbers, spaces, or other special cases.
            if letter in self.__dict__:
                out += self.__dict__[letter]
            else:
                out += letter
        return out

    def __str__(self):
        """
        Shows the encoded alphabet
        """
        return self.encode(alphabet)

    def set(self, letter, string):
        """
        Sets the letter to string.
        """
        self.__dict__[letter] = string

    def get(self, letter):
        """
        Gets the string mapped to letter
        """
        return self.__dict__[letter]

def test():
    """
    A simple test to show how Ciphers can be used.
    """
    double = Cipher()
    for letter in alphabet:
        double.set(letter, letter*2)
    print double.encode("hello world")

    internet = Cipher()
    internet.set("a", "4")
    internet.set("i", "1")
    internet.set("e", "3")
    internet.set("l", "w")
    internet.set("s", "z")
    print internet.encode("hello world")

#test()

def guessing_game():
    """
    The main function.
    You have to configure a guess to match my random cipher.
    """
    guess = Cipher()
    while (True):
        letter = raw_input("\nWhat letter would you like to set? ")
        value = raw_input("What would you like to replace it with? ")

        # We want to let users to be able to do things like "5"*37, or "\n"
        # but we don't want anything nasty getting in that eval statement
        filtered_value = ""
        for val in value:
            if val not in "{}();#=":
                filtered_value += val
        try:
            final_value = eval(filtered_value)
        except:
            # If that doesn't work, just default to raw string
            final_value = filtered_value

        guess.set(letter, final_value)

        answer = raw_input("Want to test? y/n ")
        if answer == "y":
            # Create a random guess
            secret = Cipher()
            for i in xrange(26):
                secret.set(alphabet[i], choice(alphabet))
            # Check if it fits our constraints
            if guess == secret:
                print "Congratulations! Send me your exploit so I can see "+\
                "how you did this"
                break
            else:
                print "Sorry, better luck next time.\nYour guess encodes to "+\
                str(guess)+"\nMy secret encodes to "+str(secret)
        elif answer != "n":
            print "We asked y/n. Going to assume n."

guessing_game()

