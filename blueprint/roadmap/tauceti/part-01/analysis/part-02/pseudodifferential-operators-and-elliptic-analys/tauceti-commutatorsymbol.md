---
declaration: def
origin: cited
lean: TauCeti.commutatorSymbol
statement: formalized
---

# TauCeti.commutatorSymbol

The commutator symbol of a differential operator `D` of order at most `m`: the `R`-multilinear
map sending `(a₁, …, aₘ)` to the `A`-linear iterated commutator `[⋯[D, a₁], …, aₘ]`
(`commutatorSymbol_apply_apply`). It depends `R`-linearly on `D`. For the smooth functions on a
manifold acting on smooth sections of vector bundles, its value at `a₁ = ⋯ = aₘ = f` is `m!`
times the principal symbol of `D` at `df`.

```lean
TauCeti.commutatorSymbol.{u_1, u_2, u_3, u_4} (R : Type u_1) (A : Type u_2) (M : Type u_3)
  (N : Type u_4) [CommSemiring R] [CommSemiring A] [Algebra R A] [AddCommMonoid M]
  [_root_.Module A M] [_root_.Module R M] [IsScalarTower R A M] [AddCommGroup N] [_root_.Module A N]
  [_root_.Module R N] [IsScalarTower R A N] (m : ℕ) :
  ↥(TauCeti.differentialOperators R A M N m) →ₗ[R] (Fin m → A) →ₘₗ[R] M →ₗ[A] N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.commutatorSymbol`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/PrincipalSymbol.html#TauCeti.commutatorSymbol).

## Sources

- [Tau Ceti documentation: `TauCeti.commutatorSymbol`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/PrincipalSymbol.html#TauCeti.commutatorSymbol)
- [Source of `TauCeti.commutatorSymbol` in TauCeti/RingTheory/Derivation/PrincipalSymbol.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Derivation/PrincipalSymbol.lean#L102)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
