---
declaration: theorem
origin: cited
lean: LogDerivZetaFinalBound
statement: formalized
proof: formalized
---

# LogDerivZetaFinalBound

Let $t\in\mathbb{R}$ with $|t|\geq 2$ and $0 < r' < r < R' < R<1$. If $f(z)=\zeta(z+3/2+it)$, then for all $z\in\overline{\mathbb{D}_{r'}}\setminus\mathcal{K}_f(R')$ we have that

$$
\left|\frac{f'}{f}(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}\right|
\ll\left(\frac{16r^2}{(r-r')^3}+\frac{1}{(R^2/R'-R')\,\log(R/R')}\right)\log|t|.
$$

## Depends on

- [SetOfZeros](../part-01/setofzeros.md)

## Proof depends on

- [norm-zeta-strict-mono-ofReal](norm-zeta-strict-mono-ofreal.md)
- [GlobalBound](globalbound.md)
- [ZetaFixedLowerBound](zetafixedlowerbound.md)
- [FinalBound](finalbound.md)

## Proof

Let $g(z)=\zeta(z+3/2+it)/\zeta(3/2+it)$. Note that $g(0)=1$ and for $|z|\leq R$

$$
|g(z)|=\frac{|\zeta(z+3/2+it)|}{|\zeta(3/2+it)|}
\leq\frac{\zeta(3/2)}{\zeta(3)}\cdot(7+2\,|t|)\leq\frac{13\,\zeta(3/2)}{3\,\zeta(3)}\,|t|
$$

by Theorems [ZetaFixedLowerBound](zetafixedlowerbound.md) and [GlobalBound](globalbound.md). Thus by Theorem [FinalBound](finalbound.md) we have that

$$
\left|\frac{g'}{g}(z)-\sum_{\rho\in\mathcal{K}_g(r)}\frac{m_g(\rho)}{z-\rho}\right|
\leq\left(\frac{16r^2}{(r-r')^3}+\frac{1}{(R^2/R'-R')\,\log(R/R')}\right)
\left(\log|t|+\log\left(\frac{13\,\zeta(3/2)}{3\,\zeta(3)}\right)\right).
$$

Now note that $f'/f=g'/g$, $\mathcal{K}_f(r)=\mathcal{K}_g(r)$, and $m_g(\rho)=m_f(\rho)$ for all $\rho\in\mathcal{K}_f(r)$. Thus we have that,

$$
\left|\frac{f'}{f}(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}\right|
\ll\left(\frac{16r^2}{(r-r')^3}+\frac{1}{(R^2/R'-R')\,\log(R/R')}\right)\log|t|
$$

where the implied constant $C$ is taken to be

$$
C\geq 1+\frac{\log(11\,\zeta(3/2)/\zeta(3))}{\log 2}.
$$

## Lean

Formalized as [`LogDerivZetaFinalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaFinalBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
