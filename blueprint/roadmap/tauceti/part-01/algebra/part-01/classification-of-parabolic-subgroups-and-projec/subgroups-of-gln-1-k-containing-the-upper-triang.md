---
declaration: theorem
origin: cited
lean: TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq
statement: formalized
proof: formalized
---

# Subgroups of `GLₙ₊₁(k)` containing the upper-triangular group are block triangular

Over a field with a nontrivial unit group, every subgroup of `GLₙ₊₁(k)` containing the
invertible upper-triangular matrices is the group of `k`-points of the weight parabolic of a
decreasing integer weight.

```lean
TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq.{u} (k : Type u) [Field k]
  [Nontrivial kˣ] {n : ℕ} {H : Subgroup (GL (Fin (n + 1)) k)}
  (hH : TauCeti.upperTriangularGroup (Fin (n + 1)) k ≤ H) :
  ∃ w, Antitone w ∧ TauCeti.GeneralLinear.weightParabolicPoints k w k = H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/TitsSystem.html#TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/TitsSystem.html#TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq)
- [Source of `TauCeti.GeneralLinear.exists_antitone_weightParabolicPoints_eq` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/TitsSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/TitsSystem.lean#L179)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
