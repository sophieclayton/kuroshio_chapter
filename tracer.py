import sys
import numpy as np
import scipy.io as sio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import date


def daynToDate(dt):
    year = dt / 1000
    dayn = dt % 1000
    dat = date.fromordinal(date(year, 1, 1).toordinal() + dayn - 1)
    return dat


def loadLCS(runNumber, itnumStart, field):
    if field>=1 and field<=25:
        path = 'C:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    elif field>=26 and field<=60:   
        path = 'H:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    elif field>=61 and field<=85:   
        path = 'E:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    elif field>=86 and field<=100:   
        path = 'D:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    elif field>=101 and field<=120:   
        path = 'F:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    elif field>=121 and field<=147:   
        path = 'J:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);


    #path = 'F:/Mohammad/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    #path = 'J:/CS_Trunk/%10.10d/Lagrangian/MAT/Trajectory/%10.10d_%10.10d.mat' % (runNumber,itnumStart,field);
    content = sio.loadmat(path)
    X = content['X1']
    Y = content['Y1']
    X = X - 360
    return X, Y


def tracerBlock(X, Y, lonIndex1, lonIndex2, latIndex1, latIndex2):
    lons = X[lonIndex1:lonIndex2+1, latIndex1:latIndex2+1]
    lats = Y[lonIndex1:lonIndex2+1, latIndex1:latIndex2+1]
    lons = lons.flatten()
    lats = lats.flatten()
    return lons, lats    


def bwFat():
    ################ zonal elongation ######################
    h, w = 50, 200
    lonsPolar, latsPolar = tracerBlock(X, Y, 4950, 4950+w, 3420, 3420+h)    
    lonsNorth, latsNorth = tracerBlock(X, Y, 4950, 4950+w, 3200, 3200+h)    
    #lonsTZ, latsTZ = tracerBlock(X, Y, 4950, 4950+w, 3025, 3025+h)
    lonsTZ1, latsTZ1 = tracerBlock(X, Y, 4950, 4950+w, 3000, 3030)
    lonsTZ2, latsTZ2 = tracerBlock(X, Y, 4950, 4950+w, 3030, 3060)
    lonsTZ3, latsTZ3 = tracerBlock(X, Y, 4950, 4950+w, 3060, 3090)
    lonsTZ4, latsTZ4 = tracerBlock(X, Y, 4950, 4950+w, 3120, 3150)
    lonsSouth, latsSouth = tracerBlock(X, Y, 4950, 4950+w, 2840, 2840+h)
    ########################################################
    return lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth

    

def bwSkinny():
    ################ meridional elongation ######################
    h, w = 50, 30
    lonsPolar, latsPolar = tracerBlock(X, Y, 5032, 5032+w, 3420, 3420+h)    
    lonsNorth, latsNorth = tracerBlock(X, Y, 5032, 5032+w, 3200, 3200+h)    
    #lonsTZ, latsTZ = tracerBlock(X, Y, 5032, 5032+w, 3025, 3025+h)
    lonsTZ1, latsTZ1 = tracerBlock(X, Y, 5032, 5032+w, 2990, 3030)
    lonsTZ2, latsTZ2 = tracerBlock(X, Y, 5032, 5032+w, 3030, 3060)
    lonsTZ3, latsTZ3 = tracerBlock(X, Y, 5032, 5032+w, 3060, 3100)
    lonsTZ4, latsTZ4 = tracerBlock(X, Y, 5032, 5032+w, 3120, 3150)
    lonsSouth, latsSouth = tracerBlock(X, Y, 5032, 5032+w, 2840, 2840+h)
    ########################################################
    return lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth



def grad2Domain():
    lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth = bwFat()
    #lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth = bwSkinny()
    
    map = Basemap(llcrnrlon=-168,llcrnrlat=18.,urcrnrlon=-140,urcrnrlat=55,\
        rsphere=(6378137.00,6356752.3142),\
        resolution='l',area_thresh=1000.,projection='lcc',\
        lat_1=40.,lon_0=-158.)
    map.plot(lonsPolar, latsPolar, 'o', color='maroon', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsNorth, latsNorth, 'o', color='springgreen', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ1, latsTZ1, 'o', color='crimson', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ2, latsTZ2, 'o', color='white', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ3, latsTZ3, 'o', color='darkslategrey', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ4, latsTZ4, 'o', color='darkorange', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsSouth, latsSouth, 'o', color='darkviolet', markeredgecolor='none', markersize=1, latlon=True)
    
    map.drawcoastlines(linewidth=0.1)
    map.fillcontinents(color='#222222', lake_color='#222222')
    map.drawparallels(np.arange(10,60,5), linewidth=.2, labels=[1,1,0,0], fontsize=8)
    map.drawmeridians([-174, -170, -166, -162, -158, -154, -150, -146, -142], linewidth=.2, labels=[0,0,0,1], fontsize=8)
    map.shadedrelief()
    return



def kuroshio():
    ################ meridional elongation ######################

    h, w = 80, 200
    #cent = 5045   ## near 158W
    cent = 4495   ## near 180
    lonsPolar, latsPolar = tracerBlock(X, Y, cent-w, cent+w, 3300, 3400)    
    lonsNorth, latsNorth = tracerBlock(X, Y, cent-w, cent+w, 3200, 3300)    
    #lonsTZ, latsTZ = tracerBlock(X, Y, 4832-w, 4832+w, 3025, 3025+h)
    lonsTZ1, latsTZ1 = tracerBlock(X, Y, cent-w, cent+w, 2990, 3030)
    lonsTZ2, latsTZ2 = tracerBlock(X, Y, cent-w, cent+w, 3030, 3060)
    lonsTZ3, latsTZ3 = tracerBlock(X, Y, cent-w, cent+w, 3060, 3100)
    lonsTZ4, latsTZ4 = tracerBlock(X, Y, cent-w, cent+w, 3100, 3200)
    lonsSouth, latsSouth = tracerBlock(X, Y, cent-w, cent+w, 2840, 2840+h)
    ########################################################
    return lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth


def NPDomain():
    #lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth = bwFat()
    #lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth = bwSkinny()
    lonsPolar, latsPolar, lonsNorth, latsNorth, lonsTZ1, latsTZ1, lonsTZ2, latsTZ2, lonsTZ3, latsTZ3, lonsTZ4, latsTZ4, lonsSouth, latsSouth = kuroshio()
    
    map = Basemap(llcrnrlon=-210,llcrnrlat=10.,urcrnrlon=-130,urcrnrlat=55,\
        rsphere=(6378137.00,6356752.3142),\
        resolution='l',area_thresh=1000.,projection='lcc',\
        lat_1=40.,lon_0=-175.)
    map.plot(lonsPolar, latsPolar, 'o', color='maroon', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsNorth, latsNorth, 'o', color='springgreen', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ1, latsTZ1, 'o', color='crimson', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ2, latsTZ2, 'o', color='white', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ3, latsTZ3, 'o', color='darkslategrey', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsTZ4, latsTZ4, 'o', color='darkorange', markeredgecolor='none', markersize=1, latlon=True)
    map.plot(lonsSouth, latsSouth, 'o', color='darkviolet', markeredgecolor='none', markersize=1, latlon=True)
    
    map.drawcoastlines(linewidth=0.1)
    map.fillcontinents(color='#222222', lake_color='#222222')
    map.drawparallels(np.arange(10,60,5), linewidth=.2, labels=[1,1,0,0], fontsize=8)
    #map.drawmeridians([-174, -170, -166, -162, -158, -154, -150, -146, -142], linewidth=.2, labels=[0,0,0,1], fontsize=8)
    map.drawmeridians([-158, -140, 140, 160, 180], linewidth=.2, labels=[0,0,0,1], fontsize=8)
    map.shadedrelief()
    return


direction = -1
runNumber = 2017147
itnumStart = 2017147


#startFrame = 1
#endFrame = 118

startFrame = int(sys.argv[1])
endFrame = int(sys.argv[2])


for field in range(startFrame, endFrame+1):
    print 'Field: %2.2d' % field
    X, Y = loadLCS(runNumber, itnumStart, field)
    plt.clf()

    #grad2Domain()    ## gradient2 transect
    NPDomain()       ##  north pacific - kuroshio
    

    plt.title(daynToDate(itnumStart + (direction)*field).strftime('%b %d %Y'))
    plt.show()    
    figPath = 'figs/'
    plt.savefig('%s%7.7d.png' % (figPath, field), bbox_inches='tight' , dpi=300)
