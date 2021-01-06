from character import *
from dusman import *
from dusman2 import *
from dusman3 import *
from itemler import *
import pygame
import sqlite3
import time
import random

pygame.init()

con = sqlite3.connect("Bilgiler.db")

cursor = con.cursor()


def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Bilgiler (coin INT, total_can INT, can INT, exp INT, level INT, "
                   "yetenek_puani INT, zırh INT, dayanıklılık INT, total_exp INT, total_mana INT, mana INT, "
                   "kılıç_skill_level INT, kalkan_skill_level INT, ayak_skill_level INT, can_rejen INT, mana_rejen INT,"
                   "level_puani INT, hiz INT, ad INT, chunk INT)")


def EnvanterTablosuOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Envanter (slot TEXT)")


def KullanilanEnvanter():
    cursor.execute("CREATE TABLE IF NOT EXISTS KullanEnvanter (slot TEXT)")


def MarketEnvanterOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Market (slot TEXT, zaman INT)")


tabloolustur()
EnvanterTablosuOlustur()
KullanilanEnvanter()
MarketEnvanterOlustur()

tablo = "Bilgiler"


def KayitAl(coin, totalcan, can, exp, level, yetenek_puani, zirh, dayaniklilik,  totalexp, totalmana, mana, kilic,
            kalkan, ayak, canrejen, manarejen, level_puani, hiz, ad, chunk):
    cursor.execute("DELETE FROM {} ".format(tablo))
    cursor.execute("INSERT INTO {} (coin ,total_can, can, exp, level, yetenek_puani, zırh, dayanıklılık, total_exp, "
                   "total_mana, mana, kılıç_skill_level, kalkan_skill_level , ayak_skill_level ,can_rejen, mana_rejen, "
                   "level_puani, hiz, ad, chunk) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(tablo), (coin,
                   totalcan, can, exp, level, yetenek_puani, zirh, dayaniklilik, totalexp, totalmana, mana, kilic,
                   kalkan, ayak, canrejen, manarejen, level_puani, hiz, ad, chunk))
    con.commit()


def KayitAlEnvanter(envanter: list):
    cursor.execute("DELETE FROM Envanter")
    for item in envanter:
        cursor.execute("INSERT INTO Envanter VALUES ('" + item.isim + "')")
    con.commit()


def KayitAlKullanEnvanter(envanter1: list):
    cursor.execute("DELETE FROM KullanEnvanter")
    for item in envanter1:
        cursor.execute("INSERT INTO KullanEnvanter VALUES ('" + item.isim + "')")
    con.commit()


def MarketKayit(itemler: list, zaman):
    cursor.execute("DELETE FROM Market")
    for item in itemler:
        cursor.execute("INSERT INTO Market VALUES ('" + item.isim + "', " + str(int(zaman)) + ")")
    con.commit()


class BizimOyunumuz:
    def __init__(self):
        self.pencere_genisligi = 1280
        self.pencere_yuksekligi = 720
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi, self.pencere_yuksekligi))
        pygame.display.set_caption("Maceracı PABU")
        self.Clock = pygame.time.Clock()
        self.Arkaplan1 = pygame.image.load("Resimler/Orman2.png").convert_alpha()
        self.Arkaplan1 = pygame.transform.scale(self.Arkaplan1, (10880, self.pencere_yuksekligi))
        self.Arkaplan1X = -3000
        self.Arkaplan1Y = 0
        self.Zemin = pygame.image.load("Resimler/zemin.png").convert_alpha()
        self.ZeminX = -10000
        self.music = pygame.mixer.Sound("ses efektleri/Ambient Music.wav")
        self.cursor = pygame.image.load("Resimler/imlec-export.png").convert_alpha()
        self.cursor_kucuk = pygame.image.load("Resimler/imlec-export1.png").convert_alpha()
        self.cursor_resim = self.cursor
        self.music.set_volume(0.03)

        self.Oyuncu = Oyuncu()
        self.Dusman = Dusman()
        self.Dusman2 = Dusman2()
        self.Dusman3 = Dusman3()
        self.TumDusmanlar = [Dusman(), Dusman2(), Dusman3()]
        self.Dusmanlar = [self.Dusman, self.Dusman2, self.Dusman3]
        self.DusmanlarChunk = [self.Dusman, self.Dusman2, self.Dusman3]
        self.Oyun_Durumu = "Oyun"
        self.Oyun_Durumu2 = ""
        self.Envanter = pygame.image.load("Resimler/inventory_preset (1).png").convert_alpha()
        self.Envanter = pygame.transform.scale(self.Envanter, (870, 640))
        self.Ozellikler = pygame.image.load("Resimler/Özellikler2.png").convert_alpha()
        self.Ozellikler = pygame.transform.scale(self.Ozellikler, (645, 660))
        self.EnvanterUstu = pygame.image.load("Resimler/alt envanter.png").convert_alpha()
        self.EnvanterUstu = pygame.transform.scale(self.EnvanterUstu, (540, 40))
        self.OyuncuGosterim = pygame.transform.scale(self.Oyuncu.Idle0, (250, 185))
        self.SkillAgaci = pygame.image.load("Resimler/Özellikler.png").convert_alpha()
        self.SkillAgaci = pygame.transform.scale(self.SkillAgaci, (610, 610))
        self.OzelliklerSkill = pygame.image.load("Resimler/ÖzelliklerSkill.png").convert_alpha()
        self.OzelliklerSkill = pygame.transform.scale(self.OzelliklerSkill, (645, 660))
        self.YanTaraf = pygame.image.load("Resimler/yan taraf.png").convert_alpha()
        self.YanTaraf = pygame.transform.scale(self.YanTaraf, (31, 185))
        self.collid2 = pygame.Rect(0, 309, 30, 30)
        self.collid3 = pygame.Rect(0, 350, 30, 30)
        self.collid4 = pygame.Rect(0, 387, 30, 30)
        self.collid5 = pygame.Rect(0, 423, 30, 30)

        self.font = pygame.font.Font("m5x7.ttf", 40)
        self.marketfont = pygame.font.Font("m5x7.ttf", 60)
        self.itemfontu = pygame.font.Font("m5x7.ttf", 34)
        self.mouse = pygame.mouse
        self.mouse.set_visible(False)
        self.EnvanterKutusu = pygame.Rect(325, 27, 39, 29)
        self.OzelliklerKutusu = pygame.Rect(378, 27, 39, 29)
        self.SkillAgaciKutusu = pygame.Rect(428, 27, 39, 29)
        self.SkillAgaciKutusu2 = pygame.Rect(480, 27, 39, 29)
        self.itemx = 324
        self.itemy = 149
        self.ilkzaman = pygame.time.get_ticks()
        self.sonzaman = pygame.time.get_ticks()
        self.itemkullancollid1 = pygame.Rect(762, 501, 53, 61)
        self.itemkullancollid2 = pygame.Rect(820, 501, 53, 61)
        self.itemkullancollid3 = pygame.Rect(1027, 501, 53, 61)
        self.itemkullancollid4 = pygame.Rect(1085, 501, 53, 61)
        self.kafalikcollid = pygame.Rect(901, 154, 99, 110)
        self.zirhcollid = pygame.Rect(896, 276, 109, 188)
        self.kilic_skillcollid = pygame.Rect(583, 255, 63, 60)
        self.kalkan_skillcoliid = pygame.Rect(583, 405, 67, 60)
        self.ayak_skillcollid = pygame.Rect(583, 552, 67, 60)
        self.skill_ilkzaman = pygame.time.get_ticks()
        self.skill_sonzaman = pygame.time.get_ticks()
        self.saklanskillresim = pygame.image.load("Itemler/tile063.png").convert_alpha()
        self.saklanskillresim = pygame.transform.scale(self.saklanskillresim, (64, 60))
        self.Market = pygame.image.load("Resimler/market.png").convert_alpha()
        self.Market = pygame.transform.scale(self.Market, (500, 500))
        self.MarketCollid = pygame.Rect(-2500, 400, 650, 500)
        self.MarketArayuz = pygame.image.load("Resimler/market arayüz.png").convert_alpha()
        self.MarketArayuz = pygame.transform.scale(self.MarketArayuz, (1070, 490))
        self.SatCollid = pygame.Rect(824, 391, 131, 70)
        self.AlCollid = pygame.Rect(978, 392, 131, 72)
        self.Demirci = pygame.image.load("Resimler/demirci.png").convert_alpha()
        self.Demirci = pygame.transform.scale(self.Demirci, (500, 500))
        self.DemirciX = 4500
        self.Gorevler = pygame.image.load("Resimler/yan görevler.png").convert_alpha()
        self.Gorevler = pygame.transform.scale(self.Gorevler, (300, 450))
        self.GorevlerX = 400
        self.GorevlerY = 200
        self.KaydirX = 667
        self.KaydirY = 252
        self.gorevtutus = False
        self.kaydir = pygame.image.load("Resimler/kaydır.png").convert_alpha()
        self.kaydir = pygame.transform.scale(self.kaydir, (9, 54))
        self.kaydirBool = False
        self.kayust_collid = pygame.Rect(667, 246, 8, 6)
        self.kayalt_collid = pygame.Rect(667, 624, 8, 6)
        self.uyarenvanterdolu = pygame.image.load("Resimler/uyar envanter dolu.png").convert_alpha()
        self.uyarilkzaman = pygame.time.get_ticks()
        self.uyarsonzaman = pygame.time.get_ticks()
        self.ToplamCan_Collid = pygame.Rect(584, 215, 31, 30)
        self.ToplamMana_Collid = pygame.Rect(584, 250, 31, 30)
        self.ToplamSaldiriGucu_Collid = pygame.Rect(584, 285, 31, 30)
        self.ToplamHiz_Collid = pygame.Rect(584, 320, 31, 30)
        self.ToplamDayaniklilik_Collid = pygame.Rect(584, 355, 31, 30)
        self.blituyari = ""
        self.Itemler = [Ring1(), Ring2(), Ring3(), Necklase1(), Necklase2(), Necklase3(), Zirh1(), Zirh2(), Zirh3(),
                        Zirh4(), Sapka1(), Sapka2(), Sapka3(), Sapka4(), BosItem()]
        cursor.execute("SELECT * FROM Market")
        data = cursor.fetchall()
        self.MarketEnvanter = []
        self.BosluItemler = [Ring1(), Ring2(), Ring3(), Necklase1(), Necklase2(), Necklase3(), Zirh1(), Zirh2(),
                             Zirh3(), Zirh4(), Sapka1(), Sapka2(), Sapka3(), Sapka4(), BosItem(), BosItem(), BosItem(),
                             BosItem(), BosItem(), BosItem()]
        if len(data) == 49:
            for item1 in data:
                for item2 in self.Itemler:
                    if item1[0] == item2.isim:
                        self.MarketEnvanter.append(item2)
                        self.Itemler = [Ring1(), Ring2(), Ring3(), Necklase1(), Necklase2(), Necklase3(), Zirh1(),
                                        Zirh2(), Zirh4(), Sapka1(), Sapka2(), Sapka3(), Sapka4(), BosItem()]

        else:
            for x in range(1, 50):
                item = random.choice(self.BosluItemler)
                self.MarketEnvanter.append(item)
                self.BosluItemler = [Ring1(), Ring2(), Ring3(), Necklase1(), Necklase2(), Necklase3(), Zirh1(), Zirh2(),
                                     Zirh3(), Zirh4(), Sapka1(), Sapka2(), Sapka3(), Sapka4(), BosItem(), BosItem(),
                                     BosItem(), BosItem(), BosItem(), BosItem()]

        class Cali:
            def __init__(self, x):
                self.cali = pygame.image.load("Resimler/çalı.png").convert_alpha()
                self.cali = pygame.transform.scale(self.cali, (100, 60))
                self.x = x
                self.y = 610
                self.calicollid = pygame.Rect(self.x, self.y, 100, 60)

        self.cali_listesi = []
        for x in range(-2500, 8000, 1000):
            self.cali_listesi.append(Cali(x))

        self.spawnilkzaman = time.time()
        self.spawnsonzaman = time.time()
        self.say = False
        cursor.execute("SELECT zaman FROM Market")
        datazaman = cursor.fetchall()
        if len(datazaman) != 0:
            self.marketilkzaman = datazaman[0][0]

        else:
            self.marketilkzaman = time.time()
        self.marketsonzaman = time.time()
        self.yukseltilkzaman = pygame.time.get_ticks()
        self.yukseltsonzaman = pygame.time.get_ticks()

    def Cizim(self):
        self.Pencere.blit(self.Arkaplan1, (self.Arkaplan1X, self.Arkaplan1Y))
        self.MarketCollid = (self.Arkaplan1X + 1050, 440, 365, 225)
        self.Pencere.blit(self.YanTaraf, (0, 270))
        self.Pencere.blit(self.Zemin, (self.ZeminX, 652))
        self.Pencere.blit(self.Market, (self.Arkaplan1X + 1000, 155))
        self.Pencere.blit(self.Demirci, (self.Arkaplan1X + 6000, 332))
        if -430 > self.Arkaplan1X > -9260:
            self.Oyuncu.chunk = 0
        self.mouseX = self.mouse.get_pos()[0] + 3
        self.mouseY = self.mouse.get_pos()[1] + 3
        self.mousecollid = pygame.Rect(self.mouseX, self.mouseY, 1, 1)

        self.Oyuncu.Cizdir(self.Pencere)
        for cali in self.cali_listesi:
            self.Pencere.blit(cali.cali, (cali.x, cali.y))

        for dusman in self.Dusmanlar:
            dusman.Cizdir(self.Pencere, self.Oyuncu)
            if dusman.hareket == "ölü":
                if not dusman.expverdimi:
                    self.Oyuncu.exp += 10
                    dusman.expverdimi = True

        self.marketsonzaman = time.time()
        if self.marketsonzaman - self.marketilkzaman > 900:
            self.MarketEnvanter = list()
            for x in range(1, 50):
                item = random.choice(self.BosluItemler)
                self.MarketEnvanter.append(item)
                self.BosluItemler = [Ring1(), Ring2(), Ring3(), Necklase1(), Necklase2(), Necklase3(), Zirh1(), Zirh2(),
                                     Zirh3(), Zirh4(), Sapka1(), Sapka2(), Sapka3(), Sapka4(), BosItem(), BosItem(),
                                     BosItem(), BosItem(), BosItem(), BosItem()]

            self.marketilkzaman = time.time()

        # self.music.play(-1)
        """if self.mouse.get_pressed()[0] == 1:
            print(self.mouse.get_pos()[0] + 3, self.mouse.get_pos()[1] + 3)
        
        for cali in self.cali_listesi:
            pygame.draw.rect(self.Pencere, (0, 0, 0), cali.calicollid)
            
        for dusman in self.Dusmanlar:
            pygame.draw.rect(self.Pencere, (0, 0, 0), dusman.kord)
        pygame.draw.rect(self.Pencere, (0, 0, 0), self.OzelliklerKutusu)
        pygame.draw.rect(self.Pencere, (0, 0, 0), self.SkillAgaciKutusu2)
        pygame.draw.rect(self.Pencere, (0, 0, 0), self.EnvanterKutusu)
        pygame.draw.rect(self.Pencere, (0, 0, 0), self.SkillAgaciKutusu)"""

        if self.Oyun_Durumu == "Oyun":
            self.yondegis = self.Oyuncu.OyuncuX - 500

            self.Oyuncu.OyuncuX = 500
            self.Arkaplan1X -= self.yondegis
            self.ZeminX -= self.yondegis
            for dusman in self.Dusmanlar:
                dusman.DusmanX -= self.yondegis
                if dusman.hareket == "ölü":
                    dusman.itemx -= self.yondegis
                    dusman.coinx -= self.yondegis

            for cali in self.cali_listesi:
                cali.x -= self.yondegis
                cali.calicollid = pygame.Rect(cali.x, cali.y, 100, 60)

            if -9260 > self.Arkaplan1X > -1290:
                self.Oyuncu.chunk = 1

        elif self.Oyun_Durumu == "Envanter":
            self.itemx = 323
            self.itemy = 148
            self.Oyuncu.sahne_hareket = 0
            self.Pencere.blit(self.Envanter, (300, 50))
            self.Pencere.blit(self.EnvanterUstu, (305, 22))
            self.Pencere.blit(self.font.render("Envanter", True, (0, 0, 0)), (470, 85))
            for item in self.Oyuncu.envanter:
                item.fiyat = item.level * 5
                if (not item.secili) and (not item.kullanim):
                    item.itemx = self.itemx
                    item.itemy = self.itemy

                elif item.secili and (not item.kullanim):
                    item.itemx = self.mouseX - 22
                    item.itemy = self.mouseY - 22

                for item2 in self.Oyuncu.envanter:
                    item2.colliditem = pygame.Rect(item2.itemx, item.itemy, 53, 58)

                self.Pencere.blit(item.resim, (item.itemx, item.itemy))
                self.itemcollid = pygame.Rect(item.itemx, item.itemy, 50, 60)
                self.ilkzaman = pygame.time.get_ticks()

                if self.mouse.get_pressed()[0] == 1 and self.mousecollid.colliderect(
                        self.itemcollid) == 1 and item.isim != "":
                    self.sonzaman = pygame.time.get_ticks()
                    item.baslat = True

                if 50 > self.ilkzaman - self.sonzaman > 20 and item.baslat:
                    item.secili = True

                if self.mouse.get_pressed()[0] == 1 and item.secili:
                    for item2 in self.Oyuncu.envanter:
                        if item2.colliditem.colliderect(self.mousecollid):
                            item.itemx = item2.itemx
                            item.itemy = item2.itemy
                            item.secili = False
                            item.baslat = False

                if self.Oyuncu.level >= item.level:
                    if self.mouse.get_pressed()[0] == 1 and self.itemkullancollid1.colliderect(self.itemcollid) \
                            and ("şapka" not in item.isim) and ("zırh" not in item.isim):
                        item.itemx = 763
                        item.itemy = 501
                        item.kullanim = False
                        if self.Oyuncu.kullanenvanter[0].isim == "":
                            self.Oyuncu.kullanenvanter[0] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[0].isim != "":
                            item.Etki(self.Oyuncu)
                            self.itemdegis = self.Oyuncu.kullanenvanter[0]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.Oyuncu.kullanenvanter[0] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis

                    elif self.mouse.get_pressed()[0] == 1 and self.itemkullancollid2.colliderect(self.itemcollid) \
                            and "şapka" not in item.isim and "zırh" not in item.isim:
                        item.itemx = 822
                        item.itemy = 501
                        item.kullanim = False
                        if self.Oyuncu.kullanenvanter[1].isim == "":
                            self.Oyuncu.kullanenvanter[1] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[1].isim != "":
                            item.Etki(self.Oyuncu)
                            self.itemdegis = self.Oyuncu.kullanenvanter[1]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.Oyuncu.kullanenvanter[1] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis

                    elif self.mouse.get_pressed()[0] == 1 and self.itemkullancollid3.colliderect(self.itemcollid) \
                            and "şapka" not in item.isim and "zırh" not in item.isim:
                        item.itemx = 1028
                        item.itemy = 501
                        item.kullanim = False
                        if self.Oyuncu.kullanenvanter[2].isim == "":
                            self.Oyuncu.kullanenvanter[2] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[2].isim != "":
                            item.Etki(self.Oyuncu)
                            self.itemdegis = self.Oyuncu.kullanenvanter[2]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.Oyuncu.kullanenvanter[2] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis

                    elif self.mouse.get_pressed()[0] == 1 and self.itemkullancollid4.colliderect(self.itemcollid) \
                            and "şapka" not in item.isim and "zırh" not in item.isim:
                        item.itemx = 1087
                        item.itemy = 501
                        item.kullanim = False
                        if self.Oyuncu.kullanenvanter[3].isim == "":
                            self.Oyuncu.kullanenvanter[3] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[3].isim != "":
                            item.Etki(self.Oyuncu)
                            self.itemdegis = self.Oyuncu.kullanenvanter[3]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.Oyuncu.kullanenvanter[3] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis

                    elif self.mouse.get_pressed()[0] == 1 and self.kafalikcollid.colliderect(self.itemcollid) \
                            and "şapka" in item.isim and "zırh" not in item.isim:
                        item.itemx = 901
                        item.itemy = 154
                        item.kullanim = False
                        item.resim = item.itemresim

                        if self.Oyuncu.kullanenvanter[4].isim == "":
                            self.Oyuncu.kullanenvanter[4] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[4].isim != "":
                            self.itemdegis = self.Oyuncu.kullanenvanter[4]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.itemdegis.resim = self.itemdegis.saklaresim
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis
                            self.Oyuncu.kullanenvanter[4] = item
                            item.Etki(self.Oyuncu)

                    elif self.mouse.get_pressed()[0] == 1 and self.zirhcollid.colliderect(self.itemcollid) \
                            and "zırh" in item.isim:
                        item.itemx = 905
                        item.itemy = 300
                        item.kullanim = False
                        item.resim = item.itemresim

                        if self.Oyuncu.kullanenvanter[5].isim == "":
                            self.Oyuncu.kullanenvanter[5] = item
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = BosItem()
                            item.Etki(self.Oyuncu)

                        elif self.Oyuncu.kullanenvanter[5].isim != "":
                            self.itemdegis = self.Oyuncu.kullanenvanter[5]
                            self.itemdegis.Etki_Pasif(self.Oyuncu)
                            self.itemdegis.resim = self.itemdegis.saklaresim
                            self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.itemdegis
                            self.Oyuncu.kullanenvanter[5] = item
                            item.Etki(self.Oyuncu)

                elif self.Oyuncu.level < item.level and item.secili and (not item.kullanim):
                    self.Pencere.blit(self.uyarenvanterdolu, (400, 300))
                    self.Pencere.blit(self.marketfont.render("Seviyen Yetmiyor!", True, (0, 0, 0)), (475, 365))

                self.itemx += 57

                if self.itemx > 680:
                    self.itemy += 65
                    self.itemx = 323

                for item4 in self.Oyuncu.kullanenvanter:
                    self.Pencere.blit(item4.resim, (item4.itemx, item4.itemy))

            self.itemx = 323
            self.itemy = 148

            for item in self.Oyuncu.envanter:
                item.fiyat = item.level * 5
                self.itemcollid = pygame.Rect(item.itemx, item.itemy, 50, 60)
                if self.mousecollid.colliderect(self.itemcollid):
                    if item.isim != "" and not item.secili:
                        self.Pencere.blit(item.itemgoster, (item.itemx, item.itemy))
                        self.Pencere.blit(item.resim, (item.itemx + 24, item.itemy + 25))
                        self.Pencere.blit(self.itemfontu.render("Isim: " + item.takma_lakap, True, (0, 0, 0)),
                                          (item.itemx + 95, item.itemy + 20))
                        self.Pencere.blit(self.itemfontu.render("Level: " + str(item.level), True, (0, 0, 0)),
                                          (item.itemx + 95, item.itemy + 45))
                        self.Pencere.blit(self.itemfontu.render("Etki: " + item.etki, True, (0, 0, 0)),
                                          (item.itemx + 95, item.itemy + 70))
                        if item.etki2 != "":
                            self.Pencere.blit(self.itemfontu.render("Etki 2: " + item.etki2, True, (0, 0, 0)),
                                              (item.itemx + 95, item.itemy + 95))
                            self.Pencere.blit(self.itemfontu.render("Fiyat: " + str(item.fiyat), True, (0, 0, 0)),
                                              (item.itemx + 95, item.itemy + 120))

                        else:
                            self.Pencere.blit(self.itemfontu.render("Fiyat: " + str(item.fiyat), True, (0, 0, 0)),
                                              (item.itemx + 95, item.itemy + 95))

                if not item.kullanim:
                    item.itemx = self.itemx
                    item.itemy = self.itemy

        elif self.Oyun_Durumu == "Özellikler":
            self.Pencere.blit(self.EnvanterUstu, (305, 20))
            self.Pencere.blit(self.Ozellikler, (295, 41))
            self.Pencere.blit(self.font.render("Özellikler", True, (0, 0, 0)), (530, 90))
            self.Pencere.blit(self.OyuncuGosterim, (300, 250))
            self.Pencere.blit(
                self.font.render("Can: " + str(self.Oyuncu.can) + " - " + str(self.Oyuncu.totalcan), True, (0, 0, 0)),
                (550, 200))
            self.Pencere.blit(
                self.font.render("Mana: " + str(self.Oyuncu.mana) + " - " + str(self.Oyuncu.totalmana), True,
                                 (0, 0, 0)),
                (550, 260))
            self.Pencere.blit(self.font.render("Seviye: " + str(self.Oyuncu.level), True, (0, 0, 0)), (550, 320))
            self.Pencere.blit(
                self.font.render("Exp: " + str(self.Oyuncu.exp) + " - " + str(self.Oyuncu.totalexp), True, (0, 0, 0)),
                (550, 380))
            self.Pencere.blit(self.font.render("Zırh: " + str(self.Oyuncu.zirh), True, (0, 0, 0)),
                              (550, 440))

        elif self.Oyun_Durumu == "Skill Ağacı":
            self.Pencere.blit(self.EnvanterUstu, (305, 20))
            self.Pencere.blit(self.SkillAgaci, (305, 60))
            self.Pencere.blit(self.font.render("Özellikler;", True, (0, 0, 0)), (355, 180))
            self.Pencere.blit(self.font.render("Toplam Can: " + str(self.Oyuncu.totalcan), True, (0, 0, 0)), (355, 215))
            self.Pencere.blit(self.font.render("Toplam Mana: " + str(self.Oyuncu.totalmana), True, (0, 0, 0)),
                              (355, 250))
            self.Pencere.blit(self.font.render("Saldırı Gücü: " + str(self.Oyuncu.totalad), True, (0, 0, 0)), (355, 285))
            self.Pencere.blit(self.font.render("Hız: " + str(self.Oyuncu.hiz), True, (0, 0, 0)), (355, 320))
            self.Pencere.blit(self.font.render("Dayanıklılık: " + str(self.Oyuncu.dayaniklilik), True, (0, 0, 0)),
                              (355, 355))

            self.Pencere.blit(self.font.render("Yetenek Artırma Puanı: " + str(self.Oyuncu.levelpuani), True, (0, 0, 0)), (530, 180))
            """pygame.draw.rect(self.Pencere, (255, 255, 255), self.ToplamCan_Collid)
            pygame.draw.rect(self.Pencere, (255, 255, 255), self.ToplamMana_Collid)
            pygame.draw.rect(self.Pencere, (255, 255, 255), self.ToplamSaldiriGucu_Collid)
            pygame.draw.rect(self.Pencere, (255, 255, 255), self.ToplamHiz_Collid)
            pygame.draw.rect(self.Pencere, (255, 255, 255), self.ToplamDayaniklilik_Collid)"""

            self.yukseltilkzaman = pygame.time.get_ticks()

            if self.yukseltilkzaman - self.yukseltsonzaman > 200 and self.Oyuncu.levelpuani > 0:
                if self.mousecollid.colliderect(self.ToplamCan_Collid) and self.mouse.get_pressed()[0] == 1:
                    self.Oyuncu.totalcan += 10
                    self.yukseltsonzaman = pygame.time.get_ticks()
                    self.Oyuncu.levelpuani -= 1

                elif self.mousecollid.colliderect(self.ToplamMana_Collid) and self.mouse.get_pressed()[0] == 1:
                    self.Oyuncu.totalmana += 10
                    self.yukseltsonzaman = pygame.time.get_ticks()
                    self.Oyuncu.levelpuani -= 1

                elif self.mousecollid.colliderect(self.ToplamSaldiriGucu_Collid) and self.mouse.get_pressed()[0] == 1:
                    self.Oyuncu.ad += 1
                    self.Oyuncu.totalad += 1
                    self.yukseltsonzaman = pygame.time.get_ticks()
                    self.Oyuncu.levelpuani -= 1

                elif self.mousecollid.colliderect(self.ToplamHiz_Collid) and self.mouse.get_pressed()[0] == 1:
                    self.Oyuncu.hiz += 1
                    self.Oyuncu.totalhiz += 1
                    self.yukseltsonzaman = pygame.time.get_ticks()
                    self.Oyuncu.levelpuani -= 1

                elif self.mousecollid.colliderect(self.ToplamDayaniklilik_Collid) and self.mouse.get_pressed()[0] == 1:
                    self.Oyuncu.dayaniklilik += 2
                    self.yukseltsonzaman = pygame.time.get_ticks()
                    self.Oyuncu.levelpuani -= 1

        elif self.Oyun_Durumu == "Skiller":
            self.Pencere.blit(self.EnvanterUstu, (305, 20))
            self.Pencere.blit(self.OzelliklerSkill, (295, 55))
            self.Pencere.blit(self.saklanskillresim, (585, 403))
            self.Pencere.blit(self.font.render("Yetenek Puanları: " + str(self.Oyuncu.yetenek_puani), True, (0, 0, 0)),
                              (500, 150))
            self.Pencere.blit(self.font.render("Farklı Kılıç Saldırıları", True, (0, 0, 0)), (487, 198))
            self.Pencere.blit(self.font.render("Level: " + str(self.Oyuncu.skill_kiliclevel), True, (0, 0, 0)),
                              (565, 223))
            self.Pencere.blit(self.font.render("Direnç ve Karşı Saldırılar", True, (0, 0, 0)), (480, 343))
            self.Pencere.blit(self.font.render("Level: " + str(self.Oyuncu.skill_kalkanlevel), True, (0, 0, 0)),
                              (567, 368))
            self.Pencere.blit(self.font.render("Atılma", True, (0, 0, 0)), (575, 498))
            self.Pencere.blit(self.font.render("Level: " + str(self.Oyuncu.skill_ayaklevel), True, (0, 0, 0)),
                              (570, 518))
            self.skill_ilkzaman = pygame.time.get_ticks()
            if self.Oyuncu.yetenek_puani > 0:
                if self.mousecollid.colliderect(self.kilic_skillcollid) and self.mouse.get_pressed()[0] == 1 \
                        and self.skill_ilkzaman - self.skill_sonzaman > 250:
                    self.skill_sonzaman = pygame.time.get_ticks()
                    self.Oyuncu.skill_kiliclevel += 1
                    self.Oyuncu.yetenek_puani -= 1
                    if self.Oyuncu.skill_kiliclevel == 1:
                        self.Saldir10oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-00.png")
                        self.Saldir10oyuncu = pygame.transform.scale(self.Saldir10oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Saldir11oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-01.png")
                        self.Saldir11oyuncu = pygame.transform.scale(self.Saldir11oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Saldir12oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-02.png")
                        self.Saldir12oyuncu = pygame.transform.scale(self.Saldir12oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Saldir13oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-03.png")
                        self.Saldir13oyuncu = pygame.transform.scale(self.Saldir13oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Saldir14oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-04.png")
                        self.Saldir14oyuncu = pygame.transform.scale(self.Saldir14oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Saldir15oyuncu = pygame.image.load(
                            "Adventurer/Individual Sprites/adventurer-attack2-05.png")
                        self.Saldir15oyuncu = pygame.transform.scale(self.Saldir15oyuncu,
                                                                     (self.Oyuncu.ScaleX, self.Oyuncu.ScaleY))
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir10oyuncu)
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir11oyuncu)
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir12oyuncu)
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir13oyuncu)
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir14oyuncu)
                        self.Oyuncu.Saldir0Listesi.append(self.Saldir15oyuncu)

                if self.mousecollid.colliderect(self.kalkan_skillcoliid) and self.mouse.get_pressed()[0] == 1 \
                        and self.skill_ilkzaman - self.skill_sonzaman > 250:
                    self.skill_sonzaman = pygame.time.get_ticks()
                    self.Oyuncu.skill_kalkanlevel += 1
                    self.Oyuncu.yetenek_puani -= 1
                if self.mousecollid.colliderect(self.ayak_skillcollid) and self.mouse.get_pressed()[0] == 1 \
                        and self.skill_ilkzaman - self.skill_sonzaman > 250:
                    self.skill_sonzaman = pygame.time.get_ticks()
                    self.Oyuncu.skill_ayaklevel += 1
                    self.Oyuncu.yetenek_puani -= 1

        elif self.Oyun_Durumu == "Market":
            self.itemx = 141
            self.itemy = 182
            self.Oyuncu.hareket = "stabil"
            self.Pencere.blit(self.MarketArayuz, (100, 100))
            self.Pencere.blit(self.font.render("Envanter", True, (0, 0, 0)), (240, 135))
            self.Pencere.blit(self.font.render("Market", True, (0, 0, 0)), (625, 160))
            self.Pencere.blit(self.marketfont.render("SAT", True, (0, 255, 0)), (860, 390))
            self.Pencere.blit(self.marketfont.render("AL", True, (255, 0, 0)), (1020, 390))
            self.Pencere.blit(self.marketfont.render("EZIO'NUN YERI", True, (0, 0, 0)), (850, 470))
            """pygame.draw.rect(self.Pencere, (0, 0, 0), self.SatCollid)
            pygame.draw.rect(self.Pencere, (0, 0, 0), self.AlCollid)"""
            for item in self.Oyuncu.envanter:
                item.fiyat = item.level * 5
                item.satisfiyat = item.fiyat * (7 / 10)
                if item.secili and (not item.kullanim):
                    self.Pencere.blit(self.font.render("Fiyat: " + str(item.satisfiyat), True, (0, 255, 0)),
                                      (830, 430))

                if (not item.secili) and (not item.kullanim):
                    item.market_itemx = self.itemx
                    item.marketitemy = self.itemy

                elif item.secili and (not item.kullanim):
                    item.market_itemx = self.mouseX - 22
                    item.marketitemy = self.mouseY - 22

                self.Pencere.blit(item.marketarayuz, (item.market_itemx, item.marketitemy))
                self.item_marketcollid = pygame.Rect(item.market_itemx, item.marketitemy, 38, 38)
                self.ilkzaman = pygame.time.get_ticks()

                if self.mouse.get_pressed()[0] == 1 and self.mousecollid.colliderect(self.item_marketcollid) == 1 \
                        and item.isim != "":
                    self.sonzaman = pygame.time.get_ticks()
                    item.baslat = True

                if 50 > self.ilkzaman - self.sonzaman > 20 and item.baslat:
                    item.secili = True

                if self.mouse.get_pressed()[0] == 1 and item.secili:
                    for item2 in self.Oyuncu.envanter:
                        item2.colliditem = pygame.Rect(item.market_itemx, item.marketitemy, 38, 38)
                        if item2.colliditem.colliderect(self.mousecollid):
                            item.market_itemx = item2.market_itemx
                            item.marketitemy = item2.marketitemy
                            item.secili = False
                            item.baslat = False

                if self.item_marketcollid.colliderect(self.SatCollid) and self.mouse.get_pressed()[0] == 1:
                    self.BosItem = BosItem()
                    self.Oyuncu.envanter[self.Oyuncu.envanter.index(item)] = self.BosItem
                    self.BosItem = BosItem()
                    self.Oyuncu.coin += item.satisfiyat

                self.itemx += 44

                if self.itemx > 440:
                    self.itemy += 44
                    self.itemx = 141

            self.itemx = 534
            self.itemy = 210

            for market_item in self.MarketEnvanter:
                market_item.fiyat = market_item.level * 5
                market_item.alisfiyat = market_item.fiyat * (13 / 10)
                if market_item.secili and (not market_item.kullanim):
                    self.Pencere.blit(self.font.render("Fiyat: " + str(market_item.alisfiyat), True, (255, 0, 0)),
                                      (990, 430))

                if (not market_item.secili) and (not market_item.kullanim):
                    market_item.market_itemx = self.itemx
                    market_item.marketitemy = self.itemy

                elif market_item.secili and (not market_item.kullanim):
                    market_item.market_itemx = self.mouseX - 22
                    market_item.marketitemy = self.mouseY - 22

                self.Pencere.blit(market_item.marketalisarayuz, (market_item.market_itemx, market_item.marketitemy))
                self.uyarilkzaman = pygame.time.get_ticks()
                if self.blituyari == "envanter dolu":
                    if self.uyarilkzaman - self.uyarsonzaman < 350:
                        self.Pencere.blit(self.uyarenvanterdolu, (400, 250))
                        self.Pencere.blit(self.marketfont.render("Envanterin Dolu!", True, (0, 0, 0)), (485, 335))

                    else:
                        self.blituyari = ""

                elif self.blituyari == "para yok":
                    if self.uyarilkzaman - self.uyarsonzaman < 350:
                        self.Pencere.blit(self.uyarenvanterdolu, (400, 250))
                        self.Pencere.blit(self.marketfont.render("Yeterli Paran Yok!", True, (0, 0, 0)), (485, 335))

                    else:
                        self.blituyari = ""

                self.item_marketcollid = pygame.Rect(market_item.market_itemx, market_item.marketitemy, 38, 38)
                self.ilkzaman = pygame.time.get_ticks()

                if self.mouse.get_pressed()[0] == 1 and self.mousecollid.colliderect(self.item_marketcollid) == 1 \
                        and market_item.isim != "":
                    self.sonzaman = pygame.time.get_ticks()
                    market_item.baslat = True

                if 50 > self.ilkzaman - self.sonzaman > 20 and market_item.baslat:
                    market_item.secili = True

                if self.mouse.get_pressed()[0] == 1 and market_item.secili:
                    for item2 in self.Oyuncu.envanter:
                        item2.colliditem = pygame.Rect(market_item.market_itemx, market_item.marketitemy, 38, 38)
                        if item2.colliditem.colliderect(self.mousecollid):
                            market_item.market_itemx = item2.market_itemx
                            market_item.marketitemy = item2.marketitemy
                            market_item.secili = False
                            market_item.baslat = False

                if self.item_marketcollid.colliderect(self.AlCollid) and self.mouse.get_pressed()[0] == 1:
                    if self.Oyuncu.coin > market_item.alisfiyat:
                        if self.Oyuncu.BosItem in self.Oyuncu.envanter:
                            for itemenvanter in self.Oyuncu.envanter:
                                if itemenvanter.isim == "":
                                    self.Oyuncu.envanter[self.Oyuncu.envanter.index(itemenvanter)] = market_item
                                    self.BosItem = BosItem()
                                    self.MarketEnvanter[self.MarketEnvanter.index(market_item)] = self.BosItem
                                    self.BosItem = BosItem()
                                    self.Oyuncu.coin -= market_item.alisfiyat
                                    self.blituyari = ""
                                    break

                        else:
                            self.blituyari = "envanter dolu"
                            self.uyarsonzaman = pygame.time.get_ticks()

                    else:
                        self.blituyari = "para yok"
                        self.uyarsonzaman = pygame.time.get_ticks()

                self.itemx += 38

                if self.itemx > 765:
                    self.itemx = 534
                    self.itemy += 46

            self.itemx = 141
            self.itemy = 182

        if self.Oyun_Durumu2 == "Yan Görevler":
            self.kayust_collid = pygame.Rect(self.GorevlerX + 267, self.GorevlerY + 46, 8, 6)
            self.kayalt_collid = pygame.Rect(self.GorevlerX + 267, self.GorevlerY + 424, 8, 6)
            self.gorevcollid = pygame.Rect(self.GorevlerX + 18, self.GorevlerY + 1, 262, 11)
            self.kaydircollid = pygame.Rect(self.KaydirX, self.KaydirY, 9, 54)
            if self.gorevtutus:
                self.GorevlerX = self.mouseX - 130
                self.GorevlerY = self.mouseY - 5
                self.KaydirX = self.mouseX + 137
                self.KaydirY = self.mouseY + 46

            self.Pencere.blit(self.Gorevler, (self.GorevlerX, self.GorevlerY))
            self.Pencere.blit(self.kaydir, (self.KaydirX, self.KaydirY))
            if self.kaydirBool:
                if self.kaydircollid.colliderect(self.kayalt_collid) and self.mouseY - 20 < self.KaydirY:
                    self.KaydirY = self.mouseY - 20

                elif self.kaydircollid.colliderect(self.kayust_collid) and self.mouseY - 20 > self.KaydirY:
                    self.KaydirY = self.mouseY - 20

                elif not self.kaydircollid.colliderect(self.kayalt_collid):
                    self.KaydirY = self.mouseY - 20

                elif not self.kaydircollid.colliderect(self.kayust_collid):
                    self.KaydirY = self.mouseY - 20

            if self.mouse.get_pressed()[0] == 1 and self.mousecollid.colliderect(self.gorevcollid):
                self.gorevtutus = True

            if self.mouse.get_pressed()[0] == 0 and self.gorevtutus:
                self.gorevtutus = False

            if self.mouse.get_pressed()[0] == 1 and self.kaydircollid.colliderect(self.mousecollid):
                self.kaydirBool = True

            if self.mouse.get_pressed()[0] == 0 and self.kaydirBool:
                self.kaydirBool = False

        if self.OzelliklerKutusu.colliderect(self.mousecollid) and self.mouse.get_pressed()[0] == 1:
            self.Oyun_Durumu = "Özellikler"

        elif self.EnvanterKutusu.colliderect(self.mousecollid) and self.mouse.get_pressed()[0] == 1:
            self.Oyun_Durumu = "Envanter"

        elif self.SkillAgaciKutusu.colliderect(self.mousecollid) and self.mouse.get_pressed()[0] == 1:
            self.Oyun_Durumu = "Skill Ağacı"

        elif self.SkillAgaciKutusu2.colliderect(self.mousecollid) and self.mouse.get_pressed()[0] == 1:
            self.Oyun_Durumu = "Skiller"

        if self.cursor == self.cursor_resim:
            self.Pencere.blit(self.cursor, (self.mouseX, self.mouseY))

        else:
            self.Pencere.blit(self.cursor, (self.mouseX + 3, self.mouseY + 3))

        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KayitAl(self.Oyuncu.coin, self.Oyuncu.totalcan, self.Oyuncu.can, self.Oyuncu.exp, self.Oyuncu.level,
                        self.Oyuncu.yetenek_puani, self.Oyuncu.zirh, self.Oyuncu.dayaniklilik,
                        int(self.Oyuncu.totalexp), self.Oyuncu.totalmana, self.Oyuncu.mana,
                        self.Oyuncu.skill_kiliclevel, self.Oyuncu.skill_kalkanlevel, self.Oyuncu.skill_ayaklevel,
                        self.Oyuncu.canregen, self.Oyuncu.manaregen, self.Oyuncu.levelpuani, self.Oyuncu.totalhiz,
                        self.Oyuncu.totalad, self.Oyuncu.chunk)
                KayitAlEnvanter(self.Oyuncu.envanter)
                KayitAlKullanEnvanter(self.Oyuncu.kullanenvanter)
                MarketKayit(self.MarketEnvanter, time.time())
                return "Son"

        self.Tus = pygame.key.get_pressed()

        if self.mouse.get_pressed()[0] == 1:
            self.cursor = self.cursor_kucuk

        else:
            self.cursor = self.cursor_resim

        if self.mouse.get_pressed()[0] == 1 and self.mousecollid.colliderect(self.collid3):
            self.Oyun_Durumu2 = "Yan Görevler"

        self.spawnilkzaman = time.time()
        for dusman in self.DusmanlarChunk:
            if dusman.hareket == "ölü":
                self.DusmanlarChunk.remove(dusman)
                self.say = True
                self.spawnsonzaman = time.time()

        if self.say:
            if self.spawnilkzaman - self.spawnsonzaman > 10:
                ekledusman = random.choice(self.TumDusmanlar)
                self.TumDusmanlar = [Dusman(), Dusman2()]
                ekledusman.DusmanX = random.randint(-500, 1700)
                self.Dusmanlar.append(ekledusman)
                self.DusmanlarChunk.append(ekledusman)
                self.say = False

        if self.Tus[pygame.K_e] and not self.Oyuncu.OyuncuRect.colliderect(self.MarketCollid):
            self.Oyun_Durumu = "Envanter"

        elif self.Tus[pygame.K_e] and self.Oyuncu.OyuncuRect.colliderect(self.MarketCollid):
            self.Oyun_Durumu = "Market"

        if self.Tus[pygame.K_ESCAPE] and (self.Oyun_Durumu == "Envanter" or self.Oyun_Durumu == "Özellikler" or
                                          self.Oyun_Durumu == "Skiller" or self.Oyun_Durumu == "Skill Ağacı" or
                                          self.Oyun_Durumu == "Market"):
            self.Oyun_Durumu = "Oyun"

        if self.Tus[pygame.K_ESCAPE] and self.Oyun_Durumu2 == "Yan Görevler":
            self.Oyun_Durumu2 = ""

        if self.Oyun_Durumu == "Oyun":
            self.Oyuncu.Saldir(self.Dusmanlar)
            for dusman in self.Dusmanlar:
                dusman.Hareket()
                dusman.Saldir(self.Oyuncu)
            self.Oyuncu.Hareket()
            self.Oyuncu.OzelSaldiri(self.Dusmanlar)
            self.Oyuncu.SaklanSaldiri(self.cali_listesi)

        self.Cizim()


Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()
