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
gamma = 0.95        #min threshold


phi = np.linspace(-np.pi/2,np.pi/2,1000)
r_R = (2*(D*np.cos(phi))**2)/lamda      #Rayleigh distance
r_F = np.sqrt(np.abs((D**3)*np.sin(phi)*((np.cos(phi))**2))/lamda) # Fresnel distance

#NUSW model의 UPD
r_UPD = np.zeros_like(phi)
for i, pi in enumerate(phi):
    sin_pi = np.sin(pi)
    cos_pi = np.cos(pi)
    abs_sin = np.abs(sin_pi)

    r_found = False

    # Case 1: 점이 안테나 길이 내에 있는 경우(|x| <= D/2)
    A1 = cos_pi**2 - gamma**2
    B1 = -gamma**2 * D * abs_sin
    C1 = -gamma**2 * (D**2) / 4

    if A1 != 0:
        det1 = B1**2 - 4*A1*C1
        if det1 >= 0:
            root1 = (-B1 + np.sqrt(det1)) / (2*A1)
            root2 = (-B1 - np.sqrt(det1)) / (2*A1)
            for root in [root1, root2]:
                if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
                    r_UPD[i] = root
                    r_found = True
                    break
    else:
        root = -C1 / B1
        if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
            r_UPD[i] = root
            r_found = True

    #Case 2: 점이 안테나 길이를 벗어난 경우(|x| > D/2)
    if not r_found:
        A2 = 1.0
        B2 = -D * abs_sin * (1+gamma**2)/(1-gamma**2)
        C2 = (D**2) / 4

        det2 = B2**2 - 4*A2*C2
        if det2 >= 0:
            # Case 2는 원의 방정식 형태이며, 우리는 가장 바깥쪽 경계(Outer boundary)를 원함
            # 따라서 더 큰 양수 근을 취함
            root1 = (-B2 + np.sqrt(det2)) / (2*A2)
            root2 = (-B2 - np.sqrt(det2)) / (2*A2)
            
            valid_roots = [rt for rt in [root1, root2] if rt > 0 and (rt * abs_sin) > (D/2 - 1e-6)]
            if valid_roots:
                r_UPD[i] = max(valid_roots)

# General model의 UPD
r_general = np.zeros_like(phi)
for i, pi in enumerate(phi):
    sin_pi = np.sin(pi)
    cos_pi = np.cos(pi)
    abs_sin = np.abs(sin_pi)

    r_found = False

    # Case 1: 점이 안테나 길이 내에 있는 경우(|x| <= D/2)
    A1 = cos_pi**2 - gamma**(1.25)
    B1 = -gamma**(1.25) * D * abs_sin
    C1 = -gamma**(1.25) * (D**2) / 4

    if A1 != 0:
        det1 = B1**2 - 4*A1*C1
        if det1 >= 0:
            root1 = (-B1 + np.sqrt(det1)) / (2*A1)
            root2 = (-B1 - np.sqrt(det1)) / (2*A1)
            for root in [root1, root2]:
                if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
                    r_general[i] = root
                    r_found = True
                    break
    else:
        root = -C1 / B1
        if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
            r_general[i] = root
            r_found = True

    #Case 2: 점이 안테나 길이를 벗어난 경우(|x| > D/2)
    if not r_found:
        A2 = 1.0
        B2 = -D * abs_sin * (1+gamma**(1.25))/(1-gamma**(1.25))
        C2 = (D**2) / 4

        det2 = B2**2 - 4*A2*C2
        if det2 >= 0:
            # Case 2는 원의 방정식 형태이며, 우리는 가장 바깥쪽 경계(Outer boundary)를 원함
            # 따라서 더 큰 양수 근을 취함
            root1 = (-B2 + np.sqrt(det2)) / (2*A2)
            root2 = (-B2 - np.sqrt(det2)) / (2*A2)
            
            valid_roots = [rt for rt in [root1, root2] if rt > 0 and (rt * abs_sin) > (D/2 - 1e-6)]
            if valid_roots:
                r_general[i] = max(valid_roots)

#거리를 이용해서 x,y 좌표 표현
y_R = r_R * np.cos(phi)
x_R = r_R * np.sin(phi)
y_F = r_F * np.cos(phi)
x_F = r_F * np.sin(phi)
y_UPD = r_UPD * np.cos(phi)
x_UPD = r_UPD * np.sin(phi)
y_general = r_general * np.cos(phi)
x_general = r_general * np.sin(phi)

fig, ax = plt.subplots(figsize=(10,8))

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
ax.plot(y_R, x_R, 'b--', label='Rayleigh distance', linewidth=2)
ax_ins.plot(y_R, x_R, 'b--', linewidth=2)

#plot Fresnel distance
ax.plot(y_F, x_F, 'g--', label='Fresnel distance', linewidth=2)
ax_ins.plot(y_F, x_F, 'g--', linewidth=2)

#plot UPD (NUSW model) 
ax.plot(y_UPD, x_UPD, color='purple', linestyle='dotted', label='Uniform-Power distance, NUSW', linewidth=2)
ax_ins.plot(y_UPD, x_UPD, color='purple', linestyle='dotted', linewidth=2)

#plot general model
ax.plot(y_general, x_general, color='red', linestyle='solid', label='Uniform-Power distance, General', linewidth=2)
ax_ins.plot(y_general, x_general, color='red', linestyle='solid', linewidth=2)

ax.legend(loc='upper right',       # 위치 (우측 상단)
          bbox_to_anchor=(1.0, 1.0), # 세부 위치 미세 조정 (x, y 비율)
          fontsize=11,             # 폰트 크기
          frameon=False)           # 테두리 상자 없애기

plt.tight_layout()
plt.show()