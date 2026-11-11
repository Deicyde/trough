---
declaration: section
origin: cited
lean: higherHarmonic, MetaMathlibExt.harmonic_partial_sum_not_int
statement: formalized
proof: formalized
---

# Harmonic numbers and harmonic sums: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/index.html).

Harmonic, hyperharmonic and multiple harmonic sums, binomial-harmonic identities, non-integrality, harmonic congruences, Euler–Mascheroni bounds.

## Higher-order harmonic numbers

For natural numbers $n$ and $r$, the harmonic number of
order $r$ is the rational number $H_n^{(r)} = \sum_{k=1}^{n} 1/k^r$.

Formalized by `higherHarmonic`, a definition declared in [MathlibExt/NumberTheory/HigherOrderHarmonic.lean, line 18](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HigherOrderHarmonic.lean#L18). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/index.html#higher-harmonic).

## Sums of harmonic numbers starting from the second are not integers

For every natural number
$n \ge 2$, the sum $\sum_{\nu=2}^{n} H_\nu$ is not an integer, where
$H_\nu = \sum_{j=1}^{\nu} 1/j$ is the $\nu$-th harmonic number, viewed as a rational number.

The source proves this via its identity $\sum_{\nu=2}^n H_\nu = (n+1)(H_n - 1)$ (equation (1.2)),
reducing to the non-integrality of $(n+1) H_n$, in the spirit of Theisinger's theorem that $H_n$
itself is never an integer for $n > 1$.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers," Journal of Integer Sequences 29 (2026), Article 26.4.8, Theorem, lines 460–462, https://cs.uwaterloo.ca/journals/JIS/VOL29/Alzer/alzer22.tex

Formalized by `MetaMathlibExt.harmonic_partial_sum_not_int`, a theorem declared in [MathlibExt/NumberTheory/HarmonicPartialSum.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/HarmonicPartialSum.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/index.html#harmonic-partial-sum-not-int).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harmonic numbers and harmonic sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers)
