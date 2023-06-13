from scipy import constants as const
import numpy as np
import math

def p2():
    print("p2")
    E = np.array((4.9, 1.9))
    lambda0 = const.h * const.c / ( E * const.e)
    E_k = const.c * const.h / (4 * 10 ** (-7)) - (E[1] * const.e)
    v = math.sqrt((2 * E_k / const.m_e))
    p = const.m_e * v
    print(lambda0)
    print(v)
    print(p)

def p4():
    print("p4")
    a = 12 * 10 ** (-10)
    n = np.arange(1, 4)
    k = n * const.pi / a
    E = (k * const.hbar) ** 2 / 2/ const.m_e
    delta_E = E[2] - E[1]
    lambda0 = const.c * const.h / delta_E
    print(E)
    print(lambda0)
    
def p6():
    print("p6")
    mu = 9 * const.e / const.h
    lambda0 = const.c / mu
    print(mu, lambda0)

def p9():
    E = np.array([0.05, 0.5])
    k = 0.08
    m = ((k * 10**10) * const.hbar) ** 2 / (2 * E * const.e)
    print(m)

def p2_1():
    T = 400
    m = 0.48 * const.m_e
    N = 4 * const.pi * (2 * m) ** (3/2) / const.h ** 3 * (2 / 3) * (3 * const.k * T) ** (3/2)
    print(N)

def p2_2():
    ratio = pow(0.067 / 0.48, 3 / 2)
    print(ratio)

def p2_3():
    E = -0.4
    f = 1 / (1 + math.exp(E * const.e / (const.k * 300)))
    print(1-f)

def p2_4():
    m_n = 0.08 * const.m_e
    m_p = 0.75 * const.m_e
    T = 300
    deltaE = 3 / 4  * const.k * T * math.log(m_p / m_n) / const.e
    print(deltaE)

def p2_5():
    eta = - math.log(0.05)
    print(eta)

def p2_7():
    deltaEv = 0.0259*math.log(1.04e19 / 2e5)
    deltaEc = 1.12 - deltaEv
    n_0 = 2.8e19 * math.exp(-deltaEc / 0.0259)
    print(deltaEv, deltaEc, n_0)
    
def p3_1():
    n_i = 1.5e10
    p_0 = 2e5
    n_0 = pow(n_i, 2) / p_0
    print(f"{n_0:e}")

def p3_2():
    deltaE = const.k * 300 * math.log(2.8e19 / 1e15) / const.e
    print(deltaE)
    N_c = 2.8e19 * pow(5/3, 3/2)
    deltaE = const.k * 500 * math.log(N_c / 1e15) / const.e
    print(deltaE)

def p3_3():
    N_d = 1e15
    N_a = 0
    n_0 = N_d / 0.95
    n_i = math.sqrt(pow(n_0,2) - (N_d - N_a) * n_0)
    print(pow(n_i, 2))
    T = np.linspace(200, 700, num=int(1e5))
    delta = T[np.abs(pow(n_i, 2) - (2.8e19) * (1.04e19) * (T / 300) ** 3 * np.exp(-1.12 * const.e / (const.k * T))).argmin()]
    print(delta)

def p3_4():
    n_0 = 1.8e6 * math.exp(0.5 * const.e / (const.k * 300))
    print(f"{n_0:e}")
    N_a = 7e15 - n_0
    print(f"{N_a:e}")

def p3_5():
    sigma = const.e * 200 * 3.2e17
    print(sigma, f"{1/ sigma:e}")

def p3_6():
    T = 300
    n_i = math.sqrt((2e18) * (1e18) * (T / 300) ** 3 * np.exp(-1.1 * const.e / (const.k * T)))
    print(f"{n_i:e}")
    n_0 = 1e14
    J = const.e * n_0 * 800 * 100
    print(f"{J:e}")
    n_0 = 1.05 * n_0
    n_i = math.sqrt(n_0 ** 2 - 1e14 * n_0)
    T = np.linspace(200, 700, num=int(1e5))
    delta = T[np.abs(pow(n_i, 2) - (2e18) * (1e18) * (T / 300) ** 3 * np.exp(-1.1 * const.e / (const.k * T))).argmin()]
    print(delta)

def p3_7():
    x = np.array((0, -12))
    x = x * 1e-4
    L = 12e-4
    J = - const.e * 10 * 1e15 * (2*x/pow(L, 2) + 2 / L)
    print(J)

def main():
    p3_6()

if __name__ == '__main__':
    main()
