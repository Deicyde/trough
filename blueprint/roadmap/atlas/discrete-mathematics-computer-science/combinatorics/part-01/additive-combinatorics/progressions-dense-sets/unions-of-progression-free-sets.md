---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem847Wanted.HasFew3APs, MathlibExt.NumberTheory.ErdosProblem847Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem847Wanted.conjecture_refuted
statement: formalized
---

# Unions of progression-free sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets/index.html).

## Sets with uniformly large 3AP-free subsets

A set $A$ of natural numbers has this property
if there is a real number $\varepsilon > 0$ such that every finite subset $B \subseteq A$ contains
a subset $C \subseteq B$ with $|C| \ge \varepsilon |B|$ that contains no nontrivial three-term
arithmetic progression, that is, no $a, b, c \in C$ with $a + c = 2b$ and $a \ne b$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem847Wanted.HasFew3APs`, a definition declared in [WantedExt/NumberTheory/ErdosProblem847Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem847Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets/index.html#has-few3-aps).

## Erdős Problem 847

Call a set of natural numbers 3AP-free if it contains no $a, b, c$ with
$a + c = 2b$ and $a \ne b$. The proposition asserts that every infinite set $A$ of natural numbers
such that, for some real number $\varepsilon > 0$, every finite subset $B \subseteq A$ has a
3AP-free subset of size at least $\varepsilon |B|$, is a finite union of 3AP-free sets: there are
a natural number $n$ and 3AP-free sets $S_0, \dots, S_{n-1}$ of natural numbers with
$A = S_0 \cup \dots \cup S_{n-1}$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem847Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem847Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem847Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets/index.html#conjecture).

## Erdős Problem 847 is false

Call a set of natural numbers 3AP-free if it contains no
$a, b, c$ with $a + c = 2b$ and $a \ne b$. There is an infinite set $A$ of natural numbers such
that, for some real number $\varepsilon > 0$, every finite subset $B \subseteq A$ has a 3AP-free
subset of size at least $\varepsilon |B|$, but $A$ is not the union of finitely many 3AP-free sets
of natural numbers.

## Sources

- Christian Reiher, Vojtěch Rödl, and Marcelo Sales, Colouring versus density in integers and Hales–Jewett cubes, Journal of the London Mathematical Society (2024), e12987, https://doi.org/10.1112/jlms.12987.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem847Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem847Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem847Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unions of progression-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/unions-of-progression-free-sets)
