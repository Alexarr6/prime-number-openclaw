import subprocess
import sys
import unittest
from pathlib import Path

from primo import es_primo


class TestEsPrimo(unittest.TestCase):
    def test_negativo(self):
        self.assertFalse(es_primo(-7))

    def test_cero(self):
        self.assertFalse(es_primo(0))

    def test_uno(self):
        self.assertFalse(es_primo(1))

    def test_dos(self):
        self.assertTrue(es_primo(2))

    def test_tres(self):
        self.assertTrue(es_primo(3))

    def test_cuatro(self):
        self.assertFalse(es_primo(4))

    def test_par_mayor_que_dos(self):
        self.assertFalse(es_primo(10))

    def test_quince(self):
        self.assertFalse(es_primo(15))

    def test_diecisiete(self):
        self.assertTrue(es_primo(17))

    def test_primo_grande(self):
        self.assertTrue(es_primo(7919))


class TestCLIPrimo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.script = Path(__file__).with_name("primo.py")

    def run_cli(self, n):
        return subprocess.run(
            [sys.executable, str(self.script), str(n)],
            capture_output=True,
            text=True,
            check=True,
        )

    def test_cli_2(self):
        result = self.run_cli(2)
        self.assertEqual(result.stdout.strip(), "primo")

    def test_cli_15(self):
        result = self.run_cli(15)
        self.assertEqual(result.stdout.strip(), "no primo")

    def test_cli_negativo(self):
        result = self.run_cli(-7)
        self.assertEqual(result.stdout.strip(), "no primo")


if __name__ == "__main__":
    unittest.main()
