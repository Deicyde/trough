---
declaration: theorem
origin: cited
lean: ZerosBound
statement: formalized
proof: formalized
---

# ZerosBound

Let $0< r < R<1$. If $f:\mathbb{C}\to\mathbb{C}$ is a function analytic on neighborhoods of points in $\overline{\mathbb{D}_1}$ with $f(0)=1$ and $|f(z)|\leq B$ for $|z|\leq R$, then

$$
\sum_{\rho\in\mathcal{K}_f(r)}m_f(\rho)\leq\frac{\log B}{\log(R/r)}.
$$

## Depends on

- [SetOfZeros](../part-01/setofzeros.md)

## Proof depends on

- [BlaschkeB](../part-01/blaschkeb.md)
- [DiskBound](../part-01/diskbound.md)
- [BlaschkeOfZero](../part-01/blaschkeofzero.md)

## Proof

Since $f(0)=1$, by Lemma [BlaschkeOfZero](../part-01/blaschkeofzero.md) we know that

$$
|B_f(0)|
=|f(0)|\prod_{\rho\in\mathcal{K}_f(r)}\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}
=\prod_{\rho\in\mathcal{K}_f(r)}\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}.
$$

Thus, substituting this into Definition [BlaschkeB](../part-01/blaschkeb.md),

$$
(R/r)^{\sum_{\rho\in\mathcal{K}_f(r)}m_f(\rho)}
=\prod_{\rho\in\mathcal{K}_f(r)}\left(\frac{R}{r}\right)^{m_f(\rho)}
\leq\prod_{\rho\in\mathcal{K}_f(r)}\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}
=|B_f(0)|\leq B
$$

whereby Lemma [DiskBound](../part-01/diskbound.md) we know that $|B_f(z)|\leq B$ for all $|z|\leq R$. Taking the logarithm of both sides and rearranging gives the desired result.

## Lean

Formalized as [`ZerosBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZerosBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
