---
declaration: theorem
origin: cited
lean: TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero
statement: formalized
proof: formalized
---

# In characteristic zero, every closed overgroup of `B` in `GLₙ₊₁` is a standard weight parabolic

By Cartier's theorem the quotient coordinate algebra is smooth, hence reduced, so
no reducedness hypothesis is needed.

```lean
TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero.{u} {n : ℕ}
  {k : Type u} [Field k] [CharZero k]
  {I : TauCeti.HopfIdeal k ↑(TauCeti.GeneralLinear.coordinateHopfAlgebra k (n + 1))}
  (hIB : I ≤ TauCeti.GeneralLinear.UpperTriangular.definingHopfIdeal k (n + 1)) :
  ∃ w, Antitone w ∧ I = TauCeti.GeneralLinear.weightParabolicDefiningHopfIdeal k w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](../algebraic-group/cartiers-theorem.md)
- [Subgroups of `GLₙ₊₁(k)` containing the upper-triangular group are block triangular](subgroups-of-gln-1-k-containing-the-upper-triang.md)
- [Third isomorphism theorem](../algebraic-group/third-isomorphism-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.html#TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero)
- [Source of `TauCeti.GeneralLinear.exists_antitone_eq_weightParabolicDefiningHopfIdeal_of_charZero` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Classification.lean#L140)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
