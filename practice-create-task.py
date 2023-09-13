import random 

markov = input("Give your prompt here: ")

def Markovian(markov): 
    markov_chain = {}
    markov_list = markov.split(" ")

    n = 0
    for items in markov_list:
        if not markov_chain(items):
            markov_chain[items] = []
        if markov_list[n] != markov_list[n+1]:
            markov_chain[items].append(items)
        n = n + 1
    words = markov_chain.keys()
    word = words[randInt(0, len(words))]
    result = ""

    for i in len(words):
        result = word + " "
        newWord = markov_chain[word][randInt(0, len(words))]
        word = newWord

        if not word or not word in markov_chain:
            word = words[randInt(0, len(words))]
    return result


print(Markovian(markov)) 