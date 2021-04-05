from thermo import Chemical
from tkinter import *


root = Tk()
root.geometry("400x400")
root.title("fluid mechanics with python")

def calc():
    t_water = float(tempWater_ent.get())+273.15
    d = float(pipeDia_ent.get())/1000
    v = float(vel_ent.get())

    print('temp water, °C= ',t_water)
    print('diameter, m= ', d)
    print('velocity, m/s= ', v)

    water = Chemical('water', T=t_water, P=1E5)
    rho_water = water.rho  # density
    mu_water = water.mu  # viscosity dynamic

    # print(mu_water/rho_water)

    n_reynolds = int(rho_water*v*d/mu_water)
    print('renolds number=', n_reynolds)

    if n_reynolds > 4000:
        print('the flow is turbulent...')
    else:
        print('the flow is laminar...')
    
    Label(root, text="Results").grid(row=4, column=0, pady=10)
    res_lbl = Label(root, text=str(n_reynolds), relief=SUNKEN, bg='white')
    res_lbl.grid(row=5, column=1, pady=2)

tempWater_lbl = Label(root, text="water temp [°C]")
tempWater_lbl.grid(row=0, column=0, sticky="w")
tempWater_ent = Entry(root, width=15)
tempWater_ent.insert(0,"15")
tempWater_ent.grid(row=0,column=1)

pipeDia_lbl = Label(root, text="internal pipe diameter [mm]")
pipeDia_lbl.grid(row=1, column=0, sticky="w")
pipeDia_ent = Entry(root, width=15)
pipeDia_ent.insert(0,"150")
pipeDia_ent.grid(row=1, column=1)

vel_lbl = Label(root, text="water velocity [m/s]")
vel_lbl.grid(row=2, column=0, sticky="w")
vel_ent = Entry(root, width=15)
vel_ent.insert(0,'5.5')
vel_ent.grid(row=2, column=1)

calc_btn=Button(root, text="calculate", command=calc)
calc_btn.grid(row=1,column=2, padx=20)



# teste2
# new branch

root.mainloop()
