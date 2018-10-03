"""word chain: change one letter at a time to get from one english word to another"""

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
with open('/usr/share/dict/words', 'r') as f:
    #todo: store dictionary as set
    english_words = f.read().lower().splitlines()

start = 'moon' #raw_input("first word? ") #
end = 'foot' #raw_input("second word? ") #
#todo: make sure words are same length
if start in english_words:
    loc = english_words.index(start)
    print start + ' at ' + str(loc)
    #print english_words[loc]
if end in english_words:
    loc = english_words.index(end)
    print end + ' at ' + str(loc)
    #print english_words[loc]

def change_one(change_string, guesses, start_word):
    ##take in a string and a list of guesses, change one letter at a time trying each letter in alphabet and append to guesses if (1) not already there, (2) in english_words, (3) not start word
    #put start_string in a list in order to change one char at a time
    change_as_list = list(change_string)
    #print start_as_list
    for char in range(0, len(change_as_list)):
        tmp = change_as_list[:]  #make sure to do deep copy here
        #print "tmp: " + str(tmp)
        for letter in alpha_lower:
            tmp[char] = letter
            guess = ''.join(tmp)
            if guess not in guesses and guess in english_words and guess != start_word:
                guesses.append(guess)
        #print char
    return guesses

#initialize good_guesses, insert first round of guesses
good_guesses = []
good_guesses = change_one(start, good_guesses, start)
num_chars_changed = 1
print str(num_chars_changed) + " char changed "
print "remaining good_guesses to check: " + str(good_guesses)
last_guess_index = len(good_guesses) - 1
#print "last_guess: " + good_guesses[last_guess]
#if end is found, we're done! otherwise change one character of each result and see if end is found. keep track of number of characters changed.
if end in good_guesses:
    guess = good_guesses[good_guesses.index(end)]
    print "found at: " + str(good_guesses.index(end))
else:
    print "not found, generate new round to check."
    guess = good_guesses[0]
    while guess != end:
        print "guess: " + guess
        print good_guesses
        #iterate through good_guesses starting from previous round, add english words made to good_guesses, check for end word.
        for next_guess in good_guesses[guess:len(good_guesses)]:
            print "next_guess: " + next_guess
            change_one(next_guess, good_guesses, start)
            if next_guess == good_guesses[last_guess_index]:
                num_chars_changed += 1
                print str(num_chars_changed) + " chars changed."
                print "remaining good_guesses to check: " + str(good_guesses[last_guess_index:len(good_guesses)])
                last_guess_index = len(good_guesses) - 1
                print "last_guess: " + good_guesses[last_guess_index]
            elif guess == end:
                print "found at: " + str(good_guesses.index(end))
