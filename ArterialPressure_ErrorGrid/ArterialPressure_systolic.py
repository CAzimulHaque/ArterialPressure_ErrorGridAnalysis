import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from descartes import PolygonPatch
from adjustText import adjust_text
from matplotlib.patches import Circle, Wedge, Polygon, Path
from matplotlib.collections import PatchCollection

def sbp_ega(ref,est):
    fig, ax = plt.subplots()

    polygons = []

    A =  [[0,0],[0,20], [35,70],[65,70],[190,220],[190,300],[300,300],[300,190],[220,190],[140,90],[115,90],[80,65],[80,0]]
    Bl = [[35,70],[65,70],[190,220],[190,300],[160,300],[160,215],[65,78],[35,78]]
    Br = [[80,0],[80,65],[115,90],[140,90],[220,190],[300,190],[300,160],[210,160],[145,70],[100,70],[100,0]]
    Cl = [[35,78],[65,78],[160,215],[160,300],[110,300],[110,210],[60,85],[35,85]]
    Cr = [[100,0],[100,70],[145,70],[210,160],[300,160],[300,140],[210,140],[150,60],[150,0]]
    Dl=  [[35,85],[60,85], [110,210],[110,300],[80,300],[80,180],[60,110],[35,110]]
    Dr=  [[150,0],[150,60],[210,140],[300,140],[300,85],[210,85],[180,65],[180,0]]
    El=  [[0,20],[35,70],[35,110],[60,110],[80,180],[80,300],[0,300]]
    Er=  [[180,0],[180,65],[210,85],[300,85],[300,0]]


    pA = Polygon(np.asarray(A),True)
    pBl = Polygon(np.asarray(Bl),True)
    pBr = Polygon(np.asarray(Br),True)
    pCl = Polygon(np.asarray(Cl),True)
    pCr = Polygon(np.asarray(Cr),True)
    pDl = Polygon(np.asarray(Dl),True)
    pDr = Polygon(np.asarray(Dr),True)
    pEl = Polygon(np.asarray(El),True)
    pEr = Polygon(np.asarray(Er),True)
    polygons.append(pA)
    polygons.append(pBl)
    polygons.append(pBr)
    polygons.append(pCl)
    polygons.append(pCr)
    polygons.append(pDl)
    polygons.append(pDr)
    polygons.append(pEl)
    polygons.append(pEr)


    p = PatchCollection(polygons)
    p.set_color(['#0BCA6A','#0AF675','#0AF675','#FEF584','#FEF584','#FFDFC5','#FFDFC5','#FFADAD','#FFADAD'])
    ax.add_collection(p)



    plt.plot([0,300],[0,300], '--', c='#06720D')


    x = ref
    y = est

    sA = []
    sB = []
    sC = []
    sD = []
    sE = []
    for i in range(len(y)):
        sA.append(int(pA.contains_point([x[i],y[i]]))*30)
        sB.append(int(pBr.contains_point([x[i],y[i]]) or pBl.contains_point([x[i],y[i]]))*30)
        sC.append(int(pCr.contains_point([x[i],y[i]]) or pCl.contains_point([x[i],y[i]]))*30)
        sD.append(int(pDr.contains_point([x[i],y[i]]) or pDl.contains_point([x[i],y[i]]))*30)
        sE.append(int(pEr.contains_point([x[i],y[i]]) or pEl.contains_point([x[i],y[i]]))*30)

    plt.scatter(x,y,s=sA,color='#077739')
    plt.scatter(x,y,s=sB,color='#EDAA0E')
    plt.scatter(x,y,s=sC,color=[0.886, 0.654, 0.133,1])
    plt.scatter(x,y,s=sD,color=[0.854,0.213,0.068,1])
    plt.scatter(x,y,s=sE,color=[0.854,0.213,0.068,1])


    lx = np.linspace(min(x), max(x), 100)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(lx,p(lx), c='#06720D')


    plt.text(210, 250, "A", fontsize=15)
    plt.text(250, 210, "A", fontsize=15)
    plt.text(270, 170, "B", fontsize=15)
    plt.text(170, 270, "B", fontsize=15)
    plt.text(270, 145, "C", fontsize=15)
    plt.text(130, 270, "C", fontsize=15)
    plt.text(90, 270, "D", fontsize=15)
    plt.text(270, 110, "D", fontsize=15)
    plt.text(30, 270, "E", fontsize=15)
    plt.text(270, 45, "E", fontsize=15)
    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.xticks([0, 50, 100, 150, 200, 250, 300])
    plt.yticks([0, 50, 100, 150, 200, 250, 300])
    plt.xlabel('Reference',fontsize=15)
    plt.ylabel('Estimated',fontsize=15)
    plt.show()