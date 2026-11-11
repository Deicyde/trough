---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero
statement: formalized
proof: formalized
---

# The contact volume criterion

On a manifold of dimension `2 n + 1`, a smooth one-form `α`
is a contact form exactly when `α ∧ (dα)ⁿ` vanishes nowhere.

```lean
TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 2 M] {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1)
  (α : TauCeti.SmoothForm I M ℝ 1) :
  α.IsContactForm ↔
    ∀ (x : M), ↑((TauCeti.SmoothForm.wedge α) (((TauCeti.mextDerivₗ I 1) α).wedgePow n)) x ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Volume.html#TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Volume.html#TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero)
- [Source of `TauCeti.SmoothForm.isContactForm_iff_wedge_wedgePow_apply_ne_zero` in TauCeti/Geometry/Contact/Volume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Contact/Volume.lean#L144)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
