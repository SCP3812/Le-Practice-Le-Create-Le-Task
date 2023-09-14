import random 
     
#markov = input("Give your prompt here: ")

markov = "Giles Fletcher in his Of the Russe Common Wealth writes that some maps and descriptions of countries one by Herberstein mention a Slata Baba or the golden hagge an idol in the shape of an old woman who serves as an oracle for indigenous priests However Fletcher sees this as a myth He further writes that in Obdoria near the mouth of Ob River there is a rock of shape resembling a ragged woman bearing a child in her hands and Obdorian Samoyeds use it in their pagan sorcery"

def Markovian(markov): 
    markov_chain = {}
    markov_list = markov.split(" ")

    n=0
    while n < len(markov_list)-1:
        word = markov_list[n].lower().replace('\W+', "")
        print(word)
        print(n)
        if not word in markov_chain.keys():
            markov_chain[word] = []
        if markov_list[n+1]:
            markov_chain[word].append(markov_list[n+1])
        n = n + 1 
    words = list(markov_chain.keys())
    print(markov_chain.keys())
    word = words[random.randint(0, len(words)-1)]
    print(word) 
    result = ""

    for i in words:
        result = word + " "
        newWord = markov_chain[word][random.randint(0, len(markov_chain[word])-1)]
        word = newWord

        if not word or not word in markov_chain:
            word = words[random.randint(0, len(words))]
    return result


print(Markovian(markov)) 