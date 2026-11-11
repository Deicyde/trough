---
declaration: section
origin: cited
lean: Nat.IsPowerFree, Nat.isPowerFree_iff, Nat.IsPowerFree.two_le, Nat.IsPowerFree.pos, Nat.IsPowerFree.not_dvd, Nat.IsPowerFree.of_dvd, Nat.IsPowerFree.mono, Nat.isPowerFree_two
statement: formalized
proof: formalized
---

# Power-free integers

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html).

## Power-free natural numbers

Let $k$ be a natural number. A natural number $n$ is
$k$-free when $k \ge 2$, $n > 0$, and $p^k$ does not divide $n$ for any prime $p$.

Formalized by `Nat.IsPowerFree`, a definition declared in [MathlibExt/NumberTheory/PowerFree.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#is-power-free).

## Characterization of power-free numbers

For natural numbers $n$ and $k$, $n$ is $k$-free
if and only if $k \ge 2$, $n > 0$, and $p^k$ does not divide $n$ for any prime $p$.

Formalized by `Nat.isPowerFree_iff`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#is-power-free-iff).

## The exponent of a power-free number is at least two

If a natural number $n$ is $k$-free,
then $k \ge 2$.

Formalized by `Nat.IsPowerFree.two_le`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#two-le).

## Power-free numbers are positive

If a natural number $n$ is $k$-free, then $n > 0$.

Formalized by `Nat.IsPowerFree.pos`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#pos).

## A k-free number has no prime k-th power divisor

If a natural number $n$ is $k$-free and
$p$ is a prime, then $p^k$ does not divide $n$.

Formalized by `Nat.IsPowerFree.not_dvd`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#not-dvd).

## Divisors of k-free numbers are k-free

If a natural number $n$ is $k$-free and $m$ divides
$n$, then $m$ is $k$-free.

Formalized by `Nat.IsPowerFree.of_dvd`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#of-dvd).

## Power-freeness is monotone in the exponent

If a natural number $n$ is $k$-free and
$k \le l$, then $n$ is $l$-free.

Formalized by `Nat.IsPowerFree.mono`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#mono).

## A natural number is 2-free if and only if it is squarefree

For every natural number $n$,
$n$ is $2$-free if and only if $n$ is squarefree, that is, $d^2$ divides $n$ only for $d = 1$.

Formalized by `Nat.isPowerFree_two`, a theorem declared in [MathlibExt/NumberTheory/PowerFree.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerFree.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html#is-power-free-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power-free integers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/power-free-integers)
