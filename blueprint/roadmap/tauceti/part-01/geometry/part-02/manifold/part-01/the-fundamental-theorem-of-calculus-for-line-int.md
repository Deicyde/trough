---
declaration: theorem
origin: cited
lean: TauCeti.pathIntegral_mextDeriv_ofFunction, TauCeti.pathIntegral_mextDeriv
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for line integrals

The line integral of the
differential of a `C¹` function along a `C¹` curve is the difference of the values of the
function at the endpoints.

```lean
TauCeti.pathIntegral_mextDeriv_ofFunction.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {f : M → F} (hf : ContMDiff I (modelWithCornersSelf ℝ F) 1 f)
  {γ : ℝ → M} (hγ : ContMDiff (modelWithCornersSelf ℝ ℝ) I 1 γ) (a b : ℝ) :
  TauCeti.pathIntegral (TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I f)) γ a b =
    f (γ b) - f (γ a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pathIntegral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_mextDeriv_ofFunction).

## Other forms

**The fundamental theorem of calculus for line integrals, for a `C¹` form `ψ` of degree zero.** Formalized in Tau Ceti as [`TauCeti.pathIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_mextDeriv).

```lean
TauCeti.pathIntegral_mextDeriv.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] [IsManifold I 1 M] {ψ : TauCeti.RoughForm I M F 0}
  (hψ : TauCeti.IsSmoothForm I 1 ψ) {γ : ℝ → M} (hγ : ContMDiff (modelWithCornersSelf ℝ ℝ) I 1 γ)
  (a b : ℝ) : TauCeti.pathIntegral (TauCeti.mextDeriv ψ) γ a b = (ψ (γ b)) 0 - (ψ (γ a)) 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.pathIntegral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_mextDeriv_ofFunction)
- [Source of `TauCeti.pathIntegral_mextDeriv_ofFunction` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean#L381)
