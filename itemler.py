import pygame

pygame.init()


class Ring1:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/ring 1.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "ring1"
        self.etki = "+ 5 Toplam Can"
        self.etki2 = "+ 1 Can Regen"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Nikki'nin Yüzüğü"
        self.level = 1

    def Etki(self, character):
        character.totalcan += 5
        character.can += 5
        character.canregen += 1

    def Etki_Pasif(self, character):
        character.totalcan -= 5
        character.can -= 5
        character.canregen -= 1


class Ring2:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/ring 2.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "ring2"
        self.etki = "+10 Toplam Mana"
        self.etki2 = "+ 5 Mana Regen"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Nikki'nin Yüzüğü"
        self.level = 2

    def Etki(self, character):
        character.totalmana += 10
        character.mana += 10
        character.manaregen += 5

    def Etki_Pasif(self, character):
        character.totalmana -= 10
        character.mana -= 10
        character.manaregen -= 5


class Ring3:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/ring 3.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "ring3"
        self.etki = "+ 15 Toplam Mana"
        self.etki2 = "+ 10 Mana Regen"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.kullanim = False
        self.baslat = False
        self.takma_lakap = "Nikki'nin Yüzüğü"
        self.level = 3

    def Etki(self, character):
        character.totalmana += 15
        character.mana += 15
        character.manaregen += 10

    def Etki_Pasif(self, character):
        character.totalmana -= 15
        character.mana -= 15
        character.manaregen -= 10


class Necklase1:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/kolye 1.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "kolye1"
        self.etki = "- 5 Toplam Exp"
        self.etki2 = ""
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Morgoth'un Kolyesi"
        self.level = 1

    def Etki(self, character):
        character.totalexp -= 5

    def Etki_Pasif(self, character):
        character.totalexp += 5


class Necklase2:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/kolye 2.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "kolye2"
        self.etki = "- 10 Toplam Exp"
        self.etki2 = ""
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Morgoth'un Kolyesi"
        self.level = 2

    def Etki(self, character):
        character.totalexp -= 10

    def Etki_Pasif(self, character):
        character.totalexp += 10


class Necklase3:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/kolye 3.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "kolye3"
        self.etki = "- 15 Toplam Exp"
        self.etki2 = ""
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Morgoth'un Kolyesi"
        self.level = 3

    def Etki(self, character):
        character.totalexp -= 15

    def Etki_Pasif(self, character):
        character.totalexp += 15


class Sapka1:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/şapka 1.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/şapka 1.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/şapka 1.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (95, 95))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "şapka 1"
        self.etki = "+ 5 Dayanıklılık"
        self.etki2 = ""
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Bender'ın Şapkası"
        self.level = 1

    def Etki(self, character):
        character.dayaniklilik += 5

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 5


class Sapka2:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/şapka 2.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/şapka 2.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/şapka 2.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (95, 95))
        self.market_itemx = 141
        self.marketitemy = 235
        self.isim = "şapka 2"
        self.etki2 = ""
        self.etki = "+ 10 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Bender'ın Şapkası"
        self.level = 2

    def Etki(self, character):
        character.dayaniklilik += 10

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 10


class Sapka3:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/şapka 3.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/şapka 3.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/şapka 3.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (95, 95))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "şapka 3"
        self.etki2 = ""
        self.etki = "+ 15 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Bender'ın Şapkası"
        self.level = 3

    def Etki(self, character):
        character.dayaniklilik += 15

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 15


class Sapka4:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/şapka 4.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/şapka 4.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/şapka 4.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (95, 95))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "şapka 4"
        self.etki2 = ""
        self.etki = "+ 20 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Bender'ın Şapkası"
        self.level = 4

    def Etki(self, character):
        character.dayaniklilik += 20

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 20


class Zirh1:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/zırh 1.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/zırh 1.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/zırh 1.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (92, 127))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "zırh 1"
        self.etki2 = ""
        self.etki = "+ 20 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Heisen'in Zırhı"
        self.level = 1

    def Etki(self, character):
        character.dayaniklilik += 20

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 20


class Zirh2:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/zırh 2.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/zırh 2.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/zırh 2.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (92, 127))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "zırh 2"
        self.etki2 = ""
        self.etki = "+ 25 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Heisen'in Zırhı"
        self.level = 2

    def Etki(self, character):
        character.dayaniklilik += 25

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 25


class Zirh3:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/zırh 3.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/zırh 3.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/zırh 3.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (92, 127))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "zırh 3"
        self.etki2 = ""
        self.etki = "+ 30 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Heisen'in Zırhı"
        self.level = 3

    def Etki(self, character):
        character.dayaniklilik += 30

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 30


class Zirh4:
    def __init__(self):
        self.resim = pygame.image.load("Itemler/zırh 4.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (55, 55))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.saklaresim = pygame.image.load("Itemler/zırh 4.png").convert_alpha()
        self.saklaresim = pygame.transform.scale(self.saklaresim, (55, 55))
        self.resim2 = pygame.image.load("Itemler/zırh 4.png").convert_alpha()
        self.itemresim = pygame.transform.scale(self.resim2, (92, 127))
        self.market_itemx = 141
        self.marketitemy = 255
        self.isim = "zırh 4"
        self.etki2 = ""
        self.etki = "+ 35 Dayanıklılık"
        self.itemx = 325
        self.itemy = 149
        self.itemgoster = pygame.image.load("Resimler/item göster.png")
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.takma_lakap = "Heisen'in Zırhı"
        self.level = 4

    def Etki(self, character):
        character.dayaniklilik += 35

    def Etki_Pasif(self, character):
        character.dayaniklilik -= 35


class BosItem:
    def __init__(self):
        self.isim = ""
        self.itemx = 325
        self.itemy = 149
        self.resim = pygame.image.load("Adventurer/boş.png").convert_alpha()
        self.resim = pygame.transform.scale(self.resim, (50, 50))
        self.marketarayuz = pygame.transform.scale(self.resim, (41, 41))
        self.marketalisarayuz = pygame.transform.scale(self.resim, (35, 35))
        self.itemresim = pygame.transform.scale(self.resim, (50, 50))
        self.market_itemx = 141
        self.marketitemy = 255
        self.secili = False
        self.baslat = False
        self.kullanim = False
        self.level = 0

    def Etki(self, character):
        pass
