---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible
statement: formalized
proof: formalized
---

# The classification of the finite-dimensional irreducible `gl N`-modules

Over a field of
characteristic zero, a finite-dimensional irreducible `gl N K`-module on which the diagonal Cartan
subalgebra acts triangularizably is equivalent to `L(mu)` for exactly one dominant integral `mu`.

```lean
TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible.{u_1, u_2}
  {K : Type u_1} [Field K] [CharZero K] {N : ℕ} (M : Type u_2) [AddCommGroup M] [_root_.Module K M]
  [LieRingModule (Matrix (Fin N) (Fin N) K) M] [LieModule K (Matrix (Fin N) (Fin N) K) M]
  [FiniteDimensional K M] [LieModule.IsIrreducible K (Matrix (Fin N) (Fin N) K) M]
  [LieModule.IsTriangularizable K (↥(TauCeti.diagonalCartan K (Fin N))) M] :
  ∃! mu,
    TauCeti.IsGlDominantIntegral mu ∧
      Nonempty (M ≃ₗ⁅K,Matrix (Fin N) (Fin N) K⁆ TauCeti.glIrreducible N mu)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/GeneralLinear/Classification.html#TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/GeneralLinear/Classification.html#TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible)
- [Source of `TauCeti.existsUnique_isGlDominantIntegral_and_nonempty_lieModuleEquiv_glIrreducible` in TauCeti/Algebra/Lie/GeneralLinear/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/GeneralLinear/Classification.lean#L46)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
