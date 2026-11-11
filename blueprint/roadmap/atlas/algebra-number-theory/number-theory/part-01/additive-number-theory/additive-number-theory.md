---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem1Wanted.conjecture_refuted, MetaMathlibExt.exists_squarefree_add_two_pow_of_odd_lt_two_pow_fifty
statement: formalized
---

# Additive number theory: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/index.html).

Representing integers as sums from special sets, and the density of integer sets: sumsets of integers, subset sums and complete sequences, primitive sets, natural and logarithmic density, Romanoff's theorem; additive bases and complements and zero-sum constants go to additive combinatorics.

## Disproof of Erdős Problem 1 on distinct subset sums

There is no real number $C > 0$
such that for every natural number $N \ne 0$ and every finite set $A \subseteq \{1, \dots, N\}$
whose distinct subsets have distinct sums, $C \cdot 2^{|A|} < N$.

Resolved false: Disproved: machine-checked disproof recorded in the FormalConjectures source
record. Source: Lean 4 disproof of Erdos Problem 1 (proof by GPT-6 Astra in the FrontierMath
Erdos benchmark; repository by T. Adamczewski), tadamcz/erdos1 at commit
0e395153306f34b3829d118b85bdd704136f2843, theorem Erdos1.erdos_1.disproof,
https://github.com/tadamcz/erdos1/blob/0e395153306f34b3829d118b85bdd704136f2843/Erdos1/Resolutions/Erdos1_219usd_38h.lean#L2419.
Moved from `OpenConjectures/NumberTheory/ErdosProblem1`.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem1Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem1Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem1Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/index.html#conjecture-refuted).

## Odd numbers $1 < n < 2^{50}$ are squarefree plus a power of two

Every odd natural
number $n$ with $1 < n < 2^{50}$ can be written as $n = s + 2^k$, where $s$ is a squarefree
positive integer and $1 \le k \le 13$.

This is a finite verification of a conjecture of Erdős, which is open for all odd $n$.

## Sources

- Christian Hercher, *On the Sum of a Squarefree Integer and a Power of Two*, Journal of Integer Sequences 28 (2025), Article 25.3.1, Theorem 5 (`jis-2025-25.3.1-thm-5`).

Stated but not proved: `MetaMathlibExt.exists_squarefree_add_two_pow_of_odd_lt_two_pow_fifty` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquarefreePlusPowerOfTwoWanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquarefreePlusPowerOfTwoWanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/index.html#exists-squarefree-add-two-pow-of-odd-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive number theory](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory)
