class Konto_w_banku:
    def __init__(self, numer_konta, nazwa_wlasciciela_konta, srodki_na_koncie):
        self.numer_konta = numer_konta
        self.nazwa_wlasciciela_konta = nazwa_wlasciciela_konta
        self.srodki_na_koncie = srodki_na_koncie

    def Wplata(self, wpł):
        self.srodki_na_koncie = self.srodki_na_koncie + wpł
        print("Środki na koncie: ", self.srodki_na_koncie, " ZŁ")

    def Wyplata(self, wyp):
        if (self.srodki_na_koncie < wyp):
            print("Nie wystarczające środki na koncie do wykonania operacji!")
            print("Środki na koncie: ", self.srodki_na_koncie, " ZŁ")
        else:
            self.srodki_na_koncie = self.srodki_na_koncie - wyp
            print("Środki na koncie: ", self.srodki_na_koncie, " ZŁ")

    def Wyswietl(self):
        print("Nr Konta: ", self.numer_konta)
        print("Nazwa właściciela: ", self.nazwa_wlasciciela_konta)
        print("Środki na koncie: ", self.srodki_na_koncie, " ZŁ")


