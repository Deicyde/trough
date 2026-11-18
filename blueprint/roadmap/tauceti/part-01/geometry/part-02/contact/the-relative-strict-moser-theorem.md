---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq
statement: formalized
proof: formalized
---

# The relative strict Moser theorem

Let `α_t` be a smooth family of contact forms on a
boundaryless manifold and `h` a smooth time-dependent function. Let `K` be a set of points at each
of which the strict Moser vector field vanishes at all times, and let `U ⊆ ℝ × M` be an open set
on which `h_t` solves the Reeb-direction equation `R_(α_t) h_t = -(∂_t α_t)(R_(α_t))` and which
contains `(u, x)` for every `x ∈ K` and every time `u` between `s` and `t`. Then there is a smooth
partial diffeomorphism `φ` of `M`, whose source and target are open neighbourhoods of `K`, which
fixes every point of `K` and pulls `α_t` back to `α_s` on its source. Neither `K` nor `M` need be
compact, and `K` need not be closed.

```lean
TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} {h : ℝ × M → ℝ}
  [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) (↑⊤) h)
  {K : Set M} (hK : ∀ x ∈ K, ∀ (u : ℝ), α.strictMoserVectorField h u x = 0) {U : Set (ℝ × M)}
  (hU : IsOpen U) {s t : ℝ} (hKU : ∀ x ∈ K, ∀ u ∈ Set.uIcc s t, (u, x) ∈ U)
  (hR :
    ∀ p ∈ U,
      ((d% fun y => h (p.1, y)) p.2)
          (((TauCeti.SmoothForm.mpullback (Prod.mk p.1) ⋯) α).reebVectorField p.2) =
        -(↑((TauCeti.SmoothForm.mpullback (Prod.mk p.1) ⋯) α.timeDeriv) p.2)
            ![((TauCeti.SmoothForm.mpullback (Prod.mk p.1) ⋯) α).reebVectorField p.2]) :
  ∃ φ,
    K ⊆ φ.source ∧
      K ⊆ φ.target ∧
        (∀ x ∈ K, ↑φ.toPartialEquiv x = x) ∧
          ∀ x ∈ φ.source,
            TauCeti.mpullback I I (↑φ.toPartialEquiv)
                (↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) x =
              ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [The strict Moser theorem along a trajectory](the-strict-moser-theorem-along-a-trajectory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq)
- [Source of `TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq` in TauCeti/Geometry/Contact/StrictMoser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/StrictMoser.lean#L791)
