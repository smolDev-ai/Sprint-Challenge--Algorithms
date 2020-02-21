'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Idea:
# Keep count of the iterations.
# check the first two indices of the word and then use the slice api to remove
# them if they don't contain what we're looking for.
# slice them even if they do contain what we're looking for so that we can
# continue to check through the word that was given to us instead of getting
# stuck.


def count_th(word):
    # keep track of the count between instances of the function
    count = 0
    first_two = word[0:2]
    # if length of word is less than or equal to 1 return count
    if len(word) <= 1:
        return count
    # if the first index and the second index of the word equal th increment
    # count and slice them out of the word.
    if first_two == "th":
        count = count_th(word[1:]) + 1
    else:
        # if they don't just slice them out of the word
        # and run the function again.
        count = count_th(word[1:])

    return count


print(count_th("ththethghthhfklthljfth"))