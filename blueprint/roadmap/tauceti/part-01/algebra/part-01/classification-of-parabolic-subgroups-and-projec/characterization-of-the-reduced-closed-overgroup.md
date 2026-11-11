---
declaration: theorem
origin: cited
lean: TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff
statement: formalized
proof: formalized
---

# Characterization of the reduced closed overgroups of `B` in `GLₙ₊₁`

A closed subgroup
scheme of `GLₙ₊₁` is reduced and contains the upper-triangular subgroup exactly when it is the
weight parabolic of a decreasing integer weight.

```lean
TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff.{u} {n : ℕ}
  {k : Type u} [Field k]
  (I : TauCeti.HopfIdeal k ↑(TauCeti.GeneralLinear.coordinateHopfAlgebra k (n + 1))) :
  IsReduced ↑((TauCeti.GeneralLinear.coordinateHopfAlgebra k (n + 1)).quotient I) ∧
      I ≤ TauCeti.GeneralLinear.UpperTriangular.definingHopfIdeal k (n + 1) ↔
    ∃ w, Antitone w ∧ I = TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal k w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Subgroups of `GLₙ₊₁(k)` containing the upper-triangular group are block triangular](subgroups-of-gln-1-k-containing-the-upper-triang.md)
- [Third isomorphism theorem](../algebraic-group/third-isomorphism-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff)
- [Source of `TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean#L107)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
