import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #def test_lisays_liikaa_mahtuuko_nolla(self):
    #    self.varasto.lisaa_varastoon(100)

        # Varaston pitäisi olla täynnä, mahtuuko 0
    #    self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisays_liikaa_onko_saldo_taysi(self):
        self.varasto.lisaa_varastoon(100)

        # Varaston pitäisi olla täynnä, onko saldo 10
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_liikaa_onko_saldo_nolla(self):
        self.varasto.ota_varastosta(100)

        # Varaston pitäöisi olla tyhjä, onko saldo 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_negatiivinen_otto_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-1)

        # Varaston saldo (8) pitäisi pysyä ennallaan
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivinen_lisays_lisaa_nollan(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)

        # Varaston saldo (8) pitäisi pysyä ennallaan
        self.assertAlmostEqual(self.varasto.saldo, 8)

    # Yritetään alustaa varasto negatiivisella tilavuudella        
    def test_onko_tilavuus_nolla(self):
        varasto2 = Varasto(-10)
        self.assertAlmostEqual(varasto2.tilavuus, 0)
    
    # Yritetään alustaa varasto negatiivisella saldolla
    def test_onko_saldo_nolla(self):
        varasto3 = Varasto(10, -10)
        self.assertAlmostEqual(varasto3.saldo, 0)

    def test_print_string(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
