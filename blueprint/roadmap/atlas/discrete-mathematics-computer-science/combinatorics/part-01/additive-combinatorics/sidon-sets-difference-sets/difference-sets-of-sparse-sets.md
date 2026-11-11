---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem899Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem899Wanted.conjecture_holds
statement: formalized
---

# Difference sets of sparse sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-sets-of-sparse-sets/index.html).

## Erdős Problem 899 on difference sets of sparse sets

The proposition asserts the following
for every infinite set $A$ of natural numbers. Write $A(N) = |A \cap \{1, \dots, N\}|$ for its
counting function and $D(N)$ for the number of integers $d \in \{1, \dots, N\}$ of the form
$d = a - b$ with $a, b \in A$. If $A(N)/N \to 0$ as $N \to \infty$, then
$\limsup_{N \to \infty} D(N)/A(N) = +\infty$.

The ratio $D(N)/A(N)$ is computed in the extended reals and taken to be $0$ when $A(N) = 0$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem899Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem899Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem899Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-sets-of-sparse-sets/index.html#conjecture).

## Ruzsa's theorem on difference sets of sparse sets

Let $A$ be an infinite set of natural
numbers whose counting function $A(N) = |A \cap \{1, \dots, N\}|$ satisfies $A(N)/N \to 0$ as
$N \to \infty$, and let $D(N)$ be the number of integers $d \in \{1, \dots, N\}$ of the form
$d = a - b$ with $a, b \in A$. Then $\limsup_{N \to \infty} D(N)/A(N) = +\infty$, where the ratio
is computed in the extended reals and taken to be $0$ when $A(N) = 0$.

This answers Erdős Problem 899 affirmatively.

## Sources

- I. Z. Ruzsa, On the cardinality of A+A and A-A (1978), 933–938, https://mathscinet.ams.org/mathscinet-getitem?mr=519317.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem899Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem899Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem899Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-sets-of-sparse-sets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Difference sets of sparse sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-sets-of-sparse-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-sets-of-sparse-sets)
