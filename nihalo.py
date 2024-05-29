import numpy as np

"""
RK4 naredi korak metode Runge-Kutta 4. reda za podano diferencialno enačbo.
Vhod:
    h (float) ... korak
    f (function) ... funkcija, ki predstavlja diferencialno enačbo
    x_n (float) ... začetna vrednost x
    y_n (float) ... začetna vrednost y
Izhod:
    float ... vrednost y po izvedenem koraku
"""
def RK4(h, f, x_n, y_n):
    k1 = h * f(x_n, y_n)
    k2 = h * f(x_n + h/2, y_n + k1/2)
    k3 = h * f(x_n + h/2, y_n + k2/2)
    k4 = h * f(x_n + h, y_n + k3)

    y_n_plus_1 = y_n + (k1 + 2*k2 + 2*k3 + k4)/6

    return y_n_plus_1

"""
nihalo izvede simulacijo matematičnega nihala
Vhod:
    l (float) ... dolžina nihala
    t (float) ... končni čas
    theta0 (float) ... začetni odmik
    dtheta0 (float) ... začetna kotna hitrost
    n (int) ... število korakov
    return_trace (bool) ... ali funkcija vrne vse vrednosti ali le končno
Izhod:
    float ... končni odmik
    ali
    (np.array, np.array) ... sled vseh vrednosti theta in dtheta
"""
def nihalo(l, t, theta0, dtheta0, n, return_trace=False):
    # Definiramo gravitacijski pospešek
    g = 9.80665
    
    # Definiramo funkcijo, ki predstavlja sistem diferencialnih enačb
    def f(t, y):
        return np.array([y[1], -g/l * np.sin(y[0])])

    # Definiramo dolžino koraka
    dt = t / n

    # Inizializiramo spremenljivke
    theta = theta0
    dtheta = dtheta0

    theta_all = np.zeros(n + 1)
    dtheta_all = np.zeros(n + 1)

    theta_all[0] = theta
    dtheta_all[0] = dtheta

    # Izvedemo n korakov
    for i in range(n):
        # Izračunamo naslednjo vrednost in jo shranimo
        rk4_res = RK4(dt, f, i*dt, np.array([theta, dtheta]))
        theta, dtheta = rk4_res[0], rk4_res[1]

        theta_all[i + 1] = theta
        dtheta_all[i + 1] = dtheta

    if return_trace:
        return theta_all, dtheta_all
    
    return theta
