---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.HasNormalPComplement, MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.maximalClassSizePElementGivesNormalComplement, MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.maximalClassSizePElementGivesNormalComplement_refuted
statement: formalized
---

# p-parts of conjugacy class sizes

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes/index.html).

## Groups with a normal p-complement

A group $G$ has a normal $p$-complement when it has a
normal subgroup $N$ and a Sylow $p$-subgroup $P$ that are complements of each other: every element
of $G$ can be written uniquely as $nq$ with $n \in N$ and $q \in P$.

Formalized by `MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.HasNormalPComplement`, a definition declared in [WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes/index.html#has-normal-pcomplement).

## Gorshkov's problem on maximal p-parts of class sizes

For a prime $p$, the $p$-part of a
positive integer $m$ is the largest power of $p$ dividing $m$. This is the statement that for
every finite group $G$, every prime $p$ and every $p$-element $g$ of $G$ (that is, $g^{p^k} = 1$
for some natural number $k$), if for every $x \in G$ the $p$-part of the size of the conjugacy
class of $x$ is at most the $p$-part of the size of the conjugacy class of $g$, then $G$ has a
normal $p$-complement.

This is Kourovka Notebook Problem 20.27 (I. B. Gorshkov).

Formalized by `MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.maximalClassSizePElementGivesNormalComplement`, a definition declared in [WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes/index.html#maximal-class-size-pelement-gives-normal).

## A maximal p-part of a class size does not force a normal p-complement

For a prime $p$, the
$p$-part of a positive integer $m$ is the largest power of $p$ dividing $m$. There exist a finite
group $G$, a prime $p$ and a $p$-element $g$ of $G$ (that is, $g^{p^k} = 1$ for some natural
number $k$) such that for every $x \in G$ the $p$-part of the size of the conjugacy class of $x$
is at most the $p$-part of the size of the conjugacy class of $g$, but $G$ has no normal
$p$-complement.

Sambale's counterexample is the group $\mathrm{SL}(2, 3) \rtimes Q_8$ of order $192$ (number $945$
in the GAP library of small groups) with $p = 2$. In it an element of order $4$ has class size
$24$, whose $2$-part $8$ is the largest $2$-part of a class size, while the eight elements of
order $3$ form one conjugacy class, so there is no normal subgroup of order $3$, that is, no
normal $2$-complement.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.27 (I. B. Gorshkov); resolution: B. Sambale, letter of 16 February 2022, recorded in the Kourovka Notebook (21st issue), Problem 20.27: "No, not necessarily, a counterexample is given by SmallGroup(192,945)", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.maximalClassSizePElementGivesNormalComplement_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MaximalClassSizePElementNormalComplementKourovka20Problem27Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes/index.html#maximal-class-size-pelement-gives-normal-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: p-parts of conjugacy class sizes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/conjugacy-classes/p-parts-of-conjugacy-class-sizes)
