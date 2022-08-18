from random import randint

man1 = {"HP":100,"Atk":13,"Def":3}
man2 = {"HP":120,"Atk":8,"Def":6}



def attack(attacker,defancer):
    damage = attacker["Atk"] - defancer["Def"]
    defancer["HP"] -= damage

def attackBoost(attacker):
    attacker["Atk"] += 15*round

def heal(attacker):
    attacker["HP"] += 25*round

def chanceAttack(attacker,defancer):
    damage = attacker["Atk"]+randint(-20,25)*round - defancer["Def"]
    defancer["HP"] -= damage

def defanceIncreaseing(attacker):
    attacker["Def"] += 10*round

def fiftyFifty(attacker,defancer):
    attacker["Atk"] = attacker["Atk"]/2
    defancer["HP"] = defancer["HP"]/2

def nuclearPunch(attacker,defancer):
    attacker["Atk"] = attacker["Atk"]*3/4
    attacker["HP"] = attacker["HP"]*3/5
    defancer["Atk"] = defancer["Atk"]*4/3
    defancer["HP"] = defancer["HP"]/2

round = 0

while True:
    round += 1

    while True:
        print("/"*50)
        print("Round bouns:", round)
        print("""
        ----- MAN1 SEÇİYOR -----
            1 - attack
            2 - attack Boost
            3 - heal
            4 - chance Attack
            5 - defance Increasing
            6 - fifty Fifty
            7 - nuclear Punch
            """)
        inp = input("   >> ")

        if inp == "1":
            attack(man1,man2)
            print("man1 man2'ye",man1["Atk"]-man2["Def"],"hasar vurdu.")
            break
        elif inp == "2":
            attackBoost(man1)
            print("man1'in gücü artık",man1["Atk"])
            break
        elif inp == "3":
            heal(man1)
            print("man1'in HP'si",man1["HP"],"seviyesine yükseldi")
            break
        elif inp == "4":
            oldHP = man2["HP"]
            chanceAttack(man1,man2)
            newHP = man2["HP"]
            print("man1 man2'ye şans eseri",oldHP-newHP,"vurdu.")
            break
        elif inp == "5":
            defanceIncreaseing(man1)
            print("man1'nin yeni defansı:",man1["Def"])
            break
        elif inp == "6":
            fiftyFifty(man1,man2)
            print("Hammurabi döneminde mi yaşıyoruz abi.")
            break
        elif inp == "7":
            nuclearPunch(man1,man2)
            print("Bu ne tantana kardeşim!")
            break

    if man2["HP"] <= 0 :
        print("man1 kazandı.")
        break
    else:
        print("******\n","man1=", man1, "\nman2=", man2,"\n******",sep="")


    while True:
        print("/" * 50)
        print("Round bouns:",round)
        print("""
        ----- MAN2 SEÇİYOR -----
            1 - attack
            2 - attackBoost
            3 - heal
            4 - chance Attack
            5 - defance Increasing
            6 - fifty Fifty
            7 - nuclear Punch
            """)
        inp = input("   >> ")

        if inp == "1":
            attack(man2,man1)
            print("man2 man1'ye",man2["Atk"]-man1["Def"],"hasar vurdu.")
            break
        elif inp == "2":
            attackBoost(man2)
            print("man2'in gücü artık",man2["Atk"])
            break
        elif inp == "3":
            heal(man2)
            print("man2'in HP'si",man2["HP"],"seviyesine yükseldi")
            break
        elif inp == "4":
            oldHP = man1["HP"]
            chanceAttack(man2,man1)
            newHP = man1["HP"]
            print("man2 man1'ye şans eseri",oldHP-newHP,"vurdu.")
            break
        elif inp == "5":
            defanceIncreaseing(man2)
            print("man2'nin yeni defansı:",man2["Def"])
            break
        elif inp == "6":
            fiftyFifty(man2,man1)
            print("Hammurabi döneminde mi yaşıyoruz abi.")
            break
        elif inp == "7":
            nuclearPunch(man2,man1)
            print("Bu ne tantana kardeşim!")
            break

    if man1["HP"] <= 0:
        print("man2 kazandı.")
        break
    else:
        print("******\n","man1=", man1, "\nman2=", man2,"\n******",sep="")


