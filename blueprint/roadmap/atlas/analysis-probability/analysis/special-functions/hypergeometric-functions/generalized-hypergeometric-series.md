---
declaration: section
origin: cited
lean: MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricCoefficient, MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricSeries, MetaMathlibExt.GeneralizedHypergeometric.LowerParametersAdmissible, MetaMathlibExt.GeneralizedHypergeometric.SummableHypergeometric, MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricValue, MetaMathlibExt.GeneralizedHypergeometric.lowerParametersAdmissible_ascPochhammer_ne_zero, MetaMathlibExt.GeneralizedHypergeometric.summableHypergeometric_of_neg_coe_nat_mem_upper, MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometric_tsum_eq_finset_sum
statement: formalized
proof: formalized
---

# Generalized hypergeometric series

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html).

## Generalized hypergeometric coefficient

Let $K$ be a field, let $a$ and $b$ be finite
multisets of elements of $K$ (the upper and lower parameters), and let $n$ be a natural number.
The $n$-th generalized hypergeometric coefficient is

$$
(n!)^{-1} \prod_{x \in a} (x)_n \Big(\prod_{y \in b} (y)_n\Big)^{-1},
$$

where $(x)_n = x(x+1)\cdots(x+n-1)$ is the rising factorial, with $(x)_0 = 1$, and the products
run over the multisets with multiplicity. It is the coefficient of $z^n$ in the generalized
hypergeometric series ${}_pF_q$ with $p = |a|$ and $q = |b|$.

Inverses are taken in $K$ with the convention $0^{-1} = 0$, so the coefficient is $0$ whenever
the lower product or $n!$ is zero in $K$; the latter can happen in positive characteristic.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricCoefficient`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#generalized-hypergeometric-coefficient).

## Generalized hypergeometric series

Let $K$ be a field and $A$ a topological ring that is
a $K$-algebra. For finite multisets $a$ and $b$ of elements of $K$, the generalized
hypergeometric series is the formal multilinear series on $A$ whose $n$-th term is the
$n$-linear map $(x_1, \dots, x_n) \mapsto c_n \, x_1 x_2 \cdots x_n$, where $c_n \in K$ is the
$n$-th generalized hypergeometric coefficient with upper parameters $a$ and lower parameters
$b$.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricSeries`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#generalized-hypergeometric-series).

## Admissible lower parameters

A finite multiset $B$ of complex numbers is admissible as
lower parameters if no element of $B$ is $0$ or a negative integer, that is, $-k \notin B$ for
every natural number $k$.

## Sources

- arXiv:2608.10675, KMY-Conj.tex lines 456–470, the exclusion of lower parameters from $\mathbb{Z}_{\le 0}$ for ${}_{m+1}F_m$.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.LowerParametersAdmissible`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#lower-parameters-admissible).

## Summability of the generalized hypergeometric series

For finite multisets $a$ and $b$ of
complex numbers and $z \in \mathbb{C}$, the generalized hypergeometric series with upper
parameters $a$ and lower parameters $b$ is summable at $z$ if the family $(c_n z^n)_{n \ge 0}$ is
summable in $\mathbb{C}$, where $c_n$ is the $n$-th generalized hypergeometric coefficient.

Summability of a family in $\mathbb{C}$ is unconditional summability, which is equivalent to
absolute convergence of $\sum_n c_n z^n$.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.SummableHypergeometric`, an abbreviation declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#summable-hypergeometric).

## Generalized hypergeometric function

For finite multisets $a$ and $b$ of complex numbers
and $z \in \mathbb{C}$, the value ${}_pF_q(a; b; z)$, where $p = |a|$ and $q = |b|$, is the sum
$\sum_{n \ge 0} c_n z^n$, where $c_n$ is the $n$-th generalized hypergeometric coefficient with
upper parameters $a$ and lower parameters $b$.

The sum is the unconditional sum of the family $(c_n z^n)_{n \ge 0}$, which is $0$ by convention
when that family is not summable; no condition on the parameters or on $z$ is imposed.

## Sources

- arXiv:2608.10675, KMY-Conj.tex lines 456–470, the infinite-sum presentation of ${}_{m+1}F_m$.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometricValue`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#generalized-hypergeometric-value).

## Rising factorials at admissible lower parameters are nonzero

Let $B$ be a finite
multiset of complex numbers that is admissible as lower parameters. Then for every $b \in B$ and
every natural number $n$, the rising factorial $(b)_n = b(b+1)\cdots(b+n-1)$, with $(b)_0 = 1$,
is nonzero.

This follows because over $\mathbb{C}$, $(b)_n = 0$ if and only if $b = -k$ for some natural
number $k < n$.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.lowerParametersAdmissible_ascPochhammer_ne_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#lower-parameters-admissible-asc-pochhamm).

## Terminating generalized hypergeometric series are summable

Let $a$ and $b$ be finite
multisets of complex numbers, and let $c_n$ be the $n$-th generalized hypergeometric coefficient
with upper parameters $a$ and lower parameters $b$. If $-N \in a$ for some natural number $N$,
then for every $z \in \mathbb{C}$ the family $(c_n z^n)_{n \ge 0}$ is summable, that is, the
generalized hypergeometric series with these parameters is summable at $z$.

Only finitely many terms are nonzero, since $c_n = 0$ for $n > N$; no condition on the lower
parameters is needed.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.summableHypergeometric_of_neg_coe_nat_mem_upper`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#summable-hypergeometric-of-neg-coe-nat-m).

## Terminating generalized hypergeometric series are finite sums

Let $a$ and $b$ be finite
multisets of complex numbers, and let $c_n$ be the $n$-th generalized hypergeometric coefficient
with upper parameters $a$ and lower parameters $b$. If $-N \in a$ for some natural number $N$,
then for every $z \in \mathbb{C}$

$$
\sum_{n=0}^{\infty} c_n z^n = \sum_{n=0}^{N} c_n z^n.
$$

No condition on the lower parameters is needed: $c_n = 0$ for $n > N$ because the rising
factorial $(-N)_n = (-N)(-N+1)\cdots(-N+n-1)$ vanishes.

Formalized by `MetaMathlibExt.GeneralizedHypergeometric.generalizedHypergeometric_tsum_eq_finset_sum`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GeneralizedHypergeometric.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html#generalized-hypergeometric-tsum-eq-finse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized hypergeometric series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/hypergeometric-functions/generalized-hypergeometric-series)
