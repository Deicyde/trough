---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.OeisConjecturesWanted.avoidZZ1Z, MathlibExt.NumberTheory.OeisConjecturesWanted.avoidZZ1Z_spec, MathlibExt.NumberTheory.OeisConjecturesWanted.size_choose_two_pow, MathlibExt.NumberTheory.OeisConjecturesWanted.floor_sum_cbrt
statement: formalized
---

# Consecutive patterns in words

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html).

## Words avoiding the consecutive pattern $z, z+1, z$

For natural numbers $k$ and $n$,
$f_k(n)$ is the number of words $w_0 w_1 \cdots w_{n-1}$ of length $n$ over the alphabet
$\{0, 1, \dots, k-1\}$ with no position $i$ such that $i + 2 < n$, $w_{i+1} = w_i + 1$ and
$w_{i+2} = w_i$.

Formalized by `MathlibExt.NumberTheory.OeisConjecturesWanted.avoidZZ1Z`, a definition declared in [WantedExt/NumberTheory/OeisConjecturesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisConjecturesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html#avoid-zz1-z).

## Recurrence for words avoiding the pattern $z, z+1, z$

Let $k \ge 1$ and, for each
natural number $n$, let $f_k(n)$ be the number of words of length $n$ over the alphabet
$\{0, 1, \dots, k-1\}$ that avoid the consecutive pattern $z, z+1, z$. Then $f_k(0) = 1$,
$f_k(1) = k$, $f_k(2) = k^2$, and $f_k(n) = k f_k(n-1) - f_k(n-2) + f_k(n-3)$ for every $n \ge 3$.

At $k = 0$ the recurrence would read $0 = 1$ at $n = 3$.

## Sources

- Sela Fried, "Proofs of Several Conjectures From the OEIS", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.OeisConjecturesWanted.avoidZZ1Z_spec` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisConjecturesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisConjecturesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html#avoid-zz1-z-spec).

## Bit length of $\binom{2^n}{2^{n-1}}$

For every integer $n \ge 1$, the binary expansion of
the binomial coefficient $\binom{2^n}{2^{n-1}}$ has exactly $2^n - \lfloor n/2 \rfloor$ digits.

## Sources

- Sela Fried, "Proofs of Several Conjectures From the OEIS", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.OeisConjecturesWanted.size_choose_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisConjecturesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisConjecturesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html#size-choose-two-pow).

## Floor of a sum of cube roots

For every integer $m \ge 1$, the sum
$S_m = \sum_{i=1}^{10^{3m}} i^{1/3}$ of the real cube roots of $1, 2, \dots, 10^{3m}$ satisfies

$$\lfloor S_m \rfloor = \frac{3 \cdot 10^{4m}}{4} + 5 \cdot 10^{m-1} - 1.$$

## Sources

- Sela Fried, "Proofs of Several Conjectures From the OEIS", Theorem 7.

Stated but not proved: `MathlibExt.NumberTheory.OeisConjecturesWanted.floor_sum_cbrt` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisConjecturesWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisConjecturesWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html#floor-sum-cbrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Consecutive patterns in words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/consecutive-patterns-in-words)
