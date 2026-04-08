phase error를 기준으로 해서 거리를 구분하면 다음과 같다.
1. Rayleigh distance($d_r$)
   Rayleigh distance는 far-field와 radiative near-field region을 구분하는 지표이다. 만약 현재 UE와 BS 간의 거리가 $d_r$보다 크면 far-field, 작으면 radiative-near field에 있다고 해석할 수 있다.
2. Fresnel distance($d_F$)
   Fresnel distance는 radiative near-field와 reactive near-fiela를 구분하는 지표이다.

좌표평면에서 UE의 위치 벡터를 $\mathbf{r} = [x,y]^T = [r\cos\theta,r\sin\theta]^T$, BS의 위치 벡터를 $\mathbf{s}_n = [nd,0]^T$라고 할 때, 
$$||\mathbf{r}-\mathbf{s}_n|| = \sqrt{r^2+n^2d^2-2rnd\cos\theta}$$
라고 할 수 있다. 

Taylor series를 이용해서 다항식으로 표현하면, 
$$
||\mathbf{r}-\mathbf{s}_n|| \approx r - nd\sin\theta + \frac{n^2d^2\cos^2\theta}{2r}-\frac{n^3d^3\sin\theta\cos^2\theta}{2r^2} + ... 
$$ 
가 된다.

 Rayleigh distance는 far-field인지를 판단하는 지표이므로 거리 차이가 일차 식으로 표현되어 평면파가 나타날 수 있어야 한다. 관습적으로, phase error가 $\pi/8$ 정도이면 근사적으로 무시할 수 있기 때문에 Rayleigh distance는 2차항이 $\pi/8$이 되게 하는 r값으로 표현이 가능하다. 
 $$\frac{2\pi}{\lambda}\times\frac{n^2d^2\cos^2\theta}{2r}=\frac{\pi}{8} \rightarrow r = \frac{8}{\lambda}n^2d^2\cos^2\theta$$
 이때, 안테나 배열의 중심에서 멀리 떨어진 안테나일수록, n의 값이 커져서 phase error가 커지는데, 가장 phase error가 큰 안테나의 error가 $\pi/8$이면 되므로, nd 위치에 D/2(D : 안테나 배열의 길이)를 넣어서 계산하면, 
 $$d_R = \frac{2D^2\cos^2\theta}{\lambda}$$
 가 된다.   (안테나 배열의 중심이 좌표평면 상에서 원점에 위치한다고 가정 , 안테나 : ULA)

 Fresnel distance는 radiative near-field인지를 판단하는 지표이므로 phase error가 2차항까지만 나타나는 구면파로 표현되어야 한다. 따라서, 3차항의 phase error가 $\frac{\pi}{8}$이 되게 하는 r값으로 표현이 가능하다. 
 $$\frac{D^3\pi\sin\theta\cos^2\theta}{8r^2\lambda} = \frac{\pi}{8} \rightarrow d_F = \sqrt{\frac{D^3\sin\theta\cos^2\theta}{\lambda}}$$
 가 된다.

Rayleigh distance와 Fresnel distance를 통해 현재 전자기파가 평면파인지, 아니면 구면파인지를 판단할 수 있다.


phase error가 아닌 power variation을 기준으로 해서 서로 다른 region을 구분할 수 있다.
Uniform Power Distance : 전자기파의 세기가 일정한지, 아니면 거리에 따라 변하는 지를 구분하는 지표이다. phase error와는 기준이 다르기 때문에, far-field이어도 non-uniform power일 수도 있다.
$$\begin{aligned}r_{UPD} &= \argmin\limits_r r \\
&s.t. \ \frac{\min\beta_{m,n}}{\max\beta_{m,n}} >= \Gamma (논문에서는 \ 0.95로 \ 설정)
\end{aligned}
$$

1) USW model : UE의 거리가 uniform power distance보다 큰 경우, 전자기파의 amplitude는 일정하다고 가정

2) NUSW model
   - UE의 거리가 uniform power distance보다 작은 경우
   - 전자기파의 ampliude가 거리에 따라 달라진다. 

   $$\beta_{m,n} = \frac{1}{\sqrt{4\pi \Vert \mathbf{r}_m-\mathbf{s}_n \Vert^2}}$$


   $$
   \begin{aligned}
   1.& \ |x| <= \frac{D}{2} :\ d_{min}^2 = y^2 \ , \ d_{max}^2 = y^2 + (|x| + \frac{D}{2})^2 \\ 
   2.& \ |x| > \frac{D}{2}  \ d_{min}^2 = y^2 + (|x| - \frac{D}{2})^2 \ , \ d_{max}^2 = y^2 + (|x| + \frac{D}{2})^2 \\
     &\frac{\frac{1}{\sqrt{4\pi d_{max}^2}}}{\frac{1}{\sqrt{4\pi d_{min}^2}}} \rightarrow \frac{d_{min}^2}{d_{max}^2} = \Gamma^2
   \end{aligned}
   $$
   
   위의 식에 $d_{min},d_{max}$을 대입한 후에 $(x,y) = (r\cos\theta,r\sin\theta)$로 바꿔서 식을 정리하면, r에 대한 이차방정식이 나온다. 조건에 맞는 r값을 구하면 UPD값을 얻을 수 있다.

3) General model
    - 전자기파의 amplitude가 거리, effective aperture loss, polarization loss에 따라 달라진다.
    - Effective aperture loss : 안테나의 위치에 따라 전자기파가 수신되는 각도가 달라지는데, 이에 의해 발생하는 손실을 의미한다.
    - Polarization loss : 전자기파는 진행 방향에 수직인 방향으로 진동을 하는데, 수신단에서 이와 같은 방향으로 진동하는 것을 받지 않을 때 나타나는 손실을 의미한다.

    $$\beta_{m,n}^G = \sqrt{\frac{G_1G_2}{4\pi \Vert \mathbf{r}_m-\mathbf{s}_n \Vert^2}} \ , \ G_1 : effective\ aperture\ loss, \  G_2 : polarization\ loss$$

    - ULA가 x-z plane에 있다고 가정하므로 transmit antenna의 normal vector $\hat{\mathbf{u}_s} = [0,1,0]^T$
    - $G_1 = \frac{y}{d}$ 
    - 진행 방향이 y축이므로 진동 방향은 x축, $\rho_w = [1,0,0]^T = \hat{\mathbf{J}}$
    - $G_2 = \frac{y^2}{d^2}$
    - UPD 구하는 공식에 loss들을 대입하면, (G1만 대입, G2는 안테나 모양에 따라 식이 달라지기 때문에 제외)
     $$\sqrt{\frac{d_{min}^3}{d_{max}^3}} = \Gamma \rightarrow \frac{d_{min}^2}{d_{max}^2} = \Gamma^{4/3}$$