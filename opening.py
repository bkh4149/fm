
import pygame
pygame.init() 

def opening2(Cs):#--------------------
    for C in Cs:
        if C.type == "Slime":   
            if C.name == "BlueSlime":
                C.y = 4
                C.x = 1
            if C.name == "YelloSlime":
                C.y = 4
                C.x = 3
        if C.type == "Goutou" and C.name == "Yakuza":
                C.x = 2
                C.y = 2
        if C.type == "Player" and C.name == "girl":
                C.y += 1
                C.y += 0
        if C.type == "Animal" and C.name == "Cat":
                C.x = 0
                C.y = 4

#オープニング周り-------------------------------------
def animeUpdate(C):#----------最初のアニメーション
    print("first ------")
    C.tick += 1
    if C.type == "Slime":   
        if C.name == "BlueSlime":
            if C.tick == 120:
                C.x = 2
                C.y = 2
            if C.tick == 200:
                C.y = 4
            if C.tick == 400:
                C.x = 1
        if C.name == "YelloSlime":
            if C.tick == 200:
                C.x = 2
                C.y = 2
            if C.tick == 400:
                C.y = 4
            if C.tick == 500:
                C.x = 3
    if C.type == "Goutou" and C.name == "Yakuza":
        if C.tick == 400:
            C.x = 2
            C.y = 2
    if C.type == "Player" and C.name == "girl":
        if C.tick == 300:
            C.y += 1
        if C.tick == 400:
            #C.y += 4
            C.y += 0
    if C.type == "Animal" and C.name == "Cat":
        if C.tick == 400:
            C.y += 1
        if C.tick == 550:
            C.x += 1
        if C.tick == 650:
            C.y += 1        

#オープニング
def opening(screen,Cs,B,M):#--------------------
    ck = pygame.time.Clock()
    tick=0
    while True:
        tick += 1
        if tick>800:
            break
        B.draw_tile(screen)
        #---------キャプション---------
        if tick <= 500:
            mes = "喫茶店でくつろいでいたら突然強盗が入ってきた！"
            M.append_tail_line([mes])
        elif 500 < tick <= 700:
            mes = "56されたくないなら金を出せ！"
            M.append_tail_line([mes])
        if tick > 700:
            mes = "こいつら逆らう気だ、やっちまえ！"
            M.append_tail_line([mes])
        #---------アニメーション---------
        for C1 in Cs:
            animeUpdate(C1)
        #---------描画---------
        for C1 in Cs:
            C1.draw(screen)
        M.draw(screen)                          
        pygame.display.update()         
        ck.tick(60) #1秒間で30フレームになるように33msecのwait   

