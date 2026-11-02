---
declaration: lemma
origin: cited
lean: norm_fOfZero_le_norm_BlaschkeOfZero
statement: formalized
proof: formalized
---

# norm-fOfZero-le-norm-BlaschkeOfZero

Let $0 < r < R<1$, and $f:\mathbb{C}\to\mathbb{C}$ be analytic on $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. Then

$$
|f(0)|\leq|B_f(0)|.
$$

## Depends on

- [BlaschkeB](blaschkeb.md)
- [SetOfZeros](setofzeros.md)

## Proof depends on

- [BlaschkeOfZero](blaschkeofzero.md)

## Proof

Applying lemma [BlaschkeOfZero](blaschkeofzero.md) we know that

$$
|B_f(0)|=|f(0)|\prod_{\rho\in\mathcal{K}_f(r)}
\left(\frac{R}{|\rho|}\right)^{m_f(\rho)}.
$$

Note that for all $\rho\in\mathcal{K}_f(r)$ that $1\lt R/|\rho|$ since $r\lt R$. Thus, the result follows.

## Lean

Formalized as [`norm_fOfZero_le_norm_BlaschkeOfZero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/norm_fOfZero_le_norm_BlaschkeOfZero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
