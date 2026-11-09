---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.integral_divergence_eq_zero
statement: formalized
proof: formalized
---

# The divergence theorem on a manifold without boundary

the divergence of a compactly
supported `C¹` vector field has integral zero against the Riemannian volume.

```lean
TauCeti.Manifold.integral_divergence_eq_zero.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {X : (x : M) → TangentSpace I x}
  (hX : ContMDiff I I.tangent 1 fun x => ⟨x, X x⟩) (hc : HasCompactSupport X) :
  ∫ (x : M), TauCeti.Manifold.divergence I X x ∂TauCeti.riemannianVolume I M = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula on a manifold](../part-02/jacobis-formula-on-a-manifold.md)
- [The Koszul formula](../part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.integral_divergence_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.html#TauCeti.Manifold.integral_divergence_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.integral_divergence_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.html#TauCeti.Manifold.integral_divergence_eq_zero)
- [Source of `TauCeti.Manifold.integral_divergence_eq_zero` in TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/DivergenceTheorem.lean#L223)
