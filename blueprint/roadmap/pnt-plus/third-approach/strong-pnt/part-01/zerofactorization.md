---
declaration: lemma
origin: cited
lean: ZeroFactorization
statement: formalized
proof: formalized
---

# ZeroFactorization

Let $f:\mathbb{C}\to\mathbb{C}$ be analytic on $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. For all $\rho\in\mathcal{K}_f(R)$ with $R<1$ there exists $h_\rho(z)$ such that $h_\rho(z)$ is analytic at $\rho$, $h_\rho(\rho)\neq 0$, and $f(z)=(z-\rho)^{m_f(\rho)}\,h_\rho(z)$.

## Depends on

- [SetOfZeros](setofzeros.md)
- [ZeroFactor](zerofactor.md)

## Proof

Since $f$ is analytic on neighborhoods of points in $\overline{\mathbb{D}_1}$ we know that there exists a series expansion about $\rho$:

$$
f(z)=\sum_{0\leq n}a_n\,(z-\rho)^n.
$$

Now if we let $m$ be the smallest number such that $a_m\neq 0$, then

$$
f(z)=\sum_{0\leq n}a_n\,(z-\rho)^n=\sum_{m\leq n}a_n\,(z-\rho)^n
=(z-\rho)^m\sum_{m\leq n}a_n\,(z-\rho)^{n-m}=(z-\rho)^m\,h_\rho(z).
$$

Trivially, $h_\rho(z)$ is analytic at $\rho$ (we have written down the series expansion); now note that

$$
h_\rho(\rho)=\sum_{m\leq n}a_n(\rho-\rho)^{n-m}=\sum_{m\leq n}a_n0^{n-m}=a_m\neq 0.
$$

## Lean

Formalized as [`ZeroFactorization`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZeroFactorization).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
