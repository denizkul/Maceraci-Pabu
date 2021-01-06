from itemler import *
import pygame
import random
import time


class Dusman3:
    def __init__(self):
        self.DusmanX = - 700
        self.DusmanY = 400
        self.Scale = 400

        self.Idle1 = pygame.image.load("Mushroom/mushroom_idle/tile000.png").convert_alpha()
        self.Idle1 = pygame.transform.scale(self.Idle1, (self.Scale, self.Scale))
        self.Idle2 = pygame.image.load("Mushroom/mushroom_idle/tile001.png").convert_alpha()
        self.Idle2 = pygame.transform.scale(self.Idle2, (self.Scale, self.Scale))
        self.Idle3 = pygame.image.load("Mushroom/mushroom_idle/tile002.png").convert_alpha()
        self.Idle3 = pygame.transform.scale(self.Idle3, (self.Scale, self.Scale))
        self.Idle4 = pygame.image.load("Mushroom/mushroom_idle/tile003.png").convert_alpha()
        self.Idle4 = pygame.transform.scale(self.Idle4, (self.Scale, self.Scale))
        self.IdleListesi = [self.Idle1, self.Idle2, self.Idle3, self.Idle4]

        self.IdleSol1 = pygame.transform.flip(self.Idle1, True, False).convert_alpha()
        self.IdleSol2 = pygame.transform.flip(self.Idle2, True, False).convert_alpha()
        self.IdleSol3 = pygame.transform.flip(self.Idle3, True, False).convert_alpha()
        self.IdleSol4 = pygame.transform.flip(self.Idle4, True, False).convert_alpha()
        self.IdleSolListesi = [self.IdleSol1, self.IdleSol2, self.IdleSol3, self.IdleSol4]

        self.Yurume0 = pygame.image.load("Mushroom/mushroom_run/tile000.png").convert_alpha()
        self.Yurume0 = pygame.transform.scale(self.Yurume0, (self.Scale, self.Scale))
        self.Yurume1 = pygame.image.load("Mushroom/mushroom_run/tile001.png").convert_alpha()
        self.Yurume1 = pygame.transform.scale(self.Yurume1, (self.Scale, self.Scale))
        self.Yurume2 = pygame.image.load("Mushroom/mushroom_run/tile002.png").convert_alpha()
        self.Yurume2 = pygame.transform.scale(self.Yurume2, (self.Scale, self.Scale))
        self.Yurume3 = pygame.image.load("Mushroom/mushroom_run/tile003.png").convert_alpha()
        self.Yurume3 = pygame.transform.scale(self.Yurume3, (self.Scale, self.Scale))
        self.Yurume4 = pygame.image.load("Mushroom/mushroom_run/tile004.png").convert_alpha()
        self.Yurume4 = pygame.transform.scale(self.Yurume4, (self.Scale, self.Scale))
        self.Yurume5 = pygame.image.load("Mushroom/mushroom_run/tile005.png").convert_alpha()
        self.Yurume5 = pygame.transform.scale(self.Yurume5, (self.Scale, self.Scale))
        self.Yurume6 = pygame.image.load("Mushroom/mushroom_run/tile006.png").convert_alpha()
        self.Yurume6 = pygame.transform.scale(self.Yurume6, (self.Scale, self.Scale))
        self.Yurume7 = pygame.image.load("Mushroom/mushroom_run/tile007.png").convert_alpha()
        self.Yurume7 = pygame.transform.scale(self.Yurume7, (self.Scale, self.Scale))
        self.YurumeListesi = [self.Yurume0, self.Yurume1, self.Yurume2, self.Yurume3, self.Yurume4, self.Yurume5,
                              self.Yurume6, self.Yurume7]

        self.YurumeSol0 = pygame.transform.flip(self.Yurume0, True, False).convert_alpha()
        self.YurumeSol1 = pygame.transform.flip(self.Yurume1, True, False).convert_alpha()
        self.YurumeSol2 = pygame.transform.flip(self.Yurume2, True, False).convert_alpha()
        self.YurumeSol3 = pygame.transform.flip(self.Yurume3, True, False).convert_alpha()
        self.YurumeSol4 = pygame.transform.flip(self.Yurume4, True, False).convert_alpha()
        self.YurumeSol5 = pygame.transform.flip(self.Yurume5, True, False).convert_alpha()
        self.YurumeSol6 = pygame.transform.flip(self.Yurume6, True, False).convert_alpha()
        self.YurumeSol7 = pygame.transform.flip(self.Yurume7, True, False).convert_alpha()
        self.YurumeSolListesi = [self.YurumeSol0, self.YurumeSol1, self.YurumeSol2, self.YurumeSol3,
                                 self.YurumeSol4, self.YurumeSol5, self.YurumeSol6, self.YurumeSol7]

        self.Olum0 = pygame.image.load("Mushroom/mushroom_death/tile000.png").convert_alpha()
        self.Olum0 = pygame.transform.scale(self.Olum0, (self.Scale, self.Scale))
        self.Olum1 = pygame.image.load("Mushroom/mushroom_death/tile001.png").convert_alpha()
        self.Olum1 = pygame.transform.scale(self.Olum1, (self.Scale, self.Scale))
        self.Olum2 = pygame.image.load("Mushroom/mushroom_death/tile002.png").convert_alpha()
        self.Olum2 = pygame.transform.scale(self.Olum2, (self.Scale, self.Scale))
        self.Olum3 = pygame.image.load("Mushroom/mushroom_death/tile003.png").convert_alpha()
        self.Olum3 = pygame.transform.scale(self.Olum3, (self.Scale, self.Scale))
        self.OlumSolListesi = [self.Olum0, self.Olum1, self.Olum2, self.Olum3]

        self.OlumSol0 = pygame.transform.flip(self.Olum0, True, False)
        self.OlumSol1 = pygame.transform.flip(self.Olum1, True, False)
        self.OlumSol2 = pygame.transform.flip(self.Olum2, True, False)
        self.OlumSol3 = pygame.transform.flip(self.Olum3, True, False)
        self.OlumListesi = [self.OlumSol0, self.OlumSol1, self.OlumSol2, self.OlumSol3]

        self.Saldir0 = pygame.image.load("Mushroom/mushroom_attack/tile000.png").convert_alpha()
        self.Saldir0 = pygame.transform.scale(self.Saldir0, (self.Scale, self.Scale))
        self.Saldir1 = pygame.image.load("Mushroom/mushroom_attack/tile001.png").convert_alpha()
        self.Saldir1 = pygame.transform.scale(self.Saldir1, (self.Scale, self.Scale))
        self.Saldir2 = pygame.image.load("Mushroom/mushroom_attack/tile002.png").convert_alpha()
        self.Saldir2 = pygame.transform.scale(self.Saldir2, (self.Scale, self.Scale))
        self.Saldir3 = pygame.image.load("Mushroom/mushroom_attack/tile003.png").convert_alpha()
        self.Saldir3 = pygame.transform.scale(self.Saldir3, (self.Scale, self.Scale))
        self.Saldir4 = pygame.image.load("Mushroom/mushroom_attack/tile004.png").convert_alpha()
        self.Saldir4 = pygame.transform.scale(self.Saldir4, (self.Scale, self.Scale))
        self.Saldir5 = pygame.image.load("Mushroom/mushroom_attack/tile005.png").convert_alpha()
        self.Saldir5 = pygame.transform.scale(self.Saldir5, (self.Scale, self.Scale))
        self.Saldir6 = pygame.image.load("Mushroom/mushroom_attack/tile006.png").convert_alpha()
        self.Saldir6 = pygame.transform.scale(self.Saldir6, (self.Scale, self.Scale))
        self.Saldir7 = pygame.image.load("Mushroom/mushroom_attack/tile007.png").convert_alpha()
        self.Saldir7 = pygame.transform.scale(self.Olum2, (self.Scale, self.Scale))
        self.SaldirmaListesi = [self.Saldir0, self.Saldir1, self.Saldir2, self.Saldir3, self.Saldir4, self.Saldir5,
                                self.Saldir6, self.Saldir7]

        self.SaldirSol0 = pygame.transform.flip(self.Saldir0, True, False)
        self.SaldirSol1 = pygame.transform.flip(self.Saldir1, True, False)
        self.SaldirSol2 = pygame.transform.flip(self.Saldir2, True, False)
        self.SaldirSol3 = pygame.transform.flip(self.Saldir3, True, False)
        self.SaldirSol4 = pygame.transform.flip(self.Saldir4, True, False)
        self.SaldirSol5 = pygame.transform.flip(self.Saldir5, True, False)
        self.SaldirSol6 = pygame.transform.flip(self.Saldir6, True, False)
        self.SaldirSol7 = pygame.transform.flip(self.Saldir7, True, False)
        self.SaldirmaSolListesi = [self.SaldirSol0, self.SaldirSol1, self.SaldirSol2, self.SaldirSol3, self.SaldirSol4,
                                   self.SaldirSol5, self.SaldirSol6, self.SaldirSol7]

        self.HasarYe0 = pygame.image.load("Mushroom/mushroom_take hit/tile000.png").convert_alpha()
        self.HasarYe0 = pygame.transform.scale(self.HasarYe0, (self.Scale, self.Scale))
        self.HasarYe1 = pygame.image.load("Mushroom/mushroom_take hit/tile001.png").convert_alpha()
        self.HasarYe1 = pygame.transform.scale(self.HasarYe1, (self.Scale, self.Scale))
        self.HasarYe2 = pygame.image.load("Mushroom/mushroom_take hit/tile002.png").convert_alpha()
        self.HasarYe2 = pygame.transform.scale(self.HasarYe2, (self.Scale, self.Scale))
        self.HasarYe3 = pygame.image.load("Mushroom/mushroom_take hit/tile003.png").convert_alpha()
        self.HasarYe3 = pygame.transform.scale(self.HasarYe3, (self.Scale, self.Scale))

        self.HasarListesi = [self.HasarYe0, self.HasarYe1, self.HasarYe2, self.HasarYe3]

        self.HasarYeSol0 = pygame.transform.flip(self.HasarYe0, True, False)
        self.HasarYeSol1 = pygame.transform.flip(self.HasarYe1, True, False)
        self.HasarYeSol2 = pygame.transform.flip(self.HasarYe2, True, False)
        self.HasarYeSol3 = pygame.transform.flip(self.HasarYe3, True, False)

        self.HasarSolListesi = [self.HasarYeSol0, self.HasarYeSol1, self.HasarYeSol2, self.HasarYeSol3]

        self.Itemler = [Ring1(), Ring2(), Ring3(),
                        Necklase1(), Necklase2(), Necklase3(),
                        Sapka1(), Sapka2(), Sapka3(), Sapka4(),
                        Zirh1(), Zirh2(), Zirh3(), Zirh4()]

        self.CanBari = pygame.image.load("Resimler/can barı çerçeve.png").convert_alpha()
        self.CanBariCan = pygame.image.load("Resimler/düşman can barı.png").convert_alpha()

        self.sahne_idle = 0
        self.sahne_yurume_sag = 0
        self.sahne_yurume_sol = 0
        self.sahne_hasarye_sag = 0
        self.sahne_hasarye_sol = 0
        self.sahne_olm_sag = 0
        self.sahne_olm_sol = 0
        self.sahne_saldir_sag = 0
        self.sahne_saldir_sol = 0
        self.sahne_item_dus = 0
        self.hareket = "stabil"
        self.ilkzaman = pygame.time.get_ticks()
        self.yurumekararilkzaman = time.time()
        self.totalcan = 140
        self.can = 140
        self.yon = ""
        self.tekrar = 0
        self.sagsol_listesi = ["sağ", "sol"]
        self.saldir = False
        self.hasar = False
        self.hasaryonu = ""
        self.saldirma_yonu = ""
        self.expverdimi = False
        self.kord = pygame.Rect(self.DusmanX + 140, self.DusmanY + 20, 45, 400)
        self.characterhasar_yedi_mi = False
        self.ZeminRect = pygame.Rect(0, 652, 1000000, 1000000)
        self.yukari = 1
        self.yukari_cik = True
        self.itemcikar = False
        self.itemalindi = False
        self.ad = 30
        self.kord = pygame.Rect(self.DusmanX + 155, self.DusmanY + 167, 80, 115)
        self.itemyuksel_ilkzaman = pygame.time.get_ticks()
        self.itemyuksel_sonzaman = pygame.time.get_ticks()
        self.itemyukselBool = True
        self.coinx = 0
        self.itemyuksel = 3
        self.coinyuksel = 3
        self.itemyuksel_ilkzaman = pygame.time.get_ticks()
        self.itemyuksel_sonzaman = pygame.time.get_ticks()
        self.itemyuksel_ilkzaman_coin = pygame.time.get_ticks()
        self.itemyuksel_sonzaman_coin = pygame.time.get_ticks()
        self.itemyukselBool = True
        self.itemdusurdu = False
        self.coinresim = pygame.image.load("Resimler/coin_dusur.png").convert_alpha()
        self.coinresim = pygame.transform.scale(self.coinresim, (14, 18))
        self.coindusurdu = False
        self.coinalindi = False
        self.yukariitem = 1
        self.yukari_cik_item = True
        self.coinyukselBool = True
        self.blitx = self.DusmanX + 155

    def Cizdir(self, pencere, character):
        if -250 < self.DusmanX < 1250:
            if self.can > 0 and (self.hasaryonu != "sağ" or self.hasaryonu != "sol"):
                self.CanBariCan = pygame.transform.scale(self.CanBariCan, (int(95 * (self.can / self.totalcan)), 13))
                self.CanBari = pygame.transform.scale(self.CanBari, (100, 15))
                pencere.blit(self.CanBari, (self.DusmanX + 145, self.DusmanY + 136))
                pencere.blit(self.CanBariCan, (self.DusmanX + 148, self.DusmanY + 137))
                self.sonzaman = pygame.time.get_ticks()

            if not self.hasar or self.hareket == "ölü":
                if self.hareket == "stabil":
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.IdleListesi[self.sahne_idle], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 200:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_idle == len(self.IdleListesi) - 1:
                            self.sahne_idle = 0
                        else:
                            self.sahne_idle += 1

                if self.yon == "sağ" and self.hareket != "ölü":
                    pencere.blit(self.YurumeListesi[self.sahne_yurume_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 220:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_yurume_sag == len(self.YurumeListesi) - 1:
                            self.sahne_yurume_sag = 0
                        else:
                            self.sahne_yurume_sag += 1

                    self.DusmanX += 1

                elif self.yon == "sol" and self.hareket != "ölü":
                    pencere.blit(self.YurumeSolListesi[self.sahne_yurume_sol], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 220:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_yurume_sol == len(self.YurumeSolListesi) - 1:
                            self.sahne_yurume_sol = 0
                            self.tekrar -= 1
                        else:
                            self.sahne_yurume_sol += 1

                    self.DusmanX -= 1

                if self.hareket == "randomsağ" and self.hareket != "ölü":
                    pencere.blit(self.YurumeListesi[self.sahne_yurume_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 120:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_yurume_sag == len(self.YurumeListesi) - 1:
                            self.sahne_yurume_sag = 0
                            self.tekrar -= 1
                        else:
                            self.sahne_yurume_sag += 1

                    self.DusmanX += 1

                    if self.tekrar == 0:
                        self.hareket = "stabil"

                elif self.hareket == "randomsol" and self.hareket != "ölü":
                    pencere.blit(self.YurumeSolListesi[self.sahne_yurume_sol], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 120:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_yurume_sol == len(self.YurumeSolListesi) - 1:
                            self.sahne_yurume_sol = 0
                            self.tekrar -= 1
                        else:
                            self.sahne_yurume_sol += 1

                    self.DusmanX -= 1

                    if self.tekrar == 0:
                        self.hareket = "stabil"
                        self.IdleListesi = self.IdleSolListesi

                elif self.hareket == "ölü" and (self.yon == "sağ" or self.saldirma_yonu == "sağ"):
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.OlumListesi[self.sahne_olm_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 120:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_olm_sag != len(self.IdleListesi) - 1:
                            self.sahne_olm_sag += 1

                        elif self.sahne_olm_sag == len(self.IdleListesi) - 1:
                            self.hasaryonu = ""

                elif self.hareket == "ölü" and (self.yon == "sol" or self.saldirma_yonu == "sol"):
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.OlumSolListesi[self.sahne_olm_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 120:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_olm_sag != len(self.IdleListesi) - 1:
                            self.sahne_olm_sag += 1

                        elif self.sahne_olm_sol == len(self.IdleListesi) - 1:
                            self.hasaryonu = ""

                if self.hareket == "saldır" and self.saldirma_yonu == "sağ":
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.SaldirmaListesi[self.sahne_saldir_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 125:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_saldir_sag != len(self.SaldirmaListesi) - 1:
                            self.sahne_saldir_sag += 1
                            self.saldir = False

                        else:
                            self.sahne_saldir_sag = 0
                            self.saldir = True

                        if self.sahne_saldir_sag == 7:
                            self.characterhasar_yedi_mi = True

                elif self.hareket == "saldır" and self.saldirma_yonu == "sol":
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.SaldirmaSolListesi[self.sahne_saldir_sol], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 125:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_saldir_sol != len(self.SaldirmaSolListesi) - 1:
                            self.sahne_saldir_sol += 1
                            self.saldir = False

                        else:
                            self.sahne_saldir_sol = 0
                            self.saldir = True

                        if self.sahne_saldir_sol == 7:
                            self.characterhasar_yedi_mi = True

            elif self.hasaryonu == "sağ" and self.can > 0:
                self.sonzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarListesi[self.sahne_hasarye_sag], (self.DusmanX, self.DusmanY))
                if self.sonzaman - self.ilkzaman > 115:
                    self.ilkzaman = pygame.time.get_ticks()
                    if self.sahne_hasarye_sag != len(self.HasarListesi) - 1:
                        self.sahne_hasarye_sag += 1
                        self.DusmanX -= 2

                    else:
                        self.sahne_hasarye_sag = 0
                        self.hasar = False

            elif self.hasaryonu == "sol" and self.can > 0:
                self.sonzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarSolListesi[self.sahne_hasarye_sol], (self.DusmanX, self.DusmanY))
                if self.sonzaman - self.ilkzaman > 115:
                    self.ilkzaman = pygame.time.get_ticks()
                    if self.sahne_hasarye_sol != len(self.HasarListesi) - 1:
                        self.sahne_hasarye_sol += 1
                        self.DusmanX += 2

                    else:
                        self.sahne_hasarye_sol = 0
                        self.hasar = False

            if self.hareket == "ölü":
                if not self.itemdusurdu:
                    self.itemdogrultu = random.choice(["sağ", "sol"])
                    self.itemdusurdu = True

                if not self.coindusurdu:
                    self.coindogrultu = random.choice(["sağ", "sol"])
                    self.coindusurdu = True

                self.itemcollid = pygame.Rect(self.itemx, self.itemy, 32, 32)
                self.coincoliid = pygame.Rect(self.coinx, self.coiny, 18, 14)
                if not self.itemcollid.colliderect(character.OyuncuRect) and not self.itemalindi:
                    pencere.blit(self.item.resim, (self.itemx, self.itemy))

                    if not self.ZeminRect.colliderect(self.itemcollid):
                        if self.itemy - self.DusmanY >= 50 and self.yukari_cik:
                            self.itemy -= self.yukari
                            self.yukari += 2
                            if self.itemy - self.DusmanY <= 50:
                                self.yukari_cik = False
                                self.yukari = 0
                        elif not self.yukari_cik:
                            self.itemy += self.yukari
                            self.yukari += 2

                        if self.itemdogrultu == "sağ":
                            self.itemx += 2

                        elif self.itemdogrultu == "sol":
                            self.itemx -= 2

                else:
                    for i in range(0, len(character.envanter)):
                        if character.envanter[i].isim == "" and not self.itemalindi:
                            self.item.resim = pygame.transform.scale(self.item.resim, (55, 55))
                            character.envanter[i] = self.item
                            self.itemalindi = True

                if self.itemcollid.colliderect(self.ZeminRect):
                    self.itemyuksel_ilkzaman = pygame.time.get_ticks()
                    if self.itemyuksel_ilkzaman - self.itemyuksel_sonzaman > 390:
                        if self.itemyukselBool:
                            self.itemy -= self.itemyuksel
                            self.itemyuksel -= 1
                            if self.itemyuksel == 0:
                                self.itemyukselBool = False

                        elif not self.itemyukselBool:
                            self.itemy += self.itemyuksel
                            self.itemyuksel += 1
                            if self.itemyuksel == 4:
                                self.itemyukselBool = True
                                self.itemyuksel = 3
                        self.itemyuksel_sonzaman = pygame.time.get_ticks()

                if self.coincoliid.colliderect(self.ZeminRect):
                    self.itemyuksel_ilkzaman_coin = pygame.time.get_ticks()
                    if self.itemyuksel_ilkzaman_coin - self.itemyuksel_sonzaman_coin > 390:
                        if self.coinyukselBool:
                            self.coiny -= self.coinyuksel
                            self.coinyuksel -= 1
                            if self.coinyuksel == 0:
                                self.coinyukselBool = False

                        elif not self.coinyukselBool:
                            self.coiny += self.coinyuksel
                            self.coinyuksel += 1
                            if self.coinyuksel == 4:
                                self.coinyukselBool = True
                                self.coinyuksel = 3
                        self.itemyuksel_sonzaman_coin = pygame.time.get_ticks()

                if not self.coincoliid.colliderect(character.OyuncuRect) and not self.coinalindi:
                    pencere.blit(self.coinresim, (self.coinx, self.coiny))

                    if not self.ZeminRect.colliderect(self.coincoliid):
                        if self.yukari_cik_item:
                            self.coiny -= self.yukariitem
                            self.yukariitem += 2
                            if self.coiny - self.DusmanY <= 50:
                                self.yukari_cik_item = False
                                self.yukariitem = 0
                        elif not self.yukari_cik_item:
                            self.coiny += self.yukariitem
                            self.yukariitem += 2

                        if self.coindogrultu == "sağ":
                            self.coinx += 2

                        elif self.coindogrultu == "sol":
                            self.coinx -= 2

                elif self.coincoliid.colliderect(character.OyuncuRect) and not self.coinalindi:
                    character.coin += 10
                    self.coinalindi = True

    def Hareket(self):
        self.blitx = self.DusmanX + 155
        self.kord = pygame.Rect(self.blitx, self.DusmanY + 167, 80, 115)

        if self.can > 0:
            self.yurumekararsonzaman = time.time()
            if self.yurumekararsonzaman - self.yurumekararilkzaman > 10 and self.tekrar == 0:
                self.yurumekararilkzaman = time.time()
                self.dolan = random.choice(self.sagsol_listesi)
                if self.dolan == "sağ":
                    self.hareket = "randomsağ"
                    self.tekrar = 3
                    self.sagsol_listesi.append("sol")

                elif self.dolan == "sol":
                    self.hareket = "randomsol"
                    self.tekrar = 3
                    self.sagsol_listesi.append("sağ")
        else:
            self.hareket = "ölü"
            if not self.itemcikar:
                self.item = random.choice(self.Itemler)
                self.itemx = self.DusmanX + 155
                self.itemy = self.DusmanY + 110
                self.coinx = self.DusmanX + 155
                self.coiny = self.DusmanY + 110
                self.itemcikar = True

    def Saldir(self, character):
        if self.can > 0:
            if not character.gizlen:
                self.blitx = self.DusmanX + 155
                if 200 > character.OyuncuX - self.blitx > 0:
                    if character.OyuncuX - self.DusmanX > 190:
                        self.yon = "sağ"
                        self.hareket = ""
                        self.sahne_saldir_sol = 0
                        self.sahne_saldir_sag = 0

                    elif character.OyuncuX - self.blitx <= 190:
                        self.hareket = "saldır"
                        self.saldirma_yonu = "sağ"
                        self.yon = ""
                        if self.characterhasar_yedi_mi:
                            character.hasar_yedi_mi = True
                            self.characterhasar_yedi_mi = False

                elif 200 > self.blitx - character.OyuncuX > 0:
                    if self.blitx - character.OyuncuX > 190:
                        self.yon = "sol"
                        self.hareket = ""
                        self.sahne_saldir_sol = 0
                        self.sahne_saldir_sag = 0

                    elif self.blitx - character.OyuncuX <= 145:
                        self.hareket = "saldır"
                        self.saldirma_yonu = "sol"
                        self.yon = ""
                        if self.characterhasar_yedi_mi:
                            character.hasar_yedi_mi = True
                            self.characterhasar_yedi_mi = False

                elif 500 > character.OyuncuX - self.blitx >= 200:
                    self.hareket = "sağ"
                    self.yon = "sağ"

                elif 500 > self.blitx - character.OyuncuX >= 200:
                    self.hareket = "sol"
                    self.yon = "sol"

                else:
                    self.hareket = "stabil"
                    self.yon = ""

                if self.saldir:
                    self.ad -= character.toplamarmour * (1/4)
                    if self.ad > 0:
                        character.can -= self.ad

                    else:
                        character.can -= 5

                    self.saldir = False

                    self.ad = 30

            else:
                self.hareket = "stabil"
                self.yon = ""