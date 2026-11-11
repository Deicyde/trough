---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.derivedSeriesIntersectionPerfect, MathlibExt.GroupTheory.DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.derivedSeriesIntersectionPerfect_refuted
statement: formalized
---

# Intersection of the derived series

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/intersection-of-the-derived-series/index.html).

## Perfectness of the intersection of the derived series (Kourovka 17.82)

The conjecture of
R. Mikhailov that for every finitely presented group $G$, the intersection
$D = \bigcap_{n} G^{(n)}$ of the terms $G^{(n)}$ of the derived series of $G$ satisfies
$[D, D] = D$, that is, $D$ has trivial abelianization.

Formalized by `MathlibExt.GroupTheory.DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.derivedSeriesIntersectionPerfect`, a definition declared in [WantedExt/GroupTheory/DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/intersection-of-the-derived-series/index.html#derived-series-intersection-perfect).

## The intersection of the derived series need not be perfect

There exists a finitely presented
group $G$ such that the intersection $D = \bigcap_{n} G^{(n)}$ of the terms $G^{(n)}$ of the
derived series of $G$ satisfies $[D, D] \ne D$. That is, the conjecture of Kourovka Problem 17.82
is false; the Kourovka Archive credits this answer to V. A. Roman'kov (2011).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.82 (R. Mikhailov); resolution: V. A. Roman'kov, Siberian Math. J. 52 (2011), 348-351, Kourovka Archive, Problem 17.82 (No, not always).

Stated but not proved: `MathlibExt.GroupTheory.DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.derivedSeriesIntersectionPerfect_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/DerivedSeriesIntersectionPerfectKourovka17Problem82Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/intersection-of-the-derived-series/index.html#derived-series-intersection-perfect-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersection of the derived series](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/intersection-of-the-derived-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/intersection-of-the-derived-series)
