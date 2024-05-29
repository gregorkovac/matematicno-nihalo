import numpy as np

def RK4(h, f, x_n, y_n):
    k1 = h * f(x_n, y_n)
    k2 = h * f(x_n + h/2, y_n + k1/2)
    k3 = h * f(x_n + h/2, y_n + k2/2)
    k4 = h * f(x_n + h, y_n + k3)

    y_n_plus_1 = y_n + (k1 + 2*k2 + 2*k3 + k4)/6

    return y_n_plus_1

def nihalo(l, t, theta0, dtheta0, n):
    g = 9.80665
    
    def f(t, y):
        return np.array([y[1], -g/l * np.sin(y[0])])

    dt = t / n

    theta = theta0
    dtheta = dtheta0

    theta_all = np.zeros(n + 1)
    dtheta_all = np.zeros(n + 1)

    theta_all[0] = theta
    dtheta_all[0] = dtheta

    for i in range(n):
        rk4_res = RK4(dt, f, i*dt, np.array([theta, dtheta]))
        theta, dtheta = rk4_res[0], rk4_res[1]

        # A je to prav?
        theta_all[i + 1] = theta
        dtheta_all[i + 1] = dtheta

    return theta_all, dtheta_all