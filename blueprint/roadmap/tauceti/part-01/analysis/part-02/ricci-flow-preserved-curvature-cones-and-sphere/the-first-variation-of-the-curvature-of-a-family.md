---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection
statement: formalized
proof: formalized
---

# The first variation of the curvature of a family of nondegenerate metrics

Let `g` be a
smooth family of nondegenerate metrics parametrized by `P`, let `c` be a parameter curve which is
`C²` at `t`, and let `∇ˢ` be a Levi-Civita connection of `g_{c s}` for every `s`. Write `Γ'` for the
derivative at `t` of the difference tensors `∇ˢ - ∇ᵗ`, the variation of the Levi-Civita connection
characterized by `two_mul_apply_deriv_difference_eq_derivBilinearTensor`, so that
`Γ'(Z, Y) = ∂ₛ ∇ˢ_Y Z`. Then for vector fields `X`, `Y` which are `C²` at `x` and `Z` which is `C³`
at `x`, the curvature `R^s(X, Y) Z` at `x` has parameter derivative

`(∇ᵗ_X Γ')(Z, Y) - (∇ᵗ_Y Γ')(Z, X)`

at `t`, where `(∇_X Γ')(Z, Y) = ∇_X (Γ'(Z, Y)) - Γ'(∇_X Z, Y) - Γ'(Z, ∇_X Y)`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP]
  [NormedSpace ℝ EP] {HP : Type u_5} [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP}
  {P : Type u_6} [TopologicalSpace P] [ChartedSpace HP P]
  (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) {c : ℝ → P}
  {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x} {t : ℝ} [IsManifold IP 1 P] {x : M}
  (hc : ContMDiffAt (modelWithCornersSelf ℝ ℝ) IP 2 c t)
  (hcov : ∀ (s : ℝ), (g.metric (c s)).IsLeviCivitaConnection (cov s))
  {X Y Z : (y : M) → TangentSpace I y} (hX : ContMDiffAt I I.tangent 2 (fun y => ⟨y, X y⟩) x)
  (hY : ContMDiffAt I I.tangent 2 (fun y => ⟨y, Y y⟩) x)
  (hZ : ContMDiffAt I I.tangent 3 (fun y => ⟨y, Z y⟩) x) :
  HasDerivAt (fun s => (cov s).curvatureOperator X Y Z x)
    ((↑(cov t) (fun y => ((deriv (fun s => (cov s).difference (cov t) y) t) (Z y)) (Y y)) x) (X x) -
          ((deriv (fun s => (cov s).difference (cov t) x) t) ((↑(cov t) Z x) (X x))) (Y x) -
        ((deriv (fun s => (cov s).difference (cov t) x) t) (Z x)) ((↑(cov t) Y x) (X x)) -
      ((↑(cov t) (fun y => ((deriv (fun s => (cov s).difference (cov t) y) t) (Z y)) (X y)) x)
            (Y x) -
          ((deriv (fun s => (cov s).difference (cov t) x) t) ((↑(cov t) Z x) (Y x))) (X x) -
        ((deriv (fun s => (cov s).difference (cov t) x) t) (Z x)) ((↑(cov t) X x) (Y x))))
    t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)
- [TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-contmdiffnondegeneratemetric-le.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/CurvatureVariation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/CurvatureVariation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.hasDerivAt_curvatureOperator_of_isLeviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/CurvatureVariation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/CurvatureVariation.lean#L83)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
