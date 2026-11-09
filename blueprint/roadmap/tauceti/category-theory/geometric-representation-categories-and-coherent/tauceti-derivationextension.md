---
declaration: structure
origin: cited
lean: TauCeti.DerivationExtension
statement: formalized
---

# TauCeti.DerivationExtension

The **self-extension** `E_δ(M)` of a module `M` attached to a derivation `δ`: pairs `(u, v)`
of elements of `M`, on which `a` acts by `a • (u, v) = (a • u + δ a • v, a • v)`. The first
coordinate carries the submodule `M` and the second the quotient `M`.

```lean
TauCeti.DerivationExtension.{u, v, u_1} {R : Type u_1} [CommRing R] {A : Type u} [Ring A]
  [Algebra R A] (δ : ↥(TauCeti.derivationLieAlgebra R A)) (M : Type v) : Type v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivationExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.html#TauCeti.DerivationExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivationExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.html#TauCeti.DerivationExtension)
- [Source of `TauCeti.DerivationExtension` in TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.lean#L88)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
