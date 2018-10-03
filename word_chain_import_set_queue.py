"""word chain: change one letter at a time to get from one english word to another"""
import time
start_time = time.time()
def word_chain():
    from sets import Set
    from Queue import Queue

    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    with open('/usr/share/dict/words', 'r') as f:
        english_words = Set(f.read().lower().splitlines())

    start = 'dang' #'puzzled'#'fuzzily' #raw_input("first word? ").lower() #
    end = 'wolf' #'abalone' #raw_input("second word? ").lower() #

    good_input = False
    while not good_input:
        if start not in english_words:
            start = raw_input("try first word again, not in english_words: ").lower()
        elif end not in english_words:
            end = raw_input("try second word again, not in english_words: ").lower()
        elif len(start) != len(end):
            end = raw_input("words not same length, try second word again: ").lower()
        elif start == end:
            end = raw_input("same word, try second word again: ").lower()
        else:
            good_input = True
    print start + ' in english_words'
    print end + ' in english_words'

    guesses = Queue()
    guesses.put(start)
    path_storage = {start:"none"}
    found = False

    while not guesses.empty() and not found:
    #for this in range(10):
        word = guesses.get()
        #print word
        word_as_list = list(word)
        for i in range(len(word_as_list)):
            #print i
            for letter in alpha_lower:
                tmp = word_as_list[:]
                tmp[i] = letter
                guess = ''.join(tmp)
                if guess not in path_storage and guess in english_words:
                    path_storage[guess] = word
                    guesses.put(guess)
                    if guess == end:
                        found = True
                        #print "found"

    count = 1
    path = [end]
    if end not in path_storage:
        print "no path!"
        print path_storage
    else:
        while end != start:
            path.append(path_storage[end])
            end = path[count]
            count += 1
        print "found in " + str(len(path) - 1) + " steps."
        for step in range(len(path) - 1, -1, -1):
            print path[step] + " " + str(step)

word_chain()
print("--- %s seconds ---" % (time.time() - start_time))
"""


def get_guesses(last_index, next_index, existing_guesses, start_word):
    #print existing_guesses
    for word_index in range(last_index, next_index):
        #print "here: " + str(word_index) + existing_guesses[word_index]
        word_as_list = list(existing_guesses[word_index])
        for char in range(0, len(word_as_list)):
            for letter in alpha_lower:
                tmp = word_as_list[:]
                tmp[char] = letter
                guess = ''.join(tmp)
                if guess not in existing_guesses and guess in english_words and guess != start_word:
                    existing_guesses.append(guess)
                    path_storage[guess] = existing_guesses[word_index]
    return existing_guesses

guesses_storage = [start]
path_storage = {start:"none"}
num_chars_changed = 0
next_index = 0
last_index = 0
found = False
while not found:
    next_index = len(guesses_storage)
    print "last index: " + str(last_index) + " next index: " + str(next_index)
    guesses_storage = get_guesses(last_index, next_index, guesses_storage, start)
    num_chars_changed += 1
    last_index = next_index
    print str(num_chars_changed) + " chars changed "
    print "remaining good_guesses to check: " + str(guesses_storage)
    #print path_storage
    print str(last_index) + " " + str(next_index)
    if end in guesses_storage:
        found = True

found_index = guesses_storage.index(end)
print guesses_storage[found_index] + " found by changing "+ str(num_chars_changed) + " chars "

chk = end
while num_chars_changed > 0:
    print str(num_chars_changed - 1) + " " + path_storage[end]
    end = path_storage[end]
    num_chars_changed -= 1"""
