---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.linear_twirl_blocks, MIPRE.Introspection.star_averagedBlock, MIPRE.Introspection.averagedBlock_nonneg, MIPRE.Introspection.sum_averagedBlock_eq_one, MIPRE.Introspection.blockPOVM, MIPRE.Introspection.linear_twirl_povm
statement: formalized
proof: formalized
---

# Linear-map blocks of the twirl

Over a finite field of characteristic two, for a linear $L:V\to V$, twirling an operator on $\mathbb C^V\otimes H$ first by all $Z$ Paulis and then by $X(\ker L)$ gives $\sum_{y\in L(V)}P_y^Z\otimes B^y$, where $P_y^Z$ projects onto the fibre $L(v)=y$. If the original operators form a POVM, the blocks form a POVM for each nonempty fibre. Empty fibres impose no condition on $B^y$. The source proves the general-characteristic statement; the Lean theorem supplies the characteristic-two specialization. It sums over all $y\in V$, with zero projectors outside the image, and chooses valid POVMs even at empty fibres.

## Depends on

- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)
- [Ancilla extension of a bipartite model](../../downstream-results/part-02/def-ancilla-extension.md)
- [The order of a matrix algebra over an ordered $*$-ring](../../downstream-results/part-03/def-block-order.md)

## Proof

The full $Z$ twirl removes off-diagonal blocks in the sampled register. The $X(\ker L)$ twirl averages the remaining diagonal blocks on cosets of $\ker L$. Define $B^y$ by this average at a chosen preimage of $y$ (or at zero when there is none). Translation permutes each coset, so the block depends only on $y$. Principal compressions and their averages preserve positivity, while linearity sends a normalized family to a normalized family. This constructs the ancillary POVMs directly.

## Lean

Formalized as [`MIPRE.Introspection.linear_twirl_blocks`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_twirl_blocks), [`MIPRE.Introspection.star_averagedBlock`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.star_averagedBlock), [`MIPRE.Introspection.averagedBlock_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.averagedBlock_nonneg), [`MIPRE.Introspection.sum_averagedBlock_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_averagedBlock_eq_one), [`MIPRE.Introspection.blockPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.blockPOVM), [`MIPRE.Introspection.linear_twirl_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_twirl_povm).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1347](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1347)
