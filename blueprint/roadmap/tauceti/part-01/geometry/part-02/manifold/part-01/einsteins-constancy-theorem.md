---
declaration: theorem
origin: cited
lean: CovariantDerivative.eq_of_ricciTensor_eq_smul_inner, CovariantDerivative.hasMFDerivAt_zero_of_ricciTensor_eq_smul_inner
statement: formalized
proof: formalized
---

# Einstein's constancy theorem

Let a metric-compatible torsion-free connection on a
preconnected manifold, of dimension other than two, have Ricci tensor `Ric = a g` for a function
`a`. Then `a` is constant.

```lean
CovariantDerivative.eq_of_ricciTensor_eq_smul_inner.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} [cov.ContMDiffCovariantDerivative ↑⊤]
  [PreconnectedSpace M] (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0)
  (hdim : Module.finrank ℝ E ≠ 2) {a : M → ℝ}
  (ha : ∀ (y : M), cov.ricciTensor y = a y • innerₗ (TangentSpace I y)) (x y : M) : a x = a y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The second Bianchi identity](../part-04/the-second-bianchi-identity.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.eq_of_ricciTensor_eq_smul_inner`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Einstein.html#CovariantDerivative.eq_of_ricciTensor_eq_smul_inner).

## Other forms

**Einstein's constancy theorem, local form.** Formalized in Tau Ceti as [`CovariantDerivative.hasMFDerivAt_zero_of_ricciTensor_eq_smul_inner`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Einstein.html#CovariantDerivative.hasMFDerivAt_zero_of_ricciTensor_eq_smul_inner).

```lean
CovariantDerivative.hasMFDerivAt_zero_of_ricciTensor_eq_smul_inner.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} [cov.ContMDiffCovariantDerivative ↑⊤]
  (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0) (hdim : Module.finrank ℝ E ≠ 2) {a : M → ℝ}
  {x : M} (ha : ∀ᶠ (y : M) in nhds x, cov.ricciTensor y = a y • innerₗ (TangentSpace I y)) :
  HasMFDerivAt% a x 0
```

## Sources

- [Tau Ceti documentation: `CovariantDerivative.eq_of_ricciTensor_eq_smul_inner`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Einstein.html#CovariantDerivative.eq_of_ricciTensor_eq_smul_inner)
- [Source of `CovariantDerivative.eq_of_ricciTensor_eq_smul_inner` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Einstein.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Einstein.lean#L162)
