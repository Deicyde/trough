---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left
statement: formalized
proof: formalized
---

# Green's second identity on a manifold without boundary

for a compactly supported `C²`
function `f` and a `C²` function `g`, `∫ f Δg dV = ∫ (Δf) g dV`.

```lean
TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {f g : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 f) (hfc : HasCompactSupport f)
  (hg : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 g) :
  ∫ (x : M), f x * TauCeti.Manifold.laplaceBeltrami I g x ∂TauCeti.riemannianVolume I M =
    ∫ (x : M), TauCeti.Manifold.laplaceBeltrami I f x * g x ∂TauCeti.riemannianVolume I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The divergence theorem on a manifold without boundary](the-divergence-theorem-on-a-manifold-without-bou.md)
- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.html#TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.html#TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left)
- [Source of `TauCeti.Manifold.integral_mul_laplaceBeltrami_right_eq_left` in TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.lean#L335)
