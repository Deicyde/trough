---
declaration: theorem
origin: cited
lean: LogDerivZetaUniformLogSquaredBoundStrip
statement: formalized
proof: formalized
---

# LogDerivZetaUniformLogSquaredBoundStrip

There exists a constant $F\in(0,1/42)$ such that for all $t\in\mathbb{R}$ with $|t|\geq 3$ one has

$$
1-\frac{F}{\log|t|}\leq\sigma\leq 3/2
\implies\left|\frac{\zeta'}{\zeta}(\sigma+it)\right|\ll\log^2|t|
$$

where the implied constant is uniform in $\sigma$.

## Depends on

- [ZeroInequality](../part-02/zeroinequality.md)

## Proof depends on

- [DeltaT](../part-02/deltat.md)
- [ZetaShiftFiniteZeros](../part-02/zetashiftfinitezeros.md)
- [ZerosBound](../part-01/zerosbound.md)
- [norm-zeta-strict-mono-ofReal](../part-02/norm-zeta-strict-mono-ofreal.md)
- [GlobalBound](../part-02/globalbound.md)
- [SetOfZeros](../part-01/setofzeros.md)
- [ZetaFixedLowerBound](../part-02/zetafixedlowerbound.md)
- [SumBoundII](sumboundii.md)
- [ZeroWindowFinite](../part-02/zerowindowfinite.md)
- [ZeroWindow](../part-02/zerowindow.md)
- [GapSize](gapsize.md)

## Proof

Take $F=E/3$ where $E$ comes from Theorem [ZeroInequality](../part-02/zeroinequality.md). Then we have that $\sigma\geq 1-\delta_t/3$. So, we apply Lemma [SumBoundII](sumboundii.md), which gives us that

$$
\left|\frac{\zeta'}{\zeta}(z)
-\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{z-\rho}\right|\ll\log|t|.
$$

Using the reverse triangle inequality and rearranging, we have that

$$
\left|\frac{\zeta'}{\zeta}(z)\right|
\leq\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{|z-\rho|}+C\,\log|t|
$$

where $C$ is the implied constant in Lemma [SumBoundII](sumboundii.md). Now applying Lemma [GapSize](gapsize.md) we have that

$$
\left|\frac{\zeta'}{\zeta}(z)\right|
\leq\frac{6}{\delta_t}\sum_{\rho\in\mathcal{Z}_t}m_\zeta(\rho)+C\,\log|t|.
$$

Now let $f(z)=\zeta(z+3/2+it)/\zeta(3/2+it)$ with $\rho=\rho'+3/2+it$. Then if $\rho\in\mathcal{Z}_t$ we have that

$$
0=\zeta(\rho)=\zeta(\rho'+3/2+it)=f(\rho')
$$

with the same multiplicity of zero, that is $m_\zeta(\rho)=m_f(\rho')$. And also if $\rho\in\mathcal{Z}_t$ then

$$
3/4\geq|\rho-(3/2+it)|=|\rho'|.
$$

Thus we change variables to have that

$$
\left|\frac{\zeta'}{\zeta}(z)\right|
\leq\frac{6}{\delta_t}\sum_{\rho'\in\mathcal{K}_f(3/4)}m_f(\rho')+C\,\log|t|.
$$

Now note that $f(0)=1$ and for $|z|\leq 5/6$ we have

$$
|f(z)|=\frac{|\zeta(z+3/2+it)|}{|\zeta(3/2+it)|}
\leq\frac{\zeta(3/2)}{\zeta(3)}\cdot(7+2\,|t|)\leq\frac{13\,\zeta(3/2)}{3\,\zeta(3)}\,|t|
$$

by Theorems [ZetaFixedLowerBound](../part-02/zetafixedlowerbound.md) and [GlobalBound](../part-02/globalbound.md). Thus by Theorem [ZerosBound](../part-01/zerosbound.md) we have that

$$
\sum_{\rho'\in\mathcal{K}_f(3/4)}m_f(\rho')
\leq\frac{\log|t|+\log(13\,\zeta(3/2)/(3\,\zeta(3)))}{\log((5/6)/(3/4))}\leq D\log|t|
$$

where $D$ is taken to be sufficiently large. Recall, by definition that, $\delta_t=E/\log|t|$ with $E$ coming from Theorem [ZeroInequality](../part-02/zeroinequality.md). By using this fact and the above, we have that

$$
\left|\frac{\zeta'}{\zeta}(z)\right|\ll\log^2|t|+\log|t|
$$

where the implied constant is taken to be bigger than $6D/E+C$. We know that the RHS is bounded above by $\ll\log^2|t|$; so the result follows.

## Lean

Formalized as [`LogDerivZetaUniformLogSquaredBoundStrip`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaUniformLogSquaredBoundStrip).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
