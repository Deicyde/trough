---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PGroupConjugacyClassSizesKourovka14Problem77Wanted.everyPowerSetIsClassSizeSet, MathlibExt.GroupTheory.PGroupConjugacyClassSizesKourovka14Problem77Wanted.everyPowerSetIsClassSizeSet_holds, MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.numMaxSizeConjClasses, MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.oddPGroupWithPredMaxSizeConjClasses, MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.oddPGroupWithPredMaxSizeConjClasses_holds
statement: formalized
---

# Conjugacy class sizes of p-groups

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html).

## Prescribed sets of conjugacy class sizes of finite p-groups (Kourovka 14.77)

The
statement that for every prime $p$ and every finite set $X$ of natural numbers that contains $1$
and consists of powers of $p$, there is a finite $p$-group $G$ whose set of conjugacy class sizes
$\{|C| : C \text{ a conjugacy class of } G\}$ equals $X$.

Formalized by `MathlibExt.GroupTheory.PGroupConjugacyClassSizesKourovka14Problem77Wanted.everyPowerSetIsClassSizeSet`, a definition declared in [WantedExt/GroupTheory/PGroupConjugacyClassSizesKourovka14Problem77Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupConjugacyClassSizesKourovka14Problem77Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html#every-power-set-is-class-size-set).

## Cossey–Hawkes theorem on conjugacy class sizes of p-groups

For every prime $p$ and every
finite set $X$ of natural numbers that contains $1$ and consists of powers of $p$, there is a
finite $p$-group whose set of conjugacy class sizes is exactly $X$. This answers Kourovka
Problem 14.77 (Sangroniz) in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.77 (J. Sangroniz); resolution: J. Cossey and T. Hawkes, Proc. Amer. Math. Soc. 128 (2000), no. 1, 49-51, Kourovka Archive, Problem 14.77 (answer: Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.PGroupConjugacyClassSizesKourovka14Problem77Wanted.everyPowerSetIsClassSizeSet_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PGroupConjugacyClassSizesKourovka14Problem77Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupConjugacyClassSizesKourovka14Problem77Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html#every-power-set-is-class-size-set-holds).

## Number of conjugacy classes of maximum size

For a group $G$, the number of conjugacy
classes $c$ of $G$ such that every conjugacy class of $G$ has size at most the size of $c$. It is
meant for finite groups: sizes and counts are taken in $\mathbb{N}$, where an infinite set has
size $0$.

Formalized by `MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.numMaxSizeConjClasses`, a definition declared in [WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html#num-max-size-conj-classes).

## Odd $p$-groups with $p - 1$ conjugacy classes of maximum size (Kourovka 14.92)

The
statement that there exist an odd prime $p$ and a finite $p$-group with exactly $p - 1$ conjugacy
classes of maximum size.

Formalized by `MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.oddPGroupWithPredMaxSizeConjClasses`, a definition declared in [WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html#odd-pgroup-with-pred-max-size-conj-class).

## Some odd $p$-group has exactly $p - 1$ conjugacy classes of maximum size

There exist an odd
prime $p$ and a finite $p$-group with exactly $p - 1$ conjugacy classes of maximum size.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.92 (G. Fernández-Alcober); resolution: A. Jaikin-Zapirain, M. F. Newman and E. A. O'Brien, p-groups having the minimal number of conjugacy classes of maximal size, Israel J. Math. 172 (2009), no. 1, 119-123, abstract (a 3-group with exactly p - 1 = 2 conjugacy classes of the largest size); Kourovka Archive, Problem 14.92 (answer: Yes, there are, for p = 3), http://verso.mat.uam.es/~andrei.jaikin/preprints/articulos.htm.

Stated but not proved: `MathlibExt.GroupTheory.PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.oddPGroupWithPredMaxSizeConjClasses_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PGroupMaxSizeConjugacyClassesKourovka14Problem92Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html#odd-pgroup-with-pred-max-size-conj-class-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy class sizes of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/conjugacy-class-sizes-of-p-groups)
