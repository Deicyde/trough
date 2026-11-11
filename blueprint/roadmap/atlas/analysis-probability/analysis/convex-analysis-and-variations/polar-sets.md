---
declaration: section
origin: cited
lean: MetaMathlibExt.polarSet, MetaMathlibExt.mem_polarSet, MetaMathlibExt.polarSet_empty, MetaMathlibExt.zero_mem_polarSet, MetaMathlibExt.polarSet_subset_polarSet, MetaMathlibExt.polarSet_closedUnitBall, MetaMathlibExt.polarSet_coordinateCube, MetaMathlibExt.polarSet_image_eq_preimage_adjoint
statement: formalized
proof: formalized
---

# Polar sets

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html).

## Polar of a set

Let $E$ be a real inner product space. The polar of a set $A \subseteq E$
is the set $A^\circ = \{y \in E : \langle x, y \rangle \le 1 \text{ for all } x \in A\}$. This
uses the one-sided bound $\langle x, y \rangle \le 1$, not $|\langle x, y \rangle| \le 1$.

Formalized by `MetaMathlibExt.polarSet`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set).

## Membership in the polar

Let $E$ be a real inner product space, $A \subseteq E$ and
$y \in E$. Then $y$ lies in the polar $A^\circ$ of $A$ if and only if $\langle x, y \rangle \le 1$
for every $x \in A$.

Formalized by `MetaMathlibExt.mem_polarSet`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#mem-polar-set).

## Polar of the empty set

In a real inner product space $E$, the polar of the empty
set is all of $E$, since the defining condition is vacuous.

Formalized by `MetaMathlibExt.polarSet_empty`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set-empty).

## The origin lies in every polar

In a real inner product space $E$, for every set
$A \subseteq E$ the origin $0$ lies in the polar $A^\circ$ of $A$, since
$\langle x, 0 \rangle = 0 \le 1$ for every $x \in A$.

Formalized by `MetaMathlibExt.zero_mem_polarSet`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#zero-mem-polar-set).

## The polar reverses inclusion

Let $A$ and $B$ be subsets of a real inner product space.
If $A \subseteq B$, then the polar $B^\circ$ of $B$ is contained in the polar $A^\circ$ of $A$.

Formalized by `MetaMathlibExt.polarSet_subset_polarSet`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set-subset-polar-set).

## The closed unit ball is self-polar

In a real inner product space $E$, the polar of the
closed unit ball $\{x \in E : \|x\| \le 1\}$ is the closed unit ball itself.

Formalized by `MetaMathlibExt.polarSet_closedUnitBall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSet.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSet.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set-closed-unit-ball).

## The polar of the cube is the $\ell^1$ unit ball

For every $n$, the polar of the
coordinate cube $[-1, 1]^n$ in the Euclidean space $\mathbb{R}^n$, that is the set of all $y$
with $\langle x, y \rangle \le 1$ for every $x$ in the cube, is the closed $\ell^1$ unit ball
$\{y \in \mathbb{R}^n : \sum_i |y_i| \le 1\}$.

Formalized by `MetaMathlibExt.polarSet_coordinateCube`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CoordinateCubePolar.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CoordinateCubePolar.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set-coordinate-cube).

## Polar of a linear image

Let $E$ and $F$ be finite-dimensional real inner product spaces,
let $f : E \to F$ be a linear map with adjoint $f^* : F \to E$, and let $K \subseteq E$. Writing
$S^\circ$ for the polar of a set $S$, we have $(f(K))^\circ = (f^*)^{-1}(K^\circ)$, that is,
$y \in F$ lies in the polar of $f(K)$ if and only if $f^*(y)$ lies in the polar of $K$.

This is the set-theoretic transformation used by the Mahler volume product.

Formalized by `MetaMathlibExt.polarSet_image_eq_preimage_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PolarSetAdjoint.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PolarSetAdjoint.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html#polar-set-image-eq-preimage-adjoint).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polar sets](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/polar-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/polar-sets)
