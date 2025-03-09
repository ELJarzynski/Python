from collections import namedtuple

Zamowienie = namedtuple('Zamowienie', ['Kraj', 'Sprzedawca', 'Data_zamowienia', 'idZamowienia', 'Utarg'])

zamowienie1 = Zamowienie(Kraj="Polska", Sprzedawca="Firma A", Data_zamowienia="2025-03-09", idZamowienia=1, Utarg=500.0)
zamowienie2 = Zamowienie(Kraj="Niemcy", Sprzedawca="Firma B", Data_zamowienia="2025-03-10", idZamowienia=2, Utarg=1200.0)
zamowienie3 = Zamowienie(Kraj="Francja", Sprzedawca="Firma C", Data_zamowienia="2025-03-11", idZamowienia=3, Utarg=850.0)
zamowienie4 = Zamowienie(Kraj="Hiszpania", Sprzedawca="Firma D", Data_zamowienia="2025-03-12", idZamowienia=4, Utarg=450.0)
zamowienie5 = Zamowienie(Kraj="Włochy", Sprzedawca="Firma E", Data_zamowienia="2025-03-13", idZamowienia=5, Utarg=750.0)

orders = [zamowienie1, zamowienie2, zamowienie3, zamowienie4, zamowienie5]