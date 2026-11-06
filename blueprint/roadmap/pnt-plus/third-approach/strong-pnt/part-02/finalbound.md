---
declaration: theorem
origin: cited
lean: FinalBound
statement: formalized
proof: formalized
---

# FinalBound

Let $B>1$ and $0 < r' < r < R' < R<1$. If $f:\mathbb{C}\to\mathbb{C}$ is a function analytic on neighborhoods of points in $\overline{\mathbb{D}_1}$ with $f(0)=1$ and $|f(z)|\leq B$ for all $|z|\leq R$, then for all $z\in\overline{\mathbb{D}_{r'}}\setminus\mathcal{K}_f(R')$ we have

$$
\left|\frac{f'}{f}(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}\right|
\leq\left(\frac{16r^2}{(r-r')^3}+\frac{1}{(R^2/R'-R')\,\log(R/R')}\right)\log B.
$$

## Depends on

- [SetOfZeros](../part-01/setofzeros.md)

## Proof depends on

- [BlaschkeNonZero](../part-01/blaschkenonzero.md)
- [BlaschkeB](../part-01/blaschkeb.md)
- [ZerosBound](../part-01/zerosbound.md)
- [CFunction](../part-01/cfunction.md)
- [JBlaschke](../part-01/jblaschke.md)
- [ZeroFactor](../part-01/zerofactor.md)
- [JBlaschkeDerivBound](jblaschkederivbound.md)
- [BlaschkeAnalytic](../part-01/blaschkeanalytic.md)
- [LogOfAnalyticFunction'](../part-01/logofanalyticfunction-2.md)

## Proof

Since $z\in\overline{\mathbb{D}_{r'}}\setminus\mathcal{K}_f(R')$ we know that $z\not\in\mathcal{K}_f(R')$; thus, by Definition [CFunction](../part-01/cfunction.md) we know that

$$
C_f(z)=\frac{f(z)}{\displaystyle\prod_{\rho\in\mathcal{K}_f(r)}(z-\rho)^{m_f(\rho)}}.
$$

Substituting this into Definition [BlaschkeB](../part-01/blaschkeb.md) we have that

$$
B_f(z)=f(z)\prod_{\rho\in\mathcal{K}_f(r)}
\left(\frac{R-z\overline{\rho}/R}{z-\rho}\right)^{m_f(\rho)}.
$$

Taking the complex logarithm of both sides we have that

$$
\mathrm{Log}\,B_f(z)=\mathrm{Log}\,f(z)
+\sum_{\rho\in\mathcal{K}_f(r)}m_f(\rho)\,\mathrm{Log}(R-z\overline{\rho}/R)
-\sum_{\rho\in\mathcal{K}_f(r)}m_f(\rho)\,\mathrm{Log}(z-\rho).
$$

Taking the derivative of both sides we have that

$$
\frac{B_f'}{B_f}(z)=\frac{f'}{f}(z)
+\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-R^2/\overline{\rho}}
-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}.
$$

By Definition [JBlaschke](../part-01/jblaschke.md) and Theorem [LogOfAnalyticFunction](../part-01/logofanalyticfunction.md), since $L_f(z)=J_{B_f}(z)$ we have $L_f'(z)=J'_{B_f}(z)=(B_f'/B_f)(z)$. Thus,

$$
\frac{f'}{f}(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}
=L_f'(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-R^2/\overline{\rho}}.
$$

Now since $z\in\overline{\mathbb{D}_{r'}}\subseteq\overline{\mathbb{D}_{R'}}$ and $\rho\in\mathcal{K}_f(r)\subseteq\mathcal{K}_f(R')$, we know that $R^2/R'-R'\leq|z-R^2/\overline{\rho}|$. Thus by the triangle inequality we have

$$
\left|\frac{f'}{f}(z)-\sum_{\rho\in\mathcal{K}_f(r)}\frac{m_f(\rho)}{z-\rho}\right|
\leq|L_f'(z)|+\left(\frac{1}{R^2/R'-R'}\right)\sum_{\rho\in\mathcal{K}_f(r)}m_f(\rho).
$$

Now by Theorem [ZerosBound](../part-01/zerosbound.md) and [JBlaschkeDerivBound](jblaschkederivbound.md) we get our desired result with a little algebraic manipulation.

## Lean

Formalized as [`FinalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/FinalBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
