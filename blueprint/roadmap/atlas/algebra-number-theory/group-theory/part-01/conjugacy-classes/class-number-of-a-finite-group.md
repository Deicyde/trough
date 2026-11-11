---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.maximalOrderClassNumberInsoluble, MathlibExt.GroupTheory.ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.maximalOrderClassNumberInsoluble_refuted, MathlibExt.GroupTheory.ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.classNumberAtMostNilpotentSubgroupOrder, MathlibExt.GroupTheory.ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.classNumberAtMostNilpotentSubgroupOrder_refuted
statement: formalized
---

# Class number of a finite group

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html).

## Heffernan–MacHale problem on groups of maximal order with a given class number

The
proposition that for every integer $k \ge 1$ such that some insoluble finite group has exactly $k$
conjugacy classes, every finite group $G$ with exactly $k$ conjugacy classes whose order is at
least the order of every finite group with exactly $k$ conjugacy classes is insoluble. This is
Kourovka Problem 17.77 (R. Heffernan, D. MacHale).

Formalized by `MathlibExt.GroupTheory.ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.maximalOrderClassNumberInsoluble`, a definition declared in [WantedExt/GroupTheory/ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html#maximal-order-class-number-insoluble).

## A finite group of maximal order with a given class number can be soluble

There are an
integer $k \ge 1$, an insoluble finite group with exactly $k$ conjugacy classes, and a soluble
finite group $G$ with exactly $k$ conjugacy classes whose order is at least the order of every
finite group with exactly $k$ conjugacy classes. So it is not true that whenever some insoluble
finite group has exactly $k \ge 1$ conjugacy classes, every finite group of maximal order with
exactly $k$ conjugacy classes is insoluble.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.77 (R. Heffernan, D. MacHale); resolution: A. Vera-López and J. Sangroniz, Math. Nachr. 280 (2007), 676-694, Kourovka Archive, Problem 17.77 (No, it is not; see Table 1 in Vera-López-Sangroniz).

Stated but not proved: `MathlibExt.GroupTheory.ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.maximalOrderClassNumberInsoluble_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassNumberMaximalOrderInsolubleKourovka17Problem77Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html#maximal-order-class-number-insoluble-ref).

## Liebeck–Pyber problem on the class number and nilpotent subgroups

The proposition that
every finite group $G$ has a nilpotent subgroup $N$ whose order $|N|$ is at least the number
$k(G)$ of conjugacy classes of $G$. This is Kourovka Problem 14.54 (M. W. Liebeck, L. Pyber).

Formalized by `MathlibExt.GroupTheory.ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.classNumberAtMostNilpotentSubgroupOrder`, a definition declared in [WantedExt/GroupTheory/ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html#class-number-at-most-nilpotent-subgroup).

## The class number can exceed the order of every nilpotent subgroup

There is a finite group
$G$ such that the number $k(G)$ of conjugacy classes of $G$ is greater than $|N|$ for every
nilpotent subgroup $N$ of $G$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.54 (M. W. Liebeck, L. Pyber); resolution: S. Tertooy, Class numbers and nilpotent subgroups of PGL(2,q), preprint, arXiv:2606.21404 (2026), abstract: for certain odd prime powers q, k(PGL(2,q)) exceeds the order of every nilpotent subgroup; the Kourovka Notebook (21st issue) marks 14.54 solved (No, not always), https://arxiv.org/abs/2606.21404.

Stated but not proved: `MathlibExt.GroupTheory.ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.classNumberAtMostNilpotentSubgroupOrder_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ClassNumberNilpotentSubgroupKourovka14Problem54Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html#class-number-at-most-nilpotent-subgroup-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Class number of a finite group](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/conjugacy-classes/class-number-of-a-finite-group)
