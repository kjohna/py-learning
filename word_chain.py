"""word chain: change one letter at a time to get from one english word to another"""
import time
start_time = time.time()
def word_chain():
    #from sets import Set #search 'Set removed', did with built in set()
    #from Queue import Queue #search 'Queue removed', did with built-in list operations

    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    with open('/usr/share/dict/words', 'r') as f:
        english_words = set(f.read().lower().splitlines())
        #english_words = Set(f.read().lower().splitlines()) #Set removed

    start = 'dang' #'fuzzily' #'puzzled'#raw_input("first word? ").lower() #
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

    """Queue removed:
    guesses = Queue()
    guesses.put(start)
    """
    guesses = [start]
    path_storage = {start:"none"}
    found = False

    #while not guesses.empty() and not found: #Queue removed
    while not len(guesses) == 0 and not found:
        #word = guesses.get() #Queue removed
        word = guesses.pop(0)
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
                    #guesses.put(guess) #Queue removed
                    guesses.append(guess)
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
