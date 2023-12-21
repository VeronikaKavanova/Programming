import Programovani_12_05_2023_Pocet_dni as pd
import unittest

class TestyData_den( unittest.TestCase ):
    def test_den_1( self ):
        self.assertEqual(pd.PocetDnu(1,11,2023,2,11,2023),1)

    def test_den_2( self ):
        self.assertEqual(pd.PocetDnu(1,1,2023,2,1,2023),1)

class Testydata_mesice(unittest.TestCase):
    def test_mesice_1( self ):
        self.assertEqual(pd.PocetDnu(1,11,2023,1,12,2023),30)

    def test_den_2( self ):
        self.assertEqual(pd.PocetDnu(1,1,2023,1,2,2023),31)

class TestyData_roky( unittest.TestCase ):
    def test_roky_1(self):
        self.assertEqual(pd.PocetDnu(1,11,2023,1,11,2024),366)
    def test_roky_2(self):
        self.assertEqual(pd.PocetDnu(1,11,1998,1,11,1999),365)
    def test_roky_3(self):
        self.assertEqual(pd.PocetDnu(1,11,1999,1,11,2000),366)
    def test_roky_4(self):
        self.assertEqual(pd.PocetDnu(1,11,2000,1,11,2001),365)            
    def test_roky_5(self):
        self.assertEqual(pd.PocetDnu(1,11,2001,1,11,2002),365) 
    def test_roky_6(self):
        self.assertEqual(pd.PocetDnu(1,11,2002,1,11,2003),365) 
    def test_roky_7(self):
        self.assertEqual(pd.PocetDnu(1,11,2003,1,11,2004),366) 
    def test_roky_8(self):
        self.assertEqual(pd.PocetDnu(1,11,2004,1,11,2005),365) 
unittest.main() 

import time
def VypisJakDlouhoTrva( popis, f ):
    start = time.time()
    f()
    print(f"{popis}: {time.time()-start} s")

def CekaniNaVstup():
    input()

#VypisJakDlouhoTrva( "CekaniNaVstup", CekaniNaVstup) #předávám funkci, nevolám ji, proto tam nejsou závorky

#rychlost vytváření dictionary:

N = 100_000_000
def VyrobDictPomociFunkce():
    for _ in range(N):
        d = dict()

def VyrobDictPomociZavorek():
    for _ in range(N):
        d = {}

VypisJakDlouhoTrva( "VyrobDictPomociFunkce", VyrobDictPomociFunkce )

VypisJakDlouhoTrva( "VyrobDictPomociZavorek", VyrobDictPomociZavorek )

print(time.time()) #kolik uplynulo času od začátku světa. Můžeme pomocí toho měřit čas


import Programovani_1_Modul_12_05_2023 as modul
print(dir(modul))
print(modul.b)