from itemler import *
import pygame
import random
import time


class Dusman2:
    def __init__(self):
        self.DusmanX = 3000
        self.DusmanY = 532
        self.Scale = 192

        self.Idle1 = pygame.image.load("Minotaur/minotaur 0-1.png").convert_alpha()
        self.Idle1 = pygame.transform.scale(self.Idle1, (self.Scale, self.Scale))
        self.Idle2 = pygame.image.load("Minotaur/minotaur 0-2.png").convert_alpha()
        self.Idle2 = pygame.transform.scale(self.Idle2, (self.Scale, self.Scale))
        self.Idle3 = pygame.image.load("Minotaur/minotaur 0-3.png").convert_alpha()
        self.Idle3 = pygame.transform.scale(self.Idle3, (self.Scale, self.Scale))
        self.Idle4 = pygame.image.load("Minotaur/minotaur 0-4.png").convert_alpha()
        self.Idle4 = pygame.transform.scale(self.Idle4, (self.Scale, self.Scale))
        self.IdleListesi = [self.Idle1, self.Idle2, self.Idle3, self.Idle4]

        self.IdleSol1 = pygame.transform.flip(self.Idle1, True, False).convert_alpha()
        self.IdleSol2 = pygame.transform.flip(self.Idle2, True, False).convert_alpha()
        self.IdleSol3 = pygame.transform.flip(self.Idle3, True, False).convert_alpha()
        self.IdleSol4 = pygame.transform.flip(self.Idle4, True, False).convert_alpha()
        self.IdleSolListesi = [self.IdleSol1, self.IdleSol2, self.IdleSol3, self.IdleSol4]

        self.Yurume0 = pygame.image.load("Minotaur/minotaur 1-0.png").convert_alpha()
        self.Yurume0 = pygame.transform.scale(self.Yurume0, (self.Scale, self.Scale))
        self.Yurume1 = pygame.image.load("Minotaur/minotaur 1-1.png").convert_alpha()
        self.Yurume1 = pygame.transform.scale(self.Yurume1, (self.Scale, self.Scale))
        self.Yurume2 = pygame.image.load("Minotaur/minotaur 1-2.png").convert_alpha()
        self.Yurume2 = pygame.transform.scale(self.Yurume2, (self.Scale, self.Scale))
        self.Yurume3 = pygame.image.load("Minotaur/minotaur 1-3.png").convert_alpha()
        self.Yurume3 = pygame.transform.scale(self.Yurume3, (self.Scale, self.Scale))
        self.Yurume4 = pygame.image.load("Minotaur/minotaur 1-4.png").convert_alpha()
        self.Yurume4 = pygame.transform.scale(self.Yurume4, (self.Scale, self.Scale))
        self.Yurume5 = pygame.image.load("Minotaur/minotaur 1-5.png").convert_alpha()
        self.Yurume5 = pygame.transform.scale(self.Yurume5, (self.Scale, self.Scale))
        self.Yurume6 = pygame.image.load("Minotaur/minotaur 1-6.png").convert_alpha()
        self.Yurume6 = pygame.transform.scale(self.Yurume6, (self.Scale, self.Scale))
        self.Yurume7 = pygame.image.load("Minotaur/minotaur 1-7.png").convert_alpha()
        self.Yurume7 = pygame.transform.scale(self.Idle4, (self.Scale, self.Scale))
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

        self.Olum0 = pygame.image.load("Minotaur/minotaur 9-0.png").convert_alpha()
        self.Olum0 = pygame.transform.scale(self.Olum0, (self.Scale, self.Scale))
        self.Olum1 = pygame.image.load("Minotaur/minotaur 9-1.png").convert_alpha()
        self.Olum1 = pygame.transform.scale(self.Olum1, (self.Scale, self.Scale))
        self.Olum2 = pygame.image.load("Minotaur/minotaur 9-2.png").convert_alpha()
        self.Olum2 = pygame.transform.scale(self.Olum2, (self.Scale, self.Scale))
        self.Olum3 = pygame.image.load("Minotaur/minotaur 9-3.png").convert_alpha()
        self.Olum3 = pygame.transform.scale(self.Olum3, (self.Scale, self.Scale))
        self.Olum4 = pygame.image.load("Minotaur/minotaur 9-4.png").convert_alpha()
        self.Olum4 = pygame.transform.scale(self.Olum4, (self.Scale, self.Scale))
        self.Olum5 = pygame.image.load("Minotaur/minotaur 9-5.png").convert_alpha()
        self.Olum5 = pygame.transform.scale(self.Olum5, (self.Scale, self.Scale))
        self.OlumListesi = [self.Olum0, self.Olum1, self.Olum2, self.Olum3, self.Olum4, self.Olum5]

        self.OlumSol0 = pygame.transform.flip(self.Olum0, True, False)
        self.OlumSol1 = pygame.transform.flip(self.Olum1, True, False)
        self.OlumSol2 = pygame.transform.flip(self.Olum2, True, False)
        self.OlumSol3 = pygame.transform.flip(self.Olum3, True, False)
        self.OlumSol4 = pygame.transform.flip(self.Olum4, True, False)
        self.OlumSol5 = pygame.transform.flip(self.Olum5, True, False)
        self.OlumSolListesi = [self.OlumSol0, self.OlumSol1, self.OlumSol2, self.OlumSol3, self.OlumSol4, self.OlumSol5]

        self.Saldir0 = pygame.image.load("Minotaur/minotaur 3-0.png").convert_alpha()
        self.Saldir0 = pygame.transform.scale(self.Saldir0, (self.Scale, self.Scale))
        self.Saldir1 = pygame.image.load("Minotaur/minotaur 3-1.png").convert_alpha()
        self.Saldir1 = pygame.transform.scale(self.Saldir1, (self.Scale, self.Scale))
        self.Saldir2 = pygame.image.load("Minotaur/minotaur 3-2.png").convert_alpha()
        self.Saldir2 = pygame.transform.scale(self.Saldir2, (self.Scale, self.Scale))
        self.Saldir3 = pygame.image.load("Minotaur/minotaur 3-3.png").convert_alpha()
        self.Saldir3 = pygame.transform.scale(self.Saldir3, (self.Scale, self.Scale))
        self.Saldir4 = pygame.image.load("Minotaur/minotaur 3-4.png").convert_alpha()
        self.Saldir4 = pygame.transform.scale(self.Saldir4, (self.Scale, self.Scale))
        self.Saldir5 = pygame.image.load("Minotaur/minotaur 3-5.png").convert_alpha()
        self.Saldir5 = pygame.transform.scale(self.Saldir4, (self.Scale, self.Scale))
        self.Saldir6 = pygame.image.load("Minotaur/minotaur 3-6.png").convert_alpha()
        self.Saldir6 = pygame.transform.scale(self.Saldir4, (self.Scale, self.Scale))
        self.Saldir7 = pygame.image.load("Minotaur/minotaur 3-7.png").convert_alpha()
        self.Saldir7 = pygame.transform.scale(self.Saldir4, (self.Scale, self.Scale))
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

        self.HasarYe0 = pygame.image.load("Minotaur/minotaur 8-0.png").convert_alpha()
        self.HasarYe0 = pygame.transform.scale(self.HasarYe0, (self.Scale, self.Scale))
        self.HasarYe1 = pygame.image.load("Minotaur/minotaur 8-1.png").convert_alpha()
        self.HasarYe1 = pygame.transform.scale(self.HasarYe1, (self.Scale, self.Scale))
        self.HasarYe2 = pygame.image.load("Minotaur/minotaur 8-2.png").convert_alpha()
        self.HasarYe2 = pygame.transform.scale(self.HasarYe2, (self.Scale, self.Scale))
        self.HasarListesi = [self.HasarYe0, self.HasarYe1, self.HasarYe2]

        self.HasarYeSol0 = pygame.transform.flip(self.HasarYe0, True, False)
        self.HasarYeSol1 = pygame.transform.flip(self.HasarYe1, True, False)
        self.HasarYeSol2 = pygame.transform.flip(self.HasarYe2, True, False)

        self.HasarSolListesi = [self.HasarYeSol0, self.HasarYeSol1, self.HasarYeSol2]

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
        self.totalcan = 120
        self.can = 120
        self.yon = ""
        self.tekrar = 0
        self.sagsol_listesi = ["sağ", "sol"]
        self.saldir = False
        self.ad = 20
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
        self.itemyuksel = 3
        self.itemyuksel_ilkzaman = pygame.time.get_ticks()
        self.itemyuksel_sonzaman = pygame.time.get_ticks()
        self.itemyukselBool = True
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
        self.blitx = self.DusmanX + 55

    def Cizdir(self, pencere, character):
        if -250 < self.DusmanX < 1250:
            if self.can > 0 and (self.hasaryonu != "sağ" or self.hasaryonu != "sol"):
                self.CanBariCan = pygame.transform.scale(self.CanBariCan, (int(91 * (self.can / self.totalcan)), 13))
                self.CanBari = pygame.transform.scale(self.CanBari, (95, 15))
                pencere.blit(self.CanBari, (self.DusmanX + 55, self.DusmanY + 6))
                pencere.blit(self.CanBariCan, (self.DusmanX + 57, self.DusmanY + 7))
                self.sonzaman = pygame.time.get_ticks()

            if not self.hasar or self.hareket == "ölü":
                if self.hareket == "stabil":
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.IdleListesi[self.sahne_idle], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 180:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_idle == len(self.IdleListesi) - 1:
                            self.sahne_idle = 0
                        else:
                            self.sahne_idle += 1

                if self.yon == "sağ" and self.hareket != "ölü":
                    pencere.blit(self.YurumeListesi[self.sahne_yurume_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 100:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_yurume_sag == len(self.YurumeListesi) - 1:
                            self.sahne_yurume_sag = 0
                        else:
                            self.sahne_yurume_sag += 1

                    self.DusmanX += 1

                elif self.yon == "sol" and self.hareket != "ölü":
                    pencere.blit(self.YurumeSolListesi[self.sahne_yurume_sol], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 100:
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
                            self.DusmanY += 2

                        elif self.sahne_olm_sag == len(self.IdleListesi) - 1:
                            self.hasaryonu = ""

                elif self.hareket == "ölü" and (self.yon == "sol" or self.saldirma_yonu == "sol"):
                    self.sonzaman = pygame.time.get_ticks()
                    pencere.blit(self.OlumSolListesi[self.sahne_olm_sag], (self.DusmanX, self.DusmanY))
                    if self.sonzaman - self.ilkzaman > 120:
                        self.ilkzaman = pygame.time.get_ticks()
                        if self.sahne_olm_sag != len(self.IdleListesi) - 1:
                            self.sahne_olm_sag += 1
                            self.DusmanY += 2

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

                    if self.sahne_saldir_sag == 4:
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

                    if self.sahne_saldir_sol == 4:
                        self.characterhasar_yedi_mi = True

            elif self.hasar and self.hasaryonu == "sağ":
                self.sonzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarListesi[self.sahne_hasarye_sag], (self.DusmanX, self.DusmanY))
                if self.sonzaman - self.ilkzaman > 125:
                    self.ilkzaman = pygame.time.get_ticks()
                    if self.sahne_hasarye_sag != len(self.HasarListesi) - 1:
                        self.sahne_hasarye_sag += 1
                        self.DusmanX -= 2

                    else:
                        self.sahne_hasarye_sag = 0
                        self.hasar = False

            elif self.hasar and self.hasaryonu == "sol" and self.can > 0:
                self.sonzaman = pygame.time.get_ticks()
                pencere.blit(self.HasarSolListesi[self.sahne_hasarye_sol], (self.DusmanX, self.DusmanY))
                if self.sonzaman - self.ilkzaman > 125:
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
        self.blitx = self.DusmanX + 55
        self.kord = pygame.Rect(self.blitx, self.DusmanY - 15, 85, 165)

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
                self.itemx = self.DusmanX + 30
                self.itemy = self.DusmanY + 100
                self.coinx = self.DusmanX + 30
                self.coiny = self.DusmanY + 100
                self.itemcikar = True

    def Saldir(self, character):
        if self.can > 0:
            if not character.gizlen:
                if 0 < character.OyuncuX - self.DusmanX < 200:
                    if character.OyuncuX - self.DusmanX > 65:
                        self.yon = "sağ"
                        self.hareket = ""
                        self.sahne_saldir_sol = 0
                        self.sahne_saldir_sag = 0

                    elif character.OyuncuX - self.DusmanX <= 75:
                        self.hareket = "saldır"
                        self.saldirma_yonu = "sağ"
                        self.yon = ""
                        if self.characterhasar_yedi_mi:
                            character.hasar_yedi_mi = True
                            self.characterhasar_yedi_mi = False

                elif 200 > self.DusmanX - character.OyuncuX > 0:
                    if self.DusmanX - character.OyuncuX > 65:
                        self.yon = "sol"
                        self.hareket = ""
                        self.sahne_saldir_sol = 0
                        self.sahne_saldir_sag = 0

                    elif self.DusmanX - character.OyuncuX <= 75:
                        self.hareket = "saldır"
                        self.saldirma_yonu = "sol"
                        self.yon = ""
                        if self.characterhasar_yedi_mi:
                            character.hasar_yedi_mi = True
                            self.characterhasar_yedi_mi = False

                elif 500 > character.OyuncuX - self.DusmanX >= 200:
                    self.hareket = "sağ"
                    self.yon = "sağ"

                elif 500 > self.DusmanX - character.OyuncuX >= 200:
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

                    self.expverdimi = True
                    self.saldir = False

                    self.ad = 20

            else:
                self.hareket = "stabil"
                self.yon = ""
