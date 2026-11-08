---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity
statement: formalized
proof: formalized
---

# Wirtinger inequality on manifolds

For a compatible pair `(form, J)`, twice the symplectic
area density of any real-linear map into a tangent fiber is at most its standard energy density.

```lean
TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  {J : TauCeti.SmoothAlmostComplexStructure I M} (hcompat : form.Compatible J) (x : M)
  (F : ℝ × ℝ →ₗ[ℝ] TangentSpace I x) :
  2 *
      TauCeti.SmoothBundleForm.eval₂ form x (F TauCeti.stdComplexLineReal)
        (F TauCeti.stdComplexLineImag) ≤
    form.stdComplexLineEnergyDensity J x F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wirtinger inequality](wirtinger-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Energy.html#TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity)
- [Source of `TauCeti.SmoothTwoForm.Compatible.two_mul_twoForm_le_stdComplexLineEnergyDensity` in TauCeti/Geometry/Symplectic/Manifold/Energy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Manifold/Energy.lean#L364)
