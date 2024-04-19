import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(layout= 'constrained')

time: list= [*range(0,200,20)]

stuff = plt.gca()
stuff.set_xlim([time[0],time[-1]])
stuff.set_ylim(10,45)


rnx: dict={
    
    '$\ Water $': [45, 40, 41, 41, 41,40.5, 40.5,40, 40, 40]
    ,
    '$\ HCl+NaOH^p1 $': [20, 33, 35, 35, 35, 35, 35, 35, 35, 34]
    ,
    '$\ HCl+ NaOH^p2 $': [18, 28, 29, 30, 30, 29, 30, 29.5, 30, 29.5]
    ,
    '$\ NH_4Cl + NaOH^p1 $': [16.25, 16, 18, 17, 17, 18, 17, 16, 16, 17.5]
    ,
    '$\ NH_4 Cl + NaOH^p2 $': [20, 21, 21.5, 21.5, 22, 22, 22, 21.5, 21.5, 21.5]
    ,
    '$\ NH_4 OH + HCl $':[16.5, 29, 28, 29, 29, 28, 28, 28, 28, 28]
    
    }

ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')
ax.set_title('Graph 1: Change of temperature during reactions')




for i in rnx:
    ax.plot(time,rnx[i], label= i, marker='.',markersize= 6)

ax.grid(visible = None, which = 'major', axis = 'both'
, color = '#2C2642')


ax.grid(visible = None, which = 'minor', axis = 'both'
, color = '#1C1416',alpha = .1)



ax.set_xticks(np.array(time))
factor: int = 10
ax.set_xticks(np.array([k for k in range(0,180,int(20/factor))]), minor = True)

ax.set_yticks(np.array([o for o in range( 10, 45, 1)]), minor = True)

ax.axvspan(0,20,color = '#98a2eb',alpha = .3)

plt.text(0,70,'initial reaction'
,fontsize = 7, color = 'black',rotation = 0)


ax.legend(fontsize = 7,loc =9)

plt.show()
