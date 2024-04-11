import numpy as np
import matplotlib.pyplot as mpl

# function for calculating the taylorpolynomial of the cosine function
# deg = degree of the taylor polynomial
# x = point of developement
def taylorcos(deg, x): 
        r=0
        for i in range(0,deg):
            r += ((-1)**i)*((x**(2*i))/np.math.factorial(2*i))
        return r

# setup for the window
fig, graph = mpl.subplots(figsize=(10,6))
graph.set_xlabel('x aus R mit [-2pi, 2pi]')
graph.set_ylabel('y aus R')
graph.set_title("Approximation von cos(x)")
graph.axis([-2*np.pi-0.1, 2*np.pi+0.1, -1.1, 1.1])

# setup for the axes
yaxis = mpl.subplot()
xaxis = mpl.subplot()
Dfx = np.linspace(-2*np.pi-0.1, 2*np.pi+0.1, 100)
Wfx = np.linspace(0, 0, 100) 
Wfy = np.linspace(-1.1, 1.1, 100)
xaxis.plot(Dfx, Wfx, color='k', linestyle='dashed')
yaxis.plot(Wfx, Wfy, color='k', linestyle='dashed')

# plot the cosine function for comparison
cos = mpl.subplot()
cos.plot(Dfx, np.cos(Dfx), label="cos(x)")

# plot the final graph
graph.legend()
graph.grid(True)
mpl.show()

# generate and plot the polynomials of degree p
for p in range(0,11):
    # setup for the window
    fig, graph = mpl.subplots(figsize=(10,6))
    graph.set_xlabel('x aus R mit [-2pi, 2pi]')
    graph.set_ylabel('y aus R')
    graph.set_title("Approximation von cos(x)")
    graph.axis([-2*np.pi-0.1, 2*np.pi+0.1, -1.1, 1.1])

    # setup for the axes
    yaxis = mpl.subplot()
    xaxis = mpl.subplot()
    Dfx = np.linspace(-2*np.pi-0.1, 2*np.pi+0.1, 100)
    Wfx = np.linspace(0, 0, 100) 
    Wfy = np.linspace(-1.1, 1.1, 100)
    xaxis.plot(Dfx, Wfx, color='k', linestyle='dashed')
    yaxis.plot(Wfx, Wfy, color='k', linestyle='dashed')

    # plot the cosine function for comparison
    cos = mpl.subplot()
    cos.plot(Dfx, np.cos(Dfx), label="cos(x)")

    # taylor polynomial with degree p
    graph2 = mpl.subplot()
    WTC=[]
    for el in Dfx:
        WTC.append(taylorcos(p, el))
    graph2.plot(Dfx,WTC, label=('Potenzreihe mit ',p,' Summanden'))

    # plot the graph
    graph.legend(loc='lower center')
    graph.grid(True)
    mpl.show()

