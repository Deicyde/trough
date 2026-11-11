---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection
statement: formalized
proof: formalized
---

# The first variation of the Levi-Civita connection along a parameter curve

Let `g` be a
smooth family of nondegenerate metrics parametrized by `P`, let `c` be a parameter curve which is
`C²` at `t`, and let `∇ˢ` be a Levi-Civita connection of `g_{c s}` for every `s`. Write
`h = δ_{c'(t)} g` for the first variation of `g` at `c t` in the direction of the velocity of `c`,
which is the parameter derivative `∂ₜ g_{c t}`. Then for every vector field `Y` which is
differentiable at `x` and all `v, w ∈ T_x M`,

`2 g_{c t}((∂ₜ∇)_v Y, w) = (∇ᵗ_v h)(Y, w) + (∇ᵗ_Y h)(v, w) - (∇ᵗ_w h)(v, Y)`,

where `(∂ₜ∇)_v Y` is the derivative at `t` of `s ↦ ∇ˢ_v Y` and `∇ᵗh` is the covariant derivative
`CovariantDerivative.derivBilinearTensor` of `h` along `∇ᵗ`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {t : ℝ}
  {x : M} [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP] [NormedSpace ℝ EP]
  {HP : Type u_5} [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP} {P : Type u_6}
  [TopologicalSpace P] [ChartedSpace HP P]
  (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) {c : ℝ → P}
  {Y : (x : M) → TangentSpace I x} [FiniteDimensional ℝ E]
  {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x}
  (hc : ContMDiffAt (modelWithCornersSelf ℝ ℝ) IP 2 c t)
  (hcov : ∀ (s : ℝ), (g.metric (c s)).IsLeviCivitaConnection (cov s))
  (hY : (MDiffAt fun x => ⟨x, Y x⟩) x) (v w : TangentSpace I x) :
  2 * ((↑g (c t, x)) (deriv (fun s => (↑(cov s) Y x) v) t)) w =
    ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) x) (Y x)) w) v +
        ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) x) v) w) (Y x) -
      ((((cov t).derivBilinearTensor (g.variation (c t) ((mfderiv% c t) 1)) x) v) (Y x)) w
```

## Depends on

- [TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation](tauceti-manifold-contmdiffnondegeneratemetricfam.md)

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean#L302)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HopfRinow/STATUS.md)
