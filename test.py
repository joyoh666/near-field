import numpy as np
import matplotlib.pyplot as plt

# --- 파라미터 설정 ---
D = 1.0        # 안테나 배열의 길이
Gamma = 0.95    # 전력 편차 허용 기준

# --- 1. 각도(theta) 배열 생성 ---
# -pi/2 (-90도) 부터 pi/2 (90도) 까지 각도를 촘촘하게 나눔
theta = np.linspace(-np.pi/2, np.pi/2, 1000)
r = np.zeros_like(theta)

# --- 2. 각도별로 r(theta) 계산 ---
for i, th in enumerate(theta):
    sin_th = np.sin(th)
    cos_th = np.cos(th)
    abs_sin = np.abs(sin_th)
    
    r_found = False
    
    # [Case 1] 투영점이 안테나 길이 내에 있는 경우 (Region 1)
    A1 = cos_th**2 - Gamma
    B1 = -Gamma * D * abs_sin
    C1 = -Gamma * (D**2) / 4
    
    # 2차 방정식 근의 공식 계산
    if A1 != 0:
        det1 = B1**2 - 4*A1*C1
        if det1 >= 0:
            root1 = (-B1 + np.sqrt(det1)) / (2*A1)
            root2 = (-B1 - np.sqrt(det1)) / (2*A1)
            # 유효한 양수 근 중에서 Case 1의 기하학적 조건을 만족하는지 확인
            for root in [root1, root2]:
                if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
                    r[i] = root
                    r_found = True
                    break
    else: # A1 == 0 인 특이 케이스 (cos^2(theta) == Gamma)
        root = -C1 / B1
        if root > 0 and (root * abs_sin) <= (D/2 + 1e-6):
            r[i] = root
            r_found = True
            
    # [Case 2] 투영점이 안테나 길이를 벗어난 경우 (Region 2)
    # Case 1에서 해를 찾지 못했다면(즉, End-fire에 가까운 각도라면) Case 2 방정식을 풂
    if not r_found:
        A2 = 1.0
        B2 = -D * abs_sin * (1 + Gamma) / (1 - Gamma)
        C2 = (D**2) / 4
        
        det2 = B2**2 - 4*A2*C2
        if det2 >= 0:
            # Case 2는 원의 방정식 형태이며, 우리는 가장 바깥쪽 경계(Outer boundary)를 원함
            # 따라서 더 큰 양수 근을 취함
            root1 = (-B2 + np.sqrt(det2)) / (2*A2)
            root2 = (-B2 - np.sqrt(det2)) / (2*A2)
            
            valid_roots = [rt for rt in [root1, root2] if rt > 0 and (rt * abs_sin) > (D/2 - 1e-6)]
            if valid_roots:
                r[i] = max(valid_roots)

# --- 3. 극좌표(r, theta)를 직교좌표(y, x)로 변환 ---
# 논문의 그래프 축 설정에 맞춤 (가로축 y, 세로축 x)
y_plot = r * np.cos(theta)
x_plot = r * np.sin(theta)

# --- 4. 그래프 시각화 ---
plt.figure(figsize=(8, 8))

# 구한 (y, x) 좌표를 선으로 부드럽게 이음
plt.plot(y_plot, x_plot, color='purple', linestyle='dotted', linewidth=2.5, 
         label=f'Uniform-power distance, NUSW ($\Gamma$={Gamma})')

# 안테나 배열 표시
plt.plot([0, 0], [-D/2, D/2], color='black', linewidth=5, label='ULA Antenna Array')

# 축 설정 및 꾸미기
plt.xlabel('y (m)', fontsize=12)
plt.ylabel('x (m)', fontsize=12)
plt.title('Uniform Power Distance Locus (Angle-based)', fontsize=14)
plt.axhline(0, color='black', linestyle='-', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal') # 비율 유지
plt.xlim(0, 20)
plt.ylim(-30, 30)
plt.legend(loc='lower right')

plt.show()