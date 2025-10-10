
def KonwertujKolor(kolor):
    if 'czarny' == kolor:
        return 0
    if 'brazowy' == kolor:
        return 1
    if 'czerwony' == kolor:
        return 2
    if 'pomaranczowy' == kolor:
        return 3
    if 'zolty' == kolor:
        return 4
    if 'zielony' == kolor:
        return 5
    if 'niebieski' == kolor:
        return 6
    if 'fioletowy' == kolor:
        return 7
    if 'szary' == kolor:
        return 8
    if 'bialy' == kolor:
        return 9
    return -1
def kalkulatorRezystorow(kolor1, kolor2, mnoznik):
    wartosc1 = KonwertujKolor(kolor1.lower())
    wartosc2 = KonwertujKolor(kolor2.lower())
    wartosc = wartosc1 * 10 + wartosc2
    wartosc_mnoznika = pow (10, KonwertujKolor (mnoznik.lower()))
    return wartosc * wartosc_mnoznika

rezystancja = kalkulatorRezystorow('szary', 'zielony','Czarny')
print (rezystancja)