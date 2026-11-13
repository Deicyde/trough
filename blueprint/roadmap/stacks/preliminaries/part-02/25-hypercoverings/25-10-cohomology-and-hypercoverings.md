---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.homologyMap_hypercoverCochainNatFunctorMap_app_eq_of_isHomotopy, Stacks.CategoryTheory.Hypercovering.whiskerRight_hypercoverCochainNatFunctorMap_eq_of_isHomotopy, Stacks.CategoryTheory.Hypercovering.cechCohomologyHypercoveringsHomotopyFunctor, Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechCohomologyZeroCocone, Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechCoconeAtSheaf, Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechFunctorCocone, Stacks.CategoryTheory.Hypercovering.exists_hom_cechCohomologyEdge_eq, Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_cechCohomologyEdge_zero_eq
statement: formalized
proof: formalized
---

# 25.10 Cohomology and hypercoverings

Section 25.10 of the Stacks Project, [Tag 01GZ](https://stacks.math.columbia.edu/tag/01GZ). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01GZ, the section

[Tag 01GZ](https://stacks.math.columbia.edu/tag/01GZ) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.homologyMap_hypercoverCochainNatFunctorMap_app_eq_of_isHomotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean#L174). The attribute's comment: “homotopic maps of hypercoverings have the same effect on Čech cohomology”.

> **Stacks Project, Tag 01GZ.**  Homotopic maps of simplicial semi-representable objects over
> `X` have the same effect on the Čech cohomology of an abelian sheaf: by [Stacks, Tag 019Y] their
> images on the cosimplicial object of sections are homotopic, and by [Stacks, Tag 01A0] homotopic
> maps of cosimplicial objects induce the same map on the cohomology of the associated cochain
> complexes.

```lean
theorem homologyMap_hypercoverCochainNatFunctorMap_app_eq_of_isHomotopy
    {K K' : SimplicialObject (FormalCoproduct.{w} (Over X))}
    [∀ m, HasCoproduct fun _ : (Δ[1] : SSet.{t}).obj m ↦ K.obj m]
    {ψ ψ' : K ⟶ K'} {h : K.copower (Δ[1] : SSet.{t}) ⟶ K'}
    (hh : SimplicialObject.IsHomotopy h ψ ψ')
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) (p : ℕ) :
    HomologicalComplex.homologyMap
        ((hypercoverCochainNatFunctorMap.{w} J X ψ).app F) p =
      HomologicalComplex.homologyMap
        ((hypercoverCochainNatFunctorMap.{w} J X ψ').app F) p
```

**`Stacks.CategoryTheory.Hypercovering.whiskerRight_hypercoverCochainNatFunctorMap_eq_of_isHomotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean#L190). The attribute's comment: “the induced natural transformation on Ȟ^p depends only on the homotopy class”.

> **Stacks Project, Tag 01GZ**, as natural transformations.  The map `Ȟ^p(K', -) ⟶ Ȟ^p(K, -)`
> of Čech cohomology functors induced by a map `K ⟶ K'` depends only on its homotopy class.

```lean
theorem whiskerRight_hypercoverCochainNatFunctorMap_eq_of_isHomotopy
    {K K' : SimplicialObject (FormalCoproduct.{w} (Over X))}
    [∀ m, HasCoproduct fun _ : (Δ[1] : SSet.{t}).obj m ↦ K.obj m]
    {ψ ψ' : K ⟶ K'} {h : K.copower (Δ[1] : SSet.{t}) ⟶ K'}
    (hh : SimplicialObject.IsHomotopy h ψ ψ') (p : ℕ) :
    Functor.whiskerRight (hypercoverCochainNatFunctorMap.{w} J X ψ)
        (HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v w}
          (ComplexShape.up ℕ) p) =
      Functor.whiskerRight (hypercoverCochainNatFunctorMap.{w} J X ψ')
        (HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v w}
          (ComplexShape.up ℕ) p)
```

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyHypercoveringsHomotopyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyHomotopyInvariance.lean#L235). The attribute's comment: “Ȟ^p(-, 𝓕) as a diagram on HC(C, X)ᵒᵖ”.

> **Stacks Project, Tag 01GZ.**  `Ȟ^p(-, -) : HC(C, X)ᵒᵖ ⥤ (Ab(C) ⥤ Ab)`: the Čech cohomology
> of a hypercovering of `X`, as a diagram on the hypercoverings of `X` with maps up to homotopy.
>
> This is the diagram whose colimit [Stacks, Tag 01H0] compares with sheaf cohomology; it exists
> because homotopic maps have the same effect on Čech cohomology, which is
> `whiskerRight_hypercoverCochainNatFunctorMap_eq_of_isHomotopy`.

```lean
noncomputable def cechCohomologyHypercoveringsHomotopyFunctor (p : ℕ) :
    (HypercoveringsHomotopy.{w} J X)ᵒᵖ ⥤
      (Sheaf J.toGrothendieck AddCommGrpCat.{max u v w} ⥤
        AddCommGrpCat.{max u v w})
```

## Tag 01H0, a theorem

[Tag 01H0](https://stacks.math.columbia.edu/tag/01H0) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechCohomologyZeroCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean#L698). The attribute's comment: “the case i = 0: colim over hypercoverings of Ȟ⁰(K, H⁰(-)) is H⁰(X, -), as functors on Ab(C); the hypotheses carried are fibre products in C and stability of the pretopology under composition”.

> For a site with fibre products and an object `X`, the functor `𝓕 ↦ H⁰(X, 𝓕)` on abelian
> sheaves is the colimit over all hypercoverings `K` of `X` of the functors `𝓕 ↦ Ȟ⁰(K, H⁰(𝓕))`,
> the cocone being the canonical identification of each `Ȟ⁰(K, H⁰(-))` with `H⁰(X, -)`.

```lean
def isColimit_cechCohomologyZeroCocone
    [Precoverage.IsStableUnderComposition J.toPrecoverage] :
    IsColimit (cechCohomologyZeroCocone X J)
```

**`Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechCoconeAtSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean, line 1224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean#L1224). The attribute's comment: “the general case at a fixed abelian sheaf: colim over hypercoverings of Ȟ^i(K, 𝓕) is H^i(X, 𝓕); the index category is the hypercoverings of X themselves rather than the homotopy quotient HC(C, X), and the hypotheses carried are fibre products in C and stability of the pretopology under composition”. References: SGA 4 V (7.4.1), “Clause 2)”.

> For a site with fibre products, an object `X` and an abelian sheaf `𝓕`, the cohomology
> `H^n(X, 𝓕)` is the colimit over the hypercoverings of `X` of the Čech cohomology groups
> `Ȟ^n(K, 𝓕)`, the cocone being the canonical edge maps `hypercoveringCechEdge`. The index category
> is the category of hypercoverings itself, not the homotopy quotient `HC(C, X)`.

```lean
def isColimit_cechCoconeAtSheaf (n : ℕ) (F : Sheaf J.toGrothendieck AddCommGrpCat.{v}) :
    IsColimit (cechCoconeAtSheaf X J n F)
```

**`Stacks.CategoryTheory.Hypercovering.Functorial.isColimit_cechFunctorCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean, line 1309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyAsColimit.lean#L1309). The attribute's comment: “the functor-level statement in every degree, which is the claim of the tag: the edge maps exhibit the functor 𝓕 ↦ H^i(X, 𝓕) on Ab(C) as the colimit over the hypercoverings K of X of the functors 𝓕 ↦ Ȟ^i(K, 𝓕), the colimit being taken in the category of functors Ab(C) ⥤ Ab; the index category is the hypercoverings of X themselves rather than the homotopy quotient HC(C, X), and the hypotheses carried are fibre products in C and stability of the pretopology under composition”.

> Let `C` be a site with fibre products and `X` an object of `C`. For every `i`, the two
> functors `Ab(C) ⥤ Ab` given by `𝓕 ↦ H^i(X, 𝓕)` and by `𝓕 ↦ colim_K Ȟ^i(K, 𝓕)`, the colimit
> being over the hypercoverings `K` of `X`, are canonically isomorphic: the edge maps
> `hypercoveringCechEdge` exhibit the functor `H^i(X, -)` as the colimit of the functors
> `Ȟ^i(K, -)` in the category of functors `Ab(C) ⥤ Ab`. The index category is the category of
> hypercoverings itself, not the homotopy quotient `HC(C, X)`.

```lean
def isColimit_cechFunctorCocone (n : ℕ) : IsColimit (cechFunctorCocone X J n)
```

## Tag 09VZ, a proposition

[Tag 09VZ](https://stacks.math.columbia.edu/tag/09VZ) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hom_cechCohomologyEdge_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalDegeneration.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalDegeneration.lean#L851). The attribute's comment: “part (2) in every degree, at the hypercovering universe `max u v w`, which is what Tag 01GJ forces; the canonical map is the bottom-row edge map of the spectral sequence of Tag 09VY, i.e. the comparison of Tag 01GY. The size binders are those the chapter's presheaf-side tags carry -- sheafification, enough injectives and `HasExt` at the coefficient universe -- together with `WEqualsLocallyBijective`, a theorem for every essentially small site. See `exists_hom_cechCohomologyEdge_zero_eq` for degree zero at a free universe `w`”.

> **In every degree `i`, two Čech classes in `Ȟ^i(K, 𝓕)` and `Ȟ^i(L, 𝓕)`, for hypercoverings
> `K` and `L` of the final presheaf, whose images under the canonical comparison
> `Ȟ^i(-, 𝓕) ⟶ H^i(𝓕)` agree restrict to the same class on a common refinement.**
>
> The coefficients are the sheaf `𝓕` itself, not its degree-zero cohomology presheaf.  On the
> common refinement `exists_hom_of_prod` the difference of the two restrictions is killed by the
> comparison, so it dies after a further refinement (`exists_hom_cechCohomologyMap_apply_eq_zero`),
> and on that refinement the two restrictions agree.

```lean
theorem exists_hom_cechCohomologyEdge_eq (i : ℕ)
    (K L : HypercoveringOfTerminal.{max u v w} J)
    (ξK : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) K F i)
    (ξL : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) L F i)
    (h : ConcreteCategory.hom (cechCohomologyEdge.{max u v w} J K i F) ξK =
      ConcreteCategory.hom (cechCohomologyEdge.{max u v w} J L i F) ξL) :
    ∃ (M : HypercoveringOfTerminal.{max u v w} J) (f : M.Hom K) (g : M.Hom L),
      ConcreteCategory.hom (f.cechCohomologyMap F i) ξK =
        ConcreteCategory.hom (g.cechCohomologyMap F i) ξL
```

**`Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_cechCohomologyEdge_zero_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalEdgeNaturality.lean, line 1329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalEdgeNaturality.lean#L1329). The attribute's comment: “part (1) in degree i = 0, universe-general: the hypercoverings are at a free universe `w`, which is what keeps this statement from being subsumed by `exists_hypercoveringOfTerminal_cechCohomologyEdge_eq`, which has every degree but is at `max u v w` because Tag 01GJ forces it; the canonical map is the bottom-row edge map of the spectral sequence of Tag 09VY, i.e. the comparison of Tag 01GY”.

> **Stacks Project, Tag 09VZ, part (1), in degree zero.**  Every degree-zero cohomology class of
> an abelian sheaf is the image, under the canonical comparison `Ȟ⁰(K, 𝓕) ⟶ H⁰(𝓕)` of
> [Stacks, Tag 09VY], of a degree-zero Čech class on some hypercovering `K` of the final presheaf.
>
> A hypercovering exists by [Stacks, Tag 0DAX] applied to the identity coverings, and in degree
> zero the comparison is an isomorphism, `isIso_cechCohomologyEdge_zero`.

```lean
theorem exists_hypercoveringOfTerminal_cechCohomologyEdge_zero_eq
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max v w)})
    (ξ : (globalCohomologyFunctor.{max u v w} J 0).obj F) :
    ∃ (K : HypercoveringOfTerminal.{max u v w} J)
      (ξK : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) K F 0),
      ConcreteCategory.hom (cechCohomologyEdge.{max u v w} J K 0 F) ξK = ξ
```

**`Stacks.CategoryTheory.Hypercovering.exists_hom_cechCohomologyEdge_zero_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalEdgeNaturality.lean, line 1383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalEdgeNaturality.lean#L1383). The attribute's comment: “part (2) in degree i = 0, universe-general: the hypercoverings are at a free universe `w`, which is what keeps this statement from being subsumed by `exists_hom_cechCohomologyEdge_eq`, the same part (2) in every degree but with the hypercoverings at `max u v w`, the universe Tag 01GJ forces. The canonical map is the bottom-row edge map of the spectral sequence of Tag 09VY, i.e. the comparison of Tag 01GY, and its naturality in the hypercovering is proved, not assumed”.

> **Stacks Project, Tag 09VZ, part (2), in degree zero.**  Two degree-zero Čech classes on
> hypercoverings `K` and `L` of the final presheaf whose images under the canonical comparison
> `Ȟ⁰(-, 𝓕) ⟶ H⁰(𝓕)` of [Stacks, Tag 09VY] agree restrict to the same class on a common
> refinement.
>
> Nothing is assumed beyond the source's hypotheses.  The common refinement is the degreewise
> product, `exists_hom_of_prod`, which is what products of pairs in `C` are assumed for; that the
> two restrictions then agree is
> `cechCohomologyMap_apply_eq_of_cechCohomologyEdge_apply_eq`, which rests on the naturality of the
> comparison in the hypercovering, `HypercoveringOf.Hom.globalCechEdge_comp_cechCohomologyMap`.

```lean
theorem exists_hom_cechCohomologyEdge_zero_eq [HasBinaryProducts C]
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max (max u v) (max v w)})
    (K L : HypercoveringOfTerminal.{w} J)
    (ξK : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) K F 0)
    (ξL : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) L F 0)
    (h : ConcreteCategory.hom (cechCohomologyEdge.{w} J K 0 F) ξK =
      ConcreteCategory.hom (cechCohomologyEdge.{w} J L 0 F) ξL) :
    ∃ (M : HypercoveringOfTerminal.{w} J) (f : M.Hom K) (g : M.Hom L),
      ConcreteCategory.hom (f.cechCohomologyMap F 0) ξK =
        ConcreteCategory.hom (g.cechCohomologyMap F 0) ξL
```

**`Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_cechCohomologyEdge_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalFiltrationDescent.lean, line 748](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalFiltrationDescent.lean#L748). The attribute's comment: “part (1) in every degree, at the hypercovering universe `max u v w`, which is what Tag 01GJ forces; the canonical map is the bottom-row edge map of the spectral sequence of Tag 09VY, i.e. the comparison of Tag 01GY. The size binders are those the chapter's presheaf-side tags carry -- sheafification, enough injectives and `HasExt` at the coefficient universe -- together with `WEqualsLocallyBijective`, a theorem for every essentially small site, which is carried here because the degeneration of the spectral sequence rests on Tag 01GJ. See `exists_hypercoveringOfTerminal_cechCohomologyEdge_zero_eq` for degree zero at a free universe `w`”. References: SGA 4 V (7.4.1), “Clause 2)”.

> **Stacks Project, Tag 09VZ, part (1), in every degree.**  Every cohomology class of an abelian
> sheaf is the image, under the canonical comparison `Ȟ^i(K, 𝓕) ⟶ H^i(𝓕)` of [Stacks, Tag 09VY], of
> a Čech class on some hypercovering `K` of the final presheaf.
>
> The coefficients are the sheaf `𝓕` itself, not its degree-zero cohomology presheaf.  A
> hypercovering exists by [Stacks, Tag 0DAX] applied to the identity coverings; the zeroth step of
> the abutment filtration is the whole of `H^i(𝓕)` (`isIso_globalStepToAbutment_zero`), the class
> descends from there to the bottom step `F^iH^i(𝓕)` after a refinement
> (`exists_hom_globalStepToAbutment_eq`, whose engine is the degeneration of
> `StacksFrontier/CategoryTheory/Sites/Hypercovering/GlobalDegeneration.lean`), and the bottom step is
> the image of `Ȟ^i(L, 𝓕)` under the comparison
> (`exists_cechCohomologyEdge_apply_eq_globalStepToAbutment_apply`).

```lean
theorem exists_hypercoveringOfTerminal_cechCohomologyEdge_eq (i : ℕ)
    (ξ : (globalCohomologyFunctor.{max u v w} J i).obj F) :
    ∃ (K : HypercoveringOfTerminal.{max u v w} J)
      (ξK : cechCohomology J (⊤_ (Cᵒᵖ ⥤ Type v)) K F i),
      ConcreteCategory.hom (cechCohomologyEdge.{max u v w} J K i F) ξK = ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.10, Tag 01GZ](https://stacks.math.columbia.edu/tag/01GZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
