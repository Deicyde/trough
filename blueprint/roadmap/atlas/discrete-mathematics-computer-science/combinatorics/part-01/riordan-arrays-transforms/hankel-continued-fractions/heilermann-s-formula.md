---
declaration: section
origin: cited
lean: MetaMathlibExt.hankelTransform_eq_prod_of_hasJacobiFraction, MetaMathlibExt.hankelTransform_eq_of_hasJacobiFraction_same_beta, MetaMathlibExt.exists_weightedMotzkin_coefficients_of_hasJacobiFraction, MetaMathlibExt.hankelTransform_eq_prod_of_weightedMotzkin
statement: formalized
proof: formalized
---

# Heilermann's formula

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html).

## Heilermann's formula

Let $K$ be a commutative ring, let $a$, $\alpha$, $\beta$ be
sequences in $K$ and let $\mu_0 \in K$. Suppose that $a$ has Jacobi fraction data
$(\alpha, \beta, \mu_0)$: there are power series $F_0, F_1, \dots$ over $K$ with
$\sum_{n \ge 0} a_n x^n = \mu_0 F_0$ and $(1 - \alpha_i x - \beta_{i+1} x^2 F_{i+1}) F_i = 1$ for
every $i \ge 0$. Then for every $n \ge 0$ the Hankel transform of $a$ at $n$, the determinant of
the $(n+1) \times (n+1)$ matrix $(a_{i+j})_{0 \le i, j \le n}$, equals

$$\mu_0^{n+1} \prod_{j=0}^{n-1} \beta_{j+1}^{\,n-j},$$

that is, $\mu_0^{n+1} \beta_1^n \beta_2^{n-1} \cdots \beta_n$, which is $\mu_0$ for $n = 0$.

## Sources

- Paul Barry, "From Fibonacci to Robbins: Series Reversion and Hankel Transforms," Journal of Integer Sequences 24 (2021), Article 21.10.2, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Barry2/barry461.tex>, lines 110-117. Zero-indexed: `hankelTransform a n` is the determinant of the `(n + 1) x (n + 1)` Hankel matrix, and the product over `Finset.range n` with shift `beta (j + 1)` and exponent `n - j` gives `beta_1 ^ n, ..., beta_n ^ 1`; for `n = 0` the empty product yields `mu0`. Scope: only the determinant identity is stated; the Jacobi continued fraction data itself is carried by `HasJacobiFraction`.

Formalized by `MetaMathlibExt.hankelTransform_eq_prod_of_hasJacobiFraction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/HeilermannFormula.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/HeilermannFormula.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html#hankel-transform-eq-prod-of-has-jacobi-f).

## Hankel transforms of Jacobi fractions do not depend on the linear coefficients

Let $K$
be a commutative ring. Say that a sequence $a$ in $K$ has Jacobi fraction data
$(\alpha, \beta, \mu_0)$, where $\alpha$, $\beta$ are sequences in $K$ and $\mu_0 \in K$, when there
are power series $F_0, F_1, \dots$ over $K$ with $\sum_{n \ge 0} a_n x^n = \mu_0 F_0$ and
$(1 - \alpha_i x - \beta_{i+1} x^2 F_{i+1}) F_i = 1$ for every $i \ge 0$. If $a$ has Jacobi fraction
data $(\alpha, \beta, \mu_0)$ and $a'$ has Jacobi fraction data $(\alpha', \beta, \mu_0)$, with the
same $\beta$ and $\mu_0$ but arbitrary $\alpha$ and $\alpha'$, then $a$ and $a'$ have the same
Hankel transform: for every $n \ge 0$ the determinants of the $(n+1) \times (n+1)$ matrices
$(a_{i+j})_{0 \le i, j \le n}$ and $(a'_{i+j})_{0 \le i, j \le n}$ are equal.

## Sources

- Paul Barry, "From Fibonacci to Robbins: Series Reversion and Hankel Transforms," Journal of Integer Sequences 24 (2021), Article 21.10.2, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Barry2/barry461.tex>, lines 110-117. Stated over a commutative ring.

Formalized by `MetaMathlibExt.hankelTransform_eq_of_hasJacobiFraction_same_beta`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/HeilermannFormula.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/HeilermannFormula.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html#hankel-transform-eq-of-has-jacobi-fracti).

## Weighted Motzkin recurrence for the coefficients of a Jacobi fraction

Let $K$ be a ring,
let $a$, $\alpha$, $\beta$ be sequences in $K$ and let $\mu_0 \in K$. Suppose that $a$ has Jacobi
fraction data $(\alpha, \beta, \mu_0)$: there are power series $F_0, F_1, \dots$ over $K$ with
$\sum_{n \ge 0} a_n x^n = \mu_0 F_0$ and $(1 - \alpha_i x - \beta_{i+1} x^2 F_{i+1}) F_i = 1$ for
every $i \ge 0$. Then there is an array $(M_{n,j})_{n, j \ge 0}$ in $K$ with $M_{0,0} = 1$ and,
for all $n, j \ge 0$, $M_{0,j+1} = 0$, $M_{n+1,0} = \alpha_0 M_{n,0} + \beta_1 M_{n,1}$ and
$M_{n+1,j+1} = M_{n,j} + \alpha_{j+1} M_{n,j+1} + \beta_{j+2} M_{n,j+2}$, such that
$a_n = \mu_0 M_{n,0}$ for every $n \ge 0$.

## Sources

- Paul Barry, *From Fibonacci to Robbins: Series Reversion and Hankel Transforms*, Journal of Integer Sequences 24 (2021), Article 21.10.2, lines 110–117, https://cs.uwaterloo.ca/journals/JIS/VOL24/Barry2/barry461.tex. Barry does not explicitly state this auxiliary tableau lemma; it is a coefficientwise bridge for the displayed fraction.

Formalized by `MetaMathlibExt.exists_weightedMotzkin_coefficients_of_hasJacobiFraction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/HeilermannWeightedMotzkin.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/HeilermannWeightedMotzkin.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html#exists-weighted-motzkin-coefficients-of).

## Heilermann's formula for weighted Motzkin arrays

Let $K$ be a commutative ring, let
$\alpha$, $\beta$ be sequences in $K$, let $\mu_0 \in K$, and let $(M_{n,j})_{n, j \ge 0}$ be an
array in $K$ with $M_{0,0} = \mu_0$ and, for all $n, j \ge 0$, $M_{0,j+1} = 0$,
$M_{n+1,0} = \alpha_0 M_{n,0} + \beta_1 M_{n,1}$ and
$M_{n+1,j+1} = M_{n,j} + \alpha_{j+1} M_{n,j+1} + \beta_{j+2} M_{n,j+2}$. Then for every
$n \ge 0$ the Hankel transform of the column $(M_{m,0})_{m \ge 0}$ at $n$, the determinant of the
$(n+1) \times (n+1)$ matrix $(M_{i+j,0})_{0 \le i, j \le n}$, equals

$$\mu_0^{n+1} \prod_{j=0}^{n-1} \beta_{j+1}^{\,n-j},$$

that is, $\mu_0^{n+1} \beta_1^n \beta_2^{n-1} \cdots \beta_n$, which is $\mu_0$ for $n = 0$.

No hypothesis that the $\beta_i$ are nonzero is needed.

## Sources

- Paul Barry, *From Fibonacci to Robbins: Series Reversion and Hankel Transforms*, Journal of Integer Sequences 24 (2021), Article 21.10.2, lines 110–117, https://cs.uwaterloo.ca/journals/JIS/VOL24/Barry2/barry461.tex.

Formalized by `MetaMathlibExt.hankelTransform_eq_prod_of_weightedMotzkin`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/HeilermannWeightedMotzkinDeterminant.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/HeilermannWeightedMotzkinDeterminant.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html#hankel-transform-eq-prod-of-weighted-mot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heilermann's formula](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/heilermann-s-formula)
