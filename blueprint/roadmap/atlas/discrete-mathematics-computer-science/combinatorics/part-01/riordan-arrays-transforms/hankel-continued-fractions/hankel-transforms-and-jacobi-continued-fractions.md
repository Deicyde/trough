---
declaration: section
origin: cited
lean: MetaMathlibExt.hankelTransform, MetaMathlibExt.HasJacobiFraction
statement: formalized
proof: formalized
---

# Hankel transforms and Jacobi continued fractions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-transforms-and-jacobi-continued-fractions/index.html).

## Hankel transform

Let $R$ be a commutative ring and let $(a_k)_{k \ge 0}$ be a sequence
in $R$. The Hankel transform of $a$ is the sequence $(h_n)_{n \ge 0}$ in $R$ whose term $h_n$ is
the determinant of the $(n + 1) \times (n + 1)$ Hankel matrix $(a_{i+j})_{0 \le i, j \le n}$.

Formalized by `MetaMathlibExt.hankelTransform`, a definition declared in [MathlibExt/NumberTheory/HankelTransform.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HankelTransform.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-transforms-and-jacobi-continued-fractions/index.html#hankel-transform).

## Jacobi continued fraction expansion

Let $K$ be a ring, not necessarily commutative, let
$(a_n)_{n \ge 0}$, $(\alpha_n)_{n \ge 0}$ and $(\beta_n)_{n \ge 0}$ be sequences in $K$, let
$\mu_0 \in K$, and let $(F_i)_{i \ge 0}$ be a sequence of formal power series over $K$ in the
variable $x$. These data form a Jacobi continued fraction expansion of $a$ when
$\sum_{n \ge 0} a_n x^n = \mu_0 F_0$ and, for every $i \ge 0$,
$(1 - \alpha_i x - \beta_{i+1} x^2 F_{i+1}) F_i = 1$. Informally, the power series $F_i$ are the
tails of the continued fraction

$$
\sum_{n} a_n x^n = \cfrac{\mu_0}{1 - \alpha_0 x - \cfrac{\beta_1 x^2}{1 - \alpha_1 x - \cdots}}.
$$

This records only the continued fraction identities, not Heilermann's formula for the Hankel
determinants of $a$.

## Sources

- Paul Barry, "From Fibonacci to Robbins: Series Reversion and Hankel Transforms," JIS 24 (2021), Article 21.10.2, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Barry2/barry461.tex>, lines 110-117.

Formalized by `MetaMathlibExt.HasJacobiFraction`, a definition declared in [MathlibExt/NumberTheory/HankelTransform.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HankelTransform.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-transforms-and-jacobi-continued-fractions/index.html#has-jacobi-fraction).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hankel transforms and Jacobi continued fractions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-transforms-and-jacobi-continued-fractions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/hankel-transforms-and-jacobi-continued-fractions)
