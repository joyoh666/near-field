phase error를 기준으로 해서 거리를 구분하면 다음과 같다.
1. Rayleigh distance($d_r$)
   Rayleigh distance는 far-field와 radiative near-field region을 구분하는 지표이다. 만약 현재 UE와 BS 간의 거리가 $d_r$보다 크면 far-field, 작으면 radiative-near field에 있다고 해석할 수 있다.
2. Fresnel distance($d_F$)
   Fresnel distance는 radiative near-field와 reactive near-fiela를 구분하는 지표이다.

좌표평면에서 UE의 위치 벡터를 $\mathbf{r} = [r\cos\theta,r\sin\theta]^T$, BS의 위치 벡터를 $\mathbf{s}_n = [nd,0]^T$라고 할 때, 
$$||\mathbf{r}-\mathbf{s}_n|| = \sqrt{r^2+n^2d^2-2rnd\cos\theta}$$
라고 할 수 있다. 

Taylor series를 이용해서 다항식으로 표현하면, 
$$
||\mathbf{r}-\mathbf{s}_n|| \approx r - nd\sin\theta + \frac{n^2d^2\cos^2\theta}{2r}-\frac{n^3d^3\sin\theta\cos^2\theta}{2r^2} + ... 
$$ 
가 된다.

 Rayleigh distance는 far-field인지를 판단하는 지표이므로 거리 차이가 일차 식으로 표현되어 평면파가 나타날 수 있어야 한다. 관습적으로, phase error가 $\pi/8$ 정도이면 근사적으로 무시할 수 있기 때문에 Rayleigh distance는 2차항이 $\pi/8$이 되게 하는 r값으로 표현이 가능하다. 
 $$\frac{2\pi}{\lambda}\times\frac{n^2d^2\sin^2\theta}{2r}=\frac{\pi}{8} \rightarrow r = \frac{8}{\lambda}n^2d^2\sin^2\theta$$
 이때, 안테나 배열의 중심에서 멀리 떨어진 안테나일수록, n의 값이 커져서 phase error가 커지는데, 가장 phase error가 큰 안테나의 error가 $\pi/8$이면 되므로, nd 위치에 D/2(D : 안테나 배열의 길이)를 넣어서 계산하면, 
 $$d_R = \frac{2D^2\cos^2\theta}{\lambda}$$
 가 된다.   (안테나 배열의 중심이 좌표평면 상에서 원점에 위치한다고 가정 , 안테나 : ULA)

 Fresnel distance는 radiative near-field인지를 판단하는 지표이므로 phase error가 2차항까지만 나타나는 구면파로 표현되어야 한다. 따라서, 3차항의 phase error가 $\frac{\pi}{8}$이 되게 하는 r값으로 표현이 가능하다. 
 $$\frac{D^3\pi\sin\theta\cos^2\theta}{8r^2\lambda} = \frac{\pi}{8} \rightarrow d_F = \sqrt{\frac{D^3\sin\theta\cos^2\theta}{\lambda}}$$
 가 된다.

Rayleigh distance와 Fresnel distance를 통해 현재 전자기파가 평면파인지, 아니면 구면파인지를 판단할 수 있다.


phase error가 아닌 power variation을 기준으로 해서 서로 다른 region을 구분할 수 있다.
Uniform Power Distance : 전자기파의 세기가 일정한지, 아니면 거리에 따라 변하는 지를 구분하는 지표이다. phase error와는 기준이 다르기 때문에, far-field이어도 non-uniform power일 수도 있다.

1) USW model : 