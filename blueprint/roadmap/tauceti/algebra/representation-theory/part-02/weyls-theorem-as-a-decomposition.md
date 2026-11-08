---
declaration: theorem
origin: cited
lean: TauCeti.exists_isInternal_isIrreducible_of_isKilling, TauCeti.Comodule.isCompletelyReducible_of_isKilling, LieSubmodule.exists_isCompl_of_le_ker
statement: formalized
proof: formalized
---

# Weyl's theorem as a decomposition

A finite-dimensional module over a Lie algebra with
nondegenerate Killing form, over a field of characteristic zero, is the internal direct sum of a
finite family of irreducible Lie submodules.

```lean
TauCeti.exists_isInternal_isIrreducible_of_isKilling.{u, v, w} (K : Type u) (L : Type v) [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  (M : Type w) [AddCommGroup M] [_root_.Module K M] [LieRingModule L M] [LieModule K L M]
  [FiniteDimensional K M] :
  ∃ k N, (DirectSum.IsInternal fun i => ↑(N i)) ∧ ∀ (i : Fin k), LieModule.IsIrreducible K L ↥(N i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](../../algebraic-group/cartiers-theorem.md)
- [The lattice form of Weyl's theorem](the-lattice-form-of-weyls-theorem.md)
- [Weyl's complete reducibility theorem](weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isInternal_isIrreducible_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.exists_isInternal_isIrreducible_of_isKilling).

## Other forms

**Weyl's theorem for algebraic groups.** Formalized in Tau Ceti as [`TauCeti.Comodule.isCompletelyReducible_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/CompleteReducibility.html#TauCeti.Comodule.isCompletelyReducible_of_isKilling).

```lean
TauCeti.Comodule.isCompletelyReducible_of_isKilling.{u, w} {k : Type u} [Field k] [CharZero k]
  [IsAlgClosed k] {H : TauCeti.FiniteTypeCommHopfAlgCat k} [ConnectedSpace (PrimeSpectrum ↑H.obj)]
  [LieAlgebra.IsKilling k (Derivation k (↑H.obj) (TauCeti.Bialgebra.CounitAlgebra k (↑H.obj) k))]
  {M : Type w} [AddCommGroup M] [_root_.Module k M] [TauCeti.Comodule k (↑H.obj) M]
  [FiniteDimensional k M] : TauCeti.Comodule.IsCompletelyReducible k (↑H.obj) M
```

**Weyl's theorem for an action through a quotient.** Formalized in Tau Ceti as [`LieSubmodule.exists_isCompl_of_le_ker`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#LieSubmodule.exists_isCompl_of_le_ker).

```lean
LieSubmodule.exists_isCompl_of_le_ker.{u, v, w} {K : Type u} {L : Type v} [Field K] [CharZero K]
  [LieRing L] [LieAlgebra K L] {M : Type w} [AddCommGroup M] [_root_.Module K M] [LieRingModule L M]
  [LieModule K L M] [FiniteDimensional K M] (N : LieSubmodule K L M) {I : LieIdeal K L}
  [LieAlgebra.IsKilling K (L ⧸ I)] [FiniteDimensional K (L ⧸ I)] (hI : I ≤ LieModule.ker K L M) :
  ∃ N', IsCompl N N'
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isInternal_isIrreducible_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.exists_isInternal_isIrreducible_of_isKilling)
- [Source of `TauCeti.exists_isInternal_isIrreducible_of_isKilling` in TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean#L272)
