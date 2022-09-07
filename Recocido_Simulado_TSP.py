import numpy as np
import matplotlib.pyplot as plt

'''Recodido Simulado'''

N_ciudades = 10

def Generar_solucion(N_ciudades):
    sol = []
    
    for _ in range(N_ciudades):
        sol.append(City())
    
    return sol

def Vecino_aleatorio(S_act):
    S_prueb = list(S_act)
    a = 0
    b = 0
    
    while a == b:
        a = np.random.randint(0, N_ciudades)
        b = np.random.randint(0, N_ciudades)
        
    S_prueb[a], S_prueb[b] = S_prueb[b], S_prueb[a]
    
    return S_prueb

def evaluar(Sol):
    Sol_dist = 0
    
    for i in range(N_ciudades):
        Sol_dist += Sol[i].dist(Sol[(i+1)%(N_ciudades)])
    
    return Sol_dist
        
def evaluar_sol(S_cand, S_act):
    delta = evaluar(S_cand) - evaluar(S_act)
    return delta    

def crit_eval(delta, T):
    return np.exp(-(delta/T))

def Vendedor_Viajero(alpha, L, Tf):
    S_act = Generar_solucion(N_ciudades)
    T = evaluar(S_act)*0.2
    S_mejor = list(S_act)
    
    while T >= Tf:
        
        for _ in range(L):
            S_cand = Vecino_aleatorio(S_act)
            delta = evaluar_sol(S_cand, S_act)
            
            if not delta or (np.random.rand() < crit_eval(delta, T)):
                S_act = S_cand
                if evaluar_sol(S_act, S_mejor):
                    S_mejor = list(S_act)
            
        T *= alpha
    
    return S_mejor

class City:
    
    def __init__(self):
        self.x = np.random.randint(0, 20)
        self.y = np.random.randint(0, 20)
    
    def dist(self, ciudad):
        distx = np.abs(self.x - ciudad.x)
        disty = np.abs(self.y - ciudad.y)
        dist = np.sqrt(distx**2 + disty**2)
        return dist
    
S_mejor = Vendedor_Viajero(.5, 1000, .5)
x = [city.x for city in S_mejor]
y = [city.y for city in S_mejor]
x.append(S_mejor[0].x)
y.append(S_mejor[0].y)
plt.plot(x, y)
plt.xlabel(f"Número de Ciudades = {N_ciudades}")
for i in range(N_ciudades):
    plt.annotate(i, (S_mejor[i].x, S_mejor[i].y))
