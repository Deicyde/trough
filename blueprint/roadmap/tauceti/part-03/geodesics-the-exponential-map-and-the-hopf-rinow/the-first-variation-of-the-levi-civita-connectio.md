---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection
statement: formalized
proof: formalized
---

# The first variation of the Levi-Civita connection

Let `g_s` be a family of smooth
nondegenerate metrics, jointly `C²` in `(s, y)` at `(t, x)`, with parameter derivative
`h = ∂ₛ g_s` at `s = t`, and let `∇ˢ` be a Levi-Civita connection of `g_s` for every `s`. Then for
every vector field `Y` which is differentiable at `x` and all `v, w ∈ T_x M`,

`2 g_t((∂ₜ∇)_v Y, w) = (∇ᵗ_v h)(Y, w) + (∇ᵗ_Y h)(v, w) - (∇ᵗ_w h)(v, Y)`,

where `(∂ₜ∇)_v Y` is the derivative at `t` of `s ↦ ∇ˢ_v Y` and `∇ᵗh` is the covariant derivative
`CovariantDerivative.derivBilinearTensor` of `h` along `∇ᵗ`.

```lean
TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection.{u_1, u_2,
    u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  {h : (x : M) → TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ} {t : ℝ} {x : M}
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E]
  {g : ℝ → TauCeti.Manifold.ContMDiffNondegenerateMetric}
  {cov : ℝ → CovariantDerivative I E fun x => TangentSpace I x} {Y : (x : M) → TangentSpace I x}
  (hcov : ∀ (s : ℝ), (g s).IsLeviCivitaConnection (cov s))
  (hg :
    ContMDiffAt ((modelWithCornersSelf ℝ ℝ).prod I)
      (I.prod (modelWithCornersSelf ℝ (E →L[ℝ] E →L[ℝ] ℝ))) 2
      (fun q => ⟨q.2, (g q.1).toContMDiffSection q.2⟩) (t, x))
  (hh :
    ∀ (y : M) (v w : TangentSpace I y),
      HasDerivAt (fun s => (((g s).toContMDiffSection y) v) w) (((h y) v) w) t)
  (hY : (MDiffAt fun x => ⟨x, Y x⟩) x) (v w : TangentSpace I x) :
  2 * (((g t).toContMDiffSection x) (deriv (fun s => (↑(cov s) Y x) v) t)) w =
    ((((cov t).derivBilinearTensor h x) (Y x)) w) v +
        ((((cov t).derivBilinearTensor h x) v) w) (Y x) -
      ((((cov t).derivBilinearTensor h x) v) (Y x)) w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.html#TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection)
- [Source of `TauCeti.Manifold.two_mul_apply_deriv_eq_derivBilinearTensor_of_isLeviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Variation.lean#L239)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HopfRinow/STATUS.md)
