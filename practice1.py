def practice1(sentence):
    yekta = []
    tartib_tekrar = {}

    for i in sentence:
        counter = sentence.count(i)
        tartib_tekrar[i] = counter
        
        if counter == 1:
            yekta.append(i)
    return yekta, tartib_tekrar

sentence = input("Enter your sentence: \n").split()
yekta, tartib_tekrar = practice1(sentence)
