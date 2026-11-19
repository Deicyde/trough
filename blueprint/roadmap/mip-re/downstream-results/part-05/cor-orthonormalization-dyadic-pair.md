---
declaration: corollary
origin: cited
lean: MIPRE.Orthonormalization.povm_orthogonalization_dyadicPair, MIPRE.Orthonormalization.povm_orthogonalization_dyadicPairB
statement: formalized
proof: formalized
---

# Orthonormalization in a dyadic pair

Let $M$ be a dyadic pair (Definition [Dyadic pairs](def-dyadic-pair.md)) in a unit state $\psi$. A POVM $P$ of either player's algebra with $\sum_a \|\pi(P_a)\psi\|^2 > 1 - \varepsilon$ is within $\sum_a \|\pi(P_a - Q_a)\psi\|^2 < 9\varepsilon$ of a projective measurement $Q$ of that algebra.

## Depends on

- [Orthonormalization in a finite pair without abelian projections](cor-orthonormalization-finite-pair.md)
- [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)

## Proof

Neither player's operators contain a nonzero abelian projection (Lemma [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)), so Corollary [Orthonormalization in a finite pair without abelian projections](cor-orthonormalization-finite-pair.md) applies to the first player, and to the second in the model with the players exchanged, which is again a dyadic pair. This is the form the orthonormalization sites of the port call, with no hypothesis beyond the class (`reports/c6b-paper-proofs.md`, Section 3.7).

## Lean

Formalized as [`MIPRE.Orthonormalization.povm_orthogonalization_dyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_dyadicPair), [`MIPRE.Orthonormalization.povm_orthogonalization_dyadicPairB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_dyadicPairB).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3211](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3211)
