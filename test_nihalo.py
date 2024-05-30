import unittest

from nihalo import *
import numpy as np

# Metodo Runge Kutta 4 testiramo tako, da rešimo nekaj diferencialnih enačb,
# za katere poznamo rešitve
class TestRK4(unittest.TestCase):
    def test1(self):
        def f(x, y):
            return y
        
        x0 = 0
        y0 = 1

        h = 0.01
        rkres = RK4(h, f, x0, y0)
        self.assertAlmostEqual(rkres, np.exp(h), places=10)

    def test2(self):
        def f(x, y):
            return y ** 2
        
        x0 = 0
        y0 = 1

        h = 0.01
        rkres = RK4(h, f, x0, y0)
        self.assertAlmostEqual(rkres, 1 / (1 - h), places=10)

    def test3(self):
        def f(x, y):
            return (1 - y ** 3 * np.sin(x)) / (3 * y ** 2 * np.cos(x))
        
        x0 = 0
        y0 = 1

        h = 0.01
        rkres = RK4(h, f, x0, y0)
        self.assertAlmostEqual(rkres, (np.cos(h) + np.sin(h)) ** (1/3), places=10)

    def test4(self):
        def f(x, y):
            return 2 * x * y ** 2
        
        x0 = 0
        y0 = 1

        h = 0.01
        rkres = RK4(h, f, x0, y0)

        self.assertAlmostEqual(rkres, 1 / (1 - h ** 2), places=10)
        


class TestNihalo(unittest.TestCase):
    def test_return_format_default(self):
        # Nihalo vrne eno število tipa float
        l = 1
        t = 1
        theta0 = 1
        dtheta0 = 1
        n = 10

        theta = nihalo(l, t, theta0, dtheta0, n)
        self.assertIsInstance(theta, float)

    def test_format_trace(self):
        # Ob dodatnem argumentu funkcije vrnemo celotno zaporedje theta in dtheta
        l = 1
        t = 1
        theta0 = 1
        dtheta0 = 1
        n = 10

        theta, dtheta = nihalo(l, t, theta0, dtheta0, n, return_trace=True)
        self.assertIsInstance(theta, np.ndarray)
        self.assertIsInstance(dtheta, np.ndarray)
        self.assertEqual(len(theta), n + 1)
        self.assertEqual(len(dtheta), n + 1)

    def test_no_time(self):
        # Če je t enak 0, potem je končni odmik enak začetnemu
        l = 1
        t = 0
        theta0 = 0
        dtheta0 = 1
        n = 10

        theta = nihalo(l, t, theta0, dtheta0, n, return_trace=False)
        self.assertAlmostEqual(theta, 0, places=10)

    def test_small_angle_approximation(self):
        # Pri majnih odmikih je theta(t) = theta_0 * cos(sqrt(g/l) * t)
        l = 1
        t = 10
        theta0 = 0.0001
        dtheta0 = 0

        # Numerični izračun thet
        n = 1000
        theta, _ = nihalo(l, t, theta0, dtheta0, n, return_trace=True)

        # Analitični izračun thet
        g = 9.80665
        theta_analytical = theta0 * np.cos(np.sqrt(g / l) * np.linspace(0, t, n + 1))

        self.assertTrue(np.allclose(theta, theta_analytical, atol=1e-10))