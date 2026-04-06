import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# --- 물리 파라미터 ---
f_c = 28*(10**9)    # 중심 주파수 (28GHz)
c = 3*(10**8)       # 빛의 속도
lamda = c / f_c     # 파장 (lambda는 예약어이므로 lamda 혹은 lam 사용)
N = 257             # 안테나 소자 개수
d = lamda / 2       # 안테나 간격 (Half-wavelength)
D = (N - 1) * d     # 안테나 전체 크기 (Aperture)

phi = np.linspace(-np.pi,np.pi,1000)
r_R = (2*(D*np.cos(phi))**2)/lamda      #Rayleigh distance(changde of D due to effective aperture)
r_F = np.sqrt(np.abs((D**3)*np.sin(phi)*((np.cos(phi))**2))/lamda) # Fresnel distance

#거리를 이용해서 x,y 좌표 표현
y_R = r_R * np.cos(phi)
x_R = r_R * np.sin(phi)
y_F = r_F * np.cos(phi)
x_F = r_F * np.sin(phi)

fig, ax = plt.subplots(figsize=(10, 8))

ax.set_xlim(0, 300 * D)
ax.set_ylim(-200 * D, 200 * D)

ax.set_aspect('equal')

xticks = np.arange(0, 301 * D, 50 * D)
yticks = np.arange(-200 * D, 201 * D, 50 * D)

ax.set_xticks(xticks)
ax.set_yticks(yticks)

ax.set_xticklabels([f'${int(round(v/D))}D$' for v in xticks])
ax.set_yticklabels([f'${int(round(v/D))}D$' for v in yticks])

ax.set_xlabel('$y$ (m)', fontsize=13)
ax.set_ylabel('$x$ (m)', fontsize=13)
ax.grid(True, linestyle=':', alpha=0.6)

ax_ins = ax.inset_axes([0.62, 0.05, 0.35, 0.35])

ax_ins.set_xlim(0, 20 * D)
ax_ins.set_ylim(-40 * D, 40 * D)

ins_xticks = [0, 10 * D, 20 * D]
ins_yticks = [-40 * D, -20 * D, 0, 20 * D, 40 * D]
ax_ins.set_xticks(ins_xticks)
ax_ins.set_yticks(ins_yticks)

ax_ins.set_xticklabels(['$0$', '$10D$', '$20D$'], fontsize=9)
ax_ins.set_yticklabels(['$-40D$', '$-20D$', '$0$', '$20D$', '$40D$'], fontsize=9)

ax_ins.grid(True, linestyle=':', alpha=0.4)
# ---------------------------------------------------------

#plot Rayleigh distance
ax.plot(y_R, x_R, 'b--', label='Rayleigh distance (eff. aperture)', linewidth=2)
ax_ins.plot(y_R, x_R, 'b--', linewidth=2)

#plot Fresnel distance
ax.plot(y_F, x_F, 'g--', label='Rayleigh distance (eff. aperture)', linewidth=2)
ax_ins.plot(y_F, x_F, 'g--', linewidth=2)

plt.tight_layout()
plt.show()