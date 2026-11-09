---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff
statement: formalized
proof: formalized
---

# Fibre translation by a closed one-form is symplectic

Translating the fibres of the
cotangent bundle by a one-form `α` preserves the canonical symplectic form exactly when `α` is
closed.

```lean
TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff.{u_1,
    u_2, u_3}
  {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] (α : TauCeti.SmoothForm I M ℝ 1) :
  (TauCeti.SmoothForm.mpullback
          ⇑(TauCeti.vectorBundleTranslateDiffeomorph ⇑(TauCeti.SmoothForm.degreeOneEquiv α) ⋯) ⋯)
        (TauCeti.CotangentBundle.symplecticForm I M) =
      TauCeti.CotangentBundle.symplecticForm I M ↔
    α.IsClosed
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Fiberwise.html#TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Fiberwise.html#TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff)
- [Source of `TauCeti.CotangentBundle.mpullback_vectorBundleTranslateDiffeomorph_symplecticForm_eq_self_iff` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Fiberwise.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Fiberwise.lean#L148)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
