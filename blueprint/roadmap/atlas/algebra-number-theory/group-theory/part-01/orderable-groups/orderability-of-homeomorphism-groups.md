---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.Square, MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.squareBoundary, MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.boundaryFixingHomeomorphisms, MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.rightOrders, MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.discBoundaryFixingHomeomorphismsRightOrderable, MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.discBoundaryFixingHomeomorphismsRightOrderable_refuted
statement: formalized
---

# Orderability of homeomorphism groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html).

## The closed square

The closed square $I^2 = [0, 1] \times [0, 1]$, the product of two
copies of the unit interval, used as a model of the closed disc.

Formalized by `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.Square`, an abbreviation declared in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#square).

## Boundary of the square

The boundary $\partial I^2$ of the closed square
$I^2 = [0, 1] \times [0, 1]$ is the set of points $(x, y) \in I^2$ with $x = 0$, $x = 1$, $y = 0$
or $y = 1$.

Formalized by `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.squareBoundary`, a definition declared in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#square-boundary).

## Boundary-fixing homeomorphisms of the square

Let $I^2 = [0, 1] \times [0, 1]$ be the
closed square and $\partial I^2$ its boundary. $\mathrm{Homeo}(I^2; \partial I^2)$ is the subgroup
of the group of homeomorphisms of $I^2$ consisting of those homeomorphisms $h$ with $h(x) = x$ for
every $x \in \partial I^2$.

Formalized by `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.boundaryFixingHomeomorphisms`, a definition declared in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#boundary-fixing-homeomorphisms).

## Right orders of a group

The right orders of `G`: linear orders (as relations) invariant under right multiplication.

Formalized by `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.rightOrders`, a definition declared in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#right-orders).

## Right-orderability of the boundary-fixing homeomorphisms of the disc

The proposition
(Kourovka Problem 17.20, G. M. Bergman, for the closed disc) that the group
$\mathrm{Homeo}(I^2; \partial I^2)$ of homeomorphisms of the closed square
$I^2 = [0, 1] \times [0, 1]$, a model of the closed disc, that fix the boundary $\partial I^2$
pointwise is right-orderable: it carries a linear order $\le$ such that $a \le b$ implies
$ac \le bc$ for all $a, b, c$.

Formalized by `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.discBoundaryFixingHomeomorphismsRightOrderable`, a definition declared in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#disc-boundary-fixing-homeomorphisms-righ).

## Boundary-fixing homeomorphisms of the disc are not right-orderable

Let
$I^2 = [0, 1] \times [0, 1]$ be the closed square, a model of the closed disc, and let
$\mathrm{Homeo}(I^2; \partial I^2)$ be the group of homeomorphisms of $I^2$ that fix every point of
the boundary $\partial I^2$. There is no linear order $\le$ on $\mathrm{Homeo}(I^2; \partial I^2)$
such that $a \le b$ implies $ac \le bc$ for all $a, b, c$; that is, this group is not
right-orderable.

This answers Kourovka Problem 17.20 negatively: Hyde constructs a finitely generated subgroup of
$\mathrm{Homeo}(I^2; \partial I^2)$ that admits no left order, and left- and right-orderability
are equivalent via $g \mapsto g^{-1}$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.20 (G. M. Bergman); resolution: J. Hyde, The group of boundary fixing homeomorphisms of the disc is not left-orderable, Ann. of Math. (2) 190 (2019), 657-661, abstract (a finitely generated subgroup of Homeo(I²; ∂I²) admits no left order, hence neither does Homeo(I²; ∂I²)); Kourovka Archive, Problem 17.20 (No, not always), https://annals.math.princeton.edu/2019/190-2/p05.

Stated but not proved: `MathlibExt.GroupTheory.BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.discBoundaryFixingHomeomorphismsRightOrderable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BoundaryFixingHomeomorphismsOrderableKourovka17Problem20Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html#disc-boundary-fixing-homeomorphisms-righ-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orderability of homeomorphism groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/orderability-of-homeomorphism-groups)
