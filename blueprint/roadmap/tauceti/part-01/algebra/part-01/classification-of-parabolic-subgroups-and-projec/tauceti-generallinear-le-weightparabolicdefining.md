---
declaration: theorem
origin: cited
lean: TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff
statement: formalized
proof: formalized
---

# TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff

The standard block parabolic with union label is the smallest closed subgroup scheme
containing the two given standard block parabolics. Ideal inclusion reverses geometric
inclusion. No reducedness hypothesis is imposed on the competing subgroup `I`.

```lean
TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff.{u} {n : ℕ}
  (k : Type u) [Field k]
  (I : TauCeti.HopfIdeal k ↑(TauCeti.GeneralLinear.coordinateHopfAlgebra k (n + 1)))
  (J K : Finset (Fin n)) :
  I ≤
      TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal k
        (TauCeti.GeneralLinear.standardWeight (J ∪ K)) ↔
    I ≤
        TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal k
          (TauCeti.GeneralLinear.standardWeight J) ∧
      I ≤
        TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal k
          (TauCeti.GeneralLinear.standardWeight K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Third isomorphism theorem](../algebraic-group/third-isomorphism-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.html#TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.html#TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff)
- [Source of `TauCeti.GeneralLinear.le_weightParabolicDefiningHopfIdeal_standardWeight_union_iff` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.lean#L136)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
