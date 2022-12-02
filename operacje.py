from klasa import Konto_w_banku
from importowanie import content_list

konto = Konto_w_banku(content_list[0], content_list[1], float(content_list[2]))
print()
konto.Wyswietl()

while True:
        print("\nRodzaje operacji:\n1.Wypłata\n2.Wpłata\n3.Zakończ")
        wybor_operacji = input("Wybierz rodzaj operacji (1-3): ")
        if wybor_operacji in ("1","2"):
                while True:
                        try:
                                kwota = float(input("Podaj kwotę wypłaty:"))
                                break
                        except ValueError:
                                print("Nie podano liczby!")

                if wybor_operacji == "1":
                        konto.Wyplata(kwota)

                elif wybor_operacji == "2":
                        konto.Wplata(kwota)

                nastepne_dzialanie = input("\nCzy chcesz wykonać kolejną operację? (T/N): ").upper()
                if nastepne_dzialanie != "T":
                        print("Zakończono\nDowidzenia")
                        break

        elif wybor_operacji == "3":
                print("Zakończono\nDowidzenia")
                break

        else:
                print("Zła operacja, proszę wybrać ponownie")
