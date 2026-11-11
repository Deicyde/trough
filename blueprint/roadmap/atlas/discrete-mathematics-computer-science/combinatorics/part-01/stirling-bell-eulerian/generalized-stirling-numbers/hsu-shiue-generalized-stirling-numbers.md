---
declaration: section
origin: cited
lean: MetaMathlibExt.generalized_stirling_matrix_factorization, MetaMathlibExt.generalizedFallingFactorial, MetaMathlibExt.IsHsuShiueFamily
statement: formalized
proof: formalized
---

# Hsu–Shiue generalized Stirling numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers/index.html).

## Factorization of the generalized Stirling matrix

Let $S$ assign to real numbers $a, b, c$
and natural numbers $n, k$ a real number $S(a, b, c; n, k)$, such that for all real $a, b, c, x$
and every natural number $n$

$$\prod_{i=0}^{n-1} (x - i a) =
\sum_{k=0}^{n} S(a, b, c; n, k) \prod_{i=0}^{k-1} (x - c - i b),$$

and $S(a, b, c; n, k) = 0$ whenever $n < k$. Then for all real $\alpha, \beta, \gamma$ and all
natural numbers $n, k$

$$S(\alpha, \beta, \gamma; n, k) = \sum_{j=0}^{n} \sum_{l=0}^{j}
S(\alpha, 0, 0; n, j)\, S(0, 0, \gamma; j, l)\, S(0, \beta, 0; l, k).$$

In matrix form, the generalized Stirling matrix with parameters $(\alpha, \beta, \gamma)$ is the
product of the matrices for $(\alpha, 0, 0)$ (first kind), $(0, 0, \gamma)$ (translation) and
$(0, \beta, 0)$ (second kind).

## Sources

- Jiaqiang Pan, “Matrix Decomposition of the Unified Generalized Stirling Numbers and Inversion of the Generalized Factorial Matrices,” Journal of Integer Sequences 15 (2012), Article 12.6.6, Theorem `t:Decomposition`, lines 250-256, <https://cs.uwaterloo.ca/journals/JIS/VOL15/Pan/pan19.tex>.

Formalized by `MetaMathlibExt.generalized_stirling_matrix_factorization`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingMatrixFactorization.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedStirlingMatrixFactorization.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers/index.html#generalized-stirling-matrix-factorizatio).

## Generalized falling factorial

Let $K$ be $\mathbb{R}$ or $\mathbb{C}$. For
$z, \alpha \in K$ the generalized falling factorial with increment $\alpha$ is the sequence
defined by $(z \mid \alpha)_0 = 1$ and $(z \mid \alpha)_{n+1} = (z \mid \alpha)_n \, (z - n\alpha)$
for $n \ge 0$, so that $(z \mid \alpha)_n = z (z - \alpha) \cdots (z - (n-1)\alpha)$ for $n \ge 1$.

Formalized by `MetaMathlibExt.generalizedFallingFactorial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/HsuShiueGeneralizedStirlingNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/HsuShiueGeneralizedStirlingNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers/index.html#generalized-falling-factorial).

## Characterization of the Hsu–Shiue generalized Stirling numbers

Let $K$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $\alpha, \beta, r \in K$. For $z \in K$ write $(z \mid \alpha)_0 = 1$ and
$(z \mid \alpha)_n = z (z - \alpha) \cdots (z - (n-1)\alpha)$ for $n \ge 1$ (the generalized
falling factorial). An array $(S(n,k))_{n, k \ge 0}$ in $K$ is a Hsu–Shiue family with
parameters $(\alpha, \beta, r)$ when $\alpha$, $\beta$ and $r$ are not all zero,
$S(n, 0) = (r \mid \alpha)_n$ for every $n \ge 0$, $S(n, k) = 0$ whenever $n < k$, and

$$S(n+1, k+1) = S(n, k) + \bigl((k+1)\beta - n\alpha + r\bigr) S(n, k+1)$$

for all $n, k \ge 0$.

The last condition is the source recurrence
$S(n+1, k) = S(n, k-1) + (k\beta - n\alpha + r) S(n, k)$ at the indices $k \ge 1$; the initial
column and the triangular support fix the remaining values.

Formalized by `MetaMathlibExt.IsHsuShiueFamily`, a definition declared in [MathlibExt/Combinatorics/Enumerative/HsuShiueGeneralizedStirlingNumber.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/HsuShiueGeneralizedStirlingNumber.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers/index.html#is-hsu-shiue-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hsu–Shiue generalized Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/hsu-shiue-generalized-stirling-numbers)
