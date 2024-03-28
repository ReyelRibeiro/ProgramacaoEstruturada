"""
Aluno: Reyel Palma Ribeiro

"""


import random

def main():
    
    Vida_avt = 100
    Ataque_avt = random.randint (10,20)
    Def_avt = random.randint (1,5)
    Vida_mob = random.randint (60,80)
    Ataque_mob = random.randint (20,30)
    num_rodada = 0

    print("")
    print ("Aventureiro:","Vida", Vida_avt,  "- Ataque", Ataque_avt, "- Defesa", Def_avt)
    print ("Monstro:","Vida", Vida_mob,  "- Ataque", Ataque_mob)
    print ("")
    
    while Vida_avt > 0 and Vida_mob > 0:
        
        num_rodada = num_rodada + 1
        Dano_avt = (random.randint(1,Ataque_avt))
        Vida_mob = Vida_mob - Dano_avt

        if Vida_mob<=0:
            print ("Round", num_rodada)
            print ("O monstro morreu!")
        else:
            Dano_mob = (random.randint(1,Ataque_mob) - Def_avt)

            if Dano_mob <= 0:
                Vida_avt = Vida_avt - 1
            else:
                Vida_avt = Vida_avt - Dano_mob

            if Vida_avt<=0:
                print ("Round", num_rodada)
                print ("Você morreu!")
            else:
                print ("Round", num_rodada)
                print ("Aventureiro:","Vida", Vida_avt,  "- Ataque", Ataque_avt, "- Defesa", Def_avt)
                print ("Monstro:","Vida", Vida_mob,  "- Ataque", Ataque_mob)
                print ("")

main()
