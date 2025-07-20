def practice1(jomleh):
    yekta = []
    tartib_tekrar = {}

    for i in jomleh:
        shomaresh = jomleh.count(i) 

        if shomaresh == 1:
            yekta.append(i)

        tartib_tekrar[i] = shomaresh
        
    return yekta, tartib_tekrar


while True:
    try:
        jomleh = input("\njomle ra vared konid\n ").split()
        yekta, tartib_tekrar = practice1(jomleh)
        tabdil_list = list(tartib_tekrar.items())
        list_moratab = sorted(key = lambda x: x[1], reverse=True)


        print(f"kalamat yekta = {yekta}")
        print(f"tartib tekrar kalamat =  {tedad_kalamat}")

    except:
        pass