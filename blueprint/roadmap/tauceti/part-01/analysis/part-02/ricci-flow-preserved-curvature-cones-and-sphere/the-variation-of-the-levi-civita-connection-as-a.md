---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor
statement: formalized
proof: formalized
---

# The variation of the Levi-Civita connection as a tensor

Let `g` be a smooth family of
nondegenerate metrics parametrized by `P`, let `c` be a parameter curve which is `C²` at `t`, and
let `∇ˢ` be a Levi-Civita connection of `g_{c s}` for every `s`. Write `h = δ_{c'(t)} g` for the
first variation of `g` in the direction of the velocity of `c`, and `Γ'` for the derivative at `t`
of the difference tensors `∇ˢ - ∇ᵗ` at `y`. Then for all `u, v, w ∈ T_y M`,

`2 g_{c t}(Γ'(u, v), w) = (∇ᵗ_v h)(u, w) + (∇ᵗ_u h)(v, w) - (∇ᵗ_w h)(v, u)`,

where `∇ᵗh` is the covariant derivative `CovariantDerivative.derivBilinearTensor` of `h` along
`∇ᵗ`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {t : ℝ}
  [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP] [NormedSpace ℝ EP] {HP : Type u_5}
  [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP} {P : Type u_6} [TopologicalSpace P]
  [ChartedSpace HP P] (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) {c : ℝ → P}
  [FiniteDimensional ℝ E] {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x}
  (hc : ContMDiffAt (modelWithCornersSelf ℝ ℝ) IP 2 c t)
  (hcov : ∀ (s : ℝ), (g.metric (c s)).IsLeviCivitaConnection (cov s)) (y : M)
  (u v w : TangentSpace I y) :
  2 * ((↑g (c t, y)) (((deriv (fun s => (cov s).difference (cov t) y) t) u) v)) w =
    ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) y) u) w) v +
        ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) y) v) w) u -
      ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) y) v) u) w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first variation of the Levi-Civita connection along a parameter curve](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/the-first-variation-of-the-levi-civita-connectio.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_difference_eq_derivBilinearTensor` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean#L372)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
