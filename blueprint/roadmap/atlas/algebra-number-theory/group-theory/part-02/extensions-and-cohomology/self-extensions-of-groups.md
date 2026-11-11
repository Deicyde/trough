---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.IsHallGroup, MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.existsGroupIsoToSelfExtensions, MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.existsGroupIsoToSelfExtensions_holds
statement: formalized
---

# Self-extensions of groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups/index.html).

## Hall group

A group $G$ is a Hall group (in the sense of Göbel and Shelah) when it is
isomorphic to every extension of itself by itself: for every group $H$ and every normal subgroup
$N$ of $H$ with $N \cong G$ and $H/N \cong G$, also $H \cong G$.

Formalized by `MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.IsHallGroup`, a definition declared in [WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups/index.html#is-hall-group).

## Hall's problem on self-extensions (Kourovka Problem 12.44)

There is a nontrivial group $G$
that is a Hall group, that is, isomorphic to every extension of itself by itself: every group $H$
with a normal subgroup $N \cong G$ such that $H/N \cong G$ is isomorphic to $G$.

Formalized by `MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.existsGroupIsoToSelfExtensions`, a definition declared in [WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups/index.html#exists-group-iso-to-self-extensions).

## Existence of Hall groups (Göbel–Shelah; Kourovka Problem 12.44)

There is a nontrivial group
$G$ that is isomorphic to every extension of itself by itself: every group $H$ with a normal
subgroup $N \cong G$ such that $H/N \cong G$ is isomorphic to $G$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.44 (P. Hall; J. C. Lennox); resolution: R. Göbel and S. Shelah, Philip Hall's problem on non-Abelian splitters, Math. Proc. Cambridge Philos. Soc. 134 (2003), no. 1, 23-31, arXiv:math/0009091, Definition 1.1 and Corollary 1.5 (L^ω is a Hall group for every rigid group L), with the existence of rigid groups (Theorem 3.1); Kourovka Archive, Problem 12.44, https://arxiv.org/abs/math/0009091.

Stated but not proved: `MathlibExt.GroupTheory.HallGroupSelfExtensionKourovka12Problem44Wanted.existsGroupIsoToSelfExtensions_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HallGroupSelfExtensionKourovka12Problem44Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups/index.html#exists-group-iso-to-self-extensions-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-extensions of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/extensions-and-cohomology/self-extensions-of-groups)
