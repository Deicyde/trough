---
declaration: theorem
origin: cited
lean: TauCeti.smoothCommHopfAlgProperty_of_charZero
statement: formalized
proof: formalized
---

# Cartier's theorem

a finite-type commutative Hopf algebra over a field of characteristic
zero is smooth. Equivalently, every affine group scheme of finite type over such a field is
smooth.

```lean
TauCeti.smoothCommHopfAlgProperty_of_charZero.{u, v} (k : Type u) [Field k] [CharZero k]
  (H : CommHopfAlgCat k) [Algebra.FiniteType k ↑H] : TauCeti.smoothCommHopfAlgProperty k H
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobian criterion for étaleness](../../ring-theory/other-results/part-01/the-jacobian-criterion-for-etaleness.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothCommHopfAlgProperty_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.html#TauCeti.smoothCommHopfAlgProperty_of_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothCommHopfAlgProperty_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.html#TauCeti.smoothCommHopfAlgProperty_of_charZero)
- [Source of `TauCeti.smoothCommHopfAlgProperty_of_charZero` in TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.lean#L148)
