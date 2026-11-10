---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.subsiteSliceCohomology_eq_zero, AlgebraicGeometry.Stack.FlatFppf.sliceAcyclic, AlgebraicGeometry.Stack.LisseEtale.sliceAcyclic, AlgebraicGeometry.Stack.subsiteObjectCohomology_eq_zero, AlgebraicGeometry.Stack.FlatFppf.objectAcyclic, AlgebraicGeometry.Stack.LisseEtale.objectAcyclic, AlgebraicGeometry.Stack.subsiteGlobalCohomology_eq_zero, Stacks.CechSite.injective_module_subsingleton_ext_of_continuous
statement: formalized
proof: formalized
---

# 21.37 Derived lower shriek

Section 21.37 of the Stacks Project, [Tag 07AB](https://stacks.math.columbia.edu/tag/07AB). 7 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D6X, a lemma

[Tag 0D6X](https://stacks.math.columbia.edu/tag/0D6X) in the Stacks Project.

**`AlgebraicGeometry.Stack.subsiteSliceCohomology_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean#L153). The attribute's comment: “for the inclusion of a full subsite of the site of Stacks 06TP, localized at an object of the subsite”.

> **Stacks 0D6X for a slice of the inclusion of a full subsite.** Let `P` cut out a full
> subcategory of the objects of a category fibred in groupoids over the big fppf category of `S`,
> let `x` be an object of `P`, and suppose the covering morphisms of the slice at `x` of the subsite
> admit the fibre products of Stacks 00WV, preserved by the slice functor. Then the restriction
> along that functor of an injective abelian sheaf on the slice of the ambient site at `x` has
> vanishing cohomology in positive degrees.
>
> Cohomology over `x` is the global cohomology of the slice at `x`, which is cohomology over the
> terminal object `id : x ⟶ x` of that slice. The coefficient universe is the join of the two
> universes of the site, which is where the sheaves on these slices live and which is what
> `Stacks.CechSite.injective_sheaf_subsingleton_sheafH_of_functor` allows, neither site being
> small.

```lean
theorem subsiteSliceCohomology_eq_zero (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (P : ObjectProperty X)
    [P.ι.IsContinuous (subsiteTopology B S hS p τ P) (associatedTopology B S hS p τ)]
    (x : P.FullSubcategory)
    [Stacks.Sites.PreservesCoveringPullbacks ((subsiteTopology B S hS p τ P).over x)
      (Over.post (X := x) P.ι)]
    (I : Sheaf ((associatedTopology B S hS p τ).over (P.ι.obj x)) AddCommGrpCat.{max v w})
    [Injective I] (n : ℕ)
    (a : Sheaf.H ((subsiteSliceRestriction B S hS p τ P x).obj I) (n + 1)) : a = 0
```

**`AlgebraicGeometry.Stack.FlatFppf.sliceAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean#L260). The attribute's comment: “for the inclusion of the flat-fppf site of Stacks 0787, localized at a flat object”.

> **Stacks 0D6X for the inclusion of the flat-fppf site, localized at a flat object.** The
> restriction to the slice at `x` of the flat-fppf site of an injective abelian sheaf on the slice
> at `x` of the fppf site of an algebraic stack has vanishing cohomology in positive degrees.
>
> This is the hypothesis `hacyclic` of
> `AlgebraicGeometry.Stack.FlatFppf.cohomologyOverObjectIso`, part (2)(b) of Stacks 0GR0.

```lean
theorem sliceAcyclic (x : ObjectProperty.FullSubcategory (objectProperty B S hS 𝒳)) :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderFlatMorphisms B S hS 𝒳)
    ∀ I : Sheaf ((fppfTopology B S hS 𝒳).over ((objectProperty B S hS 𝒳).ι.obj x))
        AddCommGrpCat.{u + 1}, Injective I → ∀ (n : ℕ)
      (a : Sheaf.H ((subsiteSliceRestriction B S hS 𝒳.val.val.p B.topology
        (objectProperty B S hS 𝒳) x).obj I) (n + 1)), a = 0
```

**`AlgebraicGeometry.Stack.LisseEtale.sliceAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAcyclicity.lean#L327). The attribute's comment: “for the inclusion of the lisse-étale site of Stacks 0787, localized at a smooth object”.

> **Stacks 0D6X for the inclusion of the lisse-étale site, localized at a smooth object.** The
> restriction to the slice at `x` of the lisse-étale site of an injective abelian sheaf on the slice
> at `x` of the étale site of an algebraic stack has vanishing cohomology in positive degrees.
>
> This is the hypothesis `hacyclic` of
> `AlgebraicGeometry.Stack.LisseEtale.cohomologyOverObjectIso`, part (1)(b) of Stacks 0GR0.

```lean
theorem sliceAcyclic (x : ObjectProperty.FullSubcategory (smoothObject.{u, w} B S hS 𝒳)) :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    ∀ I : Sheaf ((associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)).over
        ((smoothObject.{u, w} B S hS 𝒳).ι.obj x)) AddCommGrpCat.{u + 1},
        Injective I → ∀ (n : ℕ)
      (a : Sheaf.H ((subsiteSliceRestriction B S hS 𝒳.val.val.p (etaleTopology B)
        (smoothObject.{u, w} B S hS 𝒳) x).obj I) (n + 1)), a = 0
```

**`AlgebraicGeometry.Stack.subsiteObjectCohomology_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean#L234). The attribute's comment: “for the inclusion of a full subsite of the site of Stacks 06TP, over an object of the subsite”.

> **Stacks 0D6X for the inclusion of a full subsite, over an object of the subsite.** Let `P`
> cut out a full subcategory of the objects of a category fibred in groupoids over the big fppf
> category of `S`, and suppose the covering morphisms of the subsite admit the fibre products of
> Stacks 00WV, preserved by the inclusion. Then for every object `x` of the subsite the restriction
> along the inclusion of an injective abelian sheaf on the ambient site has vanishing cohomology
> over `x` in positive degrees.
>
> Cohomology over `x` is `Ext` out of the free abelian sheaf on the representable presheaf of `x`,
> lifted to the coefficient universe, which is `CategoryTheory.extensionByZeroUnitAb`. The
> coefficient universe is the join of the two universes of the site, which is where the sheaves on
> these sites live and which is what
> `Stacks.CechSite.injective_sheaf_subsingleton_ext_of_functor` allows, neither site being
> small.

```lean
theorem subsiteObjectCohomology_eq_zero (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (P : ObjectProperty X)
    [P.ι.IsContinuous (subsiteTopology B S hS p τ P) (associatedTopology B S hS p τ)]
    [Stacks.Sites.PreservesCoveringPullbacks (subsiteTopology B S hS p τ P) P.ι]
    (I : Sheaf (associatedTopology B S hS p τ) AddCommGrpCat.{max v w}) [Injective I]
    (x : P.FullSubcategory) (n : ℕ)
    (a : Ext (extensionByZeroUnitAb.{max v w} (subsiteTopology B S hS p τ P) x)
      ((subsiteRestriction B S hS p τ P).obj I) (n + 1)) :
    a = 0
```

**`AlgebraicGeometry.Stack.FlatFppf.objectAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean#L301). The attribute's comment: “for the inclusion of the flat-fppf site of Stacks 0787, over a flat object”.

> **Stacks 0D6X for the inclusion of the flat-fppf site, over a flat object.** The restriction
> to the flat-fppf site of an injective abelian sheaf on the fppf site of an algebraic stack has
> vanishing cohomology over every flat object in positive degrees.

```lean
theorem objectAcyclic :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderFlatMorphisms B S hS 𝒳)
    ∀ I : Sheaf (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}, Injective I →
      ∀ (x : ObjectProperty.FullSubcategory (objectProperty B S hS 𝒳)) (n : ℕ)
      (a : Ext (extensionByZeroUnitAb.{u + 1} (inclusionTopology B S hS 𝒳) x)
        ((subsiteRestriction B S hS 𝒳.val.val.p B.topology
          (objectProperty B S hS 𝒳)).obj I) (n + 1)), a = 0
```

**`AlgebraicGeometry.Stack.LisseEtale.objectAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyComparison.lean#L420). The attribute's comment: “for the inclusion of the lisse-étale site of Stacks 0787, over a smooth object”.

> **Stacks 0D6X for the inclusion of the lisse-étale site, over a smooth object.** The
> restriction to the lisse-étale site of an injective abelian sheaf on the étale site of an
> algebraic stack has vanishing cohomology over every smooth object in positive degrees.

```lean
theorem objectAcyclic :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    ∀ I : Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}, Injective I →
      ∀ (x : ObjectProperty.FullSubcategory (smoothObject.{u, w} B S hS 𝒳)) (n : ℕ)
      (a : Ext (extensionByZeroUnitAb.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳) x)
        ((subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
          (smoothObject.{u, w} B S hS 𝒳)).obj I) (n + 1)), a = 0
```

**`AlgebraicGeometry.Stack.subsiteGlobalCohomology_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteTerminalCohomology.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteTerminalCohomology.lean#L55). The attribute's comment: “for the inclusion of a full subsite of the site of Stacks 06TP, for the global cohomology of a subsite with a terminal object”.

> **Vanishing of the global cohomology of a restricted injective sheaf.** Let `P` cut out a
> full subcategory of the objects of a category fibred in groupoids over the big fppf category of
> `S`, suppose the covering morphisms of the subsite admit the fibre products of Stacks 00WV,
> preserved by the inclusion, and suppose the subsite has a terminal object. Then the restriction
> along the inclusion of an injective abelian sheaf on the ambient site has vanishing global
> cohomology `CategoryTheory.Sheaf.H` in positive degrees.

```lean
theorem subsiteGlobalCohomology_eq_zero (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (P : ObjectProperty X)
    [P.ι.IsContinuous (subsiteTopology B S hS p τ P) (associatedTopology B S hS p τ)]
    [Stacks.Sites.PreservesCoveringPullbacks (subsiteTopology B S hS p τ P) P.ι]
    {e : P.FullSubcategory} (he : IsTerminal e)
    (I : Sheaf (associatedTopology B S hS p τ) AddCommGrpCat.{max v w}) [Injective I]
    (n : ℕ) (a : Sheaf.H ((subsiteRestriction B S hS p τ P).obj I) (n + 1)) :
    a = 0
```

**`Stacks.CechSite.injective_module_subsingleton_ext_of_continuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAContinuousFunctor.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAContinuousFunctor.lean#L221). The attribute's comment: “the Čech comparison derived from continuity; cocontinuity is not needed, neither site is small, and cohomology over `U` is `Ext` out of the free abelian sheaf on the lifted representable”.

> **Stacks Project, Tag 0D6X.** Let `u : C ⥤ D` be a continuous functor of sites and let
> `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi, so that `g⁻¹` is restriction along
> `u` (Sites, Lemma 00XR). Let `O_D` be a sheaf of rings on `D` and let `I` be an injective
> `O_D`-module. Then `H^p(U, g⁻¹I) = 0` for all `p > 0` and all objects `U` of `C`.
>
> Continuity of `u` (Sites, Definition 00WV) is `CategoryTheory.Functor.IsContinuous` together
> with its covering-pullback clause `Stacks.Sites.PreservesCoveringPullbacks`, and the
> identification of Čech complexes `Ȟ^p(𝒰, g⁻¹I) = Ȟ^p(u(𝒰), I)` of the source's proof is
> derived from it, by `isIso_cechProductMapOfFunctor_of_continuityCovering`. Cohomology over `U`
> is `Ext` out of the free abelian sheaf on the (lifted) representable presheaf of `U`, and the
> cohomology of a module is that of its underlying abelian sheaf. Cocontinuity of `u`, which
> makes `g` a morphism of topoi, is not needed. Neither site is assumed small; the universes of
> the two sites, of the sections of `O_D` and of `Ext` are free.

```lean
theorem injective_module_subsingleton_ext_of_continuous
    (I : SheafOfModules.{max a u v u₂ v₂ r} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    [Injective I] (U : C) (p : ℕ) (hp : 0 < p) :
    Subsingleton (Ext ((presheafToSheaf J AddCommGrpCat.{max a u v u₂ v₂ r}).obj
      (uliftYoneda.{max a u v u₂ v₂ r}.obj U ⋙ AddCommGrpCat.free))
      ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u v u₂ v₂ r} J Y.J).obj
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I)) p)
```

**`Stacks.CechSite.injective_module_sheafCohomology_isZero_of_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctor.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctor.lean#L297).

> **Stacks Project, Tag 0D6X.** Let `u : C ⥤ D` be a continuous functor of sites and let
> `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi, so that `g⁻¹` is restriction along
> `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on `D` and let `I` be an injective
> `O_D`-module. Then `H^p(U, g⁻¹I) = 0` for all `p > 0` and every object `U` of the cofinal
> system of coverings, in particular for every object of `C` when the system is cofinal
> everywhere. As in the source, the cohomology of a module is that of its underlying abelian
> sheaf.

```lean
theorem injective_module_sheafCohomology_isZero_of_functor
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (hComparison : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → (E.1.map u).I₀),
          HasProduct (fun a ↦ Over.mk ((E.1.map u).f (j a))) := hImageProducts E hE
        IsIso (cechProductMapOfFunctor u E.1 p i))
    (I : SheafOfModules.{max a u₂ v₂ r w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    [Injective I]
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    IsZero (Sheaf.H' ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u₂ v₂ r w} J Y.J).obj
      ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I)) p U)
```

**`Stacks.CechSite.injective_module_sheafCohomology_isZero_of_functor_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctor.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctor.lean#L366).

> **Stacks Project, Tag 0D6X.** Let `u : C ⥤ D` be a continuous functor of sites and let
> `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi, so that `g⁻¹` is restriction along
> `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on `D` and let `I` be an injective
> `O_D`-module. Then `H^p(U, g⁻¹I) = 0` for all `p > 0` and every object `U` of the cofinal
> system of coverings, in particular for every object of `C` when the system is cofinal
> everywhere. As in the source, the cohomology of a module is that of its underlying abelian
> sheaf.

```lean
theorem injective_module_sheafCohomology_isZero_of_functor_sheafOfRings
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (hComparison : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → (E.1.map u).I₀),
          HasProduct (fun a ↦ Over.mk ((E.1.map u).f (j a))) := hImageProducts E hE
        IsIso (cechProductMapOfFunctor u E.1 p i))
    (I : SheafOfModules.{max a u₂ v₂ r w} O) [Injective I]
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    IsZero (Sheaf.H' ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u₂ v₂ r w} J K).obj
      ((SheafOfModules.toSheaf O).obj I)) p U)
```

**`Stacks.CechSite.injective_module_subsingleton_ext_of_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean#L452). The attribute's comment: “the morphism universes of the two sites are free and the sites are not assumed small; the coefficient universe contains their objects, and cohomology over an object is `Ext` out of the free abelian sheaf on the lifted representable”.

> **Stacks Project, Tag 0D6X, with the morphism universes free.** Let `u : C ⥤ D` be a
> continuous functor of sites and let `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi,
> so that `g⁻¹` is restriction along `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on
> `D` and let `I` be an injective `O_D`-module. Then `H^p(U, g⁻¹I) = 0` for all `p > 0` and every
> object `U` of the cofinal system of coverings, in particular for every object of `C` when the
> system is cofinal everywhere. As in the source, the cohomology of a module is that of its
> underlying abelian sheaf.
>
> Neither site is assumed small, and the morphism universes of the two sites are unrelated to the
> coefficient universe, which need only contain them and the objects.

```lean
theorem injective_module_subsingleton_ext_of_functor
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (hComparison : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → (E.1.map u).I₀),
          HasProduct (fun a ↦ Over.mk ((E.1.map u).f (j a))) := hImageProducts E hE
        IsIso (cechProductMapOfFunctor u E.1 p i))
    (I : SheafOfModules.{max a u v u₂ v₂ r w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    [Injective I]
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    Subsingleton (Ext ((presheafToSheaf J AddCommGrpCat.{max a u v u₂ v₂ r w}).obj
      (uliftYoneda.{max a u v u₂ v₂ r w}.obj U ⋙ AddCommGrpCat.free))
      ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u v u₂ v₂ r w} J Y.J).obj
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I)) p)
```

**`Stacks.CechSite.injective_module_subsingleton_ext_of_functor_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean#L526). The attribute's comment: “the morphism universes of the two sites are free and the sites are not assumed small; the coefficient universe contains their objects, and cohomology over an object is `Ext` out of the free abelian sheaf on the lifted representable”.

> **Stacks Project, Tag 0D6X, with the morphism universes free.** Let `u : C ⥤ D` be a
> continuous functor of sites and let `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi,
> so that `g⁻¹` is restriction along `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on
> `D` and let `I` be an injective `O_D`-module. Then `H^p(U, g⁻¹I) = 0` for all `p > 0` and every
> object `U` of the cofinal system of coverings, in particular for every object of `C` when the
> system is cofinal everywhere. As in the source, the cohomology of a module is that of its
> underlying abelian sheaf.
>
> Neither site is assumed small, and the morphism universes of the two sites are unrelated to the
> coefficient universe, which need only contain them and the objects.

```lean
theorem injective_module_subsingleton_ext_of_functor_sheafOfRings
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (hComparison : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → (E.1.map u).I₀),
          HasProduct (fun a ↦ Over.mk ((E.1.map u).f (j a))) := hImageProducts E hE
        IsIso (cechProductMapOfFunctor u E.1 p i))
    (I : SheafOfModules.{max a u v u₂ v₂ r w} O) [Injective I]
    (U : C) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    Subsingleton (Ext ((presheafToSheaf J AddCommGrpCat.{max a u v u₂ v₂ r w}).obj
      (uliftYoneda.{max a u v u₂ v₂ r w}.obj U ⋙ AddCommGrpCat.free))
      ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u v u₂ v₂ r w} J K).obj
        ((SheafOfModules.toSheaf O).obj I)) p)
```

**`Stacks.CechSite.injective_sheaf_subsingleton_sheafH_of_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/VanishingAlongAFunctorEssentiallySmall.lean#L704). The attribute's comment: “global cohomology of the source site, at a terminal object; the morphism universes of the two sites are free and the sites are not assumed small”.

> **Stacks Project, Tag 0D6X for the global cohomology of the source site.** Let
> `u : C ⥤ D` be a continuous functor of sites, let `g : Sh(C) → Sh(D)` be the corresponding
> morphism of topoi and let `e` be a terminal object of `C` belonging to the cofinal system of
> coverings. If `I` is an injective abelian sheaf on `D` then the global cohomology
> `H^p(C, g⁻¹I)` vanishes for `p > 0`.
>
> This is the form in which the acyclicity hypothesis of Stacks 07AK is stated: the cohomology
> over an object of a site is the global cohomology of the slice at that object, and the slice
> has a terminal object.

```lean
theorem injective_sheaf_subsingleton_sheafH_of_functor
    (hCovObjects : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U),
      U ∈ B ∧ (∀ i, E.1.X i ∈ B) ∧
        ∀ (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
          letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
            HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
          (∏ᶜ (fun a ↦ Over.mk (E.1.f (i a)))).left ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ R ∈ J U,
      ∃ (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }),
        E ∈ Cov U ∧ E.1.sieve₀ ≤ R)
    (hComparison : ∀ {U : C}
      (E : { E : PreZeroHypercover.{w} U // E.sieve₀ ∈ J U }) (hE : E ∈ Cov U)
      (p : ℕ) (i : Fin (p + 1) → E.1.I₀),
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → E.1.I₀),
          HasProduct (fun a ↦ Over.mk (E.1.f (j a))) := hProducts E hE
        letI : ∀ (q : ℕ) (j : Fin (q + 1) → (E.1.map u).I₀),
          HasProduct (fun a ↦ Over.mk ((E.1.map u).f (j a))) := hImageProducts E hE
        IsIso (cechProductMapOfFunctor u E.1 p i))
    (I : Sheaf K AddCommGrpCat.{max a u v u₂ v₂ w}) [Injective I]
    {e : C} (he : IsTerminal e) (heB : e ∈ B) (p : ℕ) (hp : 0 < p) :
    Subsingleton (Sheaf.H
      ((u.sheafPushforwardContinuous AddCommGrpCat.{max a u v u₂ v₂ w} J K).obj I) p)
```

## Tag 07AC, a lemma

[Tag 07AC](https://stacks.math.columbia.edu/tag/07AC) in the Stacks Project.

**`Stacks.Cohomology.DerivedLowerShriek.derivedLowerShriek_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ModuleDerivedLowerShriek.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ModuleDerivedLowerShriek.lean#L369).

> **Stacks 07AC.** Let `u : C ⥤ D` be a continuous and cocontinuous functor of sites, let
> `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi, let `O_D` be a sheaf of rings on `D`
> and set `O_C = g^{-1} O_D`. Then the functor `g_! : Mod(O_C) ⥤ Mod(O_D)` of Stacks 0797 has a
> left derived functor `Lg_! : D(O_C) ⥤ D(O_D)`, which is left adjoint to `g^*`, and for every
> object `U` of `C`
>
> `Lg_!(j_{U!} O_U) = g_! j_{U!} O_U = j_{u(U)!} O_{u(U)}`.
>
> Continuity of `u` in the sense of the source (Stacks 00WV) is `Functor.IsContinuous` together with
> its covering-pullback clause `Stacks.Sites.PreservesCoveringPullbacks`. The derived functor is
> `derivedLowerShriek`, the total left derived functor of `SheafOfModules.pullback` along the
> identity of `O_C`, which is the lower shriek of Stacks 0797 up to the canonical isomorphism
> `Stacks.SheafOfModules.lowerShriekIsoPullback`; `g^*` on derived categories is
> `derivedRestriction`, induced by the exact restriction functor.

```lean
theorem derivedLowerShriek_spec :
    (lowerShriekOnHomotopy J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) ⋙
        DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (sourceQuasiIso J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) ∧
    (derivedLowerShriek J K f
      (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).IsLeftDerivedFunctor
      (derivedLowerShriekComparison J K f
        (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O))
      (sourceQuasiIso J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) ∧
    Nonempty (derivedLowerShriek J K f
      (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) ⊣
      derivedRestriction J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) ∧
    ∀ U : C,
      Nonempty ((derivedLowerShriek J K f
        (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).obj
          ((DerivedCategory.singleFunctor _ 0).obj (extensionByZeroUnit
            (inverseImageRing J K f
              (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) U)) ≅
        (DerivedCategory.singleFunctor _ 0).obj
          ((Stacks.SheafOfModules.lowerShriek.{u} J K f
            (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).obj
            (extensionByZeroUnit (inverseImageRing J K f
              (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) U))) ∧
      Nonempty ((Stacks.SheafOfModules.lowerShriek.{u} J K f
        (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).obj
          (extensionByZeroUnit (inverseImageRing J K f
            (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) U) ≅
        extensionByZeroUnit
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) (f.obj U))
```

**`Stacks.Cohomology.DerivedLowerShriek.pullbackExtensionByZeroUnitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/PullbackExtensionByZeroUnit.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/PullbackExtensionByZeroUnit.lean#L100). The attribute's comment: “the second equality of the displayed chain, `g_! j_{U!} O_U = j_{u(U)!} O_{u(U)}`, on sheaves of modules, for an arbitrary structure morphism of sheaves of rings `O' ⟶ u_* O` and for the sheafified-free spelling of the extensions by zero. The first equality and the existence and adjointness of `Lg_!` are NOT covered: no unbounded total left derived functor of the module-level `g_!` is constructed in this library”.

> **`g_! (j_{V!} O'_V) ≅ j_{u(V)!} O_{u(V)}` for an arbitrary structure morphism of sheaves
> of rings.** For a continuous functor of sites `u : C ⥤ D`, a sheaf of rings `O` on `D`, a sheaf
> of rings `O'` on `C`, *any* morphism `phi : O' ⟶ u_* O` whose module pushforward has a left
> adjoint, and every object `V` of `C`,
>
> `g_! (j_{V!} O'_V) ≅ j_{u(V)!} O_{u(V)}`,
>
> where `g_! = SheafOfModules.pullback phi` and both extensions by zero are the sheafified free
> modules `Stacks.SheafOfModules.extensionByZeroUnit`.

```lean
def pullbackExtensionByZeroUnitIso (V : C) :
    (SheafOfModules.pullback.{max u₁ v₁ u₂ v₂ w t} phi).obj
        (Stacks.SheafOfModules.extensionByZeroUnit.{u₁, v₁, w, max u₂ v₂ t} O' V) ≅
      Stacks.SheafOfModules.extensionByZeroUnit.{u₂, v₂, w, max u₁ v₁ t} O (u.obj V)
```

## Tag 07AE, a remark

[Tag 07AE](https://stacks.math.columbia.edu/tag/07AE) in the Stacks Project.

**`Stacks.SheafOfModules.lowerShriekForget_not_isomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L448). The attribute's comment: “underived noncommutation”.

> The lower shriek of modules may differ, even as an abelian sheaf, from lower
> shriek of the underlying abelian sheaf.

```lean
theorem lowerShriekForget_not_isomorphic :
    ∃ (J : GrothendieckTopology PUnit) (K : GrothendieckTopology Bool)
      (F : PUnit ⥤ Bool) (R : Sheaf K RingCat.{0})
      (hF : F.IsContinuous J K) (_hFc : F.IsCocontinuous J K),
      letI : F.IsContinuous J K := hF
      let S : Sheaf J RingCat.{0} :=
        (F.sheafPushforwardContinuous RingCat.{0} J K).obj R
      let φ : S ⟶ (F.sheafPushforwardContinuous RingCat.{0} J K).obj R := 𝟙 S
      ∃ (hAb : (F.sheafPushforwardContinuous AddCommGrpCat.{0} J K).IsRightAdjoint)
        (hMod : (SheafOfModules.pushforward.{0} φ).IsRightAdjoint),
      letI : (F.sheafPushforwardContinuous AddCommGrpCat.{0} J K).IsRightAdjoint := hAb
      letI : (SheafOfModules.pushforward.{0} φ).IsRightAdjoint := hMod
      ∃ M : SheafOfModules.{0} S,
        ¬ Nonempty
          (((SheafOfModules.toSheaf.{0} S ⋙
              F.sheafPullback AddCommGrpCat.{0} J K).obj M) ≅
            ((SheafOfModules.pullback.{0} φ ⋙
              SheafOfModules.toSheaf.{0} R).obj M))
```

**`Stacks.Cohomology.DerivedLowerShriek.existsUnique_derivedForgetComparison_of_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparison.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparison.lean#L218). The attribute's comment: “the comparison transformation `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!`”.

> **The comparison transformation**, conditional only on the acyclicity statement of Stacks 0794
> for lower shriek: there is exactly one natural transformation `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!`
> compatible with the counits of the two left derived functors and the comparison of Stacks 0798.

```lean
theorem existsUnique_derivedForgetComparison_of_acyclic [Small.{w} C]
    [∀ U : C, (_root_.SheafOfModules.pushforward.{w} (F := Over.forget U)
      (𝟙 ((inverseImageRing J K f O).over U) :
        (inverseImageRing J K f O).over U ⟶ (inverseImageRing J K f O).over U)).IsRightAdjoint]
    (hFP : ∀ (a : ℤ)
      (Lc : CochainComplex (_root_.SheafOfModules.{w} (inverseImageRing J K f O)) ℤ),
      Lc.IsStrictlyLE a →
      (∀ n, IsSumOfExtensionByZeroUnits (inverseImageRing J K f O) (Lc.X n)) → Lc.Acyclic →
      (((lowerShriekModules J K f O).mapHomologicalComplex (ComplexShape.up ℤ)).obj Lc).Acyclic) :
    ∃! t : (forgetSourceModules J K f O).mapDerivedCategory ⋙
        derivedLowerShriekAbelian J K f ⟶
      derivedLowerShriek J K f O ⋙ (forgetTargetModules K O).mapDerivedCategory,
      Functor.whiskerLeft DerivedCategory.Qh t ≫ derivedLowerShriekForgetCounit J K f O =
        derivedForgetComparisonCounit J K f O
```

**`Stacks.Cohomology.DerivedLowerShriek.exists_isIso_forgetComparison_not_isIso_derivedForgetComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonCounterexample.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonCounterexample.lean#L810). The attribute's comment: “the warning: the square `forget ∘ Lg_!` vs `Lg_!^{Ab} ∘ forget` need not commute even when `g_! = g_!^{Ab}` -- an example of sites, a functor satisfying the hypotheses of Stacks 07AC and a sheaf of rings for which the comparison of Stacks 0798 is an isomorphism and the comparison `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!` is not, nor are the two composites isomorphic by any natural isomorphism; the example lives in universe 0, an existence statement needing one”.

> **Stacks Project, Tag 07AE, the warning.** Let `u : C ⥤ D`, `g`, `O_D` and `O_C = g^{-1} O_D`
> be as in Stacks 07AC. In general the square
>
> ```
> D(O_C) --Lg_!--> D(O_D)
>   |                 |
> forget            forget
>   v                 v
> D(C) --Lg_!^{Ab}--> D(D)
> ```
>
> does **not** commute, and this can happen even if `g_! = g_!^{Ab}`.
>
> Stated as an existence: there are small sites `C`, `D`, a functor `u : C ⥤ D` satisfying the
> hypotheses of Stacks 07AC (continuous in the sense of Stacks 00WV, which is
> `Functor.IsContinuous` together with `Stacks.Sites.PreservesCoveringPullbacks`, and
> cocontinuous) and a sheaf of rings `O_D` on `D` such that
>
> * `g_! = g_!^{Ab}`: the canonical comparison `g_!^{Ab} ∘ forget ⟶ forget ∘ g_!` of Stacks 0798
>   (`forgetComparison`) is an isomorphism, and yet
> * the canonical comparison `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!` of Stacks 07AE
>   (`derivedForgetComparison`, characterised by
>   `existsUnique_derivedForgetComparison_of_continuous`) is not an isomorphism, and indeed the
>   two composites `Lg_!^{Ab} ∘ forget` and `forget ∘ Lg_!` are not isomorphic by any natural
>   isomorphism whatsoever.
>
> The example: `C` is the cospan category `left ⟶ one ⟵ right` and `D` is `Bool` ordered by
> `false ≤ true`, both with the trivial topology, `u` sends the legs to `false ≤ true`, and `O_D`
> is `ℤ` at `true` and the zero ring at `false`. Every `O_C`-module vanishes at `left` and `right`,
> which forces `g_! = g_!^{Ab}` (`isIso_forgetComparison`); but the underlying abelian sheaf of
> `j_{one!} O_one = O_C` has a nonzero `Ext^1` into the restriction of an injective abelian sheaf
> of `D` (`not_subsingleton_ext_unit`), which is the homotopy pushout `0 ← ℤ → 0` computing
> `Lg_!^{Ab}` at `false` having nonzero `H^{-1}`, so the comparison is not invertible
> (`not_isIso_derivedForgetComparison`, via the criterion of this tag,
> `extAcyclic_forget_extensionByZeroUnit`).

```lean
theorem exists_isIso_forgetComparison_not_isIso_derivedForgetComparison :
    ∃ (C D : Type) (_ : SmallCategory C) (_ : SmallCategory D)
      (J : GrothendieckTopology C) (K : GrothendieckTopology D) (f : C ⥤ D)
      (_ : f.IsContinuous J K) (_ : f.IsCocontinuous J K)
      (_ : Stacks.Sites.PreservesCoveringPullbacks J f) (O : Sheaf K CommRingCat.{0}),
      IsIso (forgetComparison J K f
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) ∧
        ¬ IsIso (derivedForgetComparison J K f
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) ∧
        ¬ Nonempty ((forgetSourceModules J K f
            (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).mapDerivedCategory ⋙
              derivedLowerShriekAbelian J K f ≅
          derivedLowerShriek J K f
              (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) ⋙
            (forgetTargetModules K (Stacks.SheafOfModules.Tensor.ringSheaf
              (targetRingedSite K O).O)).mapDerivedCategory)
```

**`Stacks.Cohomology.DerivedLowerShriek.isIso_derivedForgetComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonCriterionFromContinuity.lean, line 725](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonCriterionFromContinuity.lean#L725). The attribute's comment: “the criterion: `Lg_!` agrees with `Lg_!^{Ab}` (the comparison `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!` is invertible) iff every canonical map `Lg_!^{Ab} j_{U!}O_U ⟶ j_{u(U)!}O_{u(U)}` is invertible in D(D); both directions, under the hypotheses of Stacks 07AC only, in the library's convention for it: small sites with objects, morphisms and module sections in one universe, and a sheaf of (commutative) rings”.

> **Stacks Project, Tag 07AE, the criterion.** Let `u : C ⥤ D` be a continuous and
> cocontinuous functor of sites, `g` the corresponding morphism of topoi, `O_D` a sheaf of rings on
> `D` and `O_C = g^{-1}O_D`. Then `Lg_!` agrees with `Lg_!^{Ab}`, in the sense that the canonical
> comparison `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!` is an isomorphism, if and only if the canonical
> maps `Lg_!^{Ab} j_{U!}O_U ⟶ j_{u(U)!}O_{u(U)}` are isomorphisms in `D(D)` for all objects `U`
> of `C`.
>
> The comparison is `derivedForgetComparison`, the unique transformation compatible with the two
> counits and the comparison of Stacks 0798
> (`existsUnique_derivedForgetComparison_of_continuous`). The canonical map at `U` is
> `derivedForgetComparisonGenerator`: the component of the comparison at `j_{U!}O_U` in degree
> zero, followed by the identification `Lg_!(j_{U!}O_U) = g_!j_{U!}O_U = j_{u(U)!}O_{u(U)}` of
> Stacks 07AC. The hypotheses are those of Stacks 07AC; continuity in the sense of Stacks 00WV is
> `Functor.IsContinuous` with `Stacks.Sites.PreservesCoveringPullbacks`. The forward implication
> is `isIso_derivedForgetComparisonGenerator`, the converse
> `isIso_derivedForgetComparison_of_isIso_generator`.

```lean
theorem isIso_derivedForgetComparison_iff :
    IsIso (derivedForgetComparison J K f (Stacks.SheafOfModules.Tensor.ringSheaf
      (targetRingedSite K O).O)) ↔
      ∀ U : C, IsIso (derivedForgetComparisonGenerator J K f
        (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) U)
```

**`Stacks.Cohomology.DerivedLowerShriek.existsUnique_derivedForgetComparison_of_continuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonFromContinuity.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/ForgetComparisonFromContinuity.lean#L119). The attribute's comment: “the comparison transformation `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!`, with no hypothesis beyond those of Stacks 07AC: continuity of u (Stacks 00WV) is `Functor.IsContinuous` with `Stacks.Sites.PreservesCoveringPullbacks`; the existence of `g_!`, `g_!^{Ab}`, `Lg_!` and `Lg_!^{Ab}` is proved, not assumed; the sites are small and the ring sheaf commutative, as in Stacks 07AC”.

> **Stacks Project, Tag 07AE.** Let `u : C ⥤ D` be a continuous and cocontinuous functor of
> sites, let `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi, let `O_D` be a sheaf of
> rings on `D` and set `O_C = g^{-1}O_D`. There is exactly one natural transformation
>
> `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!`
>
> compatible with the counits exhibiting the two functors as left derived functors and with the
> comparison `g_!^{Ab} ∘ forget ⟶ forget ∘ g_!` of Stacks 0798.
>
> That is all the warning allows: the undifferentiated functors already need not agree, which is
> `Stacks.SheafOfModules.lowerShriekForget_not_isomorphic`, and the square commutes exactly when
> the canonical maps `Lg_!^{Ab} j_{U!}O_U ⟶ j_{u(U)!}O_{u(U)}` are isomorphisms, which they need
> not be. Uniqueness is what makes this *the* comparison of the warning rather than some
> transformation between the two composites: a left derived functor is a right Kan extension along
> the localization, so a transformation into `Lg_! ⋙ forget` is the same thing as one out of
> `Q_h ⋙ (forget ⋙ Lg_!^{Ab})` into degreewise `g_! ⋙ forget` followed by `Q_h`, and the lift is
> unique.
>
> This is `existsUnique_derivedForgetComparison_of_acyclic` with its inputs discharged; see the
> module docstring. The hypotheses are exactly those of Stacks 07AC: `[f.IsContinuous J K]` and
> `[Stacks.Sites.PreservesCoveringPullbacks J f]` together are continuity of `u` in the sense of
> Stacks 00WV, `[f.IsCocontinuous J K]` is cocontinuity, and `O` is the sheaf of rings `O_D`. The
> acyclicity statement of Stacks 0794 that the conditional form takes as `hFP`, the left adjoints
> `g_!` and `g_!^{Ab}` of restriction, and the existence of both derived functors are all found by
> instance search from the instances proved in `ModuleDerivedLowerShriek.lean`,
> `AbelianAcyclicityFromContinuity.lean` and `AdjointExistence.lean`; the transformation itself is
> `derivedForgetComparison`.

```lean
theorem existsUnique_derivedForgetComparison_of_continuous :
    ∃! t : (forgetSourceModules J K f
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).mapDerivedCategory ⋙
        derivedLowerShriekAbelian J K f ⟶
      derivedLowerShriek J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) ⋙
        (forgetTargetModules K
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)).mapDerivedCategory,
      Functor.whiskerLeft DerivedCategory.Qh t ≫
          derivedLowerShriekForgetCounit J K f
            (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) =
        derivedForgetComparisonCounit J K f
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)
```

## Tag 0D6Y, a lemma

[Tag 0D6Y](https://stacks.math.columbia.edu/tag/0D6Y) in the Stacks Project.

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L451).

> **Stacks Project, Tag 0D6Y.** Let `u : C ⥤ D` be a continuous and cocontinuous functor of
> sites and let `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi, so that `g^{-1}` is
> restriction along `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on `D` and let `I` be
> an injective `O_D`-module. If `g_!^{Sh} : Sh(C) → Sh(D)` commutes with fibre products, then
> `g^{-1}I` is totally acyclic: its cohomology over every sheaf of sets on `C` vanishes in every
> positive degree.
>
> As in the source, total acyclicity of a module is that of its underlying abelian sheaf; the
> abelian sheaf underlying `g^{-1}I` is the restriction along `u` of the abelian sheaf underlying
> `I`, which is how the conclusion is phrased.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective
    [∀ n : ℕ, PreservesLimitsOfShape (WidePullbackShape (Fin (n + 1)))
      (u.sheafPullback (Type w) J Y.J)]
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J Y.J).obj
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective_of_pullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L468). The attribute's comment: “the case of the footnote's sufficient condition: `C` has finite connected limits and `u` commutes with them”.

> **Stacks Project, Tag 0D6Y, under the sufficient condition of its footnote.** If `C` has
> fibre products and equalizers — equivalently, all finite connected limits — and `u` preserves
> them, then `g_!^{Sh}` commutes with fibre products by Sites, Lemma 00XS, and the inverse image
> of an injective `O_D`-module is totally acyclic.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective_of_pullbacks [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u] [PreservesLimitsOfShape WalkingParallelPair u]
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J Y.J).obj
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_pushforwardModule_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L485). The attribute's comment: “the conclusion read on the inverse image module rather than on the restriction of the underlying abelian sheaf”.

> **Stacks Project, Tag 0D6Y, read on the inverse image module.** The abelian sheaf underlying
> the inverse image `g^{-1}I` of an injective `O_D`-module — restriction along `u`, as a module
> over the inverse image `g^{-1}O_D` of the structure sheaf — is totally acyclic.

```lean
theorem isTotallyAcyclic_pushforwardModule_of_injective
    [∀ n : ℕ, PreservesLimitsOfShape (WidePullbackShape (Fin (n + 1)))
      (u.sheafPullback (Type w) J Y.J)]
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((SheafOfModules.toSheaf _).obj
        ((SheafOfModules.pushforward (F := u)
          (𝟙 ((u.sheafPushforwardContinuous RingCat.{w} J Y.J).obj
            (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective_of_cospans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L510). The attribute's comment: “the tag at the source's own hypothesis, that `g_!^{Sh}` commute with binary fibre products; the iterated fibre powers the proof uses follow from it”.

> **Stacks Project, Tag 0D6Y, with the hypothesis the source states.** Let `u : C ⥤ D` be a
> continuous and cocontinuous functor of sites and let `g : Sh(C) → Sh(D)` be the corresponding
> morphism of topoi. Let `O_D` be a sheaf of rings on `D` and let `I` be an injective
> `O_D`-module. If `g_!^{Sh} : Sh(C) → Sh(D)` commutes with binary fibre products, then `g^{-1}I`
> is totally acyclic.
>
> The complex of Stacks 07A1 is built from the iterated fibre powers of a surjection of sheaves of
> sets, so it is commutation with those that the proof uses. Commutation with binary fibre
> products supplies it: an iterated fibre power is a fibre product of one fewer of its factors
> against the remaining one, and `Sh(C)` has fibre products, so
> `CategoryTheory.Limits.preservesLimitsOfShape_widePullbackShape` applies.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective_of_cospans
    [PreservesLimitsOfShape WalkingCospan (u.sheafPullback (Type w) J Y.J)]
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J Y.J).obj
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L570).

> **Stacks Project, Tag 0D6Y.** Let `u : C ⥤ D` be a continuous and cocontinuous functor of
> sites and let `g : Sh(C) → Sh(D)` be the corresponding morphism of topoi, so that `g^{-1}` is
> restriction along `u` by Sites, Lemma 00XR. Let `O_D` be a sheaf of rings on `D` and let `I` be
> an injective `O_D`-module. If `g_!^{Sh} : Sh(C) → Sh(D)` commutes with fibre products, then
> `g^{-1}I` is totally acyclic: its cohomology over every sheaf of sets on `C` vanishes in every
> positive degree.
>
> As in the source, total acyclicity of a module is that of its underlying abelian sheaf; the
> abelian sheaf underlying `g^{-1}I` is the restriction along `u` of the abelian sheaf underlying
> `I`, which is how the conclusion is phrased.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective_sheafOfRings
    [∀ n : ℕ, PreservesLimitsOfShape (WidePullbackShape (Fin (n + 1)))
      (u.sheafPullback (Type w) J K)]
    (I : SheafOfModules.{w} O) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J K).obj
        ((SheafOfModules.toSheaf O).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective_of_pullbacks_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L587). The attribute's comment: “the case of the footnote's sufficient condition: `C` has finite connected limits and `u` commutes with them”.

> **Stacks Project, Tag 0D6Y, under the sufficient condition of its footnote.** If `C` has
> fibre products and equalizers — equivalently, all finite connected limits — and `u` preserves
> them, then `g_!^{Sh}` commutes with fibre products by Sites, Lemma 00XS, and the inverse image
> of an injective `O_D`-module is totally acyclic.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective_of_pullbacks_sheafOfRings
    [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u] [PreservesLimitsOfShape WalkingParallelPair u]
    (I : SheafOfModules.{w} O) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J K).obj
        ((SheafOfModules.toSheaf O).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_pushforwardModule_of_injective_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L605). The attribute's comment: “the conclusion read on the inverse image module rather than on the restriction of the underlying abelian sheaf”.

> **Stacks Project, Tag 0D6Y, read on the inverse image module.** The abelian sheaf underlying
> the inverse image `g^{-1}I` of an injective `O_D`-module — restriction along `u`, as a module
> over the inverse image `g^{-1}O_D` of the structure sheaf — is totally acyclic.

```lean
theorem isTotallyAcyclic_pushforwardModule_of_injective_sheafOfRings
    [∀ n : ℕ, PreservesLimitsOfShape (WidePullbackShape (Fin (n + 1)))
      (u.sheafPullback (Type w) J K)]
    (I : SheafOfModules.{w} O) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((SheafOfModules.toSheaf _).obj
        ((SheafOfModules.pushforward (F := u)
          (𝟙 ((u.sheafPushforwardContinuous RingCat.{w} J K).obj O))).obj I))
```

**`Stacks.Cohomology.DerivedLowerShriek.isTotallyAcyclic_inverseImage_of_injective_of_cospans_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/TotalAcyclicityOfTheInverseImage.lean#L629). The attribute's comment: “the tag at the source's own hypothesis, that `g_!^{Sh}` commute with binary fibre products; the iterated fibre powers the proof uses follow from it”.

> **Stacks Project, Tag 0D6Y, with the hypothesis the source states.** Let `u : C ⥤ D` be a
> continuous and cocontinuous functor of sites and let `g : Sh(C) → Sh(D)` be the corresponding
> morphism of topoi. Let `O_D` be a sheaf of rings on `D` and let `I` be an injective
> `O_D`-module. If `g_!^{Sh} : Sh(C) → Sh(D)` commutes with binary fibre products, then `g^{-1}I`
> is totally acyclic.
>
> The complex of Stacks 07A1 is built from the iterated fibre powers of a surjection of sheaves of
> sets, so it is commutation with those that the proof uses. Commutation with binary fibre
> products supplies it: an iterated fibre power is a fibre product of one fewer of its factors
> against the remaining one, and `Sh(C)` has fibre products, so
> `CategoryTheory.Limits.preservesLimitsOfShape_widePullbackShape` applies.

```lean
theorem isTotallyAcyclic_inverseImage_of_injective_of_cospans_sheafOfRings
    [PreservesLimitsOfShape WalkingCospan (u.sheafPullback (Type w) J K)]
    (I : SheafOfModules.{w} O) [Injective I] :
    IsTotallyAcyclic.{w} J
      ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J K).obj
        ((SheafOfModules.toSheaf O).obj I))
```

## Tag 0DD8, a lemma

[Tag 0DD8](https://stacks.math.columbia.edu/tag/0DD8) in the Stacks Project.

**`Stacks.Cohomology.DerivedLowerShriek.derivedAbelianSectionsRestrictionIso_of_continuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAContinuousFunctor.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAContinuousFunctor.lean#L96). The attribute's comment: “part (1); the two sites are small and the coefficients are in their universe, the library's standard one-universe convention for sites”.

> **Stacks Project, Tag 0DD8, part (1).** Let `u : C ⥤ D` be a continuous and cocontinuous
> functor of sites and let `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi. For every
> object `U` of `C` and every `M` in the unbounded derived category of abelian sheaves on `D`,
> `RΓ(U, g⁻¹M) = RΓ(u(U), M)`, naturally in `M`.
>
> This is `derivedAbelianSectionsRestrictionIso` with all of its inputs discharged. The
> invertibility of the derived lower-shriek counit at the single complex on `j_{U!} ℤ_U` is
> `isIso_derivedAbelianLowerShriekComparison_app`, which holds because that complex is cellular
> for the class with which `Lg_!^{Ab}` is built; the existence of `Lg_!^{Ab}` and its
> absoluteness against derived restriction are the two instances of
> `AbelianAcyclicityFromContinuity.lean`. All three come from the acyclicity statement of
> Stacks 0794 for lower shriek on abelian sheaves, which that file derives from Stacks 0D6X and so
> from the covering-pullback clause `Stacks.Sites.PreservesCoveringPullbacks` of continuity in the
> sense of Sites, Definition 00WV.

```lean
def derivedAbelianSectionsRestrictionIso_of_continuous :
    derivedAbelianRestriction.{u} J K f ⋙ derivedAbelianSections J U ≅
      derivedAbelianSections K (f.obj U)
```

**`Stacks.Cohomology.DerivedLowerShriek.derivedModuleSectionsRestrictionIso_of_continuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAContinuousFunctor.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAContinuousFunctor.lean#L123). The attribute's comment: “part (2); the two sites are small and the module sections are in their universe, the library's standard one-universe convention for sites; the structure sheaf is a sheaf of commutative rings, which is what a sheaf of rings is in the source (Stacks 0006)”.

> **Stacks Project, Tag 0DD8, part (2).** Let `u : C ⥤ D` be a continuous and cocontinuous
> functor of sites, let `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi, let `O_D` be a
> sheaf of rings on `D` and let `O_C = g⁻¹O_D`. For every object `U` of `C` and every `M` in the
> unbounded derived category of `O_D`-modules, `RΓ(U, g^*M) = RΓ(u(U), M)`, naturally in `M`.
>
> This is `derivedModuleSectionsRestrictionIso` with all of its inputs discharged. The
> invertibility of the derived lower-shriek counit at the single complex on `j_{U!} O_U` is
> `isIso_derivedLowerShriekComparison_app`, and the existence of `Lg_!` and its absoluteness
> against derived restriction are the two instances of `ModuleDerivedLowerShriek.lean`; all three
> come from `lowerShriekModules_acyclic`, the acyclicity statement of Stacks 0794 for lower shriek
> on modules, which that file derives from Stacks 0D6X and so from the covering-pullback clause
> `Stacks.Sites.PreservesCoveringPullbacks` of continuity in the sense of Sites,
> Definition 00WV.

```lean
def derivedModuleSectionsRestrictionIso_of_continuous (O : Sheaf K CommRingCat.{u}) :
    derivedRestriction J K f (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O) ⋙
        derivedModuleSections J (inverseImageRing J K f
          (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)) U ≅
      derivedModuleSections K (Stacks.SheafOfModules.Tensor.ringSheaf (targetRingedSite K O).O)
        (f.obj U)
```

**`Stacks.Cohomology.DerivedLowerShriek.derivedModuleSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAFunctor.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAFunctor.lean#L564). The attribute's comment: “part (2)”.

> **Stacks 0DD8, part (2).** Let `u : C ⥤ D` be a continuous and cocontinuous functor of
> sites, let `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi, let `O_D` be a sheaf of
> rings on `D` and let `O_C = g⁻¹O_D`. For every object `U` of `C` and every `M` in the unbounded
> derived category of `O_D`-modules, `RΓ(U, g^*M) = RΓ(u(U), M)`, naturally in `M`.

```lean
def derivedModuleSectionsRestrictionIso
    (hgen : DerivedLowerShriekComputesGenerator J K f O U) :
    derivedRestriction J K f O ⋙ derivedModuleSections J (inverseImageRing J K f O) U ≅
      derivedModuleSections K O (f.obj U)
```

**`Stacks.Cohomology.DerivedLowerShriek.derivedAbelianSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAFunctor.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriek/DerivedSectionsAlongAFunctor.lean#L689). The attribute's comment: “part (1)”.

> **Stacks 0DD8, part (1).** Let `u : C ⥤ D` be a continuous and cocontinuous functor of
> sites and let `g : Sh(C) ⟶ Sh(D)` be the corresponding morphism of topoi. For every object `U`
> of `C` and every `M` in the unbounded derived category of abelian sheaves on `D`,
> `RΓ(U, g⁻¹M) = RΓ(u(U), M)`, naturally in `M`.

```lean
def derivedAbelianSectionsRestrictionIso
    (hgen : DerivedAbelianLowerShriekComputesGenerator J K f U) :
    derivedAbelianRestriction.{u} J K f ⋙ derivedAbelianSections J U ≅
      derivedAbelianSections K (f.obj U)
```

## Tag 0FN6, a lemma

[Tag 0FN6](https://stacks.math.columbia.edu/tag/0FN6) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChange.nonempty_inverseImage_comp_totalDerivedPushforwardOf_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/UnboundedBaseChangeForACocontinuousSquare.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/UnboundedBaseChangeForACocontinuousSquare.lean#L498). The attribute's comment: “`Rf'_* ∘ (g')^* ≅ g^* ∘ Rf_*` on the unbounded derived categories `D(O_C) → D(O_{D'})`, for a commutative square of ringed topoi whose four functors `u`, `u'`, `v`, `v'` are cocontinuous, with `u' ⋙ v = v' ⋙ u`, with `v`, `v'` continuous as well, with the comparison functors `{}^{u'}_{V'} I → {}^u_{v(V')} I` of the index categories of Section 00XF cofinal, with `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`, and with the tag's condition (6) in the source's own form: exactness of `g'_! : Ab(C') → Ab(C)`, written `PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat J' J)`, right exactness of a left adjoint being automatic. `Rf_*` and `Rf'_*` are *constructed*, as the total right derived functors of the degreewise direct images of sheaves of modules, and nothing about them is required. The price of the source's condition (6) is that the four sites lie in one universe, which is where Stacks 0D6J, the transport from abelian sheaves to modules that the source's proof opens with, is available. An isomorphism rather than an equality, and asserted through `Nonempty` as its underived input Stacks 0FN3 is, a right derived functor being determined only up to a canonical isomorphism and the sheaf-level comparison of Stacks 0FN1 being a base change of right Kan extensions.”.

> **Stacks 0FN6.** For a commutative square of ringed topoi whose four functors `u : C ⥤ D`,
> `u' : C' ⥤ D'`, `v : D' ⥤ D`, `v' : C' ⥤ C` are cocontinuous — giving `f`, `f'`, `g`, `g'` with
> `f_* = {}_su`, `f'_* = {}_su'` — with `u' ⋙ v = v' ⋙ u`, with `v` and `v'` continuous as well as
> cocontinuous so that `g^{-1}`, `(g')^{-1}` are restriction, with the comparison functors
> `{}^{u'}_{V'} I ⥤ {}^u_{v(V')} I` of the index categories of Section 00XF all cofinal, with
> `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`, and with `g'_! : Ab(C') ⥤ Ab(C)` exact, we
> have `Rf'_* ∘ (g')^* = g^* ∘ Rf_*` as functors `D(O_C) ⥤ D(O_{D'})`.
>
> Condition (5) is built into the statement by taking the restrictions along `v` and `v'` as *the*
> sheaves of rings on `D'` and `C'`, so that `g^* = g^{-1}` and `(g')^* = (g')^{-1}` are
> `Stacks.SheafOfModules.inverseImage` and are exact; `(f')^♯` is the structure map the square
> forces, as in Stacks 0FN3. Condition (6) is the hypothesis
> `PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat J' J)`: `v'.sheafPullback` is the left
> adjoint `g'_! = (v')_s` of the inverse image `(g')^{-1} = (v')^p` of abelian sheaves, which
> Stacks 00XR produces for a continuous and cocontinuous `v'`, and right exactness of a left
> adjoint is automatic, so left exactness is the whole of the condition.
>
> Both `Rf_*` and `Rf'_*` are the total right derived functors of the degreewise direct images of
> sheaves of modules; nothing about them is assumed. The source's proof is followed exactly: the
> underived identity is Stacks 0FN3, which is what the cofinality hypothesis `hfinal` — condition
> (4) — feeds; condition (6) and Stacks 08BJ make `(g')^{-1}` preserve K-injectivity *of abelian
> sheaves*, Stacks 0FN1 gives the underived identity there, and Stacks 0D6J carries the resulting
> statement — that the inverse image of a K-injective complex of `O_C`-modules computes `Rf'_*` —
> back to modules.

```lean
theorem nonempty_inverseImage_comp_totalDerivedPushforwardOf_iso
    [PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat.{u} J' J)]
    (fSharp : OD ⟶ (u.sheafPushforwardCocontinuous RingCat.{u} J K).obj OC)
    (hsq : u' ⋙ v = v' ⋙ u)
    (hcomm : f'Sharp = structureMapSquare (J' := J') (K' := K') fSharp hsq)
    (hfinal : ∀ V' : D',
      (CostructuredArrow.map₂ (S := u') (T := V') (U := u) (V := v.obj V') (F := v') (G := v)
        (eqToHom hsq.symm) (𝟙 (v.obj V'))).Final) :
    Nonempty ((inverseImage.{u} J' J v' OC).mapDerivedCategory ⋙
        UnboundedComplexes.totalRightDerivedOfAdditive
          (pushforwardCocontinuous.{u} u' f'Sharp) ≅
      UnboundedComplexes.totalRightDerivedOfAdditive (pushforwardCocontinuous.{u} u fSharp) ⋙
        (inverseImage.{u} K' K v OD).mapDerivedCategory)
```

## Tag 0FN7, a lemma

[Tag 0FN7](https://stacks.math.columbia.edu/tag/0FN7) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChange.inverseImageCompDerivedPushforwardPlusIsoOfRingedSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BoundedBelowBaseChangeOverASquareOfSites.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BoundedBelowBaseChangeOverASquareOfSites.lean#L338). The attribute's comment: “first conclusion: `Rf'_* ∘ (g')^* ≅ g^* ∘ Rf_*` on the *bounded below* derived categories `D⁺(O_C) → D⁺(O_{D'})`, for a commutative square of ringed topoi whose horizontal functors `u`, `u'` are continuous and whose vertical functors `v`, `v'` are continuous as well as cocontinuous, with `v ⋙ u = u' ⋙ v'`, `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`, and WITHOUT the tag's condition (6), exactness of `g'_!` — which is what the second conclusion, on the unbounded derived categories, needs; that conclusion, under the source's own condition (6), is `Stacks.Cohomology.DerivedBaseChange.inverseImageCompTotalDerivedPushforwardIsoOfExactLowerShriek`. Proved as in the source, through the vanishing of Stacks 0D6X, the sheafified cohomology presheaf of Stacks 072W, and Leray's acyclicity lemma Stacks 015E. An isomorphism rather than an equality, a right derived functor being determined only up to a canonical isomorphism. The sites `C` and `C'` are at the single universe at which Stacks 0D6X and the Ext-to-derived-sections comparison of Stacks 03FD are available in this library — `C'` small and `C` the site of a ringed site — and `v'` is continuous in the sense of Sites, Definition 00WV, which is the hypothesis Stacks 0D6X uses and which Mathlib's `IsContinuous` does not supply; that is not an extra assumption relative to the source, where `v'` is continuous in exactly that sense, and `Stacks.Sites.preservesCoveringPullbacks_of_isContinuous` derives it from the project's formalization of Definition 00WV.”.

> **Stacks 0FN7, first conclusion, with the acyclicity step discharged.** The same statement
> as `inverseImageCompDerivedPushforwardPlusIso`, in the universes at which Stacks 0D6X and
> Stacks 072W are available: `C'` is a small site and `C` is the site of a ringed site `Y` whose
> structure sheaf, module sections and `Ext`-groups lie in the universe of its objects, while `D`
> and `D'` keep arbitrary universes.
>
> The source's condition (6) is not a hypothesis, and neither is the acyclicity it would be used
> for: it is proved here from Stacks 0D6X and Stacks 072W by
> `rightAcyclic_pushforward_inverseImage_of_injective`.

```lean
def inverseImageCompDerivedPushforwardPlusIsoOfRingedSite (hsq : v ⋙ u = u' ⋙ v')
    (hcomm : f'Sharp =
      restrictStructureMap J' Y.J K' K u u' v v' (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) OD
        fSharp hsq) :
    (inverseImage.{w} J' Y.J v'
      (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).mapDerivedCategoryPlus ⋙
        (_root_.SheafOfModules.pushforward.{w} f'Sharp).rightDerivedFunctorPlus ≅
      (_root_.SheafOfModules.pushforward.{w} fSharp).rightDerivedFunctorPlus ⋙
        (inverseImage.{w} K' K v OD).mapDerivedCategoryPlus
```

**`Stacks.Cohomology.DerivedBaseChange.inverseImageCompTotalDerivedPushforwardIsoOfExactLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/UnboundedBaseChangeForAnExactLowerShriek.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/UnboundedBaseChangeForAnExactLowerShriek.lean#L310). The attribute's comment: “the second conclusion, at the source's full statement of it: `Rf'_* ∘ (g')^* ≅ g^* ∘ Rf_*` on the *unbounded* derived categories `D(O_C) → D(O_{D'})`, for a commutative square of ringed topoi whose horizontal functors `u`, `u'` are continuous and whose vertical functors `v`, `v'` are continuous as well as cocontinuous, with `v ⋙ u = u' ⋙ v'`, `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`, and with the tag's condition (6) as the source states it — exactness of `g'_! : Ab(C') → Ab(C)`, written `PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat J' J)`, right exactness of a left adjoint being automatic. Nothing else is assumed: in particular NOT the module-level substitution for condition (6) that `Stacks.Cohomology.DerivedBaseChange.inverseImageCompDerivedPushforwardIso` and `Stacks.Cohomology.DerivedBaseChange.inverseImageCompTotalDerivedPushforwardIso` grant in its place, those two adding four independent universes instead. The price here is that the four sites lie in one universe, which is where Stacks 0D6J, the transport from abelian sheaves to modules that the source's proof opens with, is available. `Rf_*` and `Rf'_*` are *constructed*, as the total right derived functors of the degreewise direct images, and nothing about them is assumed. An isomorphism rather than an equality, a right derived functor being determined only up to a canonical isomorphism. The first conclusion of the tag, the same identity on `D^+` without condition (6), is `Stacks.Cohomology.DerivedBaseChange.inverseImageCompDerivedPushforwardPlusIsoOfRingedSite`.”.

> **Stacks 0FN7**, second conclusion, under the source's own condition (6). For a commutative
> square of ringed topoi whose horizontal functors `u : D ⥤ C`, `u' : D' ⥤ C'` are continuous —
> giving `f`, `f'` with `f_* = u^s`, `f'_* = (u')^s` — whose vertical functors `v : D' ⥤ D`,
> `v' : C' ⥤ C` are continuous as well as cocontinuous — giving `g`, `g'` with `g^{-1}`,
> `(g')^{-1}` restriction — with `v ⋙ u = u' ⋙ v'`, with `g^{-1} O_D = O_{D'}` and
> `(g')^{-1} O_C = O_{C'}`, and with `g'_! : Ab(C') ⥤ Ab(C)` exact, we have
> `Rf'_* ∘ (g')^* = g^* ∘ Rf_*` as functors `D(O_C) ⥤ D(O_{D'})`.
>
> Condition (6) is the hypothesis `PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat J' J)`:
> `v'.sheafPullback` is the left adjoint `g'_! = (v')_s` of the inverse image `(g')^{-1} = (v')^p`
> of abelian sheaves, which Stacks 00XR produces for a continuous and cocontinuous `v'`, and
> right exactness of a left adjoint is automatic, so left exactness is the whole of the condition.
>
> Both `Rf_*` and `Rf'_*` are the total right derived functors of the degreewise direct images;
> nothing about them is assumed. The source's proof is followed exactly: condition (6) and
> Stacks 08BJ make `(g')^{-1}` preserve K-injectivity *of abelian sheaves*, Stacks 0FN2 gives the
> underived identity there, and Stacks 0D6J carries the resulting statement — that the inverse
> image of a K-injective complex of `O_C`-modules computes `Rf'_*` — back to modules.

```lean
def inverseImageCompTotalDerivedPushforwardIsoOfExactLowerShriek
    [PreservesFiniteLimits (v'.sheafPullback AddCommGrpCat.{u} J' J)]
    (fSharp : OD ⟶ (u.sheafPushforwardContinuous RingCat.{u} K J).obj OC)
    (hsq : v ⋙ u = u' ⋙ v')
    (hcomm : f'Sharp = restrictStructureMap J' J K' K u u' v v' OC OD fSharp hsq) :
    (inverseImage.{u} J' J v' OC).mapDerivedCategory ⋙
        UnboundedComplexes.totalRightDerivedOfAdditive
          (_root_.SheafOfModules.pushforward.{u} f'Sharp) ≅
      UnboundedComplexes.totalRightDerivedOfAdditive
          (_root_.SheafOfModules.pushforward.{u} fSharp) ⋙
        (inverseImage.{u} K' K v OD).mapDerivedCategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.37, Tag 07AB](https://stacks.math.columbia.edu/tag/07AB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
