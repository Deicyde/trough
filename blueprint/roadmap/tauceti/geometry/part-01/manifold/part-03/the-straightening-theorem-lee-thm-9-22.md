---
declaration: theorem
origin: cited
lean: TauCeti.exists_chart_mfderiv_eq_const
statement: formalized
proof: formalized
---

# The straightening theorem [Lee, Thm. 9.22]

Let `v` be a vector field on a `C^n` manifold
with finite-dimensional boundaryless model, `C^m` on a neighbourhood of `x`, with `1 ≤ m`,
`m + 1 ≤ n` and `v x ≠ 0`. Then some chart `e` of the `C^m` maximal atlas whose domain contains `x`
carries `v` to a constant nonzero vector field: the differential of `I ∘ e` sends `v y` to the same
vector `u ≠ 0` at every point `y` of the domain of `e`.

```lean
TauCeti.exists_chart_mfderiv_eq_const.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] {m : ℕ∞}
  {n : WithTop ℕ∞} (hm : 1 ≤ m) (hmn : ↑m + 1 ≤ n) [IsManifold I 1 M] [IsManifold I n M]
  {v : (y : M) → TangentSpace I y} {U : Set M} {x : M}
  (hv : ContMDiffOn I I.tangent (↑m) (fun y => ⟨y, v y⟩) U) (hU : U ∈ nhds x) (hx : v x ≠ 0) :
  ∃ e u,
    e ∈ IsManifold.maximalAtlas I (↑m) M ∧
      x ∈ e.source ∧ u ≠ 0 ∧ ∀ y ∈ e.source, (mfderiv% (↑I ∘ ↑e) y) (v y) = u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The straightening theorem (flow-box theorem)](../../../../analysis/part-02/ode/the-straightening-theorem-flow-box-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_chart_mfderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/Straightening.html#TauCeti.exists_chart_mfderiv_eq_const).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_chart_mfderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/Straightening.html#TauCeti.exists_chart_mfderiv_eq_const)
- [Source of `TauCeti.exists_chart_mfderiv_eq_const` in TauCeti/Geometry/Manifold/Flow/Straightening.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Flow/Straightening.lean#L58)
