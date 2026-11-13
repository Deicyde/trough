---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsStandardCovering.isAffine_sigmaObj, AlgebraicGeometry.IsStandardCovering.isAffine_left_sigmaObj, AlgebraicGeometry.IsStandardCovering.isIso_cechComplexMap_coproductRefinement_bigSite, AlgebraicGeometry.IsStandardCovering.singleton_sigmaDesc_mem_fpqcPrecoverage, AlgebraicGeometry.IsStandardCovering.singleton_sigmaDesc_mem_precoverage, AlgebraicGeometry.isIso_cechComplexMap_coproductRefinement_smallEtale, CategoryTheory.PreZeroHypercover.nonempty_hom_singleton_sigmaDesc, AlgebraicGeometry.SpecIntCovering.isEmpty_hom_singleton_sigmaDesc
statement: formalized
proof: formalized
---

# 59.22 Cohomology of quasi-coherent sheaves

Section 59.22 of the Stacks Project, [Tag 03OY](https://stacks.math.columbia.edu/tag/03OY). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03OZ, a lemma

[Tag 03OZ](https://stacks.math.columbia.edu/tag/03OZ) in the Stacks Project.

**`AlgebraicGeometry.IsStandardCovering.isAffine_sigmaObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L330). The attribute's comment: “part (1)”.

> The disjoint union of the members of a standard `τ`-covering is an affine scheme: the index
> type is finite and every member is affine.

```lean
theorem IsStandardCovering.isAffine_sigmaObj (τ : CoveringTopology) {T : Scheme.{u}}
    [IsAffine T] {I : Type w} (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T)
    (h : IsStandardCovering τ U f) :
    letI : Finite I := h.finite_index
    IsAffine (∐ U)
```

**`AlgebraicGeometry.IsStandardCovering.isAffine_left_sigmaObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L343). The attribute's comment: “part (1), big site”.

> The scheme underlying the disjoint union, in the big site over `S`, of the members of a
> family whose underlying morphisms form a standard `τ`-covering is affine. The disjoint union is
> computed on underlying schemes, since the forgetful functor to schemes preserves it.

```lean
theorem IsStandardCovering.isAffine_left_sigmaObj (τ : CoveringTopology) (S : Scheme.{u})
    {T : Over S} [IsAffine T.left] (E : PreZeroHypercover.{w} T)
    (h : IsStandardCovering τ (fun i ↦ (E.X i).left) (fun i ↦ (E.f i).left)) :
    letI : Finite E.I₀ := h.finite_index
    IsAffine (∐ E.X).left
```

**`AlgebraicGeometry.IsStandardCovering.isIso_cechComplexMap_coproductRefinement_bigSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L376). The attribute's comment: “part (3), big τ-site”.

> For an abelian sheaf on the big `τ`-site over `S` and a standard `τ`-covering of an affine
> object of that site, the canonical refinement of the covering by the morphism from the disjoint
> union of its members induces an isomorphism of Čech complexes.

```lean
theorem IsStandardCovering.isIso_cechComplexMap_coproductRefinement_bigSite
    (τ : CoveringTopology) (S : Scheme.{u}) {T : Over S} [IsAffine T.left]
    (E : PreZeroHypercover.{w} T)
    (h : IsStandardCovering τ (fun i ↦ (E.X i).left) (fun i ↦ (E.f i).left))
    (F : (Over S)ᵒᵖ ⥤ Ab.{v})
    (hF : Presheaf.IsSheaf
      ((Scheme.grothendieckTopology (coveringMorphismProperty τ)).over S) F) :
    letI : Finite E.I₀ := h.finite_index
    IsIso (Stacks.CechSite.cechComplexMap E
      (PreZeroHypercover.singleton.{w} (Sigma.desc E.f))
      (Stacks.CechSite.coproductRefinement E) (F ⋙ AddCommGrpCat.uliftFunctor.{w, v}))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsStandardCovering.singleton_sigmaDesc_mem_fpqcPrecoverage`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L394) (StacksFrontier): “part (2), fpqc covering”.
- [`AlgebraicGeometry.IsStandardCovering.singleton_sigmaDesc_mem_precoverage`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L159), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L396) (StacksFrontier): “part (2), covering for τ other than Zariski”.
- [`AlgebraicGeometry.isIso_cechComplexMap_coproductRefinement_smallEtale`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L297), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringDisjointUnion.lean#L398) (StacksFrontier): “part (3), small étale site”.

## Tag 03P0, a remark

[Tag 03P0](https://stacks.math.columbia.edu/tag/03P0) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.nonempty_hom_singleton_sigmaDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean#L68). The attribute's comment: “the covering `𝒰` is a refinement of `𝒱 = {∐ Uᵢ ⟶ U}`, the direction of Stacks 03FI (2) that does hold”.

> A family of morphisms with fixed target whose members have a coproduct is a **refinement of
> the one-member family** given by the morphism from that coproduct.

```lean
theorem nonempty_hom_singleton_sigmaDesc {C : Type u} [Category.{v} C] {T : C}
    (E : PreZeroHypercover.{w} T) [HasCoproduct E.X] :
    Nonempty (E.Hom (singleton.{w} (Sigma.desc E.f)))
```

**`AlgebraicGeometry.SpecIntCovering.isEmpty_hom_singleton_sigmaDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean#L184). The attribute's comment: “`𝒱 = {∐ Uᵢ ⟶ U}` is not a refinement of `𝒰`, witnessed by the standard Zariski covering of `Spec ℤ` by the basic opens of `2` and of `3`”.

> **The one-member family given by the disjoint union of a covering need not refine it**: for
> the covering of `Spec ℤ` by the basic opens of `2` and of `3`, the one-member family given by
> the morphism from the disjoint union of its members is not a refinement of it.

```lean
theorem isEmpty_hom_singleton_sigmaDesc :
    IsEmpty ((PreZeroHypercover.singleton.{w} (Sigma.desc covering.{u, w}.f)).Hom
      covering.{u, w})
```

**`AlgebraicGeometry.SpecIntCovering.isEmpty_hom_singleton_of_mem_precoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean#L194). The attribute's comment: “no covering of the form `{V ⟶ U}` is a refinement of `𝒰`, witnessed by the standard Zariski covering of `Spec ℤ` by the basic opens of `2` and of `3`”.

> **No one-member covering of `Spec ℤ` refines the covering by the basic opens of `2` and of
> `3`**, for any topology whose coverings are jointly surjective families of morphisms with a
> given property.

```lean
theorem isEmpty_hom_singleton_of_mem_precoverage {P : MorphismProperty Scheme.{u}}
    {V : Scheme.{u}} (g : V ⟶ target.{u})
    (hg : Presieve.singleton g ∈ Scheme.precoverage P target.{u}) :
    IsEmpty ((PreZeroHypercover.singleton.{w} g).Hom covering.{u, w})
```

**`AlgebraicGeometry.SpecIntCovering.not_initial_isSingletonCovering_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean#L233). The attribute's comment: “coverings of the form `{V ⟶ U}` are not an initial subcategory of the category of all coverings of `U`, witnessed by the standard Zariski covering of `Spec ℤ` by the basic opens of `2` and of `3`; the remark's further assertion that Čech cohomology can nonetheless be computed from the coverings `{V ⟶ U}` is not proved, the source leaving it unformulated”.

> **The one-member coverings of an object do not form an initial subcategory of its category
> of coverings**: for the covering of `Spec ℤ` by the basic opens of `2` and of `3` there is no
> one-member covering mapping to it.

```lean
theorem not_initial_isSingletonCovering_inclusion (P : MorphismProperty Scheme.{u})
    (hP : (@IsOpenImmersion : MorphismProperty Scheme.{u}) ≤ P) :
    ¬ (isSingletonCovering.{u, w} (Scheme.precoverage P) target.{u}).ι.Initial
```

**`Stacks.CechSite.cechCohomologyOfObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean#L157). The attribute's comment: “`Ȟⁿ(U, ℱ)`, defined as the colimit over the opposite of the category of coverings `𝒰` of `U` of the Čech cohomology groups of `ℱ` with respect to `𝒰`”.

> **Stacks 03P0: Čech cohomology of an object.** The colimit, over the opposite of the category
> of all coverings of `U`, of the Čech cohomology groups of `ℱ` with respect to each covering.

```lean
def cechCohomologyOfObject (F : Cᵒᵖ ⥤ A) (n : ℕ)
    [HasColimit (cechCohomologyCoveringFunctor.{w} J U F n)] : A
```

**`Stacks.CechSite.isColimitWhiskerSingletonCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean#L224). The attribute's comment: “Čech cohomology `Ȟⁿ(U, ℱ)`, the colimit over all coverings of `U`, can still be computed in terms of the coverings `{V ⟶ U}`: the universal cocone restricted to the one-member coverings is again a colimit cocone, for a coefficient presheaf turning arbitrary coproducts into products, which is the source's "it only works for sheaves"”.

> **Stacks 03P0, the assertion the source leaves unformulated: Čech cohomology of a sheaf is
> computed from the one-member coverings.** For an additive presheaf `ℱ` turning `w`-indexed
> coproducts into products, on a category whose `w`-indexed coproducts are universal, the cocone
> on the diagram of Čech cohomology groups restricted to the opposite of the full subcategory of
> *one-member* coverings `{V ⟶ U}`, obtained by restricting the universal cocone on all coverings,
> is still a colimit cocone. That is: `Ȟⁿ(U, ℱ)` is the colimit over the one-member coverings
> alone — even though, as the standard Zariski covering of `Spec ℤ` by the basic opens of `2` and
> of `3` witnesses, those coverings are not an initial subcategory of all coverings of `U`.
>
> The hypotheses are the source's own. `huniv` is the infinitary extensivity of the site, the
> disjointness of the coproducts that the proof of Stacks 03OZ invokes; and
> `PreservesLimitsOfShape (Discrete I) ℱ` is the sheaf condition for the covering of a coproduct by
> its summands, the equality Stacks 03OZ (3) rests on, which the paragraph before the remark
> observes to be "false for a general presheaf". Together they are what the remark means by "it
> only works for sheaves".
>
> Because the cocone whose legs are tested is the universal cocone on *all* coverings, the
> statement contains its own canonicity: the comparison is the restriction of the identity.

```lean
def isColimitWhiskerSingletonCovering
    (huniv : ∀ {I : Type w} {D : Discrete I ⥤ C} {d : Cocone D},
      IsColimit d → IsUniversalColimit d)
    (F : Cᵒᵖ ⥤ A) [∀ I : Type w, PreservesLimitsOfShape (Discrete I) F] (n : ℕ)
    [HasColimit (cechCohomologyCoveringFunctor.{w} J U F n)] :
    IsColimit ((colimit.cocone (cechCohomologyCoveringFunctor.{w} J U F n)).whisker
      (singletonCoveringInclusion.{w} J U).op)
```

**`Stacks.CechSite.ι_cechCohomologyOfObjectIsoColimitSingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/CechCohomologyOfAnObject.lean#L270). The attribute's comment: “the computation of `Ȟⁿ(U, ℱ)` from the coverings `{V ⟶ U}` is the canonical comparison: it restricts on each one-member covering to the leg of the colimit over all coverings”.

> **Stacks 03P0.** The comparison of
> `Stacks.CechSite.cechCohomologyOfObjectIsoColimitSingleton` is the canonical one: on each
> one-member covering `{V ⟶ U}` it is the leg, at that covering, of the colimit over all
> coverings.

```lean
theorem ι_cechCohomologyOfObjectIsoColimitSingleton
    (huniv : ∀ {I : Type w} {D : Discrete I ⥤ C} {d : Cocone D},
      IsColimit d → IsUniversalColimit d)
    (F : Cᵒᵖ ⥤ A) [∀ I : Type w, PreservesLimitsOfShape (Discrete I) F] (n : ℕ)
    [HasColimit (cechCohomologyCoveringFunctor.{w} J U F n)]
    [HasColimit ((singletonCoveringInclusion.{w} J U).op ⋙
      cechCohomologyCoveringFunctor.{w} J U F n)]
    (V : (SingletonCovering J U)ᵒᵖ) :
    colimit.ι ((singletonCoveringInclusion.{w} J U).op ⋙
          cechCohomologyCoveringFunctor.{w} J U F n) V ≫
        (cechCohomologyOfObjectIsoColimitSingleton.{w} J U huniv F n).hom =
      colimit.ι (cechCohomologyCoveringFunctor.{w} J U F n)
        ((singletonCoveringInclusion.{w} J U).op.obj V)
```

## Tag 03P1, a lemma

[Tag 03P1](https://stacks.math.columbia.edu/tag/03P1) in the Stacks Project.

**`Stacks.CechComparison.exists_cover_restriction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/Locality.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/Locality.lean#L76).

> **Stacks Project, Tag 03P1.** Cohomology is local: for an abelian sheaf `F` on a site `C`,
> an object `U`, a degree `p > 0` and a class `ξ ∈ H^p(U, F)`, there is a covering
> `{U_i → U}` of `U` such that `ξ|_{U_i} = 0` for every member `i` of the covering.
>
> Here `H^p(U, F)` is `CategoryTheory.Sheaf.H' F p U`, the value over `U` of the cohomology
> presheaf of `F`, and the restriction maps are the functoriality of that presheaf.

```lean
theorem exists_cover_restriction_eq_zero (F : Sheaf J AddCommGrpCat.{u}) (p : ℕ) (hp : 0 < p)
    (U : C) (ξ : Sheaf.H' F p U) :
    ∃ S : J.Cover U, ∀ g : S.Arrow, (F.cohomologyPresheaf p).map g.f.op ξ = 0
```

## Tag 03P2, a theorem

[Tag 03P2](https://stacks.math.columbia.edu/tag/03P2) in the Stacks Project.

**`AlgebraicGeometry.bigOverQuasiCoherentGlobalCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/BigSiteQuasiCoherentCohomology.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/BigSiteQuasiCoherentCohomology.lean#L226). The attribute's comment: “the case 𝒞 = (Sch/S)\_τ: τ is a bound variable, so this one declaration covers all five of fppf, syntomic, smooth, étale and Zariski. The object the right-hand side is taken over, (opensBelowToOver hS).obj ⊤, is a final object of the site, so that side is τ-cohomology of S itself. The case 𝒞 = S\_étale is smallEtaleQuasiCoherentGlobalCohomologyIso”.

> **Zariski cohomology of a quasi-coherent module agrees with its big `τ`-site cohomology**:
> for a quasi-coherent module `F` on a scheme `S` and a degree `p`,
>
>   `H^p(S, ℱ) ≅ H^p_τ(S, Fᵃ)`.
>
> This is `AlgebraicGeometry.bigOverQuasiCoherentCohomologyIso` at the whole scheme.  The object it
> is taken over on the right, `(opensBelowToOver hS).obj ⊤`, is a final object of the big site by
> `AlgebraicGeometry.isTerminal_opensBelowToOver_top`, so the right-hand side is `τ`-cohomology of
> `S` itself.
>
> **This is [Stacks, Tag 03P2] in the case `𝒞 = (Sch/S)_τ`**, for all five `τ` at once.  Together
> with `AlgebraicGeometry.smallEtaleQuasiCoherentGlobalCohomologyIso`, which is the case
> `𝒞 = S_étale`, it is the covering set of the tag: the source lets `𝒞` be either of the two, and
> these are one declaration per case.

```lean
public def bigOverQuasiCoherentGlobalCohomologyIso (p : ℕ) :
    Sheaf.H' ((SheafOfModules.toSheaf S.ringCatSheaf).obj F) p ⊤ ≅
      Sheaf.H' (bigOverAssociatedSheaf S F τ B hS) p
        ((opensBelowToOver (κ := cutoff τ B) hS).obj ⊤)
```

**`AlgebraicGeometry.smallEtaleQuasiCoherentGlobalCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/SmallEtaleQuasiCoherentCohomology.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/SmallEtaleQuasiCoherentCohomology.lean#L89). The attribute's comment: “the case 𝒞 = S\_étale. The object the right-hand side is taken over, (opensToEtale S).obj ⊤, is a final object of the small étale site, so that side is étale cohomology of S itself. The case 𝒞 = (Sch/S)\_τ, for all five τ at once, is bigOverQuasiCoherentGlobalCohomologyIso”. References: SGA 4 VII (4.3).

> For a quasi-coherent module `F` on a scheme `S` and a degree `p`, Zariski cohomology of `F`
> agrees with small étale cohomology of its associated module:
>
>   `H^p(S, ℱ) ≅ H^p(S_étale, Fᵃ)`.
>
> The right-hand side is taken over `(opensToEtale S).obj ⊤`, a final object of the small étale
> site, so it is étale cohomology of `S` itself.

```lean
public def smallEtaleQuasiCoherentGlobalCohomologyIso (p : ℕ) :
    Sheaf.H' ((SheafOfModules.toSheaf S.ringCatSheaf).obj F) p ⊤ ≅
      Sheaf.H' (smallEtaleAssociatedSheaf S F) p ((opensToEtale S).obj ⊤)
```

## Tag 03P3, a remark

[Tag 03P3](https://stacks.math.columbia.edu/tag/03P3) in the Stacks Project.

**`AlgebraicGeometry.bigOverQuasiCoherentCohomologyIsoAtObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean#L374). The attribute's comment: “second assertion, the case 𝒞 = (Sch/S)\_τ: H^p(U, f^*F) = H^p\_τ(U, Fᵃ) at an ARBITRARY object Z of the site, final or not. τ is a bound variable, so this one declaration covers all five of fppf, syntomic, smooth, étale and Zariski. Nothing is assumed: the sheaf condition of Tag 03OG is already carried by bigOverAssociatedSheaf, and Tag 03P2 is not invoked either — the collapse its proof runs along opensBelowToOver is run here along opensBelowToOverAlong, which lands at the object Z. The case 𝒞 = S\_étale is smallEtaleQuasiCoherentCohomologyIsoAtObject”.

> **[Stacks, Tag 03P3], second assertion, for `𝒞 = (Sch/S)_τ`:** for **any** object `Z` of a
> localized big `τ`-site of `S`, with underlying scheme `U = Z.left.obj` and structure morphism
> `f = Z.hom.hom : U ⟶ S`,
>
>   `H^p(U, f^*F) ≅ H^p_τ(Z, Fᵃ)`,
>
> the left-hand side being the Zariski cohomology on `U` of the pullback module `f^*F` and the
> right-hand side the `τ`-cohomology of the associated module `Fᵃ` over the object `Z` of the
> site.
>
> This is `AlgebraicGeometry.bigOverQuasiCoherentCohomologyIsoAlong` at the whole of `U`, whose
> image is `Z` by `AlgebraicGeometry.objAtTopIso`.  Nothing is assumed: the source's own proof of
> Tag 03P2 is what is run, over `Z` instead of over `S`.

```lean
public def bigOverQuasiCoherentCohomologyIsoAtObject (p : ℕ) (Z : Over (base B S hS)) :
    Sheaf.H' ((SheafOfModules.toSheaf (Z.left.obj).ringCatSheaf).obj
        ((Scheme.Modules.pullback Z.hom.hom).obj F)) p (⊤ : (Z.left.obj).Opens) ≅
      Sheaf.H' (bigOverAssociatedSheaf S F τ B hS) p Z
```

**`AlgebraicGeometry.smallEtaleQuasiCoherentCohomologyIsoAtObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean#L550). The attribute's comment: “second assertion, the case 𝒞 = S\_étale: H^p(U, f^*F) = H^p(U, Fᵃ) at an ARBITRARY object Z of the small étale site of S, final or not. Nothing is assumed: the sheaf condition of Tag 03OG is already carried by smallEtaleAssociatedSheaf, and Tag 03P2 is not invoked either — the collapse its proof runs along opensToEtale is run here along opensToEtaleAlong, the composite of opensToEtale over U with composition along the étale structure morphism of Z, which lands at the object Z. The case 𝒞 = (Sch/S)\_τ is bigOverQuasiCoherentCohomologyIsoAtObject”.

> **[Stacks, Tag 03P3], second assertion, for `𝒞 = S_étale`:** for **any** object `Z` of the
> small étale site of `S`, with underlying scheme `U = Z.left` and étale structure morphism
> `f = Z.hom : U ⟶ S`,
>
>   `H^p(U, f^*F) ≅ H^p(Z, Fᵃ)`,
>
> the left-hand side being the Zariski cohomology on `U` of the pullback module `f^*F` and the
> right-hand side the cohomology of the associated module `Fᵃ` on the small étale site of `S`,
> taken over the object `Z` of that site.
>
> This is `AlgebraicGeometry.smallEtaleQuasiCoherentCohomologyIsoAlong` at the whole of `U`, whose
> image is `Z` by `AlgebraicGeometry.smallEtaleObjAtTopIso`.  Nothing is assumed: the source's own
> proof of Tag 03P2 is what is run, over `Z` instead of over `S`.

```lean
public def smallEtaleQuasiCoherentCohomologyIsoAtObject (p : ℕ) (Z : S.Etale) :
    Sheaf.H' ((SheafOfModules.toSheaf Z.left.ringCatSheaf).obj
        ((Scheme.Modules.pullback Z.hom).obj F)) p (⊤ : Z.left.Opens) ≅
      Sheaf.H' (smallEtaleAssociatedSheaf S F) p Z
```

**`AlgebraicGeometry.bigOverAssociatedSheafGlobalCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean#L573). The attribute's comment: “first assertion, the case 𝒞 = (Sch/S)\_τ: since S is final in 𝒞 the right-hand side of Tag 03P2 is derived global sections. The object is the very one bigOverQuasiCoherentGlobalCohomologyIso lands at, and it is final by isTerminal\_opensBelowToOver\_top; τ is a bound variable, so all five topologies are covered. The case 𝒞 = S\_étale is smallEtaleAssociatedSheafGlobalCohomologyIso”.

> **[Stacks, Tag 03P3], first assertion, for `𝒞 = (Sch/S)_τ`:** the scheme `S` is a final
> object of a localized big `τ`-site of `S`, so the groups `H^p_τ(S, Fᵃ)` on the right-hand side
> of [Stacks, Tag 03P2] are the right derived functors of the global sections functor of the site,
> that is Mathlib's global `CategoryTheory.Sheaf.H`.
>
> The object on the left is `(opensBelowToOver hS).obj ⊤`, which is exactly the object
> `AlgebraicGeometry.bigOverQuasiCoherentGlobalCohomologyIso` takes its right-hand side over, and
> it is final by `AlgebraicGeometry.isTerminal_opensBelowToOver_top`.

```lean
public def bigOverAssociatedSheafGlobalCohomologyIso (p : ℕ) :
    Sheaf.H' (bigOverAssociatedSheaf S F τ B hS) p
        ((opensBelowToOver (κ := cutoff τ B) hS).obj ⊤) ≅
      AddCommGrpCat.of (Sheaf.H.{u} (bigOverAssociatedSheaf S F τ B hS) p)
```

**`AlgebraicGeometry.smallEtaleAssociatedSheafGlobalCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/CohomologyAtAnObjectCollapse.lean#L599). The attribute's comment: “first assertion, the case 𝒞 = S\_étale: since S is final in S\_étale the right-hand side of Tag 03P2 is derived global sections. The object is the very one smallEtaleQuasiCoherentGlobalCohomologyIso lands at, and it is final by isTerminal\_opensToEtale\_top. The case 𝒞 = (Sch/S)\_τ is bigOverAssociatedSheafGlobalCohomologyIso”.

> **[Stacks, Tag 03P3], first assertion, for `𝒞 = S_étale`:** the scheme `S` is a final object
> of its small étale site, so the groups `H^p(S_étale, Fᵃ)` on the right-hand side of
> [Stacks, Tag 03P2] are the right derived functors of the global sections functor of the site.
>
> The object on the left is `(opensToEtale S).obj ⊤`, which is exactly the object
> `AlgebraicGeometry.smallEtaleQuasiCoherentGlobalCohomologyIso` takes its right-hand side over,
> and it is final by `AlgebraicGeometry.isTerminal_opensToEtale_top`.

```lean
public def smallEtaleAssociatedSheafGlobalCohomologyIso (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] (p : ℕ) :
    Sheaf.H' (smallEtaleAssociatedSheaf S F) p ((opensToEtale S).obj ⊤) ≅
      AddCommGrpCat.of (Sheaf.H.{u} (smallEtaleAssociatedSheaf S F) p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.22, Tag 03OY](https://stacks.math.columbia.edu/tag/03OY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
