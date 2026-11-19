---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc, TauCeti.SmoothForm.mpullback_timeDependentFlowOf_strictMoserVectorField, TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply, TauCeti.SmoothForm.isStrictContactomorphism_strictMoserDiffeomorph, TauCeti.SmoothForm.mpullback_strictMoserDiffeomorph
statement: formalized
proof: formalized
---

# The strict Moser theorem along a trajectory

Let `α_t` be a smooth family of contact forms
on a boundaryless manifold, `h` a smooth time-dependent function and `x` a point of the source of
the strict Moser partial isotopy `φ_(s,t)`. If at every time `u` between `s` and `t` the slice
`h_u` solves the Reeb-direction equation `R_(α_u) h_u = -(∂_t α_u)(R_(α_u))` on a neighbourhood of
the point `φ_(s,u) x` of the trajectory of `x`, then `φ_(s,t)` pulls `α_t` back to `α_s` at `x`.
The Reeb-direction equation is assumed only near the trajectory of `x`; `h` must still be smooth
everywhere.

```lean
TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1}
  {h : ℝ × M → ℝ} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) (↑⊤) h)
  {s t : ℝ} {x : M} (hx : x ∈ (TauCeti.SmoothForm.strictMoserPartialDiffeomorph hc hh s t).source)
  (hR :
    ∀ u ∈ Set.uIcc s t,
      ∀ᶠ (y : M) in
        nhds (↑(TauCeti.SmoothForm.strictMoserPartialDiffeomorph hc hh s u).toPartialEquiv x),
        ((d% fun z => h (u, z)) y)
            (((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α).reebVectorField y) =
          -(↑((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α.timeDeriv) y)
              ![((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α).reebVectorField y]) :
  TauCeti.mpullback I I
      (↑(TauCeti.SmoothForm.strictMoserPartialDiffeomorph hc hh s t).toPartialEquiv)
      (↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) x =
    ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [Moser's principle for families of forms](../manifold/part-03/mosers-principle-for-families-of-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc).

## Other forms

**The strict Moser theorem along a complete flow.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_timeDependentFlowOf_strictMoserVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.mpullback_timeDependentFlowOf_strictMoserVectorField).

```lean
TauCeti.SmoothForm.mpullback_timeDependentFlowOf_strictMoserVectorField.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1}
  {h : ℝ × M → ℝ} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm)
  (hR :
    ∀ (t : ℝ) (x : M),
      ((d% fun y => h (t, y)) x)
          (((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x) =
        -(↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α.timeDeriv) x)
            ![((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x])
  [I.Boundaryless] [T2Space M]
  (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) 3 h)
  (hcomplete :
    TauCeti.IsCompleteVectorField
      (TauCeti.timeDependentSuspensionField (α.strictMoserVectorField h)))
  (s t : ℝ) :
  TauCeti.mpullback I I (TauCeti.timeDependentFlowOf (α.strictMoserVectorField h) s t)
      (TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) ↑α) =
    TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk s) ↑α
```

**The strict Moser theorem along the domain of the flow.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply).

```lean
TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} {h : ℝ × M → ℝ}
  [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm)
  (hR :
    ∀ (t : ℝ) (x : M),
      ((d% fun y => h (t, y)) x)
          (((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x) =
        -(↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α.timeDeriv) x)
            ![((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x])
  [I.Boundaryless] [T2Space M]
  (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) (↑⊤) h) {s t : ℝ}
  {x : M} (hx : x ∈ (TauCeti.SmoothForm.strictMoserPartialDiffeomorph hc hh s t).source) :
  TauCeti.mpullback I I
      (↑(TauCeti.SmoothForm.strictMoserPartialDiffeomorph hc hh s t).toPartialEquiv)
      (↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) x =
    ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

**The strict Moser theorem for a family of contact forms.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.isStrictContactomorphism_strictMoserDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.isStrictContactomorphism_strictMoserDiffeomorph).

```lean
TauCeti.SmoothForm.isStrictContactomorphism_strictMoserDiffeomorph.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} {h : ℝ × M → ℝ}
  [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm)
  (hR :
    ∀ (t : ℝ) (x : M),
      ((d% fun y => h (t, y)) x)
          (((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x) =
        -(↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α.timeDeriv) x)
            ![((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x])
  [I.Boundaryless] [T2Space M] [CompactSpace M]
  (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) (↑⊤) h) (s t : ℝ) :
  (TauCeti.SmoothForm.strictMoserDiffeomorph hc hh s t).IsStrictContactomorphism
    ((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α)
    ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)
```

**The strict Moser theorem for a family of contact forms, as an identity of forms.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.mpullback_strictMoserDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.mpullback_strictMoserDiffeomorph).

```lean
TauCeti.SmoothForm.mpullback_strictMoserDiffeomorph.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} {h : ℝ × M → ℝ}
  [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm)
  (hR :
    ∀ (t : ℝ) (x : M),
      ((d% fun y => h (t, y)) x)
          (((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x) =
        -(↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α.timeDeriv) x)
            ![((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).reebVectorField x])
  [I.Boundaryless] [T2Space M] [CompactSpace M]
  (hh : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) (↑⊤) h) (s t : ℝ) :
  (TauCeti.SmoothForm.mpullback ⇑(TauCeti.SmoothForm.strictMoserDiffeomorph hc hh s t) ⋯)
      ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α) =
    (TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/StrictMoser.html#TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc)
- [Source of `TauCeti.SmoothForm.mpullback_strictMoserPartialDiffeomorph_apply_of_forall_mem_uIcc` in TauCeti/Geometry/Contact/StrictMoser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/StrictMoser.lean#L724)
