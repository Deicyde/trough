---
declaration: def
origin: cited
lean: DividedPowerAlgebra.symmetricTensorEquiv
statement: formalized
---

# DividedPowerAlgebra.symmetricTensorEquiv

For a free module `M`, Roby's linear equivalence between the homogeneous divided powers
`Γ^d_R(M)` and the symmetric tensors of degree `d`, sending `dp R d m` to `m ⊗ ⋯ ⊗ m`.

```lean
DividedPowerAlgebra.symmetricTensorEquiv.{u, u_1} (R : Type u) [CommSemiring R] (M : Type u_1)
  [AddCommMonoid M] [_root_.Module R M] [Module.Free R M] (d : ℕ) :
  ↥(DividedPowerAlgebra.homogeneousSubmodule d) ≃ₗ[R] ↥(TensorPower.symmetricTensors R M d)
```

## Depends on

- [Roby representability](roby-representability.md)

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.symmetricTensorEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/SymmetricTensor.html#DividedPowerAlgebra.symmetricTensorEquiv).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.symmetricTensorEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/SymmetricTensor.html#DividedPowerAlgebra.symmetricTensorEquiv)
- [Source of `DividedPowerAlgebra.symmetricTensorEquiv` in TauCeti/RingTheory/DividedPowerAlgebra/SymmetricTensor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DividedPowerAlgebra/SymmetricTensor.lean#L279)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
