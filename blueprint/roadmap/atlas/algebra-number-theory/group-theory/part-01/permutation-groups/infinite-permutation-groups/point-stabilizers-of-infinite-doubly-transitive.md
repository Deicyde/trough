---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.doublyTransitiveInfiniteCyclicStabilizer, MathlibExt.GroupTheory.DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.doublyTransitiveInfiniteCyclicStabilizer_refuted, MathlibExt.GroupTheory.DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.doublyTransitiveNonperiodicPeriodicStabilizer, MathlibExt.GroupTheory.DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.doublyTransitiveNonperiodicPeriodicStabilizer_holds
statement: formalized
---

# Point stabilizers of infinite doubly transitive groups

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html).

## Doubly transitive group with infinite cyclic point stabilizer (Kourovka 10.63)

The
statement that there exist a group $G$ and a faithful action of $G$ on a set $X$ such that for
any two ordered pairs of distinct points of $X$ some element of $G$ maps the first to the second,
and the stabilizer of some point $x \in X$ is isomorphic to the infinite cyclic group $\mathbb{Z}$.

Formalized by `MathlibExt.GroupTheory.DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.doublyTransitiveInfiniteCyclicStabilizer`, a definition declared in [WantedExt/GroupTheory/DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html#doubly-transitive-infinite-cyclic-stabil).

## No doubly transitive group has an infinite cyclic point stabilizer (Kourovka 10.63)

If a group
$G$ acts faithfully on a set $X$ such that for any two ordered pairs of distinct points of $X$
some element of $G$ maps the first to the second, then no point stabilizer of the action is
isomorphic to the infinite cyclic group $\mathbb{Z}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.63 (Ya. P. Sysak); resolution: V. D. Mazurov, Siberian Math. J. 31 (1990), 615-617; Gy. Károlyi, S. J. Kovács and P. P. Pálfy, Aequationes Math. 39, no. 1 (1990), 161-166, Kourovka Archive, Problem 10.63 ("No").

Stated but not proved: `MathlibExt.GroupTheory.DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.doublyTransitiveInfiniteCyclicStabilizer_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DoublyTransitiveCyclicStabilizerKourovka10Problem63Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html#doubly-transitive-infinite-cyclic-stabil-2).

## Non-periodic doubly transitive group with periodic point stabilizer (Kourovka 10.64)

The
statement that there exist a group $G$ and a faithful action of $G$ on a set $X$ such that for
any two ordered pairs of distinct points of $X$ some element of $G$ maps the first to the second,
$G$ has an element of infinite order, and every element of the stabilizer of some point $x \in X$
has finite order.

Formalized by `MathlibExt.GroupTheory.DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.doublyTransitiveNonperiodicPeriodicStabilizer`, a definition declared in [WantedExt/GroupTheory/DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html#doubly-transitive-nonperiodic-periodic-s).

## A non-periodic doubly transitive group with a periodic point stabilizer (Kourovka 10.64)

There
exist a group $G$ with an element of infinite order and a faithful action of $G$ on a set $X$
such that for any two ordered pairs of distinct points of $X$ some element of $G$ maps the first
to the second, and every element of the stabilizer of some point $x \in X$ has finite order.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 10.64 (Ya. P. Sysak); resolution: M. Amelio, Non-split sharply 2-transitive groups of bounded exponent, arXiv:2509.11958 (2025), Theorem 1.3 (restated as Theorem 3.5) and Section 3.2: a non-periodic non-split sharply 2-transitive group whose involution centralizers, the point stabilizers of its action on the involutions, have bounded exponent, a positive answer to the paper's Question 2 (Kourovka 10.64); the Kourovka Notebook (21st issue) marks 10.64 solved, https://arxiv.org/abs/2509.11958.

Stated but not proved: `MathlibExt.GroupTheory.DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.doublyTransitiveNonperiodicPeriodicStabilizer_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DoublyTransitivePeriodicStabilizerKourovka10Problem64Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html#doubly-transitive-nonperiodic-periodic-s-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Point stabilizers of infinite doubly transitive groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/point-stabilizers-of-infinite-doubly-transitive)
