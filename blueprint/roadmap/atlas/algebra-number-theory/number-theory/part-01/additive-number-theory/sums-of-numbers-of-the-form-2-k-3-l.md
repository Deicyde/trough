---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem845Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem845Wanted.conjecture_refuted
statement: formalized
---

# Sums of numbers of the form 2^k 3^l

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-numbers-of-the-form-2-k-3-l/index.html).

## Erdős Problem 845

The proposition asserts that for every real number $C > 0$, the set of
all sums $\sum_{(k, l) \in B} 2^k 3^l$, where $B$ is a nonempty finite set of pairs of natural
numbers such that $\max_{(k, l) \in B} 2^k 3^l \le C \min_{(k, l) \in B} 2^k 3^l$, has natural
density $0$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem845Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem845Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem845Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-numbers-of-the-form-2-k-3-l/index.html#conjecture).

## Erdős Problem 845 is false

There is a real number $C > 0$ such that the set of all sums
$\sum_{(k, l) \in B} 2^k 3^l$, where $B$ is a nonempty finite set of pairs of natural numbers such
that $\max_{(k, l) \in B} 2^k 3^l \le C \min_{(k, l) \in B} 2^k 3^l$, does not have natural
density $0$.

Van Doorn and Everts obtain a counterexample with $C = 6$.

## Sources

- Wouter van Doorn and Anneroos R. F. Everts, Smooth sums with small spacings, arXiv:2511.04585v1 (2025), https://arxiv.org/abs/2511.04585v1.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem845Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem845Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem845Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-numbers-of-the-form-2-k-3-l/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of numbers of the form 2^k 3^l](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-numbers-of-the-form-2-k-3-l/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory/sums-of-numbers-of-the-form-2-k-3-l)
