---
declaration: def
origin: cited
lean: AlgHom.cliffordProdTensor
statement: formalized
---

# The graded tensor product of Clifford modules

If `ρ₁` makes `E` a module over
`CliffordAlgebra Q₁` with a grading operator `γ`, an involution anticommuting with every vector,
and `ρ₂` makes `F` a module over `CliffordAlgebra Q₂`, then the vector `(v, w)` of the orthogonal
sum `Q₁.prod Q₂` acts on `E ⊗ F` by `c₁(v) ⊗ 1 + γ ⊗ c₂(w)`
(`AlgHom.cliffordProdTensor_ι`).

```lean
AlgHom.cliffordProdTensor.{u_1, u_2, u_3, u_4, u_5} {R : Type u_1} {M₁ : Type u_2} {M₂ : Type u_3}
  {E : Type u_4} {F : Type u_5} [CommRing R] [AddCommGroup M₁] [_root_.Module R M₁]
  [AddCommGroup M₂] [_root_.Module R M₂] {Q₁ : QuadraticForm R M₁} {Q₂ : QuadraticForm R M₂}
  [AddCommGroup E] [_root_.Module R E] [AddCommGroup F] [_root_.Module R F]
  (ρ₁ : CliffordAlgebra Q₁ →ₐ[R] Module.End R E) (γ : Module.End R E) (hγ : γ * γ = 1)
  (hγρ : ∀ (v : M₁), γ * ρ₁ ((CliffordAlgebra.ι Q₁) v) = -(ρ₁ ((CliffordAlgebra.ι Q₁) v) * γ))
  (ρ₂ : CliffordAlgebra Q₂ →ₐ[R] Module.End R F) :
  CliffordAlgebra (QuadraticMap.prod Q₁ Q₂) →ₐ[R] Module.End R (TensorProduct R E F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgHom.cliffordProdTensor`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.html#AlgHom.cliffordProdTensor).

## Sources

- [Tau Ceti documentation: `AlgHom.cliffordProdTensor`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.html#AlgHom.cliffordProdTensor)
- [Source of `AlgHom.cliffordProdTensor` in TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.lean#L106)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
