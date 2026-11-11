---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.classSizes, MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.simpleGroupRecognizedByClassSizes, MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.simpleGroupRecognizedByClassSizes_holds
statement: formalized
---

# Thompson's conjecture on conjugacy class sizes

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes/index.html).

## The set of conjugacy class sizes

For a group $G$, $N(G)$ is the set of natural numbers
$|\{y \in G : y \text{ is conjugate to } x\}|$ for $x \in G$, that is, the set of sizes of the
conjugacy classes of $G$, where an infinite class counts as size $0$.

Formalized by `MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.classSizes`, a definition declared in [WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes/index.html#class-sizes).

## Thompson's conjecture on conjugacy class sizes

Write $N(G)$ for the set of sizes of the
conjugacy classes of a group $G$. Thompson's conjecture is the statement that for all finite
groups $G$ and $H$, if $G$ is simple and non-abelian, $H$ has trivial centre, and
$N(G) = N(H)$, then $G$ and $H$ are isomorphic.

This is Kourovka Notebook Problem 12.38 (J. G. Thompson).

Formalized by `MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.simpleGroupRecognizedByClassSizes`, a definition declared in [WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes/index.html#simple-group-recognized-by-class-sizes).

## Thompson's conjecture on conjugacy class sizes is true

For all finite groups $G$ and $H$, if
$G$ is simple and non-abelian, $H$ has trivial centre, and $G$ and $H$ have the same set of
conjugacy class sizes, then $G$ and $H$ are isomorphic.

Resolved true: the Kourovka Archive answers 12.38 "Yes, it is true" (Thompson's conjecture); the
final step is I. B. Gorshkov (Commun. Algebra 47 (2019)), completing a case-by-case proof over the
finite simple groups by many authors.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.38 (J. G. Thompson; A. S. Kondratiev, W. J. Shi); resolution: I. B. Gorshkov, Commun. Algebra 47 (2019), no. 12, 5192-5206 (final step), Kourovka Archive, Problem 12.38: Yes, it is true; earlier steps by many authors cited there.

Stated but not proved: `MathlibExt.GroupTheory.ThompsonClassSizesKourovka12Problem38Wanted.simpleGroupRecognizedByClassSizes_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThompsonClassSizesKourovka12Problem38Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes/index.html#simple-group-recognized-by-class-sizes-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thompson's conjecture on conjugacy class sizes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/conjugacy-classes/thompson-s-conjecture-on-conjugacy-class-sizes)
