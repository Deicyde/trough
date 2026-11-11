---
declaration: section
origin: cited
lean: MetaMathlibExt.eulerianPolynomial_hankelDeterminant, MetaMathlibExt.hankel_transform_shifted_eulerian_polynomials
statement: formalized
proof: formalized
---

# Hankel determinants of Eulerian polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/hankel-determinants-of-eulerian-polynomials/index.html).

## Hankel determinants of the Eulerian polynomials

For $m \ge 0$ let $P_m \in \mathbb{Z}[X]$
be the Eulerian polynomial $P_m = \sum_{k=0}^{m} W_{m,k} X^k$, where
$W_{m,k} = \sum_{i=0}^{m-k} (-1)^i \binom{m+1}{i} (m-k-i)^m$ with $0^0 = 1$ (so $P_0 = 1$ and
$P_2 = 1 + X$). Then for every $n \ge 0$ the Hankel determinant
$\det(P_{i+j})_{0 \le i, j \le n}$ equals $X^{\binom{n+1}{2}} \prod_{k=1}^{n} (k!)^2$.

The proof writes $P_m$ as the moments of a weighted Motzkin table with down-step weights
$\lambda_k = k^2 X$ (Barry's Eulerian moment recurrence) and applies the weighted-Motzkin
determinant theorem.

## Sources

- Paul Barry, "Eulerian Polynomials as Moments, via Exponential Riordan Arrays," Journal of Integer Sequences 14 (2011), Article 11.9.5, corollary lines 240–243, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry7/barry172.tex>. Eulerian closed form `W_{n,k}` at lines 93–94.

Formalized by `MetaMathlibExt.eulerianPolynomial_hankelDeterminant`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/EulerianPolynomialHankel.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/EulerianPolynomialHankel.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/hankel-determinants-of-eulerian-polynomials/index.html#eulerian-polynomial-hankel-determinant).

## Hankel determinants of the shifted Eulerian polynomials

Let $n \in \mathbb{N}$ and
$x \in \mathbb{R}$. For natural numbers $k \le m$ let
$W_{m,k} = \sum_{i=0}^{m-k} (-1)^i \binom{m+1}{i} (m-k-i)^m$, with $0^0 = 1$, and let
$P_m(X) = \sum_{k=0}^{m} W_{m,k} X^k$ be the corresponding Eulerian polynomial. Then the
$(n+1) \times (n+1)$ Hankel determinant of the shifted sequence $P_1(x), P_2(x), \dots$ is

$$\det\bigl(P_{i+j+1}(x)\bigr)_{0 \le i, j \le n} =
(2x)^{\binom{n+1}{2}} \prod_{k=0}^{n-1} \binom{k+3}{2}^{n-k-1}.$$

## Sources

- Paul Barry, "Eulerian Polynomials as Moments, via Exponential Riordan Arrays," Journal of Integer Sequences 14 (2011), Article 11.9.5, corollary lines 312–315, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry7/barry172.tex>. Eulerian closed form `W_{n,k}` at lines 93–94.

Formalized by `MetaMathlibExt.hankel_transform_shifted_eulerian_polynomials`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ShiftedEulerianHankel.lean, line 733](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ShiftedEulerianHankel.lean#L733). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/hankel-determinants-of-eulerian-polynomials/index.html#hankel-transform-shifted-eulerian-polyno).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hankel determinants of Eulerian polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/hankel-determinants-of-eulerian-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/hankel-determinants-of-eulerian-polynomials)
