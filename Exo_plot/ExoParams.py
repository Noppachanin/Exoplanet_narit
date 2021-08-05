import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

def Habit_zone(host_name='Sun',Albedo = 0.36,a=1,Stellar_R = 1,ST=5778 ):
    #print("Please adding planet's name, Stellar mass, Semimajor axis to Stellar R Ratio, and Stellar Radius")
    
    sigma = 5.67e-8
    Lsun = 3.84e26
    AU = 1.496e11
    pi = np.pi
    

    # Modify this boundary equation
    def boundary(Stellar_R,Albedo,T_eq):
        
        L = Stellar_R**2*(ST/5778)**4*Lsun
        R = np.sqrt((1-Albedo)*L/(16*pi*sigma*T_eq**4))

        return(R/AU)

    
    #print mstar
    T0 = 273.15
    T100 = 373.15

    Rin = boundary(Stellar_R, Albedo, T100)
    #Rin = Rin/AU# Normalize by AU
    Rout = boundary(Stellar_R, Albedo, T0)
    
    #Rout = Rout/AU
    



    #print(Rin,Rout)
    #print("Rin= {:.2e}, Rout= {:.2e}".format(Rin,Rout))
    #print(Rin)
    #print(Rout)
    # Inner Circle
    circle1 = plt.Circle((0, 0), Rin, color='w')
    # Outer Circle
    circle2 = plt.Circle((0, 0), Rout, color='aquamarine')
    # A planet's semi-majoraxis 
    R_planet = plt.Circle((0, 0), a, color='k', fill = False)


    fig, ax = plt.subplots()
    
    axis_lim = Rout*1.5
    #print(axis_lim)

    plt.xlim(-1*axis_lim ,axis_lim)
    plt.ylim(-1*axis_lim ,axis_lim)
    plt.plot(0,0, 'r.')

    ax.set_aspect('equal')

    ax.add_artist(circle2)
    ax.add_artist(circle1)
    ax.add_artist(R_planet)
    
    plt.xlabel('Astronomical unit')
    plt.ylabel('Astronomical unit')
    plt.title( 'Habitable zone of '+ host_name  )
    plt.savefig('figures/HabitZone_'+ host_name +'.png',dpi=300)
    #plt.show()

    return ax

def Exo_plot(host_name='HATS-2', R_ratio=0.1335, Inc = 87.2 ,Stellar_R = 0.898, a =5.50, ST= 5227 ):
    #print('Check all inputs: host_name, R_ratio(R_pl/R_star), Inc, Stellar_R, a(semi_axis(au)), Stellar Temperature(ST)')
    #print('Note that R_pl is in jupiter\'s radius unit ')
    #print("Drawing Exoplanet..............")
    fig, axes = plt.subplots()
    # Get transit parameters
    #Impact_params = 5 # map from the actual value to a integer between 0 to 10
    #R_ratio = 0.1 # from 0 to 1
    Stellar_R = Stellar_R * 6.96e8
    Jupiter_R = 7.15e7 
    Impact_params = np.cos(np.radians(Inc))*a/Stellar_R # Input as degree



    # Plot an exoplanet
    position = -1*Impact_params
    Drawing_exoplanet = plt.Circle( (0, position ), R_ratio, color = 'slategray')

    Drawing_jupiter = plt.Circle( (-1.5, -1.5 ), Jupiter_R/Stellar_R ,color = 'darkorange')
    Drawing_pl = plt.Circle( (-1.0, -1.5 ), R_ratio, color = 'gray')


    # Setting color
    #print('Stellar Temperature = %d' % ST)
    
    #30000 Blue
    if ST > 30000:
        color_star = 'blue'
    #10k-30k B-W
    elif ST > 10000:
        color_star = 'lightsteelblue'
    #7500-10k W
    elif ST > 7500:
        color_star = 'white'
    #6k-7.5k Y-W
    elif ST > 6000:
        color_star = 'lightyellow'
    #5.2k-6k Y
    elif ST > 5200:
        color_star = 'yellow'
    #3.7k-5.2k Oran
    elif ST > 3700:
        color_star = 'Orange'
    #1.3k-2.4k Red
    elif ST > 1300:
        color_star = 'red'
    #0.7k-1.3k Magenta
    elif ST > 700:
        color_star = 'magenta'
    # <700 Infrared
    elif ST < 700:
        color_star = 'palevioletred'

    #print(color_star)

    # Plot Host star
    Drawing_uncolored_circle = plt.Circle( (0, 0 ), 1 ,color = color_star)
    

    axes.set_facecolor("black")
    axes.set_xlim(-2, 2)
    axes.set_ylim(-2, 2)
    axes.set_aspect('equal')
    axes.add_artist(lines.Line2D([-2,2 ], [position, position], color='slategray',linewidth=0.2))
    axes.add_artist( Drawing_uncolored_circle )
    axes.add_artist( Drawing_exoplanet )
    axes.add_artist(Drawing_jupiter )
    axes.add_artist(Drawing_pl)
    axes.text(-0.5, -1.7, 'Compare a planet(Right) \n to Jupiter(Left)',color='white')
    #plt.gca().add_patch(Drawing_jupiter)
    #plt.gca().add_patch(Drawing_pl)

    plt.xlabel('Host star unit radius')
    plt.ylabel('Host star unit radius')
    plt.title( 'Exoplanet Visualization of '+ host_name)
    plt.savefig('figures/Transit_'+ host_name +'.png',dpi=300)
    #plt.show()

    
    #Exo_plot(host_name='HATS-2', R_ratio=0.1335, Inc = 87.2 ,Stellar_R = 0.898, a =5.50, ST= 5227 )
    return axes



#Test Code : 
#Habit_zone(host_name ,Albedo = 0.36,a = 1.5,Stellar_M =1,Stellar_R = 1 ):
#Exo_plot(host_name, R_ratio=0.1, Impact_params=0.5)

#Habit_zone('HATS-2',Albedo = 0.36,Stellar_M = 0.882,a =5.50,Stellar_R = 1 )
#Exo_plot('HATS-2', R_ratio=0.1335, Impact_params=0.271)
#plt.show()