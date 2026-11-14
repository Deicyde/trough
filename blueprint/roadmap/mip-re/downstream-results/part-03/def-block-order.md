---
declaration: definition
origin: cited
lean: MIPRE.MatrixStar.cone, MIPRE.MatrixStar.instPartialOrderStar, MIPRE.MatrixStar.instStarOrderedRing, MIPRE.MatrixStar.instStarProper, MIPRE.MatrixStar.instStarProperComplex, MIPRE.StarProper.of_cstarRing, MIPRE.StarSubalgebra.instStarProper
statement: formalized
---

# The order of a matrix algebra over an ordered $*$-ring

For a $*$-ring $R$ ordered by its cone of sums of elements $z^* z$, the $n \times n$ matrices over $R$ are ordered in the same way: $X \leq Y$ when $Y - X$ is a sum of matrices $Z^* Z$. When $R$ is *proper*, $z^* z = 0$ only for $z = 0$, the relation is antisymmetric, since an element of the cone has nonnegative diagonal entries and a vanishing diagonal entry kills its row and its column, and the matrices over $R$ are proper again. $C^*$-algebras and their $*$-subalgebras are proper, and so are the complex matrices; on those the order used is the positive semidefinite one. This is what lets the players' algebras of an ancilla extension (Definition [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)) carry POVMs, over and over as registers are adjoined.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.MatrixStar.cone`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MatrixStar.cone), [`MIPRE.MatrixStar.instPartialOrderStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MatrixStar.instPartialOrderStar), [`MIPRE.MatrixStar.instStarOrderedRing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MatrixStar.instStarOrderedRing), [`MIPRE.MatrixStar.instStarProper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MatrixStar.instStarProper), [`MIPRE.MatrixStar.instStarProperComplex`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MatrixStar.instStarProperComplex), [`MIPRE.StarProper.of_cstarRing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StarProper.of_cstarRing), [`MIPRE.StarSubalgebra.instStarProper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StarSubalgebra.instStarProper).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1781](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1781)
