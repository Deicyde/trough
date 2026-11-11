---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.orderedEmbedsInThreeClasses, MathlibExt.GroupTheory.OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.orderedEmbedsInThreeClasses_refuted
statement: formalized
---

# Ordered groups with three conjugacy classes

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/ordered-groups-with-three-conjugacy-classes/index.html).

## Kourovka Problem 11.68 (ordered groups with three conjugacy classes)

The statement that
for every fully ordered group $G$ there are a fully ordered group $H$ with exactly three conjugacy
classes and a strictly increasing homomorphism $G \to H$ (an order-preserving embedding). Here a
fully ordered group is a group with a linear order $\le$ such that $a \le b$ implies $ca \le cb$
and $ac \le bc$ for all $a$, $b$, $c$.

Formalized by `MathlibExt.GroupTheory.OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.orderedEmbedsInThreeClasses`, a definition declared in [WantedExt/GroupTheory/OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/ordered-groups-with-three-conjugacy-classes/index.html#ordered-embeds-in-three-classes).

## Not every fully ordered group embeds in one with three conjugacy classes

There is a fully
ordered group $G$ such that for every fully ordered group $H$ with exactly three conjugacy
classes, no homomorphism $G \to H$ is strictly increasing. Here a fully ordered group is a group
with a linear order $\le$ such that $a \le b$ implies $ca \le cb$ and $ac \le bc$ for all $a$, $b$,
$c$. That is, the answer to Kourovka Problem 11.68 is negative.

The Kourovka Archive records the answer "No, not every", given by Bludov.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.68 (B. Neumann); resolution: V. V. Bludov, Algebra and Logic 44, no. 6 (2005), 370-380, Kourovka Archive, Problem 11.68: "No, not every", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.orderedEmbedsInThreeClasses_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OrderedGroupThreeClassesEmbeddingKourovka11Problem68Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/ordered-groups-with-three-conjugacy-classes/index.html#ordered-embeds-in-three-classes-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordered groups with three conjugacy classes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/ordered-groups-with-three-conjugacy-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orderable-groups/ordered-groups-with-three-conjugacy-classes)
