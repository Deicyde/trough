---
declaration: theorem
origin: cited
lean: SumBoundII
statement: formalized
proof: formalized
---

# SumBoundII

For all $t\in\mathbb{R}$ with $|t|\geq 2$ and $z=\sigma+it$ where $1-\delta_t/3\leq\sigma\leq 3/2$, we have that

$$
\left|\frac{\zeta'}{\zeta}(z)
-\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{z-\rho}\right|\ll\log|t|.
$$

## Depends on

- [DeltaT](../part-02/deltat.md)
- [ZeroWindow](../part-02/zerowindow.md)

## Proof depends on

- [ZeroInequality](../part-02/zeroinequality.md)
- [ZetaShiftFiniteZeros](../part-02/zetashiftfinitezeros.md)
- [SetOfZeros](../part-01/setofzeros.md)
- [DeltaRange](../part-02/deltarange.md)
- [LogDerivZetaFinalBound](../part-02/logderivzetafinalbound.md)

## Proof

By Lemma [DeltaRange](../part-02/deltarange.md) we have that

$$
-29/54<-1/2-\delta_t/3\leq\sigma-3/2\leq0.
$$

We apply Theorem [LogDerivZetaFinalBound](../part-02/logderivzetafinalbound.md) where $r'=2/3$, $r=3/4$, $R'=4/5$, and $R=5/6$. Thus for all $z\in\overline{\mathbb{D}_{2/3}}\setminus\mathcal{K}_f(4/5)$ we have that

$$
\left|\frac{\zeta'}{\zeta}(z+3/2+it)
-\sum_{\rho\in\mathcal{K}_f(3/4)}\frac{m_f(\rho)}{z-\rho}\right|\ll\log|t|
$$

where $f(z)=\zeta(z+3/2+it)$ for $t\in\mathbb{R}$ with $|t|\geq 2$. Now if we let $z=\sigma-3/2$, then $z\in(-29/54,0)\subseteq\overline{\mathbb{D}_{2/3}}$. Additionally, $f(z)=\zeta(\sigma+it)$, where $\sigma+it$ lies in the zero free region given by Lemma [ZeroInequality](../part-02/zeroinequality.md) since $\sigma\geq 1-\delta_t/3\geq 1-\delta_t$. Thus, $z\not\in\mathcal{K}_f(4/5)$. So,

$$
\left|\frac{\zeta'}{\zeta}(\sigma+it)
-\sum_{\rho\in\mathcal{K}_f(3/4)}\frac{m_f(\rho)}{\sigma-3/2-\rho}\right|\ll\log|t|.
$$

But now note that if $\rho\in\mathcal{K}_f(3/4)$, then $\zeta(\rho+3/2+it)=0$ and $|\rho|\leq 3/4$ (and the argument works in reverse). Additionally, note that $m_f(\rho)=m_\zeta(\rho+3/2+it)$. So changing variables using these facts gives us that

$$
\left|\frac{\zeta'}{\zeta}(\sigma+it)
-\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{\sigma+it-\rho}\right|\ll\log|t|.
$$

## Lean

Formalized as [`SumBoundII`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SumBoundII).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
