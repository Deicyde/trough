---
declaration: theorem
origin: cited
lean: TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder
statement: formalized
proof: formalized
---

# The zero-spatial BCR theorem is the Hausdorff--Bernstein--Widder theorem

For a real function `f`, the bounded, continuous positive-definite condition on
`(t, _) ↦ f t : ℝ≥0 × PUnit → ℂ` holds exactly when `f` is continuous on `[0, ∞)` and completely
monotone on `(0, ∞)`.

```lean
TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder (f : ℝ → ℝ) :
  (TauCeti.IsSemigroupGroupPD fun x => ↑(f ↑x.1)) ∧
      (Continuous fun x => ↑(f ↑x.1)) ∧ Bornology.IsBounded (Set.range fun x => ↑(f ↑x.1)) ↔
    TauCeti.IsContinuousCompletelyMonotoneOnIoi f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Berg--Christensen--Ressel representation theorem (Berg--Christensen--Ressel 4.1.13)](../../part-01/one-parameter-semigroups-completely-monotone-and/the-berg-christensen-ressel-representation-theor.md)
- [Hausdorff--Bernstein--Widder theorem, finite-measure version on `ℝ≥0`](../../part-01/one-parameter-semigroups-completely-monotone-and/hausdorff-bernstein-widder-theorem-finite-measur.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../../part-01/weighted-orthogonal-l2-bases-completeness-hilber/moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/ZeroSpatial.html#TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder).

## Sources

- [Tau Ceti documentation: `TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder`](https://taucetiproject.org/docs/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/ZeroSpatial.html#TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder)
- [Source of `TauCeti.bcr_zero_spatial_iff_hausdorff_bernstein_widder` in TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/ZeroSpatial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PositiveDefinite/SemigroupGroup/FourierLaplace/ZeroSpatial.lean#L116)
