---
declaration: theorem
origin: cited
lean: SumBoundI
statement: formalized
proof: formalized
---

# SumBoundI

For all $\delta\in (0,1)$ and $t\in\mathbb{R}$ with $|t|\geq 2$ we have

$$
\left|\frac{\zeta'}{\zeta}(1+\delta+it)
-\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{1+\delta+it-\rho}\right|\ll\log|t|.
$$

## Depends on

- [ZeroWindow](zerowindow.md)

## Proof depends on

- [ZetaShiftFiniteZeros](zetashiftfinitezeros.md)
- [SetOfZeros](../part-01/setofzeros.md)
- [LogDerivZetaFinalBound](logderivzetafinalbound.md)

## Proof

We apply Theorem [LogDerivZetaFinalBound](logderivzetafinalbound.md) where $r'=2/3$, $r=3/4$, $R'=4/5$, and $R=5/6$. Thus, for all $z\in\overline{\mathbb{D}_{2/3}}\setminus\mathcal{K}_f(4/5)$ we have that

$$
\left|\frac{\zeta'}{\zeta}(z+3/2+it)
-\sum_{\rho\in\mathcal{K}_f(3/4)}\frac{m_f(\rho)}{z-\rho}\right|\ll\log|t|
$$

where $f(z)=\zeta(z+3/2+it)$ for $t\in\mathbb{R}$ with $|t|\geq 2$. Now if we let $z=-1/2+\delta$, then $z\in(-1/2,1/2)\subseteq\overline{\mathbb{D}_{2/3}}$. Additionally, $f(z)=\zeta(1+\delta+it)$, where $1+\delta+it$ lies in the zero-free region where $\sigma>1$. Thus, $z\not\in\mathcal{K}_f(4/5)$. So,

$$
\left|\frac{\zeta'}{\zeta}(1+\delta+it)
-\sum_{\rho\in\mathcal{K}_f(3/4)}\frac{m_f(\rho)}{-1/2+\delta-\rho}\right|
\ll\log|t|.
$$

But now note that if $\rho\in\mathcal{K}_f(3/4)$, then $\zeta(\rho+3/2+it)=0$ and $|\rho|\leq 3/4$. Thus, $\rho+3/2+it\in\mathcal{Z}_t$ (the argument works in reverse as well). Additionally, note that $m_f(\rho)=m_\zeta(\rho+3/2+it)$. So changing variables using these facts gives us that

$$
\left|\frac{\zeta'}{\zeta}(1+\delta+it)
-\sum_{\rho\in\mathcal{Z}_t}\frac{m_\zeta(\rho)}{1+\delta+it-\rho}\right|
\ll\log|t|.
$$

## Lean

Formalized as [`SumBoundI`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SumBoundI).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
