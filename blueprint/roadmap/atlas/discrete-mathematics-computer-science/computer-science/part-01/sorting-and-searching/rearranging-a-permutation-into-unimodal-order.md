---
declaration: section
origin: cited
lean: MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.Unimodal, MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.differences, MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.minRearrange_correct
statement: formalized
---

# Rearranging a permutation into unimodal order

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order/index.html).

## Unimodal arrays

An array $a$ of natural numbers is unimodal if it is the concatenation of a
strictly increasing array $b$ followed by a strictly decreasing array $b'$, where either part may
be empty.

Formalized by `MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.Unimodal`, a definition declared in [WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order/index.html#unimodal).

## Number of differing positions

For two vectors $a, b \in \mathbb{N}^n$, this is the number of
indices $i < n$ with $a_i \neq b_i$, that is, the Hamming distance between $a$ and $b$.

Formalized by `MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.differences`, a definition declared in [WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order/index.html#differences).

## Correctness of the unimodal rearrangement algorithm

Let $a$ be an array of length $n$ that
is a permutation of $1, \dots, n$, and let $m(a)$ be the value that the program
$\mathrm{minRearrange}$ computes on $a$. Then some unimodal permutation $x$ of
$1, \dots, n$ differs from $a$ in exactly $m(a)$ positions, and every unimodal permutation of
$1, \dots, n$ differs from $a$ in at least $m(a)$ positions. So $m(a)$ is the minimum number of
positions in which $a$ differs from a unimodal permutation of $1, \dots, n$.

## Sources

- NWERC 2025 Problem G, see https://2025.nwerc.eu/problem-set.pdf. Problem `permute_to_unimodal` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.PermuteToUnimodalWanted.ProgramVerification.minRearrange_correct` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/PermuteToUnimodalWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order/index.html#min-rearrange-correct).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rearranging a permutation into unimodal order](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/rearranging-a-permutation-into-unimodal-order)
