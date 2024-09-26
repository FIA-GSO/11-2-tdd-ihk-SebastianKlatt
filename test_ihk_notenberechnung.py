import pytest
from ihk_notenrechner import *

# Tests für den Prozentrechner
def test_prozentrechner__ueber_100_prozent():
    erreichte_punkte = 101
    max_punkte = 100
    with pytest.raises(ValueError):
        prozentrechner(erreichte_punkte, max_punkte)

def test_prozentrechner__erreichte_punkte_negativ():
    erreichte_punkte = -1
    max_punkte = 100
    with pytest.raises(ValueError):
        prozentrechner(erreichte_punkte, max_punkte)

def test_prozentrechner__max_punkte_kleiner_eins():
    erreichte_punkte = 99
    max_punkte = 0
    with pytest.raises(ValueError):
        prozentrechner(erreichte_punkte, max_punkte)

def test_prozentrechner__nicht_int_eingabe_erreichte_punkte():
    erreichte_punkte = "sechsundachtzig"
    max_punkte = 100
    with pytest.raises(TypeError):
        prozentrechner(erreichte_punkte, max_punkte)

def test_prozentrechner__nicht_int_eingabe_max_punkte():
    erreichte_punkte = 77
    max_punkte = "hundertvierundfünfzig"
    with pytest.raises(TypeError):
        prozentrechner(erreichte_punkte, max_punkte)

testdata_prozentrechner = [(erreichte_punkte,max_punkte,int(erreichte_punkte/max_punkte*100))
                         for erreichte_punkte in range(101) 
                         for max_punkte in range(1, 101) 
                         if max_punkte >= erreichte_punkte]

@pytest.mark.parametrize("erreichte_punkte,max_punkte,soll_ergebnis", testdata_prozentrechner)
def test_notenrechner__positive_ergebnisse(erreichte_punkte, max_punkte, soll_ergebnis):
    assert soll_ergebnis == prozentrechner(erreichte_punkte, max_punkte)




# Tests für den Notenrechner
def test_notenrechner__ueber_100_prozent():
    erreichte_prozent = 110
    with pytest.raises(ValueError):
        notenrechner(erreichte_prozent)

def test_notenrechner__erreichte_punkte_negativ():
    erreichte_prozent = -50
    with pytest.raises(ValueError):
        notenrechner(erreichte_prozent)

def test_notenrechner__nicht_int_eingabe():
    erreichte_prozent = "sechsundachtzig"
    with pytest.raises(TypeError):
        notenrechner(erreichte_prozent)

testdata_notenrechner = [
    (100,"sehr gut"),
    (92,"sehr gut"),
    (91,"gut"),
    (81,"gut"),
    (80,"befriedigend"),
    (67,"befriedigend"),
    (66,"ausreichend"),
    (50,"ausreichend"),
    (49,"mangelhaft"),
    (30,"mangelhaft"),
    (29,"ungenügend"),
    (0,"ungenügend"),
]

@pytest.mark.parametrize("erreichte_prozent,soll_ergebnis", testdata_notenrechner)
def test_notenrechner__positive_ergebnisse(erreichte_prozent,soll_ergebnis):
    assert soll_ergebnis == notenrechner(erreichte_prozent)










