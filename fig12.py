import numpy as np
import matplotlib.pyplot as plt

# 1. 시스템 파라미터 설정
f = 28e9                # 주파수: 28 GHz
c = 3e8                 # 빛의 속도
lambda_c = c / f        # 파장
d = lambda_c / 2        # 안테나 간격
N = 257                 # 안테나 개수

# 2. 분석을 위한 거리 설정
r_targets = [10, 35, 100]           # 타겟 초점 거리 (r)
x_dist = np.logspace(0, 4, 1000)    # 관측 거리 (10^0 m ~ 10^4 m, 로그 스케일)

# 안테나 인덱스 배열 (원점 중심)
n = np.arange(N) - (N - 1) / 2

# 배열의 물리적 크기(Aperture) 및 레일리 거리(Rayleigh Distance) 계산
D = (N - 1) * d
rayleigh_dist = 2 * (D**2) / lambda_c

# 그래프 스타일 설정
line_styles = ['b--', 'r-', 'k-.']
labels = [f'$r = {r}$ m' for r in r_targets]

plt.figure(figsize=(8, 6))

# 3. 각 타겟 거리에 대한 Array Gain 계산
for idx, r_focus in enumerate(r_targets):
    gain = np.zeros(len(x_dist))
    
    for i, x in enumerate(x_dist):
        # Broadside(정면, theta = pi/2)에서의 Fresnel 근사 위상 차이
        # phase = (2*pi/lambda) * (n^2 * d^2 / 2) * (1/x - 1/r_focus)
        phase_diff = (np.pi / lambda_c) * (n**2 * d**2) * (1/x - 1/r_focus)
        
        # 정규화된 배열 이득 (Normalized Array Gain)
        # 내적의 절댓값 계산 후 안테나 개수(N)로 정규화
        gain[i] = np.abs(np.sum(np.exp(1j * phase_diff))) / N
        
    plt.semilogx(x_dist, gain, line_styles[idx], label=labels[idx], linewidth=1.5)

# 4. 레일리 거리 표시 및 그래프 꾸미기
plt.axvline(x=rayleigh_dist, color='g', linestyle=':', linewidth=3, label=f'Rayleigh distance')

plt.title('Depth of Focus (Normalized Array Gain vs Distance)', fontsize=14)
plt.xlabel('Distance (m)', fontsize=12)
plt.ylabel('Normalized Array Gain', fontsize=12)
plt.xlim([10**0, 10**4])
plt.ylim([0, 1.05])
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(loc='center right', fontsize=11, framealpha=1, edgecolor='black')
plt.tight_layout()

plt.show()