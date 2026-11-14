---
declaration: theorem
origin: cited
lean: classical_carleson
statement: formalized
proof: formalized
---

# classical Carleson

Let $f$ be a $2\pi$-periodic complex-valued continuous function on $\mathbb{R}$. Then for almost all $x \in \mathbb{R}$ we have

$$
\lim_{N\to\infty}S_N f(x) = f(x),\qquad\text{(3)}
$$

where $S_N f$ is the $N$-th partial Fourier sum of $f$ defined in [(1)](README.md) with coefficients [(2)](README.md).

## Depends on

- [classical Carleson with exceptional sets](../proof-of-the-classical-carleson-theorem/part-01/exceptional-set-carleson.md)

## Proof

*Proof of classical Carleson.* By applying [classical Carleson with exceptional sets](../proof-of-the-classical-carleson-theorem/part-01/exceptional-set-carleson.md) with a sequence of $\epsilon_n:= 2^{-n}\delta$ for $n\ge 1$ and taking the union of corresponding exceptional sets $E_n$, we see that outside a set of measure $\delta$, the partial Fourier sums converge pointwise for $N\to \infty$. Applying this with a sequence of $\delta$ shrinking to zero and taking the intersection of the corresponding exceptional sets, which has measure zero, we see that the Fourier series converges outside a set of measure zero.

## Lean

Formalized as [`classical_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/classical_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 112](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L112)
