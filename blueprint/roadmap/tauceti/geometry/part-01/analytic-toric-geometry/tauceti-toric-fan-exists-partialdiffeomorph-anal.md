---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm

The toric boundary has the holomorphic coordinate-hyperplane normal form near every point `x`
of the realization. There are a biholomorphism `e` from an open neighbourhood of `x` onto an open
subset of `ℂ ^ n`, for `n` the rank of the lattice, and an injection `j` from the set `s` of
boundary components through `x` to the coordinate indices, such that a point of the neighbourhood
lies in a boundary component exactly when that component passes through `x` and the coordinate
it is assigned vanishes.

```lean
TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm.{u} {N V : Type u}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i)
  (hΦ : Φ.IsRegular) (x : ↑(Φ.analyticRealization hΦ)) (n : WithTop ℕ∞) :
  ∃ s j e,
    x ∈ e.source ∧
      (∀ (ρ : Φ.Ray), x ∈ Φ.analyticBoundaryComponent hΦ ρ ↔ ρ ∈ s) ∧
        ∀ y ∈ e.source,
          ∀ (ρ : Φ.Ray),
            y ∈ Φ.analyticBoundaryComponent hΦ ρ ↔
              ∃ (hρ : ρ ∈ s), ↑e.toPartialEquiv y (j ⟨ρ, hρ⟩) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Tucker's theorem](../convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/NormalForm.html#TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/NormalForm.html#TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm)
- [Source of `TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm` in TauCeti/Geometry/Toric/Analytic/Fan/Boundary/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/NormalForm.lean#L83)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AnalyticToricGeometry/STATUS.md)
