---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le
statement: formalized
proof: formalized
---

# Rauch comparison under an upper sectional curvature bound

Let `γ` be a geodesic with
`|γ'(a)| = 1` and `J` a Jacobi field along it with `J(a) = 0` and `D_t J(a)` orthogonal to
`γ'(a)`. If every plane containing `γ'(t)` has sectional curvature at most `κ` for `t ∈ (a, b)`,
and `b - a < π / √κ` when `κ > 0`, then `s_κ(b - a) |D_t J(a)| ≤ |J(b)|`, with `s_κ` the model
sine of curvature `κ`.

```lean
TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {γ : ℝ → M}
  {V : (t : ℝ) → TangentSpace I (γ t)} {s : Set ℝ} {a b κ : ℝ}
  (h : TauCeti.Manifold.IsJacobiFieldOn I γ V s) (hab : a ≤ b) (hs : Set.Icc a b ⊆ s)
  (hunit : ‖TauCeti.Manifold.curveVelocityWithin I γ s a‖ = 1) (hVa : V a = 0)
  (hnormal :
    inner ℝ ((CovariantDerivative.leviCivitaConnection I M).alongCurveWithin γ V s a)
        (TauCeti.Manifold.curveVelocityWithin I γ s a) =
      0)
  (hK :
    ∀ t ∈ Set.Ioo a b,
      ∀ (u : TangentSpace I (γ t)),
        LinearIndependent ℝ ![u, TauCeti.Manifold.curveVelocityWithin I γ s t] →
          (CovariantDerivative.leviCivitaConnection I M).sectionalCurvature ⋯ (γ t) u
              (TauCeti.Manifold.curveVelocityWithin I γ s t) ≤
            κ)
  (hbound : 0 < κ → b - a < Real.pi / √κ) :
  TauCeti.curvatureSine κ (b - a) *
      ‖(CovariantDerivative.leviCivitaConnection I M).alongCurveWithin γ V s a‖ ≤
    ‖V b‖
```

## Depends on

- [TauCeti.Manifold.IsJacobiFieldOn](tauceti-manifold-isjacobifieldon.md)

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Comparison.html#TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Comparison.html#TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le)
- [Source of `TauCeti.Manifold.IsJacobiFieldOn.rauch_norm_ge_of_sectional_le` in TauCeti/Geometry/Manifold/Riemannian/Jacobi/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Comparison.lean#L320)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
