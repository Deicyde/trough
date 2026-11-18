---
declaration: theorem
origin: cited
lean: TauCeti.exists_chart_mfderiv_eq_const
statement: formalized
proof: formalized
---

# The straightening theorem [Lee, Thm. 9.22]

Let `v` be a vector field on a `C^n` manifold
with finite-dimensional model, `C^m` on a neighbourhood of an interior point `x`, with `1 ≤ m`,
`m + 1 ≤ n` and `v x ≠ 0`. Then some chart `e` of the `C^m` maximal atlas whose domain contains `x`
carries `v` to a constant nonzero vector field: the differential of `I ∘ e` sends `v y` to the same
vector `u ≠ 0` at every point `y` of the domain of `e`. This is the case of a single field in
`TauCeti.exists_chart_mfderiv_eq_const_of_eventually_mlieBracket_eq_zero`.

```lean
TauCeti.exists_chart_mfderiv_eq_const.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] {m : ℕ∞} {n : WithTop ℕ∞}
  (hm : 1 ≤ m) (hmn : ↑m + 1 ≤ n) [IsManifold I 1 M] [IsManifold I n M]
  {v : (y : M) → TangentSpace I y} {U : Set M} {x : M} (hxI : I.IsInteriorPoint x)
  (hv : ContMDiffOn I I.tangent (↑m) (fun y => ⟨y, v y⟩) U) (hU : U ∈ nhds x) (hx : v x ≠ 0) :
  ∃ e u,
    e ∈ IsManifold.maximalAtlas I (↑m) M ∧
      x ∈ e.source ∧ u ≠ 0 ∧ ∀ y ∈ e.source, (mfderiv% (↑I ∘ ↑e) y) (v y) = u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_chart_mfderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/Straightening.html#TauCeti.exists_chart_mfderiv_eq_const).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_chart_mfderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/Straightening.html#TauCeti.exists_chart_mfderiv_eq_const)
- [Source of `TauCeti.exists_chart_mfderiv_eq_const` in TauCeti/Geometry/Manifold/Flow/Straightening.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Flow/Straightening.lean#L149)
