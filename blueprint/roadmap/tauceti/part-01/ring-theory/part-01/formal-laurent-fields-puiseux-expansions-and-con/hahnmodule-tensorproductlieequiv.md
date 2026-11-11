---
declaration: def
origin: cited
lean: HahnModule.tensorProductLieEquiv
statement: formalized
---

# HahnModule.tensorProductLieEquiv

For a finite free Lie algebra `L` over `R`, the scalar extension `HahnSeries Γ R ⊗[R] L`
and the `L`-valued Hahn series are isomorphic as Lie algebras over `HahnSeries Γ R`. For a
finite-dimensional Lie algebra over a field `K`, this is `K((t)) ⊗[K] L ≃ L((t))`.

```lean
HahnModule.tensorProductLieEquiv.{u_1, u_2, u_3} (Γ : Type u_1) (R : Type u_2) (L : Type u_3)
  [AddCommMonoid Γ] [PartialOrder Γ] [IsOrderedCancelAddMonoid Γ] [CommRing R] [LieRing L]
  [LieAlgebra R L] [Module.Free R L] [Module.Finite R L] :
  TensorProduct R (HahnSeries Γ R) L ≃ₗ⁅HahnSeries Γ R⁆ HahnModule Γ R L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HahnModule.tensorProductLieEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/BaseChange/HahnModule.html#HahnModule.tensorProductLieEquiv).

## Sources

- [Tau Ceti documentation: `HahnModule.tensorProductLieEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/BaseChange/HahnModule.html#HahnModule.tensorProductLieEquiv)
- [Source of `HahnModule.tensorProductLieEquiv` in TauCeti/Algebra/Lie/BaseChange/HahnModule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/BaseChange/HahnModule.lean#L83)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
