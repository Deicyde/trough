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

- [Third isomorphism theorem](../algebraic-group/third-isomorphism-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff)
- [Source of `TauCeti.GeneralLinear.isReduced_and_le_upperTriangular_definingHopfIdeal_iff` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean#L107)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
