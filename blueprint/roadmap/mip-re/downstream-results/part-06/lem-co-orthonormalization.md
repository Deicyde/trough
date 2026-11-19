---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.MakingMeasurementsProjective.leftPlacedProjectivizationRepair_of_sourceAlmostProjective_two_mul, MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMainLemma, MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalization, MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_of_consistency_from_projectivizationRepair_heterogeneous, MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_right_of_consistency_from_projectivizationRepair_heterogeneous
statement: formalized
proof: formalized
---

# Orthonormalization, in a symmetric model

Let $\eta > 0$, and let the bipartite reading of $S$ (Definition [Symmetric models](../part-05/def-sym-model.md)) be a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) whose first player's operators contain no nonzero abelian projection.

1. If $A$ and $B$ are measurements in $\mathcal{P}$ with $\mathrm{cons}(A, B) \leq \eta$, there is a projective submeasurement $P$ in $\mathcal{P}$ with $\sum_a \| L(A_a - P_a) \Psi \|^2 \leq 84\, \eta^{1/4}$.
2. If $A$ is a submeasurement in $\mathcal{P}$ with $\max(0, \mathrm{ev}(L(A_{\mathrm{total}})) - \sum_a \mathrm{ev}(L(A_a)\, R(A_a))) \leq \eta$, there is a projective submeasurement $P$ in $\mathcal{P}$ with $\sum_a \| L(A_a - P_a) \Psi \|^2 \leq 100\, \eta^{1/4}$.
3. Let $M$ be a dyadic pair (Definition [Dyadic pairs](../part-05/def-dyadic-pair.md)) in a unit state $\psi$, and $A$ and $B$ measurements of its first and second players' algebras with $1 - \sum_a \langle \psi, \pi(\pi_A(A_a)\, \pi_B(B_a)) \psi \rangle \leq \eta$. Then there is a projective submeasurement $P$ of the first player's algebra with $\sum_a \| \pi(\pi_A(A_a - P_a)) \psi \|^2 \leq 100\, \eta^{1/4}$, and likewise one of the second player's algebra, with $B$ in place of $A$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Finite pairs](../part-04/def-finite-pair.md)
- [Dyadic pairs](../part-05/def-dyadic-pair.md)

## Proof depends on

- [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md)
- [Orthonormalization in a dyadic pair](../part-05/cor-orthonormalization-dyadic-pair.md)
- [Orthonormalization in the doubled model](thm-doubled-orthonormalization.md)

## Proof

The vendored proof, in `MIPRE/Background/LIDT/MIPStarRE/LDT/MakingMeasurementsProjective/`, passes from consistency to an almost projective measurement and rounds that to a projective one in finite dimension, through a Naimark dilation, a spectral truncation and a reduction of rank. The first half is ported (`planning/c6b-plan.md`, milestone M8): by the Cauchy–Schwarz inequality for the vector state, $\mathrm{cons}(A, B) \leq \eta$ gives $1 - \sum_a \| L(A_a) \Psi \|^2 \leq 2 \eta$, which is less than $3 \min(\eta, 1)$. The second half is replaced: Corollary [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md), applied to $A$, gives a projective measurement $P$ with $\sum_a \| L(A_a - P_a) \Psi \|^2 < 27 \min(\eta, 1) \leq 84\, \eta^{1/4}$, which is item 1. Item 2 is Theorem [Orthonormalization in the doubled model](thm-doubled-orthonormalization.md), in the form stated there for any symmetric model whose bipartite reading is such a finite pair. Item 3 is the same estimate in the two-space model, where Corollary [Orthonormalization in a dyadic pair](../part-05/cor-orthonormalization-dyadic-pair.md) applies to either player with no further hypothesis, and $27 \min(\eta, 1) \leq 100\, \eta^{1/4}$. The case $\eta = 0$ is excluded because the hypothesis of Corollary [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md) is strict.

## Lean

Formalized as [`MIPRE.LIDT.Co.MakingMeasurementsProjective.leftPlacedProjectivizationRepair_of_sourceAlmostProjective_two_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MakingMeasurementsProjective.leftPlacedProjectivizationRepair_of_sourceAlmostProjective_two_mul), [`MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMainLemma`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMainLemma), [`MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalization`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalization), [`MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_of_consistency_from_projectivizationRepair_heterogeneous`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_of_consistency_from_projectivizationRepair_heterogeneous), [`MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_right_of_consistency_from_projectivizationRepair_heterogeneous`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MakingMeasurementsProjective.orthonormalizationMeasurement_right_of_consistency_from_projectivizationRepair_heterogeneous).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3921](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3921)
