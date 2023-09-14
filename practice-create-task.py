import random 

markov = input("Give your prompt here: ")

def Markovian(markov): 
    markov_chain = {}
    markov_list = markov.split(" ")

    for items in markov_list:
        markov_chain[items] = []
        markov_chain[items].append(items)
    words = list(markov_chain.keys())
    print(markov_chain.keys())
    word = words[random.randint(0, len(words))]
    print(word) 
    result = ""

    for i in words:
        result = word + " "
        newWord = markov_chain[word][random.randint(0, len(words))]
        word = newWord

        if not word or not word in markov_chain:
            word = words[random.randint(0, len(words))]
    return result


print(Markovian(markov)) 