---
declaration: section
origin: cited
lean: MetaMathlibExt.christol_theorem, MetaMathlibExt.christol_theorem_isKAutomaticSequence
statement: formalized
proof: formalized
---

# Christol's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/christol-s-theorem/index.html).

## Christol's theorem

Let $p$ be a prime, $r \ge 1$ a natural number, and $K$ a finite field
of characteristic $p$ with $q = p^r$ elements. A formal power series
$f = \sum_n f_n X^n \in K[[X]]$ is algebraic over the polynomial ring $K[X]$ (it is a root of a
nonzero polynomial with coefficients in $K[X]$) if and only if its coefficient sequence
$n \mapsto f_n$ is $p$-automatic, that is, its $p$-kernel is finite.

Algebraicity over $K[X]$ is the denominator-cleared form of algebraicity over the rational
function field $K(X)$; it is not integrality over $K[X]$. Automaticity is taken in base $p$, not
in base $q$.

## Sources

- Adamczewski--Bell, arXiv:1205.4091v1, lines 260--265: for `q` a positive integral power of the characteristic prime `p`, a series over `F_q` is algebraic over `F_q(t)` iff its coefficient sequence is `p`-automatic.

Formalized by `MetaMathlibExt.christol_theorem`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/Christol.lean, line 1036](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/Christol.lean#L1036). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/christol-s-theorem/index.html#christol-theorem).

## Christol's theorem, automaton form

Let $p$ be a prime, $r \ge 1$ a natural number, and
$K$ a finite field of characteristic $p$ with $q = p^r$ elements. A formal power series
$f = \sum_n f_n X^n \in K[[X]]$ is algebraic over the polynomial ring $K[X]$ (it is a root of a
nonzero polynomial with coefficients in $K[X]$) if and only if its coefficient sequence
$n \mapsto f_n$ is $p$-automatic in the sense of finite automata with output.

Formalized by `MetaMathlibExt.christol_theorem_isKAutomaticSequence`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/Christol.lean, line 1066](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/Christol.lean#L1066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/christol-s-theorem/index.html#christol-theorem-is-kautomatic-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Christol's theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/christol-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/christol-s-theorem)
