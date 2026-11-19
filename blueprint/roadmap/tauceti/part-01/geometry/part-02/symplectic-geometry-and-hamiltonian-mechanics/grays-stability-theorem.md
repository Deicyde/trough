---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply, TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph, TauCeti.SmoothForm.preservesCoorientation_grayDiffeomorph, TauCeti.SmoothForm.mpullback_grayPartialDiffeomorph_apply
statement: formalized
proof: formalized
---

# Gray's stability theorem

On a compact manifold without boundary, the time-dependent flow
`φ_{s,t}` of the Gray vector field of a smooth family of contact forms `α_t` rescales the forms:
`φ_{s,t}^* α_t = exp (∫ₛᵗ μ_u ∘ φ_{s,u} du) α_s`, where `μ_u = (∂_t α_u)(R_{α_u})`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [Moser's principle for families of forms](../manifold/part-03/mosers-principle-for-families-of-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply).

## Other forms

**Gray's stability theorem.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.isContactomorphism_grayDiffeomorph).

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

**Gray's stability theorem along the domain of the flow.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_grayPartialDiffeomorph_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.mpullback_grayPartialDiffeomorph_apply).

```lean
TauCeti.SmoothForm.mpullback_grayPartialDiffeomorph_apply.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] {s t : ℝ} {x : M}
  (hx : x ∈ (TauCeti.SmoothForm.grayPartialDiffeomorph hc s t).source) :
  TauCeti.mpullback I I (↑(TauCeti.SmoothForm.grayPartialDiffeomorph hc s t).toPartialEquiv)
      (↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) x =
    Real.exp
        (∫ (u : ℝ) in s..t,
          α.grayRate (u, ↑(TauCeti.SmoothForm.grayPartialDiffeomorph hc s u).toPartialEquiv x)) •
      ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply)
- [Source of `TauCeti.SmoothForm.mpullback_grayDiffeomorph_apply` in TauCeti/Geometry/Contact/Gray.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/Gray.lean#L431)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
