---
declaration: definition
origin: cited
lean: Cf
statement: formalized
---

# CFunction

Let $0 < r < 1$, and $f:\mathbb{C}\to\mathbb{C}$ be analytic on $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. We define a function $C_f:\mathbb{C}\to\mathbb{C}$ as follows. This function is constructed by dividing $f(z)$ by a polynomial whose roots are the zeros of $f$ inside $\overline{\mathbb{D}_r}$.

$$
C_f(z)=\begin{cases}
\displaystyle\frac{f(z)}{\prod_{\rho\in\mathcal{K}_f(r)}(z-\rho)^{m_f(\rho)}}
\qquad\text{for }z\not\in\mathcal{K}_f(r) \\
\displaystyle\frac{h_z(z)}{\prod_{\rho\in\mathcal{K}_f(r)\setminus\{z\}}
(z-\rho)^{m_f(\rho)}}\qquad\text{for }z\in\mathcal{K}_f(r)
\end{cases}
$$

where $h_z(z)$ comes from Lemma [ZeroFactorization](zerofactorization.md).

## Depends on

- [SetOfZeros](setofzeros.md)
- [ZeroFactor](zerofactor.md)

## Lean

Formalized as [`Cf`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Cf).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
