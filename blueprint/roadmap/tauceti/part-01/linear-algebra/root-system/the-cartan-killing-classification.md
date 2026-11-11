---
declaration: theorem
origin: cited
lean: RootPairing.existsUnique_nonempty_equiv_rationalRootSystem, TauCeti.existsUnique_dynkinType
statement: formalized
proof: formalized
---

# The Cartan-Killing classification

Every irreducible reduced crystallographic finite root
system over `ℚ` is isomorphic to the model root system `TauCeti.DynkinType.rationalRootSystem t` of
a unique valid Dynkin type `t`.

```lean
RootPairing.existsUnique_nonempty_equiv_rationalRootSystem.{u_1, u_2, u_3} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [_root_.Module ℚ M] [AddCommGroup N]
  [_root_.Module ℚ N] (P : RootPairing ι ℚ M N) [Finite ι] [Nonempty ι] [P.IsCrystallographic]
  [P.IsReduced] [P.IsIrreducible] :
  ∃! t, ∃ (ht : t.Valid), Nonempty (P.Equiv (t.rationalRootSystem ht))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.existsUnique_nonempty_equiv_rationalRootSystem`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/FiniteType/RationalClassification.html#RootPairing.existsUnique_nonempty_equiv_rationalRootSystem).

## Other forms

**The Cartan-Killing classification, existence and uniqueness of the Dynkin type.** Formalized in Tau Ceti as [`TauCeti.existsUnique_dynkinType`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/FiniteType/Classification.html#TauCeti.existsUnique_dynkinType).

```lean
TauCeti.existsUnique_dynkinType.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] {P : RootPairing ι R M N} [Finite ι] [CharZero R] [IsDomain R]
  [P.IsRootSystem] [P.IsCrystallographic] [P.IsReduced] [P.IsIrreducible] (b : P.Base) :
  ∃! t, t.Valid ∧ TauCeti.HasCartanType P b t
```

## Sources

- [Tau Ceti documentation: `RootPairing.existsUnique_nonempty_equiv_rationalRootSystem`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/FiniteType/RationalClassification.html#RootPairing.existsUnique_nonempty_equiv_rationalRootSystem)
- [Source of `RootPairing.existsUnique_nonempty_equiv_rationalRootSystem` in TauCeti/LinearAlgebra/RootSystem/FiniteType/RationalClassification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/FiniteType/RationalClassification.lean#L69)
