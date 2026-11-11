---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ThreeAPFreeComplementProgressionErdosProblem199Wanted.threeAPFreeComplementContainsProgression, MathlibExt.Combinatorics.ThreeAPFreeComplementProgressionErdosProblem199Wanted.threeAPFreeComplementContainsProgression_refuted
statement: formalized
---

# Progression-free sets meeting every infinite progression

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progression-free-sets-meeting-every-infinite-pro/index.html).

## Erdős Problem 199

The statement that for every set $A \subseteq \mathbb{R}$ containing no
three-term arithmetic progression (no $x, y, z \in A$ with $x + z = 2y$ and $x \ne y$) there are
reals $a$ and $d \ne 0$ with $a + nd \notin A$ for every natural number $n$, that is, the
complement $\mathbb{R} \setminus A$ contains the infinite arithmetic progression
$a, a + d, a + 2d, \dots$.

Formalized by `MathlibExt.Combinatorics.ThreeAPFreeComplementProgressionErdosProblem199Wanted.threeAPFreeComplementContainsProgression`, a definition declared in [WantedExt/Combinatorics/ThreeAPFreeComplementProgressionErdosProblem199Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeAPFreeComplementProgressionErdosProblem199Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progression-free-sets-meeting-every-infinite-pro/index.html#three-apfree-complement-contains-progres).

## Erdős Problem 199 is false

There is a set $A \subseteq \mathbb{R}$ containing no three-term
arithmetic progression (no $x, y, z \in A$ with $x + z = 2y$ and $x \ne y$) such that for all reals
$a$ and $d \ne 0$ some term $a + nd$, with $n$ a natural number, lies in $A$: the complement
$\mathbb{R} \setminus A$ contains no infinite arithmetic progression $a, a + d, a + 2d, \dots$
with $d \ne 0$.

Baumgartner constructed such a set with the axiom of choice, from a basis of $\mathbb{R}$ over
$\mathbb{Q}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #199, https://www.erdosproblems.com/199 (status DISPROVED (LEAN)); resolution: J. E. Baumgartner, Partitioning vector spaces, J. Combin. Theory Ser. A 18 (1975), 231-233; formal proof plby/lean-proofs, erdosproblems.com/199: answered no by Baumgartner (construction using a Hamel basis), https://doi.org/10.1016/0097-3165(75)90011-8.

Stated but not proved: `MathlibExt.Combinatorics.ThreeAPFreeComplementProgressionErdosProblem199Wanted.threeAPFreeComplementContainsProgression_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThreeAPFreeComplementProgressionErdosProblem199Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeAPFreeComplementProgressionErdosProblem199Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progression-free-sets-meeting-every-infinite-pro/index.html#three-apfree-complement-contains-progres-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Progression-free sets meeting every infinite progression](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progression-free-sets-meeting-every-infinite-pro/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progression-free-sets-meeting-every-infinite-pro)
