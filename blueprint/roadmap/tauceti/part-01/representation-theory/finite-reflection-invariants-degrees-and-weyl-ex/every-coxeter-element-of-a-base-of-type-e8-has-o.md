---
declaration: theorem
origin: cited
lean: TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8
statement: formalized
proof: formalized
---

# Every Coxeter element of a base of type `E₈` has order 30

```lean
TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8.{u_1, u_2, u_3, u_4} {ι : Type u_1}
  {R : Type u_2} {M : Type u_3} {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M]
  [AddCommGroup N] [_root_.Module R N] {P : RootPairing ι R M N} [P.IsCrystallographic] [IsDomain R]
  [CharZero R] {b : P.Base} {l : List ↥b.support} [Finite ι]
  (h : TauCeti.HasCartanType P b TauCeti.DynkinType.E8) (hnd : l.Nodup)
  (hall : ∀ (i : ↥b.support), i ∈ l) : orderOf (TauCeti.wordProd P b l) = 30
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Every.html#TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8).

## Sources

- [Tau Ceti documentation: `TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Every.html#TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8)
- [Source of `TauCeti.Coxeter.orderOf_wordProd_of_hasCartanType_E8` in TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Every.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Every.lean#L167)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
