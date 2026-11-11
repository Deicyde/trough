---
declaration: section
origin: cited
lean: MetaMathlibExt.QPochhammer.qPochhammerInfRaw, MetaMathlibExt.QPochhammer.qPochhammerInf, MetaMathlibExt.QPochhammer.qPochhammerInf_zero_left, MetaMathlibExt.QPochhammer.hasProd_qPochhammerInf, MetaMathlibExt.QPochhammer.qPochhammerInf_one_zero, MetaMathlibExt.QPochhammer.qPochhammerInfRaw_two_one, MetaMathlibExt.qEulerProduct, MetaMathlibExt.qEulerProduct_one
statement: formalized
proof: formalized
---

# q-Pochhammer symbol

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html).

## Raw infinite q-Pochhammer product

For complex numbers $a$ and $q$, the raw infinite
q-Pochhammer product is the unconditional infinite product $\prod_{n=0}^{\infty} (1 - a q^n)$,
defined for every $q$: when this product does not converge unconditionally (in particular for
most $q$ with $|q| \ge 1$), its value is $1$ by convention.

Formalized by `MetaMathlibExt.QPochhammer.qPochhammerInfRaw`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-pochhammer-inf-raw).

## Infinite q-Pochhammer symbol

For complex numbers $a$ and $q$ with $|q| < 1$, the infinite
q-Pochhammer symbol is $(a;q)_\infty = \prod_{n=0}^{\infty} (1 - a q^n)$, the unconditional
infinite product of the factors $1 - a q^n$.

The hypothesis $|q| < 1$ is an argument of the definition, so the symbol cannot be applied to
$q$ outside the open unit disk.

## Sources

- `2607.10576:D01` / `2608.13818:D02` jointly define `(a;q)_∞ := ∏_{j=0}^{∞} (1 - a·q^j)` for complex `a, q` with `‖q‖ < 1`.

Formalized by `MetaMathlibExt.QPochhammer.qPochhammerInf`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-pochhammer-inf).

## The q-Pochhammer symbol with a = 0

For every complex number $q$ with $|q| < 1$,
$(0;q)_\infty = 1$, since every factor $1 - 0 \cdot q^n$ equals $1$.

Formalized by `MetaMathlibExt.QPochhammer.qPochhammerInf_zero_left`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-pochhammer-inf-zero-left).

## Convergence of the infinite q-Pochhammer product

For all complex numbers $a$ and $q$ with
$|q| < 1$, the infinite product $\prod_{n=0}^{\infty} (1 - a q^n)$ converges unconditionally to
the infinite q-Pochhammer symbol $(a;q)_\infty$: the products of the factors $1 - a q^n$ over
finite sets of indices $n$ tend to $(a;q)_\infty$.

No nonvanishing hypothesis is imposed, so the cases where some factor is zero (and the product
is $0$) are included.

## Sources

- `2607.10576:D01`, where the infinite product $(a;q)_\infty$ is used under $|q| < 1$.

Formalized by `MetaMathlibExt.QPochhammer.hasProd_qPochhammerInf`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#has-prod-q-pochhammer-inf).

## The q-Pochhammer symbol vanishes at a = 1 and q = 0

The infinite q-Pochhammer symbol
satisfies $(1;0)_\infty = 0$, because its factor for $n = 0$ is $1 - 1 \cdot 0^0 = 0$ (with the
convention $0^0 = 1$).

Formalized by `MetaMathlibExt.QPochhammer.qPochhammerInf_one_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-pochhammer-inf-one-zero).

## The raw q-Pochhammer product at a = 2 and q = 1 equals 1

The raw infinite q-Pochhammer
product at $a = 2$ and $q = 1$ equals $1$.

Every factor $1 - 2 \cdot 1^n$ equals $-1$, so the finite partial products alternate between $-1$
and $1$ and the product does not converge; the value $1$ is the default that the unconditional
product takes in that case, not a limit of partial products. The q-Pochhammer symbol
$(a;q)_\infty$, which requires $|q| < 1$, excludes such arguments.

Formalized by `MetaMathlibExt.QPochhammer.qPochhammerInfRaw_two_one`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/QPochhammer.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-pochhammer-inf-raw-two-one).

## The Euler products of partition theory

For a natural number $k$, the Euler product
$f_k = (q^k; q^k)_\infty = \prod_{m \ge 1} (1 - q^{km})$ is this infinite product in the ring of
integer power series in $q$, taken in the coefficientwise topology. It is used for $k \ge 1$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 2.

Formalized by `MetaMathlibExt.qEulerProduct`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-euler-product).

## Pentagonal series expansion of the first Euler product

The Euler product
$f_1 = \prod_{m \ge 1} (1 - q^m)$ equals the pentagonal series
$\sum_{j \in \mathbb{Z}} (-1)^j q^{j(3j-1)/2}$ as an integer power series.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 2.

Formalized by `MetaMathlibExt.qEulerProduct_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#q-euler-product-one).

## Constant term of the Euler products

For every natural number $k \ge 1$, the integer power
series $f_k = \prod_{m \ge 1} (1 - q^{km})$ has constant coefficient $1$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Section 1 (notation `E_k`); James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 2.

Formalized by `MetaMathlibExt.constantCoeff_qEulerProduct`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/QEulerProduct.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html#constant-coeff-q-euler-product).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: q-Pochhammer symbol](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/q-pochhammer-symbol)
