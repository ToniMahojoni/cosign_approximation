import numpy as np
import matplotlib.pyplot as mpl

#Funktion zur Berechnung der Taylorreihe des cos mit deg Summanden an Stelle x
def taylorcos(deg, x):
        r=0
        for i in range(0,deg):
            r += ((-1)**i)*((x**(2*i))/np.math.factorial(2*i))
        return r

#Fenster
fig, graph = mpl.subplots(figsize=(10,6))
graph.set_xlabel('x aus R mit [-2pi, 2pi]')
graph.set_ylabel('y aus R')
graph.set_title("Approximation von cos(x)")
graph.axis([-2*np.pi-0.1, 2*np.pi+0.1, -1.1, 1.1])

#Axen
yaxis = mpl.subplot()
xaxis = mpl.subplot()
Dfx = np.linspace(-2*np.pi-0.1, 2*np.pi+0.1, 100)
Wfx = np.linspace(0, 0, 100) 
Wfy = np.linspace(-1.1, 1.1, 100)
xaxis.plot(Dfx, Wfx, color='k', linestyle='dashed')
yaxis.plot(Wfx, Wfy, color='k', linestyle='dashed')

#cos-Funktion
cos = mpl.subplot()
cos.plot(Dfx, np.cos(Dfx), label="cos(x)")

#Graph zeigen
graph.legend()
graph.grid(True)
mpl.show()

#generieren und plotten der einzelnen Funktionen mit p Summanden
for p in range(0,11):
    #Fenster
    fig, graph = mpl.subplots(figsize=(10,6))
    graph.set_xlabel('x aus R mit [-2pi, 2pi]')
    graph.set_ylabel('y aus R')
    graph.set_title("Approximation von cos(x)")
    graph.axis([-2*np.pi-0.1, 2*np.pi+0.1, -1.1, 1.1])

    #Axen
    yaxis = mpl.subplot()
    xaxis = mpl.subplot()
    Dfx = np.linspace(-2*np.pi-0.1, 2*np.pi+0.1, 100)
    Wfx = np.linspace(0, 0, 100) 
    Wfy = np.linspace(-1.1, 1.1, 100)
    xaxis.plot(Dfx, Wfx, color='k', linestyle='dashed')
    yaxis.plot(Wfx, Wfy, color='k', linestyle='dashed')

    #cos-Funktion
    cos = mpl.subplot()
    cos.plot(Dfx, np.cos(Dfx), label="cos(x)")

    #Potenzreihe mit p Summanden
    graph2 = mpl.subplot()
    WTC=[]
    for el in Dfx:
        WTC.append(taylorcos(p, el))
    graph2.plot(Dfx,WTC, label=('Potenzreihe mit ',p,' Summanden'))
    graph.legend(loc='lower center')
    graph.grid(True)
    mpl.show()

