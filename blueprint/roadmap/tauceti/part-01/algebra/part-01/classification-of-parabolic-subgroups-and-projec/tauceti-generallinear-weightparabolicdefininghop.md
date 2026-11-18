---
declaration: theorem
origin: cited
lean: TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter
statement: formalized
proof: formalized
---

# TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter

Scheme-theoretic intersection of standard block parabolics corresponds to intersection
of their Levi labels. The sum of defining ideals retains the full scheme structure over
arbitrary base rings.

```lean
TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter.{u} {n : ℕ} (R : Type u)
  [CommRing R] (J K : Finset (Fin n)) :
  TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal R
      (TauCeti.GeneralLinear.standardWeight (J ∩ K)) =
    TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal R
        (TauCeti.GeneralLinear.standardWeight J) ⊔
      TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal R
        (TauCeti.GeneralLinear.standardWeight K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.html#TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.html#TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter)
- [Source of `TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal_standardWeight_inter` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Lattice.lean#L50)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
