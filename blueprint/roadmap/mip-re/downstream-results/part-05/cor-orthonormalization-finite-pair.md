---
declaration: corollary
origin: cited
lean: MIPRE.Orthonormalization.vnA, MIPRE.Orthonormalization.mem_vnA_iff, MIPRE.Orthonormalization.povm_orthogonalization_finitePair
statement: formalized
proof: formalized
---

# Orthonormalization in a finite pair without abelian projections

Let $M$ be a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) in a unit state $\psi$ whose first player's operators contain no nonzero abelian projection. A POVM $P$ of the first player's algebra with $\sum_a \|\pi(P_a)\psi\|^2 > 1 - \varepsilon$ is within $\sum_a \|\pi(P_a - Q_a)\psi\|^2 < 9\varepsilon$ of a projective measurement $Q$ of that algebra. The second player's version is the same statement for the model with the players exchanged.

## Depends on

- [Finite pairs](../part-04/def-finite-pair.md)
- [Orthonormalization in algebras without abelian projections](../../background-results/part-01/thm-orthonormalization-no-abelian.md)

## Proof depends on

- [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](../part-02/lem-model-strategy-co.md)

## Proof

The first player's operators are the commutant of the second player's, so they form a von Neumann algebra, with no bicommutant theorem; the vector trace of the finite pair is a faithful tracial vector functional on it, and the model's state is a vector state. Theorem [Orthonormalization in algebras without abelian projections](../../background-results/part-01/thm-orthonormalization-no-abelian.md) applies, and its projective measurement, which lies in the first player's operators, pulls back to the first player's algebra by injectivity.

## Lean

Formalized as [`MIPRE.Orthonormalization.vnA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.vnA), [`MIPRE.Orthonormalization.mem_vnA_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.mem_vnA_iff), [`MIPRE.Orthonormalization.povm_orthogonalization_finitePair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_finitePair).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3188](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3188)
