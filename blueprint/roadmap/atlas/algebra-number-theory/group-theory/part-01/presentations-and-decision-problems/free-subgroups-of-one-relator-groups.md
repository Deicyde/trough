---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.oneRelatorInfiniteIndexFreeIsFreeOrSurface, MathlibExt.GroupTheory.OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.oneRelatorInfiniteIndexFreeIsFreeOrSurface_holds, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.IsOneRelatorGroup, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.orientableSurfaceRelator, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.nonorientableSurfaceRelator, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.IsSurfaceGroup, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.oneRelatorInfiniteIndexFreeIsSurfaceGroup, MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.oneRelatorInfiniteIndexFreeIsSurfaceGroup_holds
statement: formalized
---

# Free subgroups of one-relator groups

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html).

## Kourovka Problem 20.41: one-relator groups with free infinite-index subgroups

The
proposition that every non-cyclic residually finite group $G$ such that every subgroup of finite
index in $G$ (including $G$ itself) is isomorphic to a one-relator group
$\langle x_0, \dots, x_{n-1} \mid r \rangle$ for some natural number $n$ and some element $r$ of
the free group on $x_0, \dots, x_{n-1}$, and every subgroup of infinite index in $G$ is free, is
free, or is isomorphic to
$\langle a_0, b_0, \dots, a_{g-1}, b_{g-1} \mid [a_0, b_0] \cdots [a_{g-1}, b_{g-1}] \rangle$ for
some $g \ge 0$, where $[a, b] = a b a^{-1} b^{-1}$, or is isomorphic to
$\langle c_0, \dots, c_{k-1} \mid c_0^2 \cdots c_{k-1}^2 \rangle$ for some $k \ge 1$. The problem is
due to L. Ciobanu, B. Fine and G. Rosenberger.

These presentations are the fundamental groups of the closed orientable surface of genus $g$ and
the closed non-orientable surface of genus $k$; compact surfaces with boundary have free
fundamental groups.

Formalized by `MathlibExt.GroupTheory.OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.oneRelatorInfiniteIndexFreeIsFreeOrSurface`, a definition declared in [WantedExt/GroupTheory/OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#one-relator-infinite-index-free-is-free).

## Kourovka Problem 20.41 has a positive answer

Let $G$ be a non-cyclic residually finite group
such that every subgroup of finite index in $G$ (including $G$ itself) is isomorphic to a
one-relator group $\langle x_0, \dots, x_{n-1} \mid r \rangle$ for some natural number $n$ and
some element $r$ of the free group on $x_0, \dots, x_{n-1}$, and every subgroup of infinite index
in $G$ is free. Then $G$ is free, or $G$ is isomorphic to
$\langle a_0, b_0, \dots, a_{g-1}, b_{g-1} \mid [a_0, b_0] \cdots [a_{g-1}, b_{g-1}] \rangle$ for
some $g \ge 0$, where $[a, b] = a b a^{-1} b^{-1}$, or $G$ is isomorphic to
$\langle c_0, \dots, c_{k-1} \mid c_0^2 \cdots c_{k-1}^2 \rangle$ for some $k \ge 1$.

These presentations are the fundamental groups of the closed orientable surface of genus $g$ and
the closed non-orientable surface of genus $k$; compact surfaces with boundary have free
fundamental groups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.41 (L. Ciobanu, B. Fine, G. Rosenberger); resolution: H. Wilton, Surface groups among cubulated hyperbolic and one-relator groups, preprint, arXiv:2406.02121 (2024, v3 2026), Theorem D: an infinite one-relator group that is neither free nor a surface group has a subgroup of infinite index that is not free (a non-cyclic one-relator group has at least two generators and is infinite); Kourovka Notebook (21st issue), Problem 20.41: Yes, it is true, https://arxiv.org/abs/2406.02121.

Stated but not proved: `MathlibExt.GroupTheory.OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.oneRelatorInfiniteIndexFreeIsFreeOrSurface_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorInfiniteIndexFreeKourovka20Problem41Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#one-relator-infinite-index-free-is-free-2).

## One-relator groups with finitely many generators

A group $G$ is a one-relator group if,
for some $n \ge 0$ and some element $r$ of the free group on $x_1, \dots, x_n$, $G$ is isomorphic
to the group $\langle x_1, \dots, x_n \mid r \rangle$ with generators $x_1, \dots, x_n$ and the
single relator $r$.

Formalized by `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.IsOneRelatorGroup`, a definition declared in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#is-one-relator-group).

## Orientable surface relator

For $g \ge 0$, the orientable surface relator of genus $g$ is
the element $[a_1, b_1] [a_2, b_2] \cdots [a_g, b_g]$ of the free group on the $2g$ generators
$a_1, \dots, a_g, b_1, \dots, b_g$, where $[a, b] = a b a^{-1} b^{-1}$; for $g = 0$ it is the
identity.

Formalized by `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.orientableSurfaceRelator`, a definition declared in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#orientable-surface-relator).

## Non-orientable surface relator

For $k \ge 0$, the non-orientable surface relator of genus
$k$ is the element $a_1^2 a_2^2 \cdots a_k^2$ of the free group on the $k$ generators
$a_1, \dots, a_k$; for $k = 0$ it is the identity.

Formalized by `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.nonorientableSurfaceRelator`, a definition declared in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#nonorientable-surface-relator).

## Surface groups

A group $G$ is a surface group if either $G$ is isomorphic to
$\langle a_1, b_1, \dots, a_g, b_g \mid [a_1, b_1] \cdots [a_g, b_g] \rangle$ for some $g \ge 1$,
where $[a, b] = a b a^{-1} b^{-1}$, or $G$ is isomorphic to
$\langle a_1, \dots, a_k \mid a_1^2 \cdots a_k^2 \rangle$ for some $k \ge 2$.

These are the standard one-relator presentations of the fundamental groups of the closed
orientable surfaces of genus $g \ge 1$ and the closed non-orientable surfaces of genus $k \ge 2$,
that is, of the closed aspherical surfaces.

Formalized by `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.IsSurfaceGroup`, a definition declared in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#is-surface-group).

## Kourovka Problem 20.22 (statement)

The statement that every group $G$ with the following
properties is a surface group: $G$ is isomorphic to $\langle x_1, \dots, x_n \mid r \rangle$ for
some $n \ge 0$ and some element $r$ of the free group on $x_1, \dots, x_n$; $G$ is neither free nor
cyclic; and every subgroup of infinite index in $G$ is free. Here $G$ is a surface group if it is
isomorphic to $\langle a_1, b_1, \dots, a_g, b_g \mid [a_1, b_1] \cdots [a_g, b_g] \rangle$ for some
$g \ge 1$, where $[a, b] = a b a^{-1} b^{-1}$, or to
$\langle a_1, \dots, a_k \mid a_1^2 \cdots a_k^2 \rangle$ for some $k \ge 2$.

Formalized by `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.oneRelatorInfiniteIndexFreeIsSurfaceGroup`, a definition declared in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#one-relator-infinite-index-free-is-surfa).

## Wilton's theorem (Kourovka Problem 20.22)

Let $G$ be a group isomorphic to
$\langle x_1, \dots, x_n \mid r \rangle$ for some $n \ge 0$ and some element $r$ of the free group
on $x_1, \dots, x_n$. If $G$ is neither free nor cyclic and every subgroup of infinite index in $G$
is free, then $G$ is a surface group: $G$ is isomorphic to
$\langle a_1, b_1, \dots, a_g, b_g \mid [a_1, b_1] \cdots [a_g, b_g] \rangle$ for some $g \ge 1$,
where $[a, b] = a b a^{-1} b^{-1}$, or to $\langle a_1, \dots, a_k \mid a_1^2 \cdots a_k^2 \rangle$
for some $k \ge 2$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.22 (B. Fine, G. Rosenberger, L. Wienke); resolution: H. Wilton, Surface groups among cubulated hyperbolic and one-relator groups, preprint, arXiv:2406.02121 (2024), Theorem D: an infinite one-relator group that is neither free nor a surface group has a subgroup of infinite index that is not free; the Kourovka Notebook (21st issue) marks 20.22 solved, https://arxiv.org/abs/2406.02121.

Stated but not proved: `MathlibExt.GroupTheory.OneRelatorSurfaceGroupKourovka20Problem22Wanted.oneRelatorInfiniteIndexFreeIsSurfaceGroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OneRelatorSurfaceGroupKourovka20Problem22Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html#one-relator-infinite-index-free-is-surfa-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Free subgroups of one-relator groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/free-subgroups-of-one-relator-groups)
