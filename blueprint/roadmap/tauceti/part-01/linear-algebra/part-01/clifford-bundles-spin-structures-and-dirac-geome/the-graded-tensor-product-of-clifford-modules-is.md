---
declaration: theorem
origin: cited
lean: AlgHom.cliffordProdTensor_toProd_tmul
statement: formalized
proof: formalized
---

# The graded tensor product of Clifford modules is the Koszul-signed tensor action of `CliffordAlgebra.prodEquiv`

Under Mathlib's identification `CliffordAlgebra.prodEquiv` of
`CliffordAlgebra (Q₁.prod Q₂)` with the graded tensor product `evenOdd Q₁ ᵍ⊗ evenOdd Q₂`, whose
inverse is `CliffordAlgebra.toProd`, the pure tensor `a ᵍ⊗ b` with `b` of parity `j` acts on
`E ⊗ F` by `ρ₁ a γ ^ j ⊗ ρ₂ b`.

```lean
AlgHom.cliffordProdTensor_toProd_tmul.{u_1, u_2, u_3, u_4, u_5} {R : Type u_1} {M₁ : Type u_2}
  {M₂ : Type u_3} {E : Type u_4} {F : Type u_5} [CommRing R] [AddCommGroup M₁] [_root_.Module R M₁]
  [AddCommGroup M₂] [_root_.Module R M₂] {Q₁ : QuadraticForm R M₁} {Q₂ : QuadraticForm R M₂}
  [AddCommGroup E] [_root_.Module R E] [AddCommGroup F] [_root_.Module R F]
  (ρ₁ : CliffordAlgebra Q₁ →ₐ[R] Module.End R E) (γ : Module.End R E) (hγ : γ * γ = 1)
  (hγρ : ∀ (v : M₁), γ * ρ₁ ((CliffordAlgebra.ι Q₁) v) = -(ρ₁ ((CliffordAlgebra.ι Q₁) v) * γ))
  (ρ₂ : CliffordAlgebra Q₂ →ₐ[R] Module.End R F) (a : CliffordAlgebra Q₁) {j : ZMod 2}
  {b : CliffordAlgebra Q₂} (hb : b ∈ CliffordAlgebra.evenOdd Q₂ j) :
  (ρ₁.cliffordProdTensor γ hγ hγρ ρ₂) ((CliffordAlgebra.toProd Q₁ Q₂) (a ᵍ⊗ₜ[R] b)) =
    TensorProduct.map (ρ₁ a * γ ^ j.val) (ρ₂ b)
```

## Depends on

- [The graded tensor product of Clifford modules](the-graded-tensor-product-of-clifford-modules.md)

## Lean

Formalized in Tau Ceti as [`AlgHom.cliffordProdTensor_toProd_tmul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.html#AlgHom.cliffordProdTensor_toProd_tmul).

## Sources

- [Tau Ceti documentation: `AlgHom.cliffordProdTensor_toProd_tmul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.html#AlgHom.cliffordProdTensor_toProd_tmul)
- [Source of `AlgHom.cliffordProdTensor_toProd_tmul` in TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Basic.lean#L215)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
