---
declaration: lemma
origin: cited
lean: BlaschkeOfZero
statement: formalized
proof: formalized
---

# BlaschkeOfZero

Let $0 < r < R<1$, and $f:\mathbb{C}\to\mathbb{C}$ be analytic on $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. Then

$$
|B_f(0)|=|f(0)|\prod_{\rho\in\mathcal{K}_f(r)}
\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}.
$$

## Depends on

- [BlaschkeB](blaschkeb.md)
- [SetOfZeros](setofzeros.md)

## Proof depends on

- [CFunction](cfunction.md)
- [ZeroFactor](zerofactor.md)

## Proof

Since $f(0)\neq 0$, we know that $0\not\in\mathcal{K}_f(r)$. Thus,

$$
C_f(0)=\frac{f(0)}{\displaystyle\prod_{\rho\in\mathcal{K}_f(r)}(-\rho)^{m_f(\rho)}}.
$$

Thus, substituting this into Definition [BlaschkeB](blaschkeb.md),

$$
|B_f(0)|=|C_f(0)|\prod_{\rho\in\mathcal{K}_f(r)}R^{m_f(\rho)}
=|f(0)|\prod_{\rho\in\mathcal{K}_f(r)}\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}.
$$

## Lean

Formalized as [`BlaschkeOfZero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/BlaschkeOfZero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
