---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraicSpace_iff_forall_isAlgebraicSpace_relocalizeRestrict, AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor, AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor_of_colimit, AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor_specStalk, AlgebraicGeometry.FinitePresentationSpacesOver.isGlueingColimitEquivalence_of_colimit, AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_specStalkStageColimitFunctor, AlgebraicGeometry.FinitePresentationSpacesOver.ClosedPointsGlueingData.essSurj_comparisonFunctor, AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_comparisonFunctor_closedPoints
statement: formalized
proof: formalized
---

# 70.18 Glueing in closed fibres

Section 70.18 of the Stacks Project, [Tag 0E8Y](https://stacks.math.columbia.edu/tag/0E8Y). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E8Z, a lemma

[Tag 0E8Z](https://stacks.math.columbia.edu/tag/0E8Z) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_iff_forall_isAlgebraicSpace_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlgebraicityOnBaseCover.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AlgebraicityOnBaseCover.lean#L141). The attribute's comment: “algebraicity is detected on an open covering of the base”.

> **Stacks 0E8Z, the algebraicity criterion.** Let `{jᵢ : Tᵢ ⟶ S}` be a finite family of open
> immersions of a big fppf site whose images cover `S`. An fppf sheaf on the big fppf site of `S`
> is an algebraic space over `S` exactly when its restriction along each `jᵢ` is an algebraic
> space over `Tᵢ`.

```lean
theorem isAlgebraicSpace_iff_forall_isAlgebraicSpace_relocalizeRestrict [Finite I]
    (hj : ∀ i, IsOpenImmersion (B.inclusion.map (j i)))
    (hcov : ∀ x : S, ∃ i, x ∈ Set.range (B.inclusion.map (j i)))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F) :
    IsAlgebraicSpace B S hS F ↔
      ∀ i, IsAlgebraicSpace B (T i) (hT i) ((OverShriek.relocalizeRestrict (j i)).obj F)
```

**`AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationSliceGlueing.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationSliceGlueing.lean#L64). The attribute's comment: “the equivalence clause: for an open covering of the base, base change is an equivalence onto the 2-fibre product of the categories of finite-presentation algebraic spaces over the two members. The criterion clause, that algebraicity is detected on such a covering, is `AlgebraicGeometry.isAlgebraicSpace_iff_forall_isAlgebraicSpace_relocalizeRestrict` in `StacksFrontier.AlgebraicGeometry.Spaces.AlgebraicityOnBaseCover`, which this module imports, so the two clauses cannot live in one file”.

> **The algebraic spaces of finite presentation over a base covered by two opens `U` and `W`
> with intersection `V` are the `2`-fibre product `FP_U ×_{FP_V} FP_W`.** The comparison functor
> taking a space to its two restrictions together with their canonical identification over `V` is
> an equivalence: it is faithful and full by the sheaf condition at the Mayer--Vietoris squares of
> the covering, and essentially surjective because the space glued from a datum restricts back to
> it.

```lean
theorem isEquivalence_glueingFunctor : (glueingFunctor B S hS hV.w).IsEquivalence
```

## Tag 0E90, a lemma

[Tag 0E90](https://stacks.math.columbia.edu/tag/0E90) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor_of_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedFibreGlueing.lean, line 909](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedFibreGlueing.lean#L909). The attribute's comment: “the equivalence, granted the two colimit identifications. The theorem is stated for an arbitrary object `M` of the site equipped with a cofiltered system of open neighbourhoods `W i` of the point complementary to `U`, and an object `N` over their intersections with `U`, such that base change exhibits `FP_M` as the cofiltered 2-colimit of the `FP_{W i}` and `FP_N` as that of the `FP_{W i ∩ U}`; these two statements are the hypotheses `hloc` and `hoverlap`. For `M = Spec O_{S,s}` they are what Stacks 07SK gives once the affine open neighbourhoods of `s` are known to have `Spec O_{S,s}` as their limit and the `W i ∩ U` to have its puncture as theirs — neither limit identification is available in this library, which is why the two colimit statements are carried as hypotheses rather than proved”.

> **The algebraic spaces of finite presentation over the base are the `2`-fibre product
> `FP_U ×_{FP_N} FP_M`, when `M` is a cofiltered limit of open neighbourhoods of the point
> complementary to `U` and `N` is the corresponding limit of their intersections with `U`.**
>
> This is Stacks 0E90 for `M = Spec O_{S,s}` and `N = Spec O_{S,s} ∖ {s}`, granted the two
> colimit identifications carried as the hypotheses `hloc` and `hoverlap`: what the theorem proves
> is the formal combination, namely that the comparison functor is faithful, full and essentially
> surjective. Faithfulness and fullness come from the equivalence of Stacks 0E8Z at a single
> neighbourhood, which applies because the complement of the point and any neighbourhood of it
> cover the base; essential surjectivity needs in addition that a glueing datum descends to a
> neighbourhood.

```lean
theorem isEquivalence_glueingFunctor_of_colimit :
    (glueingFunctor B S hS hsq.w).IsEquivalence
```

**`AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_glueingFunctor_specStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationSpecStalkGlueing.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationSpecStalkGlueing.lean#L198). The attribute's comment: “the equivalence, unconditionally: for a point `s` of `S` whose complement is an open `U` with quasi-compact inclusion — the tag's closed point and quasi-compact `U → S` — the comparison functor `FP_S ⥤ FP_U ×_{FP_V} FP_{Spec O_{S,s}}` is an equivalence, with `V = Spec O_{S,s} ∖ {s}` the complement of the closed point, which the vertex of the system of overlaps is by `toScheme_obj_opensSpecStalkSiteObj_eq_compl_closedPoint`. The two colimit identifications that the general theorem `isEquivalence_glueingFunctor_of_colimit` carries as hypotheses are discharged here from Stacks 07SK and the identification of `Spec O_{S,s}` and of its puncture as the limits of the affine open neighbourhoods of `s` and of their intersections with `U`”.

> **Stacks 0E90.**  Let `S` be a scheme, let `s` be a point of `S` and let `U` be an open of `S`
> whose underlying set is the complement of `s` — so `s` is a closed point of `S` — with
> quasi-compact inclusion morphism.  Then for every affine open neighbourhood `W₀` of `s` the
> comparison functor
> `FP_S ⥤ FP_U ×_{FP_V} FP_{Spec 𝒪_{S, s}}`
> is an equivalence, where `FP_T` is the category of algebraic spaces of finite presentation over
> `T` and `V` is the vertex of the system of overlaps, whose underlying scheme is the complement of
> the closed point of `Spec 𝒪_{S, s}` — the tag's `V` —
> by `AlgebraicGeometry.toScheme_obj_opensSpecStalkSiteObj_eq_compl_closedPoint`.
>
> Every input is unconditional.  The two cartesian squares are
> `AlgebraicGeometry.isPullback_opensSpecStalkApex` and
> `AlgebraicGeometry.isPullback_opensSpecStalkStage`; the four compatibilities hold by terminality;
> the colimit identification over the neighbourhoods is
> `FinitePresentationSpacesOver.isFinitePresentationColimit_restrictedSpecStalkSiteCone`,
> which has no hypothesis, and the one over the overlaps is
> `AlgebraicGeometry.FinitePresentationSpacesOver.isFinitePresentationColimit_opensSpecStalkSiteCone`,
> whose single hypothesis is retrocompactness of `U` — the form the tag's quasi-compactness of
> `U → S` takes, by `AlgebraicGeometry.isRetrocompact_of_quasiCompact_ι`.  Quasi-compactness of
> `U → S` is used in that one place, exactly as in the tag's proof.

```lean
theorem isEquivalence_glueingFunctor_specStalk (hUc : (U : Set S) = {s}ᶜ)
    (hqc : QuasiCompact U.ι) :
    (glueingFunctor B S hS (isPullback_opensSpecStalkApex B S hS s W₀ U).w).IsEquivalence
```

## Tag 0E91, a lemma

[Tag 0E91](https://stacks.math.columbia.edu/tag/0E91) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationSpacesOver.isGlueingColimitEquivalence_of_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationLocalRingGlueing.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationLocalRingGlueing.lean#L591). The attribute's comment: “the equivalence out of the filtered 2-colimit, in the concrete form: the comparison functors out of the stages are jointly essentially surjective, full and faithful. The 2-colimit category itself is not constructed. The theorem is stated for an arbitrary object `M` of the site equipped with a cofiltered system of opens `W i` under it, an object `N` over the system of the `Wn i`, and a system of stages `Z i` covered by `U` and `W i`, such that base change exhibits `FP_M` as the cofiltered 2-colimit of the `FP_{W i}` and `FP_N` as that of the `FP_{Wn i}` — the hypotheses `hloc` and `hoverlap`. For `M = Spec O_{S,s}`, `W i` the affine open neighbourhoods of `s`, `Wn i = W i ∩ U` and `Z i = U ∪ W i` these two are what Stacks 07SK gives once the `W i` are known to have `Spec O_{S,s}` as their limit and the `Wn i` to have `V = Spec O_{S,s} ∩ U` as theirs — the `Wn i` being quasi-compact because `U` is retrocompact in `S`. Neither limit identification is available in this library, which is why the two colimit statements are carried as hypotheses rather than proved; `hstage` is Stacks 0E8Z at the stage `Z i`, which this library proves only for a base that is terminal in the site”.

> **The algebraic spaces of finite presentation over the opens between `U` and `S` containing
> the point `s` have the `2`-fibre product `FP_U ×_{FP_V} FP_{Spec 𝒪_{S,s}}` as their filtered
> `2`-colimit**, when `M` is a cofiltered limit of the stages `W i` and `N` the corresponding
> limit of the `Wn i = U ∩ W i`, and the stages `Z i = U ∪ W i` are covered by `U` and `W i`.
>
> This is Stacks 0E91. What the theorem proves is the formal combination: the comparison functors
> `FP_{Z i} ⥤ FP_U ×_{FP_N} FP_M` are jointly essentially surjective, full and faithful in the
> sense of an equivalence out of a filtered `2`-colimit, which is the content of
> `AlgebraicGeometry.FinitePresentationSpacesOver.IsGlueingColimitEquivalence`.

```lean
theorem isGlueingColimitEquivalence_of_colimit :
    IsGlueingColimitEquivalence B S hS Z jU jM
      (glueingSquare B S hS hsqW hjMW hpNU hpNW) hjUZ
      (glueingCone B S hS hjWZ hjMW hpM)
```

**`AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_specStalkStageColimitFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationLocalRingGlueingRealised.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationLocalRingGlueingRealised.lean#L259). The attribute's comment: “the equivalence of categories out of the filtered 2-colimit. The colimit of the categories `FP_{U ∪ W}` is the category `StageColimit` — objects the spaces over a stage, morphisms the germs — and the comparison functor `specStalkStageColimitFunctor` out of it to `FP_U ×_{FP_V} FP_{Spec O_{S,s}}` is full, faithful and essentially surjective, which is the fifth clause. The colimit runs over the stages `U ∪ W`, `W` an affine open neighbourhood of `s` inside a fixed one; the first two clauses say these are a cofinal family among the tag's opens `U'` with `U ⊆ U'` and `s ∈ U'`, so the colimit is the tag's. The third and fourth clauses pin the other two vertices: `Spec O_{S,s}`, and `V` as the preimage of `U` in it. The sole hypothesis is the tag's, that `U` is retrocompact in `S`; the tag's `s ∉ U` is unused, so the statement covers it”.

> Let `S` be a scheme, `U` a retrocompact open of `S` and `s` a point of `S`, and put
> `V = Spec 𝒪_{S, s} ∩ U`. Then the comparison functor
> `colim_{s ∈ U' ⊇ U open} FP_{U'} ⟶ FP_U ×_{FP_V} FP_{Spec 𝒪_{S, s}}`
> is an equivalence of categories.
>
> The colimit is the category `StageColimit` over the stages `U ∪ W`, `W` running over the affine
> open neighbourhoods of `s` contained in `W₀`. The first two clauses say that the stages are
> cofinal among the opens `U'` of `S` with `U ⊆ U'` and `s ∈ U'`; the third and fourth identify
> the remaining vertices of the `2`-fibre product as `Spec 𝒪_{S, s}` and as `V`, the preimage of
> `U` in `Spec 𝒪_{S, s}`; the fifth is the equivalence.

```lean
theorem isEquivalence_specStalkStageColimitFunctor (hU : IsRetrocompact (U : Set S)) :
    (∀ j : Over W₀, U ≤ U ⊔ j.left.obj.1 ∧ s ∈ U ⊔ j.left.obj.1) ∧
      (∀ U' : S.Opens, U ≤ U' → s ∈ U' → ∃ j : Over W₀, U ⊔ j.left.obj.1 ≤ U') ∧
        (BigFppfOver.toScheme B S hS).obj (restrictedSpecStalkSiteCone B S hS s W₀).pt =
            Spec (S.presheaf.stalk s) ∧
          (BigFppfOver.toScheme B S hS).obj (opensSpecStalkSiteObj B S hS s W₀ U) =
              (S.fromSpecStalk s ⁻¹ᵁ U).toScheme ∧
            (specStalkStageColimitFunctor B S hS s W₀ U).IsEquivalence
```

## Tag 0E92, a lemma

[Tag 0E92](https://stacks.math.columbia.edu/tag/0E92) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationSpacesOver.ClosedPointsGlueingData.essSurj_comparisonFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedPointsGlueing.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedPointsGlueing.lean#L526). The attribute's comment: “the comparison functor, and its essential surjectivity granted the case n = 1 of the lemma — that is, Stacks 0E90 — at each step of a tower of intermediate bases, carried as the hypothesis `Solvable`. The target is the iso-comma category of the two functors into `∀ i, FP_{Uᵢ}` assembled from the base changes, which is the 2-fibre product the lemma names. Full faithfulness, and hence that the functor is an equivalence, is NOT proved: the proof of Stacks 0E92 omits it”.

> **Stacks 0E92, essential surjectivity of the comparison functor, granted the case `n = 1`.**
> Every object of the `n`-fold `2`-fibre product — an algebraic space of finite presentation over
> the open part, a family of such over the local parts, and a family of identifications over the
> overlaps — is, up to isomorphism, the image of an algebraic space of finite presentation over
> the base, as soon as the glueing data admits a tower of splittings whose binary comparison
> functors are essentially surjective. The induction splits off the last point by one such
> comparison functor and applies the induction hypothesis to the remaining points.

```lean
theorem essSurj_comparisonFunctor :
    ∀ (n : ℕ) (D : ClosedPointsGlueingData B S hS n), Solvable n D →
      D.comparisonFunctor.EssSurj
```

**`AlgebraicGeometry.FinitePresentationSpacesOver.isEquivalence_comparisonFunctor_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedPointsGlueingEquivalence.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationClosedPointsGlueingEquivalence.lean#L463).

> **Stacks 0E92.** Let `S` be a scheme of a big fppf site and let `s₁, …, sₙ` be pairwise
> distinct closed points of `S` such that `U = S ∖ {s₁, …, sₙ} ⟶ S` is quasi-compact. With
> `Sᵢ = Spec 𝒪_{S,sᵢ}` and `Uᵢ = Sᵢ ∖ {sᵢ}`, the comparison functor
> `FP_S ⥤ FP_U ×_{(FP_{U₁} × ⋯ × FP_{Uₙ})} (FP_{S₁} × ⋯ × FP_{Sₙ})`,
> taking an algebraic space of finite presentation over `S` to its base change to `U`, the family
> of its base changes to the `Sᵢ` and the family of the canonical identifications of their base
> changes to the `Uᵢ`, is an equivalence of categories. Here `FP_T` is the category of algebraic
> spaces of finite presentation over `T`, and the `2`-fibre product is the iso-comma category of
> the two functors into `∀ i, FP_{Uᵢ}` assembled from the base changes.

```lean
theorem isEquivalence_comparisonFunctor_closedPoints {n : ℕ} (s : Fin n → S)
    (hinj : Function.Injective s) (hs : ∀ i, IsClosed ({s i} : Set S)) (U : S.Opens)
    (hU : (U : Set S) = (Set.range s)ᶜ) (hqc : QuasiCompact U.ι) :
    (closedPointsGlueingData B S hS s hs U hU).comparisonFunctor.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.18, Tag 0E8Y](https://stacks.math.columbia.edu/tag/0E8Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
