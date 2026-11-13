---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.wanderingSub, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_pullback, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.pow_mem_range, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_wandering, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_wandering', MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.isCompl_wandering, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.exists_wandering_add_range, MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.exists_wold_decomposition
statement: formalized
proof: formalized
---

# Wold decomposition

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html).

## Wandering subspaces

## Wandering subspace of an isometry

The **wandering subspace** of an isometry `V`: the orthogonal complement of
its range. Vectors here are orthogonal to every vector in the range of `V`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.wanderingSub`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#wandering-sub).

## Powers of an isometry preserve inner products

Pulling inner products back along powers of an isometry.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_pullback`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#inner-pow-pullback).

## Positive powers of an isometry land in its range

A positive power of an isometry lands in the range of the isometry.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.pow_mem_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#pow-mem-range).

## Orthogonality of pushed-forward wandering vectors

A wandering vector, pushed forward `k` times, is orthogonal to any vector
pushed forward strictly more times.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_wandering`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#inner-pow-wandering).

## Orthogonality of pushed-forward wandering vectors, symmetric form

The symmetric form of `inner_pow_wandering`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_pow_wandering'`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#inner-pow-wandering-2).

## Wandering subspace and range are complementary

The ambient space splits as the wandering subspace plus the range.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.isCompl_wandering`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#is-compl-wandering).

## One-step Wold splitting into wandering vector plus range

One step of the Wold decomposition: every vector splits as a wandering
vector plus a vector in the range.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.exists_wandering_add_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#exists-wandering-add-range).

## Finite Wold decomposition

Finite Wold decomposition: every vector is a finite sum of pushed-forward
wandering vectors plus a remainder in the range of `V ^ n`. The wandering
coefficients vanish at and beyond `n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.exists_wold_decomposition`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#exists-wold-decomposition).

## Pythagorean identity for the Wold decomposition

Pythagoras for a Wold decomposition: the squared norm of a vector is the sum
of the squared norms of its wandering coefficients plus the squared norm of
the remainder.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.wold_norm_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#wold-norm-sq).

## Uniqueness of the finite Wold decomposition

Uniqueness of the Wold decomposition at level `n`: the remainder and the
finite wandering sum are uniquely determined.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.wold_decomposition_unique`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#wold-decomposition-unique).

## Residual subspace of an isometry

The **residual subspace** of an isometry: vectors in the range of every
power of `V`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.residualSub`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#residual-sub).

## An isometry maps its residual subspace into itself

The isometry maps its residual subspace into itself.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.mapsTo_residual`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#maps-to-residual).

## Residual subspace is orthogonal to the wandering part

The residual subspace is orthogonal to every pushed-forward wandering
vector: the wandering part and the residual part of Wold's decomposition are
orthogonal.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_residual_wandering`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#inner-residual-wandering).

## Isometry restricted to the residual subspace is bijective

The restriction of an isometry to its residual subspace is bijective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.restrict_residual_bijective`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#restrict-residual-bijective).

## Isometry restricted to the residual subspace preserves inner products

The restriction of an isometry to its residual subspace preserves inner
products.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.inner_restrict_residual`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#inner-restrict-residual).

## Unitary part of an isometry on its residual subspace

The isometry restricts to a unitary operator (a linear isometric
equivalence) on its residual subspace.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.woldResidualEquiv`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#wold-residual-equiv).

## Action of the residual unitary of an isometry

Applying the residual unitary is the same as applying `V` and viewing the
result in the ambient space.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WoldDecomposition.woldResidualEquiv_apply_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WoldDecomposition.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html#wold-residual-equiv-apply-coe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wold decomposition](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators/wold-decomposition)
