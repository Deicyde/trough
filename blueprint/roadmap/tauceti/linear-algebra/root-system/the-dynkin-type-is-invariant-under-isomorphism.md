---
declaration: theorem
origin: cited
lean: RootPairing.Equiv.classifiedDynkinType_map
statement: formalized
proof: formalized
---

# The Dynkin type is invariant under isomorphism

pushing a base forward along an equivalence
of root systems does not change its Dynkin type.

```lean
RootPairing.Equiv.classifiedDynkinType_map.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {ι : Type u_1}
  {R : Type u_2} {M : Type u_3} {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M]
  [AddCommGroup N] [_root_.Module R N] {P : RootPairing ι R M N} [Finite ι] [CharZero R]
  [IsDomain R] [P.IsRootSystem] [P.IsCrystallographic] [P.IsReduced] [P.IsIrreducible] [Nonempty ι]
  {ι₂ : Type u_5} {M₂ : Type u_6} {N₂ : Type u_7} [AddCommGroup M₂] [_root_.Module R M₂]
  [AddCommGroup N₂] [_root_.Module R N₂] {P₂ : RootPairing ι₂ R M₂ N₂} [Finite ι₂] [P₂.IsRootSystem]
  [P₂.IsCrystallographic] [P₂.IsReduced] [P₂.IsIrreducible] [Nonempty ι₂] (e : P.Equiv P₂)
  (b : P.Base) : TauCeti.classifiedDynkinType (b.map e) = TauCeti.classifiedDynkinType b
```

## Depends on

- [The Cartan-Killing classification](the-cartan-killing-classification.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.Equiv.classifiedDynkinType_map`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/FiniteType/Classification.html#RootPairing.Equiv.classifiedDynkinType_map).

## Sources

- [Tau Ceti documentation: `RootPairing.Equiv.classifiedDynkinType_map`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/FiniteType/Classification.html#RootPairing.Equiv.classifiedDynkinType_map)
- [Source of `RootPairing.Equiv.classifiedDynkinType_map` in TauCeti/LinearAlgebra/RootSystem/FiniteType/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/FiniteType/Classification.lean#L205)
