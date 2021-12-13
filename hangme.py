import string
import random

print("\x1b[38;2;255;70;70m  WELCOME   TO   HANGMAN   GAME\x1b[m")
print("\n\n")

print("\x1b[38;2;22;211;224m            __Describtion__ \x1b[m")
print("\n")
print("\x1b[38;2;211;195;47m * Here you have to guess the cartoon name before you hang yourself\x1b[38;2;255;75;75m x_x \x1b[m")
print("\x1b[38;2;211;195;47m * You will get 10 lives \x1b[m")
print("\x1b[38;2;211;195;47m * The new updates will come soon with new features, want to give any suggestions message me on Github\x1b[38;2;11;212;45m @het08 \x1b[38;2;211;195;47m or on IG\x1b[38;2;11;212;45m @het08 \x1b[m")

cartoon_name = ["peppa pig", "beavis & butthead", "vegie tales", "rugrats", "coast to coast", "johnny bravo", "felix the cat", "the fairly oddparents", "arthur", "yogi bear", "ed edd & eddy", "family guy", "popeye the sailor", "phineas and ferb", "the simpsons", "harley quinn", "looney tunes",
                 "regular show", "ducktales", "rick and morty", "bob`s burgers", "the flintstones", "south park", "the powerpuff girls", "winnie the pooh", "adventure time", "steven universe", "teenage mutant ninja turtles", "scooby-doo", "mickey mouse", "spongebob squarepants", "tom and jerry",
                 "peanuts", "batman", "recess", "dexter`s laboratory", "animaniacs", "courage the cowardly dog", "x-men", "talespin", "the jungle book", "the jetsons", "the addams family", "the mask", "the road runner show", "pokemon", "dragon ball z", "timon & pumbaa", "aladdin", "teen titans",
                 "mr.bean animated seires", "the transformer", "the bugs bunny", "the smurfs", "alvin & the chipmunks", "spiderman show", "darkwing duck", "the woody woodpecker show", "the pink panther", "doraemon", "oggy and the cockroaches", "ben 10", "richie rich", "the little mermaid",
                 "casper", "zig and sharko", "dalton brothers", "oscar`s oasis", "shinchan", "hagemaru", "kiteretsu", "perman", "ninja hattori", "luckyman"]

diagram_hangme = [
    """
             _____________
            |  /       |
            | /      (x_x)
            |/         |
            |         \|/
            |          |
            |         / \\
            |
            |   you hanged yourself
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|/
            |          |
            |         / \\
            |
            |   last chance
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|/
            |          |
            |         /
            |
            |   better to be correct next time
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|/
            |          |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|/
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|/
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |         \|
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/         |
            |          |
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /      (-_-)
            |/
            |
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /       |
            | /
            |/
            |
            |
            |
            |
            |
         -------
""",
    """
             _____________
            |  /
            | /
            |/
            |
            |
            |
            |
            |
         -------
""",
]

def hangme():
    word = random.choice(cartoon_name).upper()
    alphabet = set(string.ascii_uppercase)
    word_letters = set()
    for letter in word:
        if letter.upper() in alphabet:
            word_letters.add(letter.upper())

    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('you have', '\x1b[38;2;11;212;45m', lives,'\x1b[m' 'lives left and you have used these letters:',' '.join(used_letters))

        print('\x1b[38;2;255;255;0m', diagram_hangme[lives], '\x1b[m')

        print('Current word:', end=' ')
        for letter in word:
            if letter in word_letters:
                print(' _', end=' ')
            else:
                print(' ', letter, end=' ')

        print()

        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\n \x1b[38;2;38;41;218m your letter, \x1b[m', '\x1b[38;2;255;75;75m', user_letter, '\x1b[m',' \x1b[38;2;38;41;218m is not in the cartoon_name \x1b[m')

        elif user_letter in used_letters:
            print("\n \x1b[38;2;38;41;218m you have already used that letter. Guess the another letter \x1b[m")

        else:
            print("\n \x1b[38;2;38;41;218m that is not a valid letter \x1b[m")

    if lives == 0:
        print('\x1b[38;2;255;255;0m', diagram_hangme[lives], '\x1b[m')
        print("you have lost the game, you hanged yourself x_x \nThe cartoon name was:", '\x1b[38;2;224;15;15m',word,'\x1b[m')
    else:
        print("congratulations!! you have won the game, The cartoon name was:", '\x1b[38;2;224;15;15m',word,'\x1b[m')


hangme()
