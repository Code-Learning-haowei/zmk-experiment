import segyio
import numpy as np

den = segyio.open('./resource/MODEL_DENSITY_125cm.segy', ignore_geometry=True)
vel = segyio.open('./resource/MODEL_P-WAVE_VELOCITY_125cm.segy', ignore_geometry=True)

n_il = 1
n_xl = den.bin[segyio.BinField.Traces]
n_sam = den.bin[segyio.BinField.Samples]
del_D = den.bin[segyio.BinField.Interval]

den_tr = den.trace.raw[:]
vel_tr = vel.trace.raw[:]
Imp = den_tr*vel_tr
dt_iterval = np.zeros_like(vel_tr)
TWT = np.zeros_like(vel_tr)
dt_iterval = 2*del_D/1000./vel_tr
TWT = np.cumsum(dt_iterval, axis=1)

dt = 0.001
t_max = 4.004
t = np.repeat(np.arange(0, t_max, dt)[None, :], n_xl, axis=0)
Imp_tdom = np.array([np.interp(x=t[i], xp=TWT[i], fp=Imp[i]) for i in range(n_xl)])

Rc_tdom = np.zeros_like(Imp_tdom)

for i in range(n_xl):
    for j in range(np.int(t_max/dt)):
        Rc_tdom[i][j] = (Imp_tdom[i][j+1]-Imp_tdom[i][j])/(Imp_tdom[i][j+1]+Imp_tdom[i][j])
        print(Rc_tdom[i][j])

np.savetxt('./resource/Rc_tdom_td0001_result.txt', Rc_tdom)