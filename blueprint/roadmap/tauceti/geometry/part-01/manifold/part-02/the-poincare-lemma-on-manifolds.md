---
declaration: theorem
origin: cited
lean: TauCeti.exists_mextDeriv_eq_nhds, TauCeti.exactForms_succ_eq_closedForms_normedSpace
statement: formalized
proof: formalized
---

# The Poincaré lemma on manifolds

A `C^r` form of positive degree, `r ≥ 1`, that is closed
near a point `x` is, on a neighbourhood of `x`, the exterior derivative of a `C^r` form defined on
the whole manifold. The manifold may have boundary or corners.

The coefficient space is complete: with values in the finitely supported sequences there is a
smooth closed `1`-form on `ℝ` with no local primitive. Finite dimensionality of the model and the
Hausdorff property are used only to cut the local primitive off by a smooth bump function.

```lean
TauCeti.exists_mextDeriv_eq_nhds.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {k : ℕ} [FiniteDimensional ℝ E] [T2Space M]
  [IsManifold I (↑⊤) M] {r : ℕ∞} (hr : 1 ≤ r) {φ : TauCeti.RoughForm I M F (k + 1)}
  (hφ : TauCeti.IsSmoothForm I (↑r) φ) {x : M}
  (hclosed : ∀ᶠ (y : M) in nhds x, TauCeti.mextDeriv φ y = 0) :
  ∃ U ∈ nhds x, ∃ ψ, TauCeti.IsSmoothForm I (↑r) ψ ∧ ∀ y ∈ U, TauCeti.mextDeriv ψ y = φ y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré lemma](../../../../analysis/part-01/calculus/part-01/the-poincare-lemma.md)
- [The relative Poincaré lemma](../../../../analysis/part-01/calculus/part-01/the-relative-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mextDeriv_eq_nhds`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Poincare.html#TauCeti.exists_mextDeriv_eq_nhds).

## Other forms

**The Poincaré lemma on a normed space.** Formalized in Tau Ceti as [`TauCeti.exactForms_succ_eq_closedForms_normedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/NormedSpace.html#TauCeti.exactForms_succ_eq_closedForms_normedSpace).

```lean
TauCeti.exactForms_succ_eq_closedForms_normedSpace.{u_1} (E : Type u_1) [NormedAddCommGroup E]
  [NormedSpace ℝ E] (k : ℕ) :
  TauCeti.exactForms (modelWithCornersSelf ℝ E) E (k + 1) =
    TauCeti.closedForms (modelWithCornersSelf ℝ E) E (k + 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mextDeriv_eq_nhds`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Poincare.html#TauCeti.exists_mextDeriv_eq_nhds)
- [Source of `TauCeti.exists_mextDeriv_eq_nhds` in TauCeti/Geometry/Manifold/DifferentialForm/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/Poincare.lean#L94)
