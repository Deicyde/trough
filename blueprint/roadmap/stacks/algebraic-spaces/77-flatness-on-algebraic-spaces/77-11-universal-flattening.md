---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FlatnessSituation.HasUniversalFlattening, AlgebraicGeometry.Space.HasUniversalFlattening, AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnSomeChartDiagram_iff_hasTrdegLt, AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnEveryChartDiagram_iff_hasTrdegLt, AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnSomeChartDiagram_iff_onEveryChartDiagram, AlgebraicGeometry.Space.isFlatOverInDimensionsGE_modulePullback_of_hasTrdegLt, AlgebraicGeometry.Space.IsFlatOverInDimensionsGE, AlgebraicGeometry.Space.FlatDimensionSituation
statement: formalized
proof: formalized
---

# 77.11 Universal flattening

Section 77.11 of the Stacks Project, [Tag 0CWQ](https://stacks.math.columbia.edu/tag/0CWQ). 8 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CWR, a definition

[Tag 0CWR](https://stacks.math.columbia.edu/tag/0CWR) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatnessSituation.HasUniversalFlattening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlattening.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlattening.lean#L147). The attribute's comment: “the universal flattening of a module”.

> **Stacks 0CWR.** The universal flattening of `F` exists when the flatness condition of
> Stacks 0CWX is stable under base change and the functor `F_flat` it cuts out of `Y` is an
> algebraic space.

```lean
def HasUniversalFlattening (D : FlatnessSituation.{u} B S hS) : Prop
```

**`AlgebraicGeometry.Space.HasUniversalFlattening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlattening.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlattening.lean#L166). The attribute's comment: “the universal flattening of the space”.

> **Stacks 0CWR.** The universal flattening of an algebraic space `X` over `Y` exists when the
> universal flattening of its structure sheaf `𝒪_X` does.

```lean
def HasUniversalFlattening {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0CWS, a lemma

[Tag 0CWS](https://stacks.math.columbia.edu/tag/0CWS) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnSomeChartDiagram_iff_hasTrdegLt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean#L330). The attribute's comment: “the equivalence of conditions (1) and (3)”.

> **Stacks 0CWS, conditions (1) and (3).** Flatness in dimensions `≥ n` on some commuting
> square of surjective étale scheme charts is the bound `trdeg < n` at every point at which `F`
> is not flat over `Y`.

```lean
theorem isFlatOverInDimensionsGEOnSomeChartDiagram_iff_hasTrdegLt (n : ℕ) :
    IsFlatOverInDimensionsGEOnSomeChartDiagram B S hS Xs.2 f.hom F n ↔
      HasTrdegLtAtNonflatPoints B S hS Xs.2 f.hom F n
```

**`AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnEveryChartDiagram_iff_hasTrdegLt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean#L344). The attribute's comment: “the equivalence of conditions (2) and (3)”.

> **Stacks 0CWS, conditions (2) and (3).** Flatness in dimensions `≥ n` on every commuting
> square of étale scheme charts is the bound `trdeg < n` at every point at which `F` is not flat
> over `Y`.

```lean
theorem isFlatOverInDimensionsGEOnEveryChartDiagram_iff_hasTrdegLt (n : ℕ) :
    IsFlatOverInDimensionsGEOnEveryChartDiagram B S hS Xs.2 f.hom F n ↔
      HasTrdegLtAtNonflatPoints B S hS Xs.2 f.hom F n
```

**`AlgebraicGeometry.Space.isFlatOverInDimensionsGEOnSomeChartDiagram_iff_onEveryChartDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean#L357). The attribute's comment: “the equivalence of conditions (1) and (2)”.

> **Stacks 0CWS, conditions (1) and (2).** Flatness in dimensions `≥ n` can be tested on one
> commuting square of surjective étale scheme charts, and then holds on every commuting square of
> étale scheme charts.

```lean
theorem isFlatOverInDimensionsGEOnSomeChartDiagram_iff_onEveryChartDiagram (n : ℕ) :
    IsFlatOverInDimensionsGEOnSomeChartDiagram B S hS Xs.2 f.hom F n ↔
      IsFlatOverInDimensionsGEOnEveryChartDiagram B S hS Xs.2 f.hom F n
```

**`AlgebraicGeometry.Space.isFlatOverInDimensionsGE_modulePullback_of_hasTrdegLt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean#L548). The attribute's comment: “the base-change clause: if the transcendence degree over its image of every point at which the module is not flat over the target is < n -- condition (3) of the tag, written out -- then the inverse image of the module is flat over the new target in dimensions >= n”.

> **Stacks 0CWS, the base-change clause.** Let `f : X ⟶ Y` be locally of finite type, let `F`
> be quasi-coherent of finite type, and let the square be cartesian over a morphism `Y' ⟶ Y`.
> If the transcendence degree over its image of every point of `|X|` at which `F` is not flat
> over `Y` is less than `n`, then the inverse image `(g')^*F` of `F` on `X' = X ×_Y Y'` is flat
> over `Y'` in dimensions `≥ n`.
>
> The hypothesis is condition (3) of Stacks 0CWS written out: the flat locus is
> `AlgebraicGeometry.Space.flatLocus` of Stacks 0DLR and the transcendence degree is
> `AlgebraicGeometry.Space.HasTranscendenceDegreeAt` of Stacks 04NM, and by
> `AlgebraicGeometry.Space.isFlatOverInDimensionsGE_iff_hasTrdegLt` it is exactly flatness over
> `Y` in dimensions `≥ n` in the sense of Stacks 0CWT, which is what
> `AlgebraicGeometry.Space.isFlatOverInDimensionsGE_modulePullback_of_isPullback` below states it
> as.  Writing it out is what keeps the registered form of the clause free of the abbreviations
> introduced in this file, so that no hypothesis of it is read as standing in for an input.
>
> The clause is that condition on the two sides together with
> `AlgebraicGeometry.Space.hasTrdegLtAtNonflatPoints_modulePullback_of_isPullback`, which is where
> Stacks 05VW at a point enters.
>
> The hypotheses on `F` are the source's, read on the small étale site: quasi-coherence and finite
> type there, which the inverse image inherits by Stacks 03GA and by Stacks 03DO for the clause
> 03DL (5), `AlgebraicGeometry.Space.isFiniteTypeOnSite_modulePullback`.  The chartwise forms of
> the two, which the equivalence of Stacks 0CWS consumes, follow for both modules by
> `AlgebraicGeometry.Space.isQuasicoherentOnCharts_of_isQuasicoherentOnSite` and
> `AlgebraicGeometry.Space.isFiniteTypeOnCharts_of_isFiniteTypeOnSite`, so neither is assumed of
> the inverse image.

```lean
theorem isFlatOverInDimensionsGE_modulePullback_of_hasTrdegLt
    (hftS : SheafOfModules.IsFiniteTypeOnSite F) {g' : X' ⟶ Xs} {f' : X' ⟶ Y'}
    {g : Y' ⟶ Ys} (sq : IsPullback g'.hom f'.hom f.hom g.hom) (n : ℕ)
    (h : ∀ x : points B S hS Xs.1, x ∉ flatLocus B S hS Xs.2 f.hom F →
      ∃ r : ℕ∞, HasTranscendenceDegreeAt B S hS f.hom x r ∧ r < (n : ℕ∞)) :
    IsFlatOverInDimensionsGE B S hS f' ((modulePullback B S hS g').obj F) n
```

## Tag 0CWT, a definition

[Tag 0CWT](https://stacks.math.columbia.edu/tag/0CWT) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFlatOverInDimensionsGE`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleInDimensionsGE.lean#L370). The attribute's comment: “the definition, taken in the form of condition (2) of Stacks 0CWS; conditions (1) and (3) are interchangeable with it by `isFlatOverInDimensionsGEOnSomeChartDiagram_iff_onEveryChartDiagram` and `isFlatOverInDimensionsGEOnEveryChartDiagram_iff_hasTrdegLt`”.

> **Stacks 0CWT.** `F` is *flat over `Y` in dimensions `≥ n`*. The source defines this by the
> equivalent conditions of Stacks 0CWS; condition (2) is taken as the definition, and the three
> conditions are interchangeable by the theorems above.

```lean
abbrev IsFlatOverInDimensionsGE (n : ℕ) : Prop
```

## Tag 0CWU, a situation

[Tag 0CWU](https://stacks.math.columbia.edu/tag/0CWU) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatDimensionSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean#L144). The attribute's comment: “standing data”.

> **Situation 0CWU.** The standing data of Situation 0CWU: the flatness situation of
> Stacks 0CWX — a morphism `f : X ⟶ Y` of algebraic spaces over `S` and a quasi-coherent
> `𝒪_X`-module `F` — in which moreover `f` is locally of finite type and `F` is of finite type.

```lean
structure FlatDimensionSituation extends FlatnessSituation.{u} B S hS
```

**`AlgebraicGeometry.Space.FlatDimensionSituation.isLocallyOfFiniteType_baseChangeInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean#L165). The attribute's comment: “the base-changed morphism is locally of finite type; corrected from the source's "of finite type", which does not follow from its hypothesis that f is only locally of finite type”.

> **Situation 0CWU, the first observation.** The base change `f_T : X_T ⟶ T` of a locally
> finite type morphism to a test scheme is again locally of finite type. This is **Stacks 03XH**,
> stability of the property under base change, at the fibre product square defining `X_T`.
>
> The source says `f_T` is *of* finite type, which does not follow from its own hypotheses: `f` is
> assumed only locally of finite type, and base change preserves exactly that. The half of
> Stacks 03XH the source cites is the locally-of-finite-type one, and it is also what
> Definition 0CWT consumes, so the corrected statement is the one that is used.

```lean
theorem isLocallyOfFiniteType_baseChangeInclusion (D : FlatDimensionSituation.{u} B S hS)
    (T : SchemesOver D.Y) :
    IsLocallyOfFiniteType B S hS (baseChangeInclusion D.f T).hom
```

**`AlgebraicGeometry.Space.FlatDimensionSituation.isFiniteTypeOnSite_baseChangeModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean#L178). The attribute's comment: “the base-changed module is of finite type”.

> **Situation 0CWU, the second observation.** The base change `F_T` of a finite type module to
> a test scheme is again of finite type. This is **Stacks 03DO** for the inverse image of
> Stacks 03LU along the projection `X_T ⟶ X`.

```lean
theorem isFiniteTypeOnSite_baseChangeModule (D : FlatDimensionSituation.{u} B S hS)
    (T : SchemesOver D.Y) :
    SheafOfModules.IsFiniteTypeOnSite (D.toFlatnessSituation.baseChangeModule T)
```

**`AlgebraicGeometry.Space.FlatDimensionSituation.flatDimensionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctor.lean#L236). The attribute's comment: “the functor F_n of equation 0CWV”.

> **Equation 0CWV, the functor `F_n` of Situation 0CWU**: the functor on the test schemes
> over `Y` whose value at `T` is a one-point set when `F_T` is flat over `T` in dimensions `≥ n`,
> and is empty otherwise.
>
> That the condition is inherited along a morphism of test schemes, which is what makes the
> assignment a functor, is
> `AlgebraicGeometry.Space.FlatDimensionSituation.isFlatInDimensionsGEAfterBaseChange_of_hom`.

```lean
def flatDimensionFunctor (D : FlatDimensionSituation.{u} B S hS) (n : ℕ) :
    (SchemesOver D.Y)ᵒᵖ ⥤ Type u
```

## Tag 0CWW, a lemma

[Tag 0CWW](https://stacks.math.columbia.edu/tag/0CWW) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatDimensionSituation.flatDimensionFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorDescent.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorDescent.lean#L385). The attribute's comment: “clause (1): in Situation 0CWU the functor F_n of equation 0CWV is a sheaf for the fpqc topology on the test schemes over Y. Proved for every situation of the tag, from nothing but the data of Situation 0CWU: the functor is subterminal, so its sheaf property is fpqc locality of the condition of Stacks 0CWT on the base change, and that locality is the pointwise descent of condition (3) of Stacks 0CWS along the jointly surjective flat family a covering sieve contains”.

> **Stacks 0CWW, clause (1).** In Situation 0CWU the functor `F_n` of equation 0CWV satisfies
> the sheaf property for the fpqc topology on the test schemes over `Y`.
>
> `F_n` is subterminal, so its sheaf property is exactly fpqc locality of the condition of
> Stacks 0CWT on the base change, which is
> `isFlatInDimensionsGEAfterBaseChange_of_mem_fpqcTopology` of this namespace.

```lean
theorem flatDimensionFunctor_isSheaf_fpqc (D : FlatDimensionSituation.{u} B S hS) (n : ℕ) :
    Presheaf.IsSheaf (fpqcTopology D.Y) (D.flatDimensionFunctor n)
```

**`AlgebraicGeometry.Space.FlatDimensionSituation.flatDimensionFunctor_limitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorDescent.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorDescent.lean#L526). The attribute's comment: “clause (2), limit preservation of F_n”.

> **Stacks 0CWW, clause (2).** In Situation 0CWU, if `f` is quasi-compact and locally of
> finite presentation and `ℱ` is of finite presentation, then the functor `F_n` of equation 0CWV
> is limit preserving.
>
> The proof is the source's, with the chart presentation constructed rather than assumed.  Since
> `F_n` is subterminal, limit preservation is descent of the condition of Stacks 0CWT along a
> cofiltered inverse system of affine test schemes with affine limit
> (`limitPreserving_flatDimensionFunctor_iff`), so a system `T = lim T_i` of affine test schemes
> may be fixed first.  The presentation is then taken at one of its stages: for an index `i₀`, the
> base change `X_{T_{i₀}}` is quasi-compact over the affine scheme underlying `T_{i₀}`, hence has
> a surjective étale scheme chart `U` with affine scheme
> (`AlgebraicGeometry.Space.exists_isAffine_isSurjective_chart_baseChangeSpace`, Stacks 03H6), and
> `U ⟶ T_{i₀}` together with the restriction of `F_{T_{i₀}}` to `U` is a scheme-level situation
> `E` of Stacks 05MT (`AlgebraicGeometry.Space.FlatDimensionSituation.stageSituation`).  That is
> the chart presentation of the source read over a stage instead of over `Y`: because `T_{i₀}` is
> represented, the target chart of the presenting square is the identity chart, so no base change
> of a chart of `Y` and no affine open of one is needed, and the value of the presentation at a
> test scheme `T'` over `T_{i₀}` is `T'` itself.
>
> The identification of the two conditions at every test scheme over `T_{i₀}` is the theorem
> `isFlatInDimensionsGEAfterBaseChange_iff_stageSituation` of that same namespace,
> the chart clause of Stacks 0CWS at the square whose source chart is the base change of `U` and
> whose target chart is the identity chart.  The system `K` of affine schemes over the scheme
> underlying `T_{i₀}` is the given system restricted to the indices over `i₀`,
> `CategoryTheory.Over.post` of `T ↦ T` on `CategoryTheory.Over i₀`; its limit is the given one
> because `CategoryTheory.Over.forget i₀` is initial for a cofiltered index category.  Limit
> preservation of the scheme-level `F'_n` is part (2) of **Stacks 05MV**,
> `AlgebraicGeometry.FlatDimensionSituation.flatDimensionFunctor_limitPreserving`, applied to `E`
> and to `K`; the three hypotheses it asks of `E` are the hypotheses on `f` and `ℱ` read on the
> presentation, and are where they enter.
>
> The schemes live in the maximum of the two index universes of the tested inverse system and a
> third parameter.  That is the universe signature every limit-preservation statement in this
> library carries: Stacks 05MY and part (2) of Stacks 05MV both have it, and it is the signature
> at which the limit of a cofiltered system of affine schemes indexed by a category of those
> universes exists in the first place.  It is also the signature of the statement of
> Stacks 0CWW (limit preserving).

```lean
theorem flatDimensionFunctor_limitPreserving
    (D : FlatDimensionSituation.{max u w w'} B₁ S₁ hS₁) (n : ℕ)
    (hqc : IsQuasiCompact B₁ S₁ hS₁ D.f.hom)
    (hlfp : IsLocallyOfFinitePresentation B₁ S₁ hS₁ D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F) :
    LimitPreserving.{max u w w', max u w w', w, w'}
      (testSchemeFunctor D.Y) (D.flatDimensionFunctor n)
```

## Tag 0CX0, a lemma

[Tag 0CX0](https://stacks.math.columbia.edu/tag/0CX0) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatDimensionSituation.mono_etalePullbackComparison_and_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorEtale.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorEtale.lean#L411). The attribute's comment: “the full statement at the source's hypotheses, nothing granted or assumed: Situation 0CWU (f locally of finite type, F quasi-coherent of finite type) and h etale only. 'F_n is a subfunctor of F'_n' is that the canonical natural transformation F_n -> F'_n between these subterminal functors is a monomorphism, and 'F_n = F'_n' is that it is an isomorphism. Ass_{X/Y}(F) is the relative weak assassin of Stacks 0CV0, which the source writes Ass_{X/Y}(F) as the fibres of f are locally Noetherian, and h(X') is the image of |X'| -> |X|”.

> **Stacks 0CX0.** In Situation 0CWU, let `h : X' ⟶ X` be an étale morphism, set `F' = h^* F`
> and `f' = f ∘ h`, and let `F'_n` be the functor of equation 0CWV for `(f' : X' ⟶ Y, F')`. Then
> `F_n` is a subfunctor of `F'_n` — the canonical natural transformation `F_n ⟶ F'_n` is a
> monomorphism — and if `h(|X'|) ⊇ Ass_{X/Y}(F)` then `F_n = F'_n` — that monomorphism is an
> isomorphism.

```lean
theorem mono_etalePullbackComparison_and_isIso (n : ℕ) :
    Mono (D.etalePullbackComparison h hh n) ∧
      (relativeWeaklyAssociatedPoints B S hS D.f D.F ⊆
          Set.range (pointsMap B S hS X'.1 h.hom) →
        IsIso (D.etalePullbackComparison h hh n))
```

## Tag 0CX1, a theorem

[Tag 0CX1](https://stacks.math.columbia.edu/tag/0CX1) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatDimensionSituation.isAlgebraicSpace_flatDimensionSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorRepresentable.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatDimensionFunctorRepresentable.lean#L277). The attribute's comment: “the full statement under exactly the source's hypotheses, nothing granted or assumed: F_n is the subfunctor of Y of the maps T ⟶ Y along which F_T is flat in dimensions ≥ n (equation 0CWV); purity relative to Y is purity above every point of Y (Stacks 0CVD (5)); finite presentation of f is local finite presentation, quasi-compactness and quasi-separatedness (Stacks 03XP (3))”.

> **Stacks Project, Tag 0CX1.** In Situation 0CWU, assume moreover that `f` is of finite
> presentation, that `F` is an `𝒪_X`-module of finite presentation, and that `F` is pure relative
> to `Y`. Then `F_n` is an algebraic space and `F_n ⟶ Y` is a monomorphism of finite presentation.
>
> `F_n` is `AlgebraicGeometry.Space.FlatDimensionSituation.flatDimensionSubfunctor`, the functor of
> equation 0CWV read on the big fppf site of `S` as a subfunctor of `Y`. Purity of `F` relative to
> `Y` is purity above every point of `Y`, Stacks 0CVD part (5), for the situation of Stacks 0CV6
> which `f` and `F` determine; that situation is formed from the hypotheses of the theorem, since a
> morphism of finite presentation is of finite type and decent.

```lean
theorem isAlgebraicSpace_flatDimensionSubfunctor (n : ℕ)
    (hf : IsFinitePresentation B S hS D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F)
    (hpure : ∀ y, IsPureAbove (D.fpPrePureSituation hf y)) :
    IsAlgebraicSpace B S hS (D.flatDimensionSubfunctor n).toFunctor ∧
      Mono (D.flatDimensionSubfunctor n).ι ∧
      IsFinitePresentation B S hS (D.flatDimensionSubfunctor n).ι
```

## Tag 0CX2, a lemma

[Tag 0CX2](https://stacks.math.columbia.edu/tag/0CX2) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatnessSituation.hasUniversalFlattening_of_isPureAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean#L115). The attribute's comment: “part (1)”.

> **Stacks 0CX2, part (1).** Let `f : X ⟶ Y` be a morphism of algebraic spaces of finite
> presentation and let `F` be a quasi-coherent `𝒪_X`-module of finite presentation which is pure
> relative to `Y`, that is, pure above every point `y ∈ |Y|`. Then the universal flattening
> `Y' ⟶ Y` of `F` exists, and `Y' ⟶ Y` is a monomorphism of finite presentation.
>
> Here `Y'` is the subfunctor `F_flat` of `Y` and `Y' ⟶ Y` is its inclusion. This is Theorem 0CX1
> at `n = 0`, where `F_0 = F_flat`.

```lean
theorem hasUniversalFlattening_of_isPureAbove (D : FlatnessSituation.{u} B S hS)
    (hf : IsFinitePresentation B S hS D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F)
    (hpure : ∀ y : points B S hS D.Y.1,
      IsPureAbove ((D.toFlatDimensionSituation hf hF).fpPrePureSituation hf y)) :
    D.HasUniversalFlattening ∧ Mono (D.flatSubfunctor D.isFlatStableUnderBaseChange).ι ∧
      IsFinitePresentation B S hS (D.flatSubfunctor D.isFlatStableUnderBaseChange).ι
```

**`AlgebraicGeometry.Space.FlatnessSituation.hasUniversalFlattening_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean#L135). The attribute's comment: “part (3)”.

> **Stacks 0CX2, part (3).** Let `f : X ⟶ Y` be a proper morphism of algebraic spaces of finite
> presentation and let `F` be a quasi-coherent `𝒪_X`-module of finite presentation. Then the
> universal flattening `Y' ⟶ Y` of `F` exists, and `Y' ⟶ Y` is a monomorphism of finite
> presentation.
>
> Over a proper morphism `F` is universally pure above every point of `Y`, by Stacks 0CVI, part (2).
> So it is pure relative to `Y`, and part (1) applies.

```lean
theorem hasUniversalFlattening_of_isProper (D : FlatnessSituation.{u} B S hS)
    (hproper : IsProper B S hS D.f.hom) (hf : IsFinitePresentation B S hS D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F) :
    D.HasUniversalFlattening ∧ Mono (D.flatSubfunctor D.isFlatStableUnderBaseChange).ι ∧
      IsFinitePresentation B S hS (D.flatSubfunctor D.isFlatStableUnderBaseChange).ι
```

**`AlgebraicGeometry.Space.hasUniversalFlattening_of_isPureAbove_structure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean#L158). The attribute's comment: “part (2)”.

> **Stacks 0CX2, part (2).** Let `f : X ⟶ Y` be a morphism of algebraic spaces of finite
> presentation such that `X` is pure relative to `Y`, that is, `𝒪_X` is pure above every point
> `y ∈ |Y|`. Then the universal flattening `Y' ⟶ Y` of `X` exists, and `Y' ⟶ Y` is a monomorphism
> of finite presentation.
>
> This is part (1) for the module `𝒪_X`, which is of finite presentation.

```lean
theorem hasUniversalFlattening_of_isPureAbove_structure {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom)
    (hpure : ∀ y : points B S hS Y.1, IsPureAbove (structurePrePureSituation X.2 Y.2 f.hom
      (isFiniteType_of_isFinitePresentation B S hS hf)
      (isDecent_of_isFinitePresentation B S hS f hf) y)) :
    HasUniversalFlattening f ∧
      Mono ((structureSheafFlatnessSituation f).flatSubfunctor
        (structureSheafFlatnessSituation f).isFlatStableUnderBaseChange).ι ∧
      IsFinitePresentation B S hS ((structureSheafFlatnessSituation f).flatSubfunctor
        (structureSheafFlatnessSituation f).isFlatStableUnderBaseChange).ι
```

**`AlgebraicGeometry.Space.hasUniversalFlattening_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFlatteningExistence.lean#L176). The attribute's comment: “part (4)”.

> **Stacks 0CX2, part (4).** Let `f : X ⟶ Y` be a proper morphism of algebraic spaces of finite
> presentation. Then the universal flattening of `X` exists.
>
> This is part (3) for the module `𝒪_X`, which is of finite presentation.

```lean
theorem hasUniversalFlattening_of_isProper {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hproper : IsProper B S hS f.hom) (hf : IsFinitePresentation B S hS f.hom) :
    HasUniversalFlattening f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.11, Tag 0CWQ](https://stacks.math.columbia.edu/tag/0CWQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
