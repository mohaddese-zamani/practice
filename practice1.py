def practice1(sentence):
    yekta = []
    tartib_tekrar = {}

    for i in sentence:
        counter = sentence.count(i)
        tartib_tekrar[i] = counter
        
        if counter == 1:
            yekta.append(i)
    return yekta, tartib_tekrar

while True:
    jomleh = input("\n\njomle ra vared konid or Enter ra bezanin\n ").strip()

    if jomleh == "":
        break

    sentence = jomleh.split()
    yekta, tartib_tekrar = practice1(sentence)
    tedad_kalamat = sorted(tartib_tekrar.items(), key=lambda item: item[1], reverse=True)

    print(f"kalamat yekta = {yekta}")
    print(f"tartib tekrar kalamat =  {tedad_kalamat}")

