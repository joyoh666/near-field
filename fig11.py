import numpy as np
import matplotlib.pyplot as plt

# 1. 파라미터 설정
f = 28e9                # 주파수: 28 GHz
c = 3e8                 # 빛의 속도
lambda_c = c / f        # 파장
d = lambda_c / 2        # 안테나 간격

N_list = [65, 129, 257, 513]

# 변경된 타겟 파라미터 (극좌표계)
r_target = 5.5          # 반경 5.5 m
theta_target = np.pi / 4 # 각도 45도

# 관측 공간 그리드 설정
y_grid = np.linspace(0.1, 8, 200)
x_grid = np.linspace(0.1, 8, 200)
Y, X = np.meshgrid(y_grid, x_grid)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

for idx, N in enumerate(N_list):
    # 2. 안테나 배열 위치 인덱스 n
    n = np.arange(N) - (N - 1) / 2
    
    # 3. 타겟 위치에 대한 Steering Vector 생성 (Fresnel 근사 공식)
    cos_theta_target = np.cos(theta_target)
    sin_theta_target = np.sin(theta_target)
    
    phase_target = -n * d * cos_theta_target + (n**2 * d**2 * sin_theta_target**2) / (2 * r_target)
    a_target = np.exp(-1j * 2 * np.pi / lambda_c * phase_target)
    
    # 4. 전체 공간에 대한 상관도 계산
    R_scan = np.sqrt(X**2 + Y**2)
    cos_theta_scan = Y / R_scan
    sin_theta_scan = X / R_scan
    
    n_ext = n[np.newaxis, np.newaxis, :]
    R_ext = R_scan[..., np.newaxis]
    cos_ext = cos_theta_scan[..., np.newaxis]
    sin_ext = sin_theta_scan[..., np.newaxis]
    
    phase_scan = -n_ext * d * cos_ext + (n_ext**2 * d**2 * sin_ext**2) / (2 * R_ext)
    a_scan = np.exp(-1j * 2 * np.pi / lambda_c * phase_scan)
    
    correlation = np.abs(np.sum(np.conj(a_target)[np.newaxis, np.newaxis, :] * a_scan, axis=-1)) / N
    
    # 5. 그래프 그리기
    ax = axes[idx]
    im = ax.pcolormesh(Y, X, correlation, cmap='jet', vmin=0, vmax=1, shading='auto')
    
    # 포커싱 타겟 지점 마커 표시 (극좌표 -> 직교좌표 변환)
    target_y_cartesian = r_target * cos_theta_target
    target_x_cartesian = r_target * sin_theta_target
    ax.plot(target_y_cartesian, target_x_cartesian, 'w+', markersize=12, markeredgewidth=2)
    
    ax.set_title(f'({"abcd"[idx]}) $N = {N}$', fontsize=14, pad=15)
    ax.set_xlabel('y (m)', fontsize=12)
    ax.set_ylabel('x (m)', fontsize=12)
    ax.set_aspect('equal')
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()