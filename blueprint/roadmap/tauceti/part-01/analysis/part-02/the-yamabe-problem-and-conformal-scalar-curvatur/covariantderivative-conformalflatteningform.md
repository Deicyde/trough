---
declaration: def
origin: cited
lean: CovariantDerivative.conformalFlatteningForm
statement: formalized
---

# CovariantDerivative.conformalFlatteningForm

The right side of the conformal flattening equation `Hess φ = Φ_(grad φ)`,
`Φ_ξ(u, v) = P(u, v) + ⟪ξ, u⟫ ⟪ξ, v⟫ - (‖ξ‖² / 2) ⟪u, v⟫`, where `P` is the Schouten tensor.

```lean
CovariantDerivative.conformalFlatteningForm.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle (TangentSpace I)]
  (cov : CovariantDerivative I E (TangentSpace I)) [cov.ContMDiffCovariantDerivative ↑⊤] (x : M)
  (ξ : TangentSpace I x) : TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.conformalFlatteningForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Weyl/Integrability.html#CovariantDerivative.conformalFlatteningForm).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.conformalFlatteningForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Weyl/Integrability.html#CovariantDerivative.conformalFlatteningForm)
- [Source of `CovariantDerivative.conformalFlatteningForm` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Weyl/Integrability.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Weyl/Integrability.lean#L101)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
