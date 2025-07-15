def practice1(sentence):
    yekta = []
    tartib_tekrar = {}

    for i in sentence:
        counter = sentence.count(i)
        tartib_tekrar[i] = counter
        
    if counter == 1:
        yekta.append(i)
    reaturn yekta, tartib_tekrar
practice1()