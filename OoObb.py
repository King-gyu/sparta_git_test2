import random
import time


#플레이어 생성
print("당신의 이름은 무엇입니까?")
ID = input()
time.sleep(1)
print(f"{ID}의 능력을 설정하겠습니다. HP와 MP는 고정입니다.")

#Stat
hp = 100
mp = 70
power = 0
magic = 0

#stat설정 반복문
while 1:
    #HP와 MP는 고정, 공격력(power)와 마법공격력(magic)만 랜덤
    power = random.randrange(5,15)
    magic = random.randrange(10,20)
    print(f"HP = {hp}, MP = {mp} 공격력 = {power} 마법공격력 = {magic}")
    print("계속 진행하시겠습니까? 그대로 진행한다 = y , 다시 설정한다 = n") 
    #O는 진행여부
    O = input()
    if O == "n":
        continue
    #O 가 yes 일경우 다시 물어보고, 아니라고 하면 재시도
    if O == "y":
        print("이대로 진행하시겠습니까? 그대로 진행한다 = y , 다시 설정한다 = n")
        OO = input()
        if OO == "n":
            continue
        #2번의 확인후 능력치 확정
        if OO == "y":
            print("능력치가 설정되었습니다.")
            print(f"""
            ---------------------------
            [STAT]
            이름 = {ID}
            HP = {hp}
            MP = {mp}
            공격력 = {power}
            마법공격력 = {magic}
            ---------------------------""")
            break
time.sleep(1)
print(f"\n앗! {ID}은(는) 야생의 몬스터와 조우했다!")
time.sleep(1)
mhp = 60
mpower = random.randrange(5,10)

print(f"""\n        고블린 등장!
    ---------------------------
        고블린 HP : {mhp}
        고블린 공격력 : {mpower}
    ---------------------------""")

hp1 = hp

while 1:
    #내 턴
    time.sleep(1)
    print(f"\n{ID}의 차례입니다.")
    time.sleep(1)
    #Turn이 왔을 때 행동
    print("a)싸운다 s)도망간다")
    T = input()
    if T == "a":
        print("\na)일반공격 s)마법공격")
        A = input()
        #a을 눌렀다면 일반공격
        if A == "a":
            #공격할 때 파워기준으로 랜덤성
            damage = power + random.choice([-2,-1,0,1,2])
            print(f"\n{ID}은(는) 고블린을 향해 무기를 휘둘렀다!")
            time.sleep(1)
            print(f"\n고블린에게 {damage}만큼의 데미지!")
            mhp = (mhp - damage)
            time.sleep(1)
            print(f"\n고블린의 남은 체력 : {mhp}")
            time.sleep(1)
            print(f"""
            -----------------------------------------------------------------
                                 [현재 상황]
            이름 = {ID}                     고블린
            HP = {hp}                       {mhp}
            MP = {mp}                       
            공격력 = {power}                   {mpower}
            마법공격력 = {magic}
            -----------------------------------------------------------------""")
        #a가 아닐경우 마법공격
        else :
            print(f"\n{ID}은(는) 고블린을 향해 마법을 사용했다!")
            time.sleep(1)
            if mp < 30:
                print("\nMP가 부족하여 사용할 수 없다!")
                continue
            else :
                print(f"\n{ID}는 MP를 30만큼 소모했다.")
                time.sleep(1)
                #마법공격도 마법공격력 기준으로 랜덤성 추가
                mgdamage = magic * 2 + random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
                print(f"\n고블린에게 마법으로 {mgdamage}만큼의 데미지!")
                time.sleep(1)
                mhp = (mhp - mgdamage)
                mp = mp - 30
                print(f"\n고블린의 남은 체력 : {mhp}")
                time.sleep(1)
                print(f"""
                -----------------------------------------------------------------
                                    [현재 상황]
                이름 = {ID}                     고블린
                HP = {hp}                       {mhp}
                MP = {mp}                       
                공격력 = {power}                    {mpower}
                마법공격력 = {magic}
                -----------------------------------------------------------------""")
                time.sleep(1)
        #적 체력이 0이되면 전투 종료
        if mhp <= 0:
            print(f"\n고블린을 물리쳤다!")
            print(f"\n전투에서 승리했다!")
            break
    else :
        print(f"\n성공적으로 도망쳤다.")
        break

   #몬스터의 턴
    time.sleep(1)
    E = random.randrange(1,5)
    print("\n몬스터의 차례입니다.")

    time.sleep(1)

    #20% 확률로 적의 공격을 회피
    if E == 1:
        print("\n고블린의 공격은 빗나갔다!")
        time.sleep(1)
        print(f"""
            -----------------------------------------------------------------
                                 [현재 상황]
            이름 = {ID}                     고블린
            HP = {hp}                       {mhp}
            MP = {mp}                       
            공격력 = {power}                    {mpower}
            마법공격력 = {magic}
            -----------------------------------------------------------------""")
    else :
        print(f"\n고블린은 {ID}에게 몽둥이를 휘둘렀다!")
        hit = mpower + random.choice([-3,-2,-1,0,1,2,3])
        time.sleep(1)
        print(f"\n고블린의 공격으로 {hit}만큼의 데미지를 입었다!")
        hp = (hp - hit)
        time.sleep(1)
        print(f"\n{ID}의 남은 체력 : {hp}")
        time.sleep(1)
        print(f"""
            -----------------------------------------------------------------
                                 [현재 상황]
            이름 = {ID}                     고블린
            HP = {hp}                       {mhp}
            MP = {mp}                       
            공격력 = {power}                    {mpower}
            마법공격력 = {magic}
            -----------------------------------------------------------------""")
    #플레이어의 체력이 0이 되면 종료
    if hp <= 0:
        print(f"\n{ID}의 눈앞은 깜깜해졌다!")
        break