---
declaration: section
origin: cited
lean: MetaMathlibExt.oddHarmonic, MetaMathlibExt.oddHarmonic_zero, MetaMathlibExt.oddHarmonic_succ, MetaMathlibExt.oddHarmonic_eq_harmonic
statement: formalized
proof: formalized
---

# Odd harmonic numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html).

## Odd harmonic numbers

For a natural number $n$, the $n$-th odd harmonic number is the
rational number $O_n = \sum_{m=1}^{n} \frac{1}{2m-1}$, the sum of the reciprocals of the first
$n$ odd positive integers; in particular $O_0 = 0$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 1 (definition of `O_n`).

Formalized by `MetaMathlibExt.oddHarmonic`, a definition declared in [MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html#odd-harmonic).

## The zeroth odd harmonic number

The odd harmonic number $O_0$ equals $0$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 1.

Formalized by `MetaMathlibExt.oddHarmonic_zero`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html#odd-harmonic-zero).

## Recurrence for the odd harmonic numbers

For every natural number $n$, the odd harmonic
numbers satisfy $O_{n+1} = O_n + \frac{1}{2n+1}$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 1 (used in the Remark after Corollary 1).

Formalized by `MetaMathlibExt.oddHarmonic_succ`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html#odd-harmonic-succ).

## Odd harmonic numbers in terms of harmonic numbers

For every natural number $n$, the odd
harmonic number $O_n$ and the harmonic numbers $H_k = \sum_{j=1}^{k} \frac{1}{j}$ satisfy
$O_n = H_{2n} - \frac{H_n}{2}$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Section 1 (definition of `O_n`).

Formalized by `MetaMathlibExt.oddHarmonic_eq_harmonic`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Harmonic/OddHarmonic.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html#odd-harmonic-eq-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd harmonic numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/odd-harmonic-numbers)
