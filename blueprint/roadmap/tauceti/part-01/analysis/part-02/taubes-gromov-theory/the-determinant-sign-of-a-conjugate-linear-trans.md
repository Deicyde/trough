---
declaration: theorem
origin: cited
lean: LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr
statement: formalized
proof: formalized
---

# The determinant sign of a conjugate-linear transport

Transport along a commuting square
of real isomorphisms anticommuting with `I`, that is, of conjugate-linear isomorphisms, maps a
complex positive element of the determinant line of `f` to `(-1) ^ (k + c)` times a complex
positive element of the determinant line of `f'`, where `k` and `c` are the complex dimensions of
the kernel and the cokernel of `f`. The sign is `(-1)` to the complex index `k - c`.

```lean
LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr.{u_1, u_2, u_3, u_4} {M : Type u_1}
  {N : Type u_2} [AddCommGroup M] [_root_.Module ℂ M] [_root_.Module ℝ M] [IsScalarTower ℝ ℂ M]
  [AddCommGroup N] [_root_.Module ℂ N] [_root_.Module ℝ N] [IsScalarTower ℝ ℂ N] {f : M →ₗ[ℂ] N}
  {M' : Type u_3} {N' : Type u_4} [AddCommGroup M'] [_root_.Module ℂ M'] [_root_.Module ℝ M']
  [IsScalarTower ℝ ℂ M'] [AddCommGroup N'] [_root_.Module ℂ N'] [_root_.Module ℝ N']
  [IsScalarTower ℝ ℂ N'] {f' : M' →ₗ[ℂ] N'} (e₁ : M ≃ₗ[ℝ] M') (e₂ : N ≃ₗ[ℝ] N')
  (h : ↑ℝ f' ∘ₗ ↑e₁ = ↑e₂ ∘ₗ ↑ℝ f) [FiniteDimensional ℂ ↥f.ker] [FiniteDimensional ℂ (N ⧸ f.range)]
  {z : (↑ℝ f).detLine} (hz : f.IsComplexPositiveDetLine z)
  (he₁ : ∀ (x : M), e₁ (Complex.I • x) = -(Complex.I • e₁ x))
  (he₂ : ∀ (y : N), e₂ (Complex.I • y) = -(Complex.I • e₂ y)) :
  f'.IsComplexPositiveDetLine
    ((-1) ^ (Module.finrank ℂ ↥f.ker + Module.finrank ℂ (N ⧸ f.range)) •
      ((↑ℝ f).detLineCongr e₁ e₂ h) z)
```

## Depends on

- [LinearMap.IsComplexPositiveDetLine](linearmap-iscomplexpositivedetline.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.html#LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr).

## Sources

- [Tau Ceti documentation: `LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.html#LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr)
- [Source of `LinearMap.IsComplexPositiveDetLine.neg_one_pow_smul_detLineCongr` in TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Determinant/Complex/LinearMap.lean#L258)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
