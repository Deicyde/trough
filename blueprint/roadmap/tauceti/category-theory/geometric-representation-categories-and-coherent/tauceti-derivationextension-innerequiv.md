---
declaration: def
origin: cited
lean: TauCeti.DerivationExtension.innerEquiv
statement: formalized
---

# TauCeti.DerivationExtension.innerEquiv

Changing a derivation by an inner derivation does not change its self-extension: when
`δ' = δ + ad b`, the map `(u, v) ↦ (u + b • v, v)` is an isomorphism `E_δ(M) ≃ E_δ'(M)`.

```lean
TauCeti.DerivationExtension.innerEquiv.{u, v, u_1} {R : Type u_1} [CommRing R] {A : Type u} [Ring A]
  [Algebra R A] {δ δ' : ↥(TauCeti.derivationLieAlgebra R A)} {b : A} (M : Type v) [AddCommGroup M]
  [_root_.Module A M] (h : δ' = δ + (TauCeti.innerDerivation R) b) :
  TauCeti.DerivationExtension δ M ≃ₗ[A] TauCeti.DerivationExtension δ' M
```

## Depends on

- [TauCeti.DerivationExtension](tauceti-derivationextension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivationExtension.innerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.html#TauCeti.DerivationExtension.innerEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivationExtension.innerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.html#TauCeti.DerivationExtension.innerEquiv)
- [Source of `TauCeti.DerivationExtension.innerEquiv` in TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Basic.lean#L280)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
