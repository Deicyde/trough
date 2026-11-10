---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isQuasicoherentOnSite_etaleRestriction, AlgebraicGeometry.Space.isEquivalence_quasicoherentRestriction_unconditional, AlgebraicGeometry.Space.nonempty_inv_toSiteModules_iso_projectionModulePullback_unconditional, AlgebraicGeometry.Space.nonempty_projectionPullbackModules_comp_iso, AlgebraicGeometry.Stack.quotientStackModulePullback, AlgebraicGeometry.Stack.quotientPrestackQuasicoherentPullback, AlgebraicGeometry.Stack.quotientStackQuasicoherentEquivalence, AlgebraicGeometry.Stack.quasicoherentEquivalenceGroupoid
statement: formalized
proof: formalized
---

# 96.14 Quasi-coherent sheaves and presentations

Section 96.14 of the Stacks Project, [Tag 06WS](https://stacks.math.columbia.edu/tag/06WS). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GQC, a lemma

[Tag 0GQC](https://stacks.math.columbia.edu/tag/0GQC) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_etaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartRestrictionModuleIdentification.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartRestrictionModuleIdentification.lean#L672).

> Let `𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids representable by the algebraic
> space `U`, through a chosen equivalence over the site as in Stacks 073M. If `ℱ` is a locally
> quasi-coherent `𝒪_𝒳`-module (Stacks 06WJ) then its restriction `ℱ|_{U_étale}` (equation 075K) is
> quasi-coherent.
>
> The auxiliary big étale site is taken to be `AlgebraicGeometry.associatedBigEtaleSite` of the big
> fppf site, which the source does not name; that is the canonical choice, and it is the one
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_of_chartLocalModuleIdentification` already makes.

```lean
theorem isQuasicoherentOnSite_etaleRestriction
    (ℱ : inheritedEtaleModules B S hS p hp)
    (hℱ : Stack.IsLocallyQuasicoherent B (associatedBigEtaleSite B) rfl S hS p hp ℱ.val) :
    (etaleRestrictedModuleInverseImage B S hS p p hp hp e (𝟭 𝒳)
      (Functor.IsFibredOneMorphism.id p) ℱ).IsQuasicoherentOnSite
```

## Tag 0GQD, a lemma

[Tag 0GQD](https://stacks.math.columbia.edu/tag/0GQD) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isEquivalence_quasicoherentRestriction_unconditional`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartSliceCounitDescent.lean#L309), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L34) (StacksFrontier): “the equivalence clause, with no hypothesis beyond the source's, at the module universe `u` and for `𝒳 : Type (u + 1)` with `Category.{u} 𝒳`. `hres` is `AlgebraicGeometry.Space.restrictionPreservesQuasicoherent`, `hqcoh` is `AlgebraicGeometry.Space.projectionPullbackPreservesQuasicoherent`, `hunit` is `AlgebraicGeometry.Space.isIso_unit_moduleRestriction'`, and `hcounit` is `AlgebraicGeometry.Space.projectionPullbackCounitIsIso'`, the source's chart-slice argument over `AlgebraicGeometry.Space.chartSliceOpensAreCharts`. The pullback clause is registered separately on `AlgebraicGeometry.Space.nonempty_projectionPullbackModules_comp_iso`”.
- [`AlgebraicGeometry.Space.nonempty_inv_toSiteModules_iso_projectionModulePullback_unconditional`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartSliceCounitDescent.lean#L318), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L44) (StacksFrontier): “the quasi-inverse is the inverse image along the projection, with no hypothesis beyond the source's, at the module universe `u` and for `𝒳 : Type (u + 1)` with `Category.{u} 𝒳`”.
- [`AlgebraicGeometry.Space.nonempty_projectionPullbackModules_comp_iso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionPullbackClause.lean#L154), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L49) (StacksFrontier): “compatibility with pullback”.

## Tag 06WT, a proposition

[Tag 06WT](https://stacks.math.columbia.edu/tag/06WT) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackQuasicoherentModules.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackQuasicoherentModules.lean#L88). The attribute's comment: “the inverse image of modules along the canonical map from the object space, the first step of the forward functor”.

> The functor `ℱ ↦ x^*ℱ`, the inverse image of sheaves of modules of Stacks 06WE along the
> canonical projection `x : 𝒮_U ⟶ [U/R]` of Stacks 044R.

```lean
def quotientStackModulePullback (G : GroupoidInAlgebraicSpaces C S hS B) :
    SheafOfModules.{u + 1}
        (ringStructureSheafCore C S hS (quotientStack G).p
          (isFiberedInGroupoids_quotientStack G) C.topology le_rfl) ⥤
      SheafOfModules.{u + 1}
        (ringStructureSheafCore C S hS (fibredCategory C S hS G.objects.obj).val.p
          (fibredCategory C S hS G.objects.obj).property C.topology le_rfl)
```

**`AlgebraicGeometry.Stack.quotientPrestackQuasicoherentPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackQuasicoherentModules.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackQuasicoherentModules.lean#L104). The attribute's comment: “the restriction of quasi-coherent modules along the stackification map of the pointwise quotient”.

> The restriction of quasi-coherent modules along the stackification map `[U/_pR] ⟶ [U/R]`: the
> inverse image of modules of Stacks 06WE, which preserves quasi-coherence by Stacks 06WH.

```lean
def quotientPrestackQuasicoherentPullback (G : GroupoidInAlgebraicSpaces C S hS B) :
    FibredSite.quasicoherentModules.{u, u + 1, u + 1, u + 1} C S hS (quotientStack G).p
        (isFiberedInGroupoids_quotientStack G) ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u + 1, u + 1} C S hS (quotientPrestack G).p
        (isFiberedInGroupoids_quotientPrestack G)
```

**`AlgebraicGeometry.Stack.quotientStackQuasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuotientStackQuasicoherentEquivalence.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuotientStackQuasicoherentEquivalence.lean#L53).

> For a groupoid in algebraic spaces `(U, R, s, t, c)` over `S` with quotient stack `𝒳 = [U/R]`,
> the category of quasi-coherent `𝒪_𝒳`-modules is equivalent to the category of quasi-coherent
> modules on `(U, R, s, t, c)`, by `ℱ ↦ (x^*ℱ|_{U_étale}, α)`.

```lean
def quotientStackQuasicoherentEquivalence :
    FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} C S hS (quotientStack G).p
        (isFiberedInGroupoids_quotientStack G) ≌ Space.QuasicoherentModule C S hS G
```

**`AlgebraicGeometry.Stack.quasicoherentEquivalenceGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackQuasicoherentEquivalence.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackQuasicoherentEquivalence.lean#L83). The attribute's comment: “the equivalence QCoh(𝒪_{[U/R]}) ≌ QCoh(U, R, s, t, c), with functor ℱ ↦ (x^*ℱ|_{U_étale}, α)”.

> For a groupoid `(U, R, s, t, c)` in algebraic spaces, the category of quasi-coherent modules
> on the quotient stack `[U/R]` is equivalent to the category of quasi-coherent modules on
> `(U, R, s, t, c)`, by the functor `ℱ ↦ (x^*ℱ|_{U_étale}, α)` with `α` the transport of the
> canonical 2-morphism of Stacks 044S through the comparison maps of equation 076R.

```lean
def quasicoherentEquivalenceGroupoid (G : GroupoidInAlgebraicSpaces C S hS A) :
    FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} C S hS (quotientStack G).p
        (isFiberedInGroupoids_quotientStack G) ≌ Space.QuasicoherentModule C S hS G
```

## Tag 076S, a lemma

[Tag 076S](https://stacks.math.columbia.edu/tag/076S) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackObjectRestrictionMap_injective_and_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuotientStackHomRestriction.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuotientStackHomRestriction.lean#L415).

> **Stacks 076S.**  Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` whose source
> and target are flat and locally of finite presentation, let `𝒳 = [U/R]` be the quotient stack and
> `x` the object of `𝒳` over `U` (the canonical projection of Stacks 044R).  Let `ℱ` be a
> quasi-coherent `𝒪_𝒳`-module and `ℋ` any `𝒪_𝒳`-module.  Then the map
> `Hom_{𝒪_𝒳}(ℱ, ℋ) ⟶ Hom_{𝒪_U}(x^*ℱ|_{U_étale}, x^*ℋ|_{U_étale})`, `ψ ↦ x^*ψ|_{U_étale}`, is
> injective, and its image consists of exactly those `φ` which give rise to a commutative diagram
> of modules on `R_étale`: there is a morphism `χ : (x ∘ s)^*ℱ|_{R_étale} ⟶ (x ∘ s)^*ℋ|_{R_étale}`
> with `c_s(ℱ) ≫ χ = s_small^*φ ≫ c_s(ℋ)` and `c_t(ℱ) ≫ χ = t_small^*φ ≫ c_t(ℋ)`, where `c_s` and
> `c_t` are the comparison maps of equation 076R of the triangles through the source and through
> the target, the latter carried by the 2-morphism of Stacks 044S which identifies
> `(x ∘ t)^*ℱ|_{R_étale}` with `(x ∘ s)^*ℱ|_{R_étale}`.

```lean
theorem quotientStackObjectRestrictionMap_injective_and_range
    (_hsflat : Space.IsFlat C S hS G.source.hom) (_htflat : Space.IsFlat C S hS G.target.hom)
    (_hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (_htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom)
    (F : FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} C S hS (quotientStack G).p
      (isFiberedInGroupoids_quotientStack G))
    (H : QuotientStackModules G) :
    Function.Injective (fun ψ : F.obj ⟶ H => quotientStackObjectRestrictionMap G ψ) ∧
      ∀ φ : quotientStackObjectRestriction G F.obj ⟶ quotientStackObjectRestriction G H,
        (∃ ψ : F.obj ⟶ H, quotientStackObjectRestrictionMap G ψ = φ) ↔
          ∃ χ, quotientStackSourceComparison G F.obj ≫ χ =
              (Space.modulePullback C S hS G.source).map φ ≫ quotientStackSourceComparison G H ∧
            quotientStackTargetComparison G F.obj ≫ χ =
              (Space.modulePullback C S hS G.target).map φ ≫ quotientStackTargetComparison G H
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.14, Tag 06WS](https://stacks.math.columbia.edu/tag/06WS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
