#infinite monkey theorem with 'hill climb' improvement: attempt to generate "methinks it is like a weasel" by producing strings 27 characters long using random characters choosing from 26 letters of the alphabet plus space
import random
alphabet = 'abcdefghijklmnopqrstuvwxyz '
goal = 'methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel v methinks it is like a weasel v v vmethinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weasel methinks it is like a weas '

def generate(guess, goal):
    #generate a string replacing characters not matching a goal string with random characters selected from alphabet (global var), lenth of string determined by function input.
    guess = list(guess)
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            guess[i] = random.choice(alphabet)
    return ''.join(guess)

def score(guess, goal):
    #score the correctness of a guess string compared to a goal string, character by character. returns -1 if strings are not same length.
    score = 0
    if len(guess) != len(goal):
        return -1
    for i in range(len(guess)):
        if guess[i] == goal[i]:
            score += 1
    return score

def monkeys(goal):
    #call generate then score generated string against goal string until generated string is equivalent to goal string. check each string's score and keep best score seen. print current guess and best guess/score
    current_score = 0
    best_score = 0
    best_guess = ''
    guess_count = 0
    guess = "*" * len(goal)
    while current_score != len(goal):
        guess = generate(guess, goal)
        current_score = score(guess, goal)
        guess_count += 1
        if current_score > best_score:
            best_score = current_score
            best_guess = guess
        if guess_count % 1 == 0:
            print "current guess = " + "{:,}".format(guess_count)
            print "best_score = " + str(best_score) + " for: " + best_guess
    print "success on guess #" + "{:,}".format(guess_count)
    print "got " + goal

print str(len(goal))
monkeys(goal)
