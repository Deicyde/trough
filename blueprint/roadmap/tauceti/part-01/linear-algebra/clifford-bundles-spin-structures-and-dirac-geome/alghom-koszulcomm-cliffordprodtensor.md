---
declaration: theorem
origin: cited
lean: AlgHom.koszulComm_cliffordProdTensor
statement: formalized
proof: formalized
---

# AlgHom.koszulComm_cliffordProdTensor

The Koszul commutor intertwines the graded Clifford tensor actions under exchange of
quadratic-form summands.

```lean
AlgHom.koszulComm_cliffordProdTensor.{u_1, u_2, u_3, u_4, u_5} {R : Type u_1} {M₁ : Type u_2}
  {M₂ : Type u_3} {E : Type u_4} {F : Type u_5} [CommRing R] [Invertible 2] [AddCommGroup M₁]
  [_root_.Module R M₁] [AddCommGroup M₂] [_root_.Module R M₂] {Q₁ : QuadraticForm R M₁}
  {Q₂ : QuadraticForm R M₂} [AddCommGroup E] [_root_.Module R E] [AddCommGroup F]
  [_root_.Module R F] (ρ₁ : CliffordAlgebra Q₁ →ₐ[R] Module.End R E) (γ : Module.End R E)
  (hγ : Function.Involutive ⇑γ)
  (hγρ : ∀ (v : M₁), γ * ρ₁ ((CliffordAlgebra.ι Q₁) v) = -(ρ₁ ((CliffordAlgebra.ι Q₁) v) * γ))
  (ρ₂ : CliffordAlgebra Q₂ →ₐ[R] Module.End R F) (δ : Module.End R F) (hδ : Function.Involutive ⇑δ)
  (hδρ : ∀ (w : M₂), δ * ρ₂ ((CliffordAlgebra.ι Q₂) w) = -(ρ₂ ((CliffordAlgebra.ι Q₂) w) * δ))
  (a : CliffordAlgebra (QuadraticMap.prod Q₁ Q₂)) (z : TensorProduct R E F) :
  (γ.koszulComm δ hγ hδ) (((ρ₁.cliffordProdTensor γ ⋯ hγρ ρ₂) a) z) =
    ((ρ₂.cliffordProdTensor δ ⋯ hδρ ρ₁)
        ((CliffordAlgebra.map (QuadraticMap.IsometryEquiv.prodComm Q₁ Q₂).toIsometry) a))
      ((γ.koszulComm δ hγ hδ) z)
```

## Depends on

- [The graded tensor product of Clifford modules](the-graded-tensor-product-of-clifford-modules.md)

## Lean

Formalized in Tau Ceti as [`AlgHom.koszulComm_cliffordProdTensor`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Comm.html#AlgHom.koszulComm_cliffordProdTensor).

## Sources

- [Tau Ceti documentation: `AlgHom.koszulComm_cliffordProdTensor`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Comm.html#AlgHom.koszulComm_cliffordProdTensor)
- [Source of `AlgHom.koszulComm_cliffordProdTensor` in TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Comm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Prod/Comm.lean#L43)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
