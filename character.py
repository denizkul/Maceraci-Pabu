from itemler import *
import sqlite3
import pygame

pygame.init()

con = sqlite3.connect("Bilgiler.db")

cursor = con.cursor()
tablo = "Bilgiler"


class Oyuncu:
    def __init__(self):
        self.OyuncuX = 500
        self.OyuncuY = 535
        self.ScaleX = 175
        self.ScaleY = 125
        self.kafa = pygame.image.load("Resimler/kafa.png").convert_alpha()
        self.cerceve = pygame.image.load("Resimler/cerceve.png").convert_alpha()
        self.cerceve = pygame.transform.scale(self.cerceve, (93, 93))
        self.ManaBari = pygame.image.load("Resimler/Mana Barı.png").convert_alpha()
        self.ManaBari = pygame.transform.scale(self.ManaBari, (97, 15))
        self.CoinPic = pygame.image.load("Resimler/coin.png").convert_alpha()
        self.CoinPic = pygame.transform.scale(self.CoinPic, (21, 27))
        self.Idle0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-00.png").convert_alpha()
        self.Idle0 = pygame.transform.scale(self.Idle0, (self.ScaleX, self.ScaleY))
        self.Idle1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-01.png").convert_alpha()
        self.Idle1 = pygame.transform.scale(self.Idle1, (self.ScaleX, self.ScaleY))
        self.Idle2 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-02.png").convert_alpha()
        self.Idle2 = pygame.transform.scale(self.Idle2, (self.ScaleX, self.ScaleY))
        self.Idle3 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-03.png").convert_alpha()
        self.Idle3 = pygame.transform.scale(self.Idle3, (self.ScaleX, self.ScaleY))
        self.IdleListesi = [self.Idle0, self.Idle1, self.Idle2, self.Idle3]

        self.IdleSol0 = pygame.transform.flip(self.Idle0, True, False)
        self.IdleSol1 = pygame.transform.flip(self.Idle1, True, False)
        self.IdleSol2 = pygame.transform.flip(self.Idle2, True, False)
        self.IdleSol3 = pygame.transform.flip(self.Idle3, True, False)
        self.IdleSolListesi = [self.IdleSol0, self.IdleSol1, self.IdleSol2, self.IdleSol3]

        self.Idle10 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-2-00.png").convert_alpha()
        self.Idle10 = pygame.transform.scale(self.Idle10, (self.ScaleX, self.ScaleY))
        self.Idle11 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-2-01.png").convert_alpha()
        self.Idle11 = pygame.transform.scale(self.Idle11, (self.ScaleX, self.ScaleY))
        self.Idle12 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-2-02.png").convert_alpha()
        self.Idle12 = pygame.transform.scale(self.Idle12, (self.ScaleX, self.ScaleY))
        self.Idle13 = pygame.image.load("Adventurer/Individual Sprites/adventurer-idle-2-03.png").convert_alpha()
        self.Idle13 = pygame.transform.scale(self.Idle13, (self.ScaleX, self.ScaleY))
        self.Idle1Listesi = [self.Idle10, self.Idle11, self.Idle12, self.Idle13]

        self.IdleSol10 = pygame.transform.flip(self.Idle10, True, False)
        self.IdleSol11 = pygame.transform.flip(self.Idle11, True, False)
        self.IdleSol12 = pygame.transform.flip(self.Idle12, True, False)
        self.IdleSol13 = pygame.transform.flip(self.Idle13, True, False)
        self.IdleSol1Listesi = [self.IdleSol10, self.IdleSol11, self.IdleSol12, self.IdleSol13]

        self.Hareket0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-00.png").convert_alpha()
        self.Hareket0 = pygame.transform.scale(self.Hareket0, (self.ScaleX, self.ScaleY))
        self.Hareket1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-01.png").convert_alpha()
        self.Hareket1 = pygame.transform.scale(self.Hareket1, (self.ScaleX, self.ScaleY))
        self.Hareket2 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-02.png").convert_alpha()
        self.Hareket2 = pygame.transform.scale(self.Hareket2, (self.ScaleX, self.ScaleY))
        self.Hareket3 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-03.png").convert_alpha()
        self.Hareket3 = pygame.transform.scale(self.Hareket3, (self.ScaleX, self.ScaleY))
        self.Hareket4 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-04.png").convert_alpha()
        self.Hareket4 = pygame.transform.scale(self.Hareket4, (self.ScaleX, self.ScaleY))
        self.Hareket5 = pygame.image.load("Adventurer/Individual Sprites/adventurer-run-05.png").convert_alpha()
        self.Hareket5 = pygame.transform.scale(self.Hareket5, (self.ScaleX, self.ScaleY))
        self.HareketListesi = [self.Hareket0, self.Hareket1, self.Hareket2, self.Hareket3, self.Hareket4, self.Hareket5]
        self.harekete_basladi = pygame.time.get_ticks()

        self.HareketSol0 = pygame.transform.flip(self.Hareket0, True, False)
        self.HareketSol1 = pygame.transform.flip(self.Hareket1, True, False)
        self.HareketSol2 = pygame.transform.flip(self.Hareket2, True, False)
        self.HareketSol3 = pygame.transform.flip(self.Hareket3, True, False)
        self.HareketSol4 = pygame.transform.flip(self.Hareket4, True, False)
        self.HareketSol5 = pygame.transform.flip(self.Hareket5, True, False)
        self.HareketSolListesi = [self.HareketSol0, self.HareketSol1, self.HareketSol2,
                                  self.HareketSol3, self.HareketSol4, self.HareketSol5]

        self.Saldir00 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack1-00.png").convert_alpha()
        self.Saldir00 = pygame.transform.scale(self.Saldir00, (self.ScaleX, self.ScaleY))
        self.Saldir01 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack1-01.png").convert_alpha()
        self.Saldir01 = pygame.transform.scale(self.Saldir01, (self.ScaleX, self.ScaleY))
        self.Saldir02 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack1-02.png").convert_alpha()
        self.Saldir02 = pygame.transform.scale(self.Saldir02, (self.ScaleX, self.ScaleY))
        self.Saldir03 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack1-03.png").convert_alpha()
        self.Saldir03 = pygame.transform.scale(self.Saldir03, (self.ScaleX, self.ScaleY))
        self.Saldir0Listesi = [self.Saldir00, self.Saldir01, self.Saldir02, self.Saldir03]

        self.SaldirSol00 = pygame.transform.flip(self.Saldir00, True, False).convert_alpha()
        self.SaldirSol01 = pygame.transform.flip(self.Saldir01, True, False).convert_alpha()
        self.SaldirSol02 = pygame.transform.flip(self.Saldir02, True, False).convert_alpha()
        self.SaldirSol03 = pygame.transform.flip(self.Saldir03, True, False).convert_alpha()
        self.Saldir0SolListesi = [self.SaldirSol00, self.SaldirSol01, self.SaldirSol02, self.SaldirSol03]

        self.ZiplaIdle0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-jump-00.png").convert_alpha()
        self.ZiplaIdle0 = pygame.transform.scale(self.ZiplaIdle0, (self.ScaleX, self.ScaleY))
        self.ZiplaIdle1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-jump-01.png").convert_alpha()
        self.ZiplaIdle1 = pygame.transform.scale(self.ZiplaIdle1, (self.ScaleX, self.ScaleY))
        self.ZiplaIdle2 = pygame.image.load("Adventurer/Individual Sprites/adventurer-jump-02.png").convert_alpha()
        self.ZiplaIdle2 = pygame.transform.scale(self.ZiplaIdle2, (self.ScaleX, self.ScaleY))
        self.ZiplaIdle3 = pygame.image.load("Adventurer/Individual Sprites/adventurer-jump-03.png").convert_alpha()
        self.ZiplaIdle3 = pygame.transform.scale(self.ZiplaIdle3, (self.ScaleX, self.ScaleY))
        self.ZiplaListesi = [self.ZiplaIdle0, self.ZiplaIdle1, self.ZiplaIdle2, self.ZiplaIdle3]

        self.ZiplaIdleSol0 = pygame.transform.flip(self.ZiplaIdle0, True, False)
        self.ZiplaIdleSol1 = pygame.transform.flip(self.ZiplaIdle1, True, False)
        self.ZiplaIdleSol2 = pygame.transform.flip(self.ZiplaIdle2, True, False)
        self.ZiplaIdleSol3 = pygame.transform.flip(self.ZiplaIdle3, True, False)
        self.ZiplaSolListesi = [self.ZiplaIdleSol0, self.ZiplaIdleSol1, self.ZiplaIdleSol2, self.ZiplaIdleSol3]

        self.DusIdle0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-fall-00.png").convert_alpha()
        self.DusIdle0 = pygame.transform.scale(self.DusIdle0, (self.ScaleX, self.ScaleY))
        self.DusIdle1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-fall-01.png").convert_alpha()
        self.DusIdle1 = pygame.transform.scale(self.DusIdle1, (self.ScaleX, self.ScaleY))
        self.DusListesi = [self.DusIdle0, self.DusIdle1]

        self.DusIdleSol0 = pygame.transform.flip(self.DusIdle0, True, False)
        self.DusIdleSol1 = pygame.transform.flip(self.DusIdle1, True, False)
        self.DusListesiSol = [self.DusIdleSol0, self.DusIdleSol1]

        self.HasarYe0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-hurt-00.png")
        self.HasarYe0 = pygame.transform.scale(self.HasarYe0, (self.ScaleX, self.ScaleY))
        self.HasarYe1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-hurt-01.png")
        self.HasarYe1 = pygame.transform.scale(self.HasarYe1, (self.ScaleX, self.ScaleY))
        self.HasarYe2 = pygame.image.load("Adventurer/Individual Sprites/adventurer-hurt-02.png")
        self.HasarYe2 = pygame.transform.scale(self.HasarYe2, (self.ScaleX, self.ScaleY))
        self.HasarYeListesi = [self.HasarYe0, self.HasarYe1, self.HasarYe2]

        self.HasarYeSol0 = pygame.transform.flip(self.HasarYe0, True, False)
        self.HasarYeSol1 = pygame.transform.flip(self.HasarYe1, True, False)
        self.HasarYeSol2 = pygame.transform.flip(self.HasarYe2, True, False)
        self.HasarYeSolListesi = [self.HasarYeSol0, self.HasarYeSol1, self.HasarYeSol2]

        self.Cok0 = pygame.image.load("Adventurer/Individual Sprites/adventurer-crouch-00.png")
        self.Cok0 = pygame.transform.scale(self.Cok0, (self.ScaleX, self.ScaleY))
        self.Cok1 = pygame.image.load("Adventurer/Individual Sprites/adventurer-crouch-01.png")
        self.Cok1 = pygame.transform.scale(self.Cok1, (self.ScaleX, self.ScaleY))
        self.Cok2 = pygame.image.load("Adventurer/Individual Sprites/adventurer-crouch-02.png")
        self.Cok2 = pygame.transform.scale(self.Cok2, (self.ScaleX, self.ScaleY))
        self.Cok3 = pygame.image.load("Adventurer/Individual Sprites/adventurer-crouch-03.png")
        self.Cok3 = pygame.transform.scale(self.Cok3, (self.ScaleX, self.ScaleY))
        self.CokListesi = [self.Cok0, self.Cok1, self.Cok2, self.Cok3]

        self.CokSol0 = pygame.transform.flip(self.Cok0, True, False)
        self.CokSol1 = pygame.transform.flip(self.Cok1, True, False)
        self.CokSol2 = pygame.transform.flip(self.Cok2, True, False)
        self.CokSol3 = pygame.transform.flip(self.Cok3, True, False)
        self.CokSolListesi = [self.CokSol0, self.CokSol1, self.CokSol2, self.CokSol3]

        self.CanBari = pygame.image.load("Resimler/Can Barı.png").convert_alpha()
        self.CanBariSafe = self.CanBari
        self.CanBariCerceve = pygame.image.load("Resimler/can barı çerçeve.png").convert_alpha()
        self.ExpCerceve = pygame.image.load("Resimler/bar.png").convert_alpha()
        self.ExpBari = pygame.image.load("Resimler/Exp Barı.png").convert_alpha()
        self.ExpBari = pygame.transform.scale(self.ExpBari, (126, 6))

        self.Cimende_Yurume_Sesi = pygame.mixer.Sound("ses efektleri/Grass Running.wav")
        self.Cimende_Yurume_Sesi.set_volume(0.05)

        self.SaldirmaSesi = pygame.mixer.Sound("ses efektleri/attack1.wav")
        self.SaldirmaSesi.set_volume(0.1)

        self.sonzaman = pygame.time.get_ticks()
        self.sahne_idle = 0
        self.sahne_solidle = 0
        self.sahne_hareket = 0
        self.sahne_saldiri0 = 0
        self.sahne_solsaldir = 0
        self.sahne_saldiri1sag = 0
        self.sahne_saldiri1sol = 0
        self.sahne_coksag = 0
        self.sahne_coksol = 0
        self.sahne_zipla = 0
        self.sahne_dus = 0
        self.sahne_hasa_ye = 0
        self.sahne_hasa_yesol = 0
        self.hareket = "stabil"
        self.mouse = pygame.mouse
        self.durum_sonzaman = pygame.time.get_ticks()
        self.havada = False
        self.ZeminRect = pygame.Rect(0, 664, 100000, 793)
        self.yuksel = 22
        self.asagiin = 5
        self.ucmasonzamani = pygame.time.get_ticks()
        self.canyenile_sonzaman = pygame.time.get_ticks()
        self.zipla = "yerde"
        self.ziplama_izni = "var"
        self.yon = "sağ"
        self.hasar_ver = False
        self.font = pygame.font.Font("m5x7.ttf", 40)
        self.hasar_yedi_mi = False
        self.AyakRect = pygame.Rect(self.OyuncuX + 30, self.OyuncuY + 100, 50, 20)
        self.OyuncuRect = pygame.Rect(self.OyuncuX + 50, self.OyuncuY, 65, self.ScaleY)
        self.ucma_ilkzamani = pygame.time.get_ticks()
        self.ucx = 44
        self.ucy = 20
        self.ozelsaldiri_izni = True
        self.manarejenerasyonu_ilkzaman = pygame.time.get_ticks()
        self.manarejenerasyonu_sonzaman = pygame.time.get_ticks()
        self.gizlen = False
        self.durum = "idle1"

        self.bilgiler = self.Bilgiler()
        if len(self.bilgiler) != 0:
            self.coin = self.bilgiler[0][0]
            self.totalcan = self.bilgiler[0][1]
            self.can = self.bilgiler[0][2]
            self.exp = self.bilgiler[0][3]
            self.level = self.bilgiler[0][4]
            self.yetenek_puani = self.bilgiler[0][5]
            self.zirh = self.bilgiler[0][6]
            self.dayaniklilik = self.bilgiler[0][7]
            self.totalexp = self.bilgiler[0][8]
            self.totalmana = self.bilgiler[0][9]
            self.mana = self.bilgiler[0][10]
            self.skill_kiliclevel = self.bilgiler[0][11]
            self.skill_kalkanlevel = self.bilgiler[0][12]
            self.skill_ayaklevel = self.bilgiler[0][13]
            self.canregen = self.bilgiler[0][14]
            self.manaregen = self.bilgiler[0][15]
            self.levelpuani = self.bilgiler[0][16]
            self.totalhiz = self.bilgiler[0][17]
            self.totalad = self.bilgiler[0][18]

        else:
            self.can = 100
            self.totalcan = 100
            self.coin = 30
            self.mana = 100
            self.exp = 0
            self.level = 1
            self.chunk = 0
            self.yetenek_puani = 0
            self.zirh = 10
            self.totalexp = 100
            self.totalmana = 100
            self.skill_kiliclevel = 0
            self.skill_kalkanlevel = 0
            self.skill_ayaklevel = 0
            self.manaregen = 5
            self.canregen = 3
            self.dayaniklilik = 5
            self.levelpuani = 0
            self.ad = 15
            self.totalad = 15
            self.hiz = 6
            self.totalhiz = 6
            self.durum = "idle1"

        self.toplamarmour = self.dayaniklilik + self.zirh
        self.hiz = self.totalhiz
        self.ad = self.totalad

        if self.skill_kiliclevel == 1:
            self.Saldir10 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-00.png")
            self.Saldir10 = pygame.transform.scale(self.Saldir10, (self.ScaleX, self.ScaleY))
            self.Saldir11 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-01.png")
            self.Saldir11 = pygame.transform.scale(self.Saldir11, (self.ScaleX, self.ScaleY))
            self.Saldir12 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-02.png")
            self.Saldir12 = pygame.transform.scale(self.Saldir12, (self.ScaleX, self.ScaleY))
            self.Saldir13 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-03.png")
            self.Saldir13 = pygame.transform.scale(self.Saldir13, (self.ScaleX, self.ScaleY))
            self.Saldir14 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-04.png")
            self.Saldir14 = pygame.transform.scale(self.Saldir14, (self.ScaleX, self.ScaleY))
            self.Saldir15 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-05.png")
            self.Saldir15 = pygame.transform.scale(self.Saldir15, (self.ScaleX, self.ScaleY))
            self.Saldir0Listesi.append(self.Saldir10)
            self.Saldir0Listesi.append(self.Saldir11)
            self.Saldir0Listesi.append(self.Saldir12)
            self.Saldir0Listesi.append(self.Saldir13)
            self.Saldir0Listesi.append(self.Saldir14)
            self.Saldir0Listesi.append(self.Saldir15)

            self.SaldirSol10 = pygame.transform.flip(self.Saldir10, True, False)
            self.SaldirSol11 = pygame.transform.flip(self.Saldir11, True, False)
            self.SaldirSol12 = pygame.transform.flip(self.Saldir12, True, False)
            self.SaldirSol13 = pygame.transform.flip(self.Saldir13, True, False)
            self.SaldirSol14 = pygame.transform.flip(self.Saldir14, True, False)
            self.SaldirSol15 = pygame.transform.flip(self.Saldir15, True, False)
            self.Saldir0SolListesi.append(self.SaldirSol10)
            self.Saldir0SolListesi.append(self.SaldirSol11)
            self.Saldir0SolListesi.append(self.SaldirSol12)
            self.Saldir0SolListesi.append(self.SaldirSol13)
            self.Saldir0SolListesi.append(self.SaldirSol14)
            self.Saldir0SolListesi.append(self.SaldirSol15)

        if self.skill_kiliclevel > 1:
            self.Saldir10 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-00.png")
            self.Saldir10 = pygame.transform.scale(self.Saldir10, (self.ScaleX, self.ScaleY))
            self.Saldir11 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-01.png")
            self.Saldir11 = pygame.transform.scale(self.Saldir11, (self.ScaleX, self.ScaleY))
            self.Saldir12 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-02.png")
            self.Saldir12 = pygame.transform.scale(self.Saldir12, (self.ScaleX, self.ScaleY))
            self.Saldir13 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-03.png")
            self.Saldir13 = pygame.transform.scale(self.Saldir13, (self.ScaleX, self.ScaleY))
            self.Saldir14 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-04.png")
            self.Saldir14 = pygame.transform.scale(self.Saldir14, (self.ScaleX, self.ScaleY))
            self.Saldir15 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack2-05.png")
            self.Saldir15 = pygame.transform.scale(self.Saldir15, (self.ScaleX, self.ScaleY))
            self.Saldir0Listesi.append(self.Saldir10)
            self.Saldir0Listesi.append(self.Saldir11)
            self.Saldir0Listesi.append(self.Saldir12)
            self.Saldir0Listesi.append(self.Saldir13)
            self.Saldir0Listesi.append(self.Saldir14)
            self.Saldir0Listesi.append(self.Saldir15)

            self.SaldirSol10 = pygame.transform.flip(self.Saldir10, True, False)
            self.SaldirSol11 = pygame.transform.flip(self.Saldir11, True, False)
            self.SaldirSol12 = pygame.transform.flip(self.Saldir12, True, False)
            self.SaldirSol13 = pygame.transform.flip(self.Saldir13, True, False)
            self.SaldirSol14 = pygame.transform.flip(self.Saldir14, True, False)
            self.SaldirSol15 = pygame.transform.flip(self.Saldir15, True, False)

            self.Saldir0SolListesi.append(self.SaldirSol10)
            self.Saldir0SolListesi.append(self.SaldirSol11)
            self.Saldir0SolListesi.append(self.SaldirSol12)
            self.Saldir0SolListesi.append(self.SaldirSol13)
            self.Saldir0SolListesi.append(self.SaldirSol14)
            self.Saldir0SolListesi.append(self.SaldirSol15)

            self.Saldir20 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-00.png")
            self.Saldir20 = pygame.transform.scale(self.Saldir20, (self.ScaleX, self.ScaleY))
            self.Saldir21 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-01.png")
            self.Saldir21 = pygame.transform.scale(self.Saldir21, (self.ScaleX, self.ScaleY))
            self.Saldir22 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-02.png")
            self.Saldir22 = pygame.transform.scale(self.Saldir22, (self.ScaleX, self.ScaleY))
            self.Saldir23 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-03.png")
            self.Saldir23 = pygame.transform.scale(self.Saldir23, (self.ScaleX, self.ScaleY))
            self.Saldir24 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-04.png")
            self.Saldir24 = pygame.transform.scale(self.Saldir24, (self.ScaleX, self.ScaleY))
            self.Saldir25 = pygame.image.load("Adventurer/Individual Sprites/adventurer-attack3-05.png")
            self.Saldir25 = pygame.transform.scale(self.Saldir25, (self.ScaleX, self.ScaleY))

            self.Saldir0Listesi.append(self.Saldir20)
            self.Saldir0Listesi.append(self.Saldir21)
            self.Saldir0Listesi.append(self.Saldir22)
            self.Saldir0Listesi.append(self.Saldir23)
            self.Saldir0Listesi.append(self.Saldir24)
            self.Saldir0Listesi.append(self.Saldir25)

            self.SaldirSol20 = pygame.transform.flip(self.Saldir20, True, False)
            self.SaldirSol21 = pygame.transform.flip(self.Saldir21, True, False)
            self.SaldirSol22 = pygame.transform.flip(self.Saldir22, True, False)
            self.SaldirSol23 = pygame.transform.flip(self.Saldir23, True, False)
            self.SaldirSol24 = pygame.transform.flip(self.Saldir24, True, False)
            self.SaldirSol25 = pygame.transform.flip(self.Saldir25, True, False)
            self.Saldir0SolListesi.append(self.SaldirSol20)
            self.Saldir0SolListesi.append(self.SaldirSol21)
            self.Saldir0SolListesi.append(self.SaldirSol22)
            self.Saldir0SolListesi.append(self.SaldirSol23)
            self.Saldir0SolListesi.append(self.SaldirSol24)
            self.Saldir0SolListesi.append(self.SaldirSol25)

        self.BosItem = BosItem()

        self.Itemler = [Ring1(), Ring2(), Ring3(),
                        Necklase1(), Necklase2(), Necklase3(),
                        Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                        Zirh1(), Zirh2(), Zirh3(), Zirh4()]

        self.envanterbilgileri = self.Envanter()

        if len(self.envanterbilgileri) != 0 or len(self.KullanEnvanter()) != 0:
            self.envanter = []
            self.item_isimleri = []
            self.index = 0
            self.itemlistesi = []
            self.kullanenvanter = []

            for item1 in self.envanterbilgileri:
                for item2 in self.Itemler:
                    if item1[0] == item2.isim:
                        self.Itemler = [Ring1(), Ring2(), Ring3(),
                                        Necklase1(), Necklase2(), Necklase3(),
                                        Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                                        Zirh1(), Zirh2(), Zirh3(), Zirh4()]
                        self.envanter.append(item2)
                        self.index += 1

            for item in range(self.index, 49):
                self.envanter.append(self.BosItem)
            self.Itemler = [Ring1(), Ring2(), Ring3(),
                            Necklase1(), Necklase2(), Necklase3(),
                            Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                            Zirh1(), Zirh2(), Zirh3(), Zirh4(), BosItem()]
            i = 0
            for item2 in self.KullanEnvanter():
                i += 1
                for item3 in self.Itemler:
                    if item2[0] == item3.isim:
                        self.Itemler = [Ring1(), Ring2(), Ring3(),
                                        Necklase1(), Necklase2(), Necklase3(),
                                        Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                                        Zirh1(), Zirh2(), Zirh3(), Zirh4(), BosItem()]
                        self.kullanenvanter.append(item3)
                        if i == 1:
                            item3.itemx = 763
                            item3.itemy = 501
                        elif i == 2:
                            item3.itemx = 822
                            item3.itemy = 501
                        elif i == 3:
                            item3.itemx = 1028
                            item3.itemy = 501
                        elif i == 4:
                            item3.itemx = 1087
                            item3.itemy = 501
                        elif i == 5:
                            item3.itemx = 901
                            item3.itemy = 154
                            item3.resim = pygame.transform.scale(item3.resim, (95, 95))
                        elif i == 6:
                            item3.itemx = 905
                            item3.itemy = 300
                            item3.resim = item3.itemresim

            self.Itemler = [Ring1(), Ring2(), Ring3(),
                            Necklase1(), Necklase2(), Necklase3(),
                            Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                            Zirh1(), Zirh2(), Zirh3(), Zirh4(), BosItem()]

        else:
            self.envanter = []
            self.kullanenvanter = []
            for item in range(1, 50):
                self.envanter.append(self.BosItem)

            for item in range(1, 7):
                self.kullanenvanter.append(self.BosItem)

    def Bilgiler(self):
        cursor.execute("SELECT * FROM {}".format(tablo))
        data = cursor.fetchall()
        return data

    def Envanter(self):

        cursor.execute("SELECT * FROM Envanter")
        data = cursor.fetchall()
        return data

    def KullanEnvanter(self):
        cursor.execute("SELECT * FROM KullanEnvanter")
        data = cursor.fetchall()
        return data

    def Cizdir(self, pencere):
        self.OyuncuRect = pygame.Rect(self.OyuncuX + 50, self.OyuncuY, 65, self.ScaleY)

        pencere.blit(self.cerceve, (0, 0))
        pencere.blit(self.kafa, (0, 0))
        self.AyakRect = pygame.Rect(self.OyuncuX + 65, self.OyuncuY + 110, 45, 20)
        if self.can > 0:
            self.CanBari = pygame.transform.scale(self.CanBariSafe, (int(138 * (self.can / self.totalcan)), 17))

        else:
            self.CanBari = pygame.transform.scale(self.CanBari, (0, 17))

        if self.mana > 0:
            self.ManaBari = pygame.transform.scale(self.ManaBari, (int(138 * (self.mana / self.totalmana)), 17))

        else:
            self.ManaBari = pygame.transform.scale(self.ManaBari, (0, 17))

        self.CanBariCerceve = pygame.transform.scale(self.CanBariCerceve, (145, 20))
        self.ExpBari = pygame.transform.scale(self.ExpBari, (int(128 * (self.exp / self.totalexp)), 6))
        pencere.blit(self.CanBariCerceve, (93, 0))
        pencere.blit(self.CanBariCerceve, (93, 20))
        pencere.blit(self.ExpCerceve, (93, 40))
        pencere.blit(self.CanBari, (97, 2))
        pencere.blit(self.ManaBari, (97, 22))
        pencere.blit(self.ExpBari, (95, 42))
        pencere.blit(self.CoinPic, (100, 52))
        pencere.blit(self.font.render(": " + str(self.coin), True, (0, 0, 0)), (125, 50))

        if not self.gizlen:

            if (self.zipla != "zıpla" or self.zipla != "süzül") and not self.hasar_yedi_mi:
                if self.hareket == "stabil" and self.yon == "sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.IdleListesi[self.sahne_idle], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 250:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_idle == 3:
                            self.sahne_idle = 0

                        else:
                            self.sahne_idle += 1

                elif self.hareket == "stabil" and self.yon == "sol":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.IdleSolListesi[self.sahne_solidle], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 250:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_solidle == 3:
                            self.sahne_solidle = 0

                        else:
                            self.sahne_solidle += 1

                elif self.hareket == "sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.HareketListesi[self.sahne_hareket], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 125:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_hareket == 5:
                            self.sahne_hareket = 0

                        else:
                            self.sahne_hareket += 1

                        if self.sahne_hareket % 2 == 1:
                            self.Cimende_Yurume_Sesi.play()

                elif self.hareket == "sol":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.HareketSolListesi[self.sahne_hareket], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 125:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_hareket == 5:
                            self.sahne_hareket = 0

                        else:
                            self.sahne_hareket += 1

                        if self.sahne_hareket % 2 == 1:
                            self.Cimende_Yurume_Sesi.play()

                elif self.hareket == "saldır" and self.yon == "sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.Saldir0Listesi[self.sahne_saldiri0], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 85:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_saldiri0 == 2:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True

                        elif self.sahne_saldiri0 == 7:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True

                        elif self.sahne_saldiri0 == 13:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True

                        if self.sahne_saldiri0 == len(self.Saldir0Listesi) - 1:
                            self.hareket = "stabil"
                            self.sahne_saldiri0 = 0

                        else:
                            self.sahne_saldiri0 += 1

                elif self.hareket == "saldır" and self.yon == "sol":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.Saldir0SolListesi[self.sahne_solsaldir], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 85:
                        self.sonzaman = pygame.time.get_ticks()

                        if self.sahne_solsaldir == 2:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True

                        elif self.sahne_solsaldir == 7:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True

                        elif self.sahne_solsaldir == 13:
                            self.SaldirmaSesi.play()
                            self.hasar_ver = True
                        if self.sahne_solsaldir == len(self.Saldir0SolListesi) - 1:
                            self.hareket = "stabil"
                            self.sahne_solsaldir = 0

                        else:
                            self.sahne_solsaldir += 1

                elif self.hareket == "özel 1 sağ":
                    self.OyuncuX += self.ucx
                    self.OyuncuY -= self.ucy
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.DusListesi[self.sahne_dus], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 65:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_dus == 1:
                            self.sahne_dus = 0
                            self.ucx -= 4
                            self.ucy -= 4

                        else:
                            self.sahne_dus += 1

                elif self.hareket == "özel 1 sol":
                    self.OyuncuX -= self.ucx
                    self.OyuncuY -= self.ucy
                    pencere.blit(self.DusListesiSol[self.sahne_dus], (self.OyuncuX, self.OyuncuY))
                    self.ilkzaman = pygame.time.get_ticks()
                    if self.ilkzaman - self.sonzaman > 65:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_dus == 1:
                            self.sahne_dus = 0
                            self.ucx -= 4
                            self.ucy -= 4

                        else:
                            self.sahne_dus += 1

                elif self.hareket == "çök sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.CokListesi[self.sahne_coksag], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 200:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_coksag == len(self.CokListesi) - 1:
                            self.sahne_coksag = 0
                            self.gizlen = True

                        else:
                            self.sahne_coksag += 1

                elif self.hareket == "çök sol":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.CokSolListesi[self.sahne_coksol], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 200:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_coksol == len(self.CokSolListesi) - 1:
                            self.sahne_coksol = 0
                            self.gizlen = True

                        else:
                            self.sahne_coksol += 1

            if self.zipla == "zıpla":
                if self.yon == "sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.ZiplaListesi[self.sahne_zipla], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 25:
                        self.sonzaman = pygame.time.get_ticks()

                        if self.sahne_zipla != 3:
                            self.sahne_zipla += 1

                elif self.yon == "sol":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.ZiplaSolListesi[self.sahne_zipla], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 25:
                        self.sonzaman = pygame.time.get_ticks()

                        if self.sahne_zipla != 3:
                            self.sahne_zipla += 1

            elif self.zipla == "süzül":
                if self.yon == "sağ":
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.DusListesi[self.sahne_dus], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 65:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_dus == 1:
                            self.sahne_dus = 0

                        else:
                            self.sahne_dus += 1

                else:
                    self.ilkzaman = pygame.time.get_ticks()
                    pencere.blit(self.DusListesiSol[self.sahne_dus], (self.OyuncuX, self.OyuncuY))
                    if self.ilkzaman - self.sonzaman > 65:
                        self.sonzaman = pygame.time.get_ticks()
                        if self.sahne_dus == 1:
                            self.sahne_dus = 0

                        else:
                            self.sahne_dus += 1

                if self.AyakRect.colliderect(self.ZeminRect):
                    pencere.blit(self.DusListesi[0], (self.OyuncuX, self.OyuncuY))
                    self.zipla = "yerde"
                    if self.hareket != "saldır":
                        self.hareket = "stabil"

            if self.hasar_yedi_mi and self.yon == "sağ":
                self.ilkzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarYeListesi[self.sahne_hasa_ye], (self.OyuncuX, self.OyuncuY))
                if self.ilkzaman - self.sonzaman > 75:
                    self.sonzaman = pygame.time.get_ticks()
                    if self.sahne_hasa_ye == len(self.HasarYeListesi) - 1:
                        self.sahne_hasa_ye = 0
                        self.hareket = "stabil"
                        self.hasar_yedi_mi = False

                    else:
                        self.sahne_hasa_ye += 1

            if self.hasar_yedi_mi and self.yon == "sol":
                self.ilkzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarYeSolListesi[self.sahne_hasa_yesol], (self.OyuncuX, self.OyuncuY))
                if self.ilkzaman - self.sonzaman > 75:
                    self.sonzaman = pygame.time.get_ticks()
                    if self.sahne_hasa_yesol == len(self.HasarYeSolListesi) - 1:
                        self.sahne_hasa_yesol = 0
                        self.hareket = "stabil"
                        self.hasar_yedi_mi = False

                    else:
                        self.sahne_hasa_yesol += 1

    def Hareket(self):

        if self.exp >= self.totalexp:
            self.gelisim = self.totalexp * (1 / 3)
            self.level += 1
            self.exp -= self.totalexp
            self.totalexp += int(self.gelisim)
            self.levelpuani += 1
            if self.level % 3 == 0:
                self.yetenek_puani += 1

        self.Tus = pygame.key.get_pressed()
        self.ilkzaman = pygame.time.get_ticks()
        self.canyenile_ilkzaman = pygame.time.get_ticks()
        self.manarejenerasyonu_ilkzaman = pygame.time.get_ticks()

        if self.canyenile_ilkzaman - self.canyenile_sonzaman > 1500 and self.can + self.canregen < self.totalcan:
            self.can += self.canregen
            self.canyenile_sonzaman = pygame.time.get_ticks()

        elif self.canyenile_ilkzaman - self.canyenile_sonzaman > 1500 and self.can + self.canregen >= self.totalcan:
            self.can = self.totalcan
            self.canyenile_sonzaman = pygame.time.get_ticks()

        if self.manarejenerasyonu_ilkzaman - self.manarejenerasyonu_sonzaman > 2500:
            if self.mana + self.manaregen > self.totalmana:
                self.mana = self.totalmana
            else:
                self.mana += self.manaregen
            self.manarejenerasyonu_sonzaman = pygame.time.get_ticks()
        self.yon2 = ""

        if self.Tus[pygame.K_a]:
            self.harekete_basladi = pygame.time.get_ticks()
            self.OyuncuX -= self.hiz
            self.yon = "sol"
            self.yon2 = "sol"
            if self.zipla != "süzül" or self.zipla != "zıpla":
                self.hareket = "sol"

        if self.Tus[pygame.K_d]:
            self.OyuncuX += self.hiz
            self.yon = "sağ"
            self.yon2 = "sağ"
            self.harekete_basladi = pygame.time.get_ticks()
            if self.zipla != "süzül" or self.zipla != "zıpla":
                self.hareket = "sağ"

        if self.Tus[pygame.K_SPACE] and self.ziplama_izni == "var":
            self.hareket = ""
            self.zipla = "zıpla"
            self.havada = True
            self.ucmasonzamani = pygame.time.get_ticks()

        if self.AyakRect.colliderect(self.ZeminRect):
            self.ziplama_izni = "var"
            self.ozelsaldiri_izni = True

        else:
            self.ziplama_izni = "yok"
            self.ozelsaldiri_izni = False

        if self.AyakRect.colliderect(self.ZeminRect) and self.zipla == "süzül":
            self.hareket = "stabil"
        self.ucx = 44
        self.ucy = 20

        self.ucma_ilkzamani = pygame.time.get_ticks()
        if self.havada:
            self.OyuncuY -= self.yuksel
            if self.ucma_ilkzamani - self.ucmasonzamani > 25:
                self.yuksel -= 2
                if self.yuksel == 0:
                    self.yuksel = 22
                    self.havada = False
                    self.zipla = "süzül"

        elif not self.havada and not self.AyakRect.colliderect(self.ZeminRect):
            self.OyuncuY += self.asagiin
            if self.ucma_ilkzamani - self.ucmasonzamani > 25:
                self.asagiin += 1
                self.ucmasonzamani = pygame.time.get_ticks()

        if self.AyakRect.colliderect(self.ZeminRect):
            self.asagiin = 5

        self.durum_ilkzaman = pygame.time.get_ticks()
        if self.mouse.get_pressed()[2]:
            if self.hareket == "sağ" or self.yon == "sağ":
                if self.durum == "idle1":
                    if self.durum_ilkzaman - self.durum_sonzaman > 120:
                        self.IdleListesi = [self.Idle10, self.Idle11, self.Idle12, self.Idle13]
                        self.IdleSolListesi = [self.IdleSol10, self.IdleSol11, self.IdleSol12, self.IdleSol13]
                        self.durum = "idle2"
                        self.durum_sonzaman = pygame.time.get_ticks()
                        self.hiz -= 1
                        self.ad += 5

                elif self.durum == "idle2":
                    if self.durum_ilkzaman - self.durum_sonzaman > 120:
                        self.IdleListesi = [self.Idle0, self.Idle1, self.Idle2, self.Idle3]
                        self.IdleSolListesi = [self.IdleSol0, self.IdleSol1, self.IdleSol2, self.IdleSol3]
                        self.durum = "idle1"
                        self.durum_sonzaman = pygame.time.get_ticks()
                        self.hiz += 1
                        self.ad -= 5

            else:
                if self.durum == "idle1":
                    if self.durum_ilkzaman - self.durum_sonzaman > 103:
                        self.IdleListesi = [self.Idle10, self.Idle11, self.Idle12, self.Idle13]
                        self.IdleSolListesi = [self.IdleSol10, self.IdleSol11, self.IdleSol12, self.IdleSol13]
                        self.durum = "idle2"
                        self.durum_sonzaman = pygame.time.get_ticks()
                        self.hiz -= 1
                        self.ad += 5

                elif self.durum == "idle2":
                    if self.durum_ilkzaman - self.durum_sonzaman > 103:
                        self.IdleListesi = [self.Idle0, self.Idle1, self.Idle2, self.Idle3]
                        self.IdleSolListesi = [self.IdleSol0, self.IdleSol1, self.IdleSol2, self.IdleSol3]
                        self.durum = "idle1"
                        self.durum_sonzaman = pygame.time.get_ticks()
                        self.hiz += 1
                        self.ad -= 5

        if self.ilkzaman - self.harekete_basladi > 85 and self.hareket != "saldır" and "çök" not in self.hareket:
            self.hareket = "stabil"

        elif self.ilkzaman - self.harekete_basladi > len(self.Saldir0Listesi) * 90 and self.hareket == "saldır":
            self.hareket = "stabil"

        if self.zipla == "zıpla" or self.zipla == "süzül":
            self.hareket = ""

    def Saldir(self, hedefler: list):

        for hedef in hedefler:
            if self.mouse.get_pressed()[0] == 1:
                self.hareket = "saldır"
                self.harekete_basladi = pygame.time.get_ticks()

            if self.hareket != "saldır":
                self.sahne_saldiri0 = 0
                self.sahne_solsaldir = 0

            if self.yon == "sağ":
                self.KilicRect = pygame.Rect(self.OyuncuX + 100, self.OyuncuY, 70, self.ScaleY)

            elif self.yon == "sol":
                self.KilicRect = pygame.Rect(self.OyuncuX, self.OyuncuY, 70, self.ScaleY)

            if self.OyuncuX - hedef.blitx > 0:
                hedef.hasaryonu = "sağ"

            elif self.OyuncuX - hedef.blitx < 0:
                hedef.hasaryonu = "sol"

            if self.KilicRect.colliderect(hedef.kord) and self.hareket == "saldır" and self.hasar_ver:
                hedef.can -= self.ad
                self.hasar_ver = False
                hedef.hasar = True

    def OzelSaldiri(self, dusmanlar: list):
        self.Tus = pygame.key.get_pressed()
        self.collidskill = pygame.Rect(self.OyuncuX, self.OyuncuY, self.ScaleX, self.ScaleY)
        for dusman in dusmanlar:
            if dusman.hareket != "ölü":
                if dusman.kord.colliderect(self.collidskill) and self.ozelsaldiri_izni == True and self.mana - 5 > 0:
                    if self.Tus[pygame.K_d] and self.Tus[pygame.K_f] and dusman.kord.colliderect(self.collidskill):
                        self.hareket = "özel 1 sağ"
                        self.mana -= 5

                    if self.Tus[pygame.K_a] and self.Tus[pygame.K_f] and dusman.kord.colliderect(self.collidskill):
                        self.hareket = "özel 1 sol"
                        self.mana -= 5

    def SaklanSaldiri(self, calilar: list):
        self.Tus = pygame.key.get_pressed()
        tekrar = 0
        for cali in calilar:
            if self.hareket != "sol" and self.hareket != "sağ":
                if not self.Tus[pygame.K_LCTRL] and cali.calicollid.colliderect(self.OyuncuRect):
                    self.gizlen = False

                elif self.Tus[pygame.K_LCTRL] and cali.calicollid.colliderect(self.OyuncuRect) and self.yon == "sağ":
                    self.hareket = "çök sağ"

                elif self.Tus[pygame.K_LCTRL] and cali.calicollid.colliderect(self.OyuncuRect) and self.yon == "sol":
                    self.hareket = "çök sol"

            if not self.OyuncuRect.colliderect(cali.calicollid):
                tekrar += 1

            if tekrar == len(calilar):
                self.gizlen = False
