import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from descartes import PolygonPatch
from adjustText import adjust_text
from matplotlib.patches import Circle, Wedge, Polygon, Path
from matplotlib.collections import PatchCollection

def map_ega(ref,est):
    fig, ax = plt.subplots()

    polygons = []

    A =  [[0,0],[0,10], [20,30],[20,50],[48,50],[120,140],[120,300],[300,300],[300,120],[140,120],[50,35],[50,0]]
    Bl = [[20,50],[48,50],[120,140],[120,300],[100,300],[100,150],[45,55],[20,55]]
    Br = [[50,0],[50,35],[140,120],[300,120],[300,100],[145,100],[65,35],[65,0]]
    Cl = [[20,55],[45,55],[100,150],[100,300],[75,300],[75,150],[40,60],[20,60]]
    Cr = [[65,0],[65,35],[145,100],[300,100],[300,85],[145,85],[90,45],[90,0]]
    Dl=  [[20,60],[40,60], [75,150],[75,300],[60,300],[60,130],[35,70],[20,70]]
    Dr=  [[90,0],[90,45],[145,85],[300,85],[300,60],[140,60],[120,50],[120,0]]
    El=  [[0,10],[20,30],[20,70],[35,70],[60,130],[60,300],[0,300]]
    Er=  [[120,0],[120,50],[140,60],[300,60],[300,0]]


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
    plt.text(105, 270, "B", fontsize=15)  #Bl
    plt.text(270, 105, "B", fontsize=15)  #Br
    plt.text(85, 270, "C", fontsize=15)  #Cl
    plt.text(270, 90, "C", fontsize=15)  #Cr
    plt.text(63, 270, "D", fontsize=15)   #Dl
    plt.text(270, 68, "D", fontsize=15)  #Dr
    plt.text(30, 270, "E", fontsize=15)   #El
    plt.text(270, 30, "E", fontsize=15)   #Er
    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.xticks([0, 50, 100, 150, 200, 250, 300])
    plt.yticks([0, 50, 100, 150, 200, 250, 300])
    plt.xlabel('Reference',fontsize=15)
    plt.ylabel('Estimated',fontsize=15)
    plt.show()