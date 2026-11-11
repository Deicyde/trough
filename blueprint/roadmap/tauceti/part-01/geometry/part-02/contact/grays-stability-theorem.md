---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph, TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply, TauCeti.SmoothForm.preservesCoorientation_grayDiffeomorph
statement: formalized
proof: formalized
---

# Gray's stability theorem

Gray's isotopy from `s` to `t` is a contactomorphism from
`ker α_s` to `ker α_t`.

```lean
TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] [CompactSpace M] (s t : ℝ) :
  (TauCeti.SmoothForm.grayDiffeomorph hc s t).IsContactomorphism
    ((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α)
    ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [Moser's principle for families of forms](../manifold/part-02/mosers-principle-for-families-of-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph).

## Other forms

**Gray's stability theorem.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply).

```lean
TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] [CompactSpace M] (s t : ℝ) (x : M) :
  ↑((TauCeti.SmoothForm.mpullback ⇑(TauCeti.SmoothForm.grayDiffeomorph hc s t) ⋯)
          ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α))
      x =
    Real.exp (∫ (u : ℝ) in s..t, α.grayRate (u, (TauCeti.SmoothForm.grayDiffeomorph hc s u) x)) •
      ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

**Gray's stability theorem, coorientation form.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.preservesCoorientation_grayDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.preservesCoorientation_grayDiffeomorph).

```lean
TauCeti.SmoothForm.preservesCoorientation_grayDiffeomorph.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] [CompactSpace M] (s t : ℝ) :
  (TauCeti.SmoothForm.grayDiffeomorph hc s t).PreservesCoorientation
    ((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α)
    ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph)
- [Source of `TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph` in TauCeti/Geometry/Contact/Gray.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Contact/Gray.lean#L289)
