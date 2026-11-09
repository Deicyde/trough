---
declaration: theorem
origin: cited
lean: TauCeti.pathClassIntegral_mextDeriv_ofFunction, TauCeti.pathClassIntegral_mextDeriv
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for path classes

The integral of the differential of
a `C²` function along a path class is the difference of the values of the function at the
endpoints.

```lean
TauCeti.pathClassIntegral_mextDeriv_ofFunction.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M] [CompleteSpace F]
  {x y : M} {g : M → F} (hg : ContMDiff I (modelWithCornersSelf ℝ F) 2 g)
  (γ : Path.Homotopic.Quotient x y) :
  TauCeti.pathClassIntegral (TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I g)) γ = g y - g x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré lemma on manifolds](../../manifold/part-02/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.pathClassIntegral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Period.html#TauCeti.pathClassIntegral_mextDeriv_ofFunction).

## Other forms

**The fundamental theorem of calculus for path classes, for a `C²` form `ψ` of degree zero.** Formalized in Tau Ceti as [`TauCeti.pathClassIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Period.html#TauCeti.pathClassIntegral_mextDeriv).

```lean
TauCeti.pathClassIntegral_mextDeriv.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M] [CompleteSpace F]
  {x y : M} {ψ : TauCeti.RoughForm I M F 0} (hψ : TauCeti.IsSmoothForm I 2 ψ)
  (γ : Path.Homotopic.Quotient x y) :
  TauCeti.pathClassIntegral (TauCeti.mextDeriv ψ) γ = (ψ y) 0 - (ψ x) 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.pathClassIntegral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Period.html#TauCeti.pathClassIntegral_mextDeriv_ofFunction)
- [Source of `TauCeti.pathClassIntegral_mextDeriv_ofFunction` in TauCeti/Geometry/Manifold/DeRham/Period.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/Period.lean#L187)
