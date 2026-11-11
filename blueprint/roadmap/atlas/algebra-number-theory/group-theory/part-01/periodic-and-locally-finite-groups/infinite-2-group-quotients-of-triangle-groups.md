---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.wiegoldGroup, MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.uncountablyManyInfiniteTwoGroupQuotients, MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.uncountablyManyInfiniteTwoGroupQuotients_holds
statement: formalized
---

# Infinite 2-group quotients of triangle groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups/index.html).

## The (2, 4, 8) triangle group

The $(2, 4, 8)$ triangle group is the group with
presentation $\langle x, y \mid x^2 = y^4 = (xy)^8 = 1 \rangle$.

Formalized by `MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.wiegoldGroup`, an abbreviation declared in [WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups/index.html#wiegold-group).

## Wiegold's question on 2-group quotients of the (2, 4, 8) triangle group (Kourovka 16.101)

The statement that there are an uncountable index set $I$ and normal subgroups $N_i$ of
$\Gamma = \langle x, y \mid x^2 = y^4 = (xy)^8 = 1 \rangle$, for $i \in I$, such that every
quotient $\Gamma / N_i$ is an infinite $2$-group (a group in which every element has order a
power of $2$), and $\Gamma / N_i \cong \Gamma / N_j$ only when $i = j$.

Formalized by `MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.uncountablyManyInfiniteTwoGroupQuotients`, a definition declared in [WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups/index.html#uncountably-many-infinite-two-group-quot).

## Uncountably many infinite 2-group quotients of the (2, 4, 8) triangle group (Kourovka 16.101)

Let $\Gamma = \langle x, y \mid x^2 = y^4 = (xy)^8 = 1 \rangle$. There are an uncountable index set
$I$ and normal subgroups $N_i$ of $\Gamma$, for $i \in I$, such that every quotient $\Gamma / N_i$
is an infinite $2$-group (a group in which every element has order a power of $2$), and
$\Gamma / N_i \cong \Gamma / N_j$ only when $i = j$. So Wiegold's question has a positive answer.

The Kourovka Archive answers 16.101 "Yes, there do" (Grigorchuk; Minasyan, Olshanskii and
Sonkin).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.101 (J. Wiegold); resolution: R. I. Grigorchuk, Algebra Discrete Math. 2009, no. 4, 78-96; A. Minasyan, A. Yu. Olshanskii and D. Sonkin, Periodic quotients of hyperbolic and large groups, Groups Geom. Dyn. 3 (2009), no. 3, 423-452, arXiv:0804.3328, Kourovka Archive, Problem 16.101 (answer: Yes, there do); Minasyan, Olshanskii and Sonkin, abstract (continua of pairwise non-isomorphic periodic quotients, with a positive answer to Wiegold's question), https://arxiv.org/abs/0804.3328.

Stated but not proved: `MathlibExt.GroupTheory.TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.uncountablyManyInfiniteTwoGroupQuotients_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TriangleGroupTwoGroupQuotientsKourovka16Problem101Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups/index.html#uncountably-many-infinite-two-group-quot-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinite 2-group quotients of triangle groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/infinite-2-group-quotients-of-triangle-groups)
