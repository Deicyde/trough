---
declaration: def
origin: cited
lean: LinearMap.BilinForm.sesqComplexification
statement: formalized
---

# LinearMap.BilinForm.sesqComplexification

**The sesquilinear complexification** of a real bilinear form `B`: the form
`h (x, y) = B_ℂ (conj x, y)` on `ℂ ⊗[ℝ] V`, conjugate-linear in the first argument and linear in
the second, with `h (z ⊗ v, w ⊗ u) = conj z * w * B (v, u)`
(`LinearMap.BilinForm.sesqComplexification_tmul_tmul`). For a Euclidean metric it is the
induced positive Hermitian form on the complexification.

```lean
LinearMap.BilinForm.sesqComplexification.{u_1} {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V]
  (B : LinearMap.BilinForm ℝ V) : TensorProduct ℝ ℂ V →ₗ⋆[ℂ] TensorProduct ℝ ℂ V →ₗ[ℂ] ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.sesqComplexification`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Complexification.html#LinearMap.BilinForm.sesqComplexification).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.sesqComplexification`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Complexification.html#LinearMap.BilinForm.sesqComplexification)
- [Source of `LinearMap.BilinForm.sesqComplexification` in TauCeti/LinearAlgebra/BilinearForm/Complexification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/BilinearForm/Complexification.lean#L87)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
