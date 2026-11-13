---
declaration: section
origin: cited
lean: Stacks.Topology.LocallyQuasiCompactZariskiSituation.isContinuous_id_zariski_qc, Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcComparisonMorphism, Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiComparisonMorphism, Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalMorphism, IsQcCovering.of_isOpenEmbedding, IsQcCovering.of_iSup_eq_top, Stacks.Topology.LocallyQuasiCompactHausdorff.qcPretopology, Stacks.Topology.LocallyQuasiCompactHausdorff.qcTopology
statement: formalized
proof: formalized
---

# 21.31 Cohomology on Hausdorff and locally quasi-compact spaces

Section 21.31 of the Stacks Project, [Tag 09WY](https://stacks.math.columbia.edu/tag/09WY). 13 tags here are carried by 76 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09WY, the section

[Tag 09WY](https://stacks.math.columbia.edu/tag/09WY) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isContinuous_id_zariski_qc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L112). The attribute's comment: “ε\_X comes from the identity functor of LC/X, which is continuous”.

> A quasi-compact sheaf on a localized site is a Zariski sheaf.

```lean
theorem isContinuous_id_zariski_qc (X : S.category) :
    (Functor.id (Over X)).IsContinuous (S.zariskiTopology.over X)
      (S.qcSite.grothendieckTopology.over X)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L163). The attribute's comment: “the induced morphism ε\_X : LC\_qc/X → LC\_Zar/X”.

> The change-of-topology morphism of topoi `ε_X : Sh(LC_qc/X) → Sh(LC_Zar/X)`.

```lean
def qcComparisonMorphism (X : S.category) :
    MorphismOfTopoi
      (Sheaf (S.qcSite.grothendieckTopology.over X) (Type (max u t)))
      (Sheaf (S.zariskiTopology.over X) (Type (max u t)))
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L178). The attribute's comment: “the morphism π\_X : Sh(LC\_Zar/X) → Sh(X)”.

> The Zariski comparison morphism of topoi `π_X : Sh(LC_Zar/X) → Sh(X)`.

```lean
def zariskiComparisonMorphism (X : S.category) :
    MorphismOfTopoi
      (Sheaf (S.zariskiTopology.over X) (Type (max u t)))
      (Sheaf (Opens.grothendieckTopology X.obj) (Type (max u t)))
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L190). The attribute's comment: “the morphism of topoi a\_X = π\_X ∘ ε\_X : Sh(LC\_qc/X) → Sh(X)”.

> The comparison morphism of topoi `a_X : Sh(LC_qc/X) → Sh(X)`, defined as the composite
> `π_X ∘ ε_X`.

```lean
def qcTopologicalMorphism (X : S.category) :
    MorphismOfTopoi
      (Sheaf (S.qcSite.grothendieckTopology.over X) (Type (max u t)))
      (Sheaf (Opens.grothendieckTopology X.obj) (Type (max u t)))
```

**`IsQcCovering.of_isOpenEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L73). The attribute's comment: “an open covering of an object of LC is a qc covering”.

> **An open covering is a qc covering.** A jointly surjective family of open embeddings into a
> locally quasi-compact space is a qc covering: a point `x` lies in the image of some `fᵢ`, which
> is open, so `x` has a quasi-compact neighbourhood `K` inside that image, and `K` is the image of
> the quasi-compact set `fᵢ⁻¹(K)`.

```lean
theorem IsQcCovering.of_isOpenEmbedding {ι : Type*} {X : ι → Type*} {Y : Type*}
    [∀ i, TopologicalSpace (X i)] [TopologicalSpace Y] [LocallyCompactSpace Y]
    {f : ∀ i, X i → Y} (hf : ∀ i, IsOpenEmbedding (f i))
    (hsurj : ∀ y, ∃ i, y ∈ Set.range (f i)) : IsQcCovering f
```

**`IsQcCovering.of_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L92). The attribute's comment: “an open covering of an object of LC is a qc covering”.

> **An open covering `X = ⋃ Uᵢ` gives a qc covering `{Uᵢ → X}`**, for a locally quasi-compact
> space `X`.

```lean
theorem IsQcCovering.of_iSup_eq_top {ι : Type*} {X : Type*} [TopologicalSpace X]
    [LocallyCompactSpace X] (U : ι → TopologicalSpace.Opens X) (hU : iSup U = ⊤) :
    IsQcCovering (fun i => (Subtype.val : U i → X))
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.qcPretopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L208). The attribute's comment: “LC with the collection of qc coverings forms a site”.

> **`LC` with its qc coverings is a site.** The qc coverings of Stacks 09X0 form a
> pretopology on `LC`, by Stacks 09X1.

```lean
noncomputable def qcPretopology : Pretopology LocallyQuasiCompactHausdorff.{u}
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.qcTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L213). The attribute's comment: “the qc topology on LC”.

> The qc topology on `LC`: the Grothendieck topology generated by the qc coverings.

```lean
def qcTopology : GrothendieckTopology LocallyQuasiCompactHausdorff.{u}
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.comap_precoverage_le_qcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L225). The attribute's comment: “the qc topology is stronger than the usual one”.

> **The qc topology is stronger than the usual one.** Every open covering of an object of
> `LC`, i.e. every jointly surjective family of open embeddings, is a qc covering, because the
> objects of `LC` are locally quasi-compact.

```lean
theorem comap_precoverage_le_qcPrecoverage :
    TopCat.precoverage.comap locallyQuasiCompactHausdorffToTop.{u} ≤ qcPrecoverage
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.toGrothendieck_comap_precoverage_le_qcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcTopology.lean#L241). The attribute's comment: “the qc topology is stronger than the usual one, as topologies”.

> The topology of open coverings of `LC` is coarser than the qc topology.

```lean
theorem toGrothendieck_comap_precoverage_le_qcTopology :
    (TopCat.precoverage.comap locallyQuasiCompactHausdorffToTop.{u}).toGrothendieck ≤
      qcTopology
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean#L213). The attribute's comment: “the topology of the site LC\_Zar”.

> The Zariski Grothendieck topology, on the same category as the quasi-compact site.

```lean
def zariskiTopology
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) :
    GrothendieckTopology S.category
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiObjectCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean#L283). The attribute's comment: “the cohomology H^n\_Zar(U, H) over an object U of LC\_Zar/X”.

> Cohomology of an abelian sheaf on the localized Zariski site `LC_Zar/X`, over an object `U`
> over `X`.

```lean
abbrev zariskiObjectCohomology
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category)
    (F : Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})
    (U : Over X) (n : ℕ)
    [HasSheafify ((S.zariskiTopology.over X).over U) AddCommGrpCat.{max (u + 1) v}]
    [HasExt.{a} (Sheaf ((S.zariskiTopology.over X).over U)
      AddCommGrpCat.{max (u + 1) v})] : Type a
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.opensToSlice`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean#L297). The attribute's comment: “the functor X\_Zar → LC\_Zar/X, U ↦ U”.

> The open subsets of `X`, as objects over `X`: the functor `Opens X ⥤ LC_Zar/X` sending an
> open `U` to the open immersion `U → X`. The accompanying property fixes the underlying map of
> `U` as the open embedding with image exactly `U`, which determines the functor up to the unique
> isomorphism over `X`.

```lean
noncomputable def opensToSlice
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category) :
    {F : Opens X.obj ⥤ Over X // ∀ U : Opens X.obj,
      Topology.IsOpenEmbedding ((F.obj U).hom : ((F.obj U).left).obj → X.obj) ∧
      Set.range ((F.obj U).hom : ((F.obj U).left).obj → X.obj) = U.1}
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.opensToSlice_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSite.lean#L478). The attribute's comment: “the functor X\_Zar → LC\_Zar/X is continuous”.

> The open-subset functor is continuous from the small Zariski site of `X` to the localized
> Zariski site of `LC`, so it induces the comparison morphism of topoi.

```lean
theorem opensToSlice_isContinuous
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category) :
    (S.opensToSlice X).1.IsContinuous (Opens.grothendieckTopology X.obj)
      (S.zariskiTopology.over X)
```

**`Stacks.Topology.opens_hasPullbacks_and_hasTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L71). The attribute's comment: “X\_Zar has fibre products and a final object”.

> **`X_Zar` has fibre products and a final object.** The category of open subsets of a
> topological space has fibre products (intersections) and a final object (the whole space).

```lean
theorem opens_hasPullbacks_and_hasTerminal (X : TopCat.{u}) :
    HasPullbacks (Opens X) ∧ HasTerminal (Opens X)
```

**`Stacks.Topology.sheaf_opens_grothendieckTopology_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L78). The attribute's comment: “the equality Sh(X\_Zar) = Sh(X)”.

> **`Sh(X_Zar) = Sh(X)`.** The sheaves on the small site `X_Zar` of open subsets of `X` are by
> definition the sheaves on the topological space `X`.

```lean
theorem sheaf_opens_grothendieckTopology_eq (X : TopCat.{u}) (A : Type*) [Category* A] :
    Sheaf (Opens.grothendieckTopology X) A = TopCat.Sheaf A X
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.ofArrows_mem_zariskiPrecoverage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L92). The attribute's comment: “the site LC\_Zar: the coverings of LC\_qc by open immersions”.

> **The coverings of `LC_Zar`.** A family of morphisms of `LC_qc` is a covering of `LC_Zar`
> exactly when it is a covering of `LC_qc` all of whose members are open immersions. A family of
> open immersions is a qc covering iff it is jointly surjective: a qc covering is jointly
> surjective, and an open covering is a qc covering because the target is locally quasi-compact.

```lean
theorem ofArrows_mem_zariskiPrecoverage_iff {ι : Type*} {T : S.category}
    {Y : ι → S.category} (f : ∀ i, Y i ⟶ T) :
    Presieve.ofArrows Y f ∈ S.zariskiPrecoverage T ↔
      Presieve.ofArrows Y f ∈ S.qcSite.pretopology T ∧
        ∀ i, IsOpenEmbedding (f i : (Y i).obj → T.obj)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isContinuous_id_zariskiTopology_qc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L120). The attribute's comment: “the identity functor LC\_Zar → LC\_qc is continuous”.

> **The identity functor `LC_Zar → LC_qc` is continuous**, because every covering of `LC_Zar`
> is a covering of `LC_qc`.

```lean
theorem isContinuous_id_zariskiTopology_qc :
    (𝟭 S.category).IsContinuous S.zariskiTopology S.qcSite.grothendieckTopology
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcSiteComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L185). The attribute's comment: “the morphism of sites ε : LC\_qc → LC\_Zar”.

> **The morphism of sites `ε : LC_qc → LC_Zar`.** The identity functor `LC_Zar → LC_qc` is
> continuous (`isContinuous_id_zariskiTopology_qc`) and its induced functor on sheaves of sets,
> qc sheafification `qcSiteInverseImage`, is exact (`qcSiteInverseImage_preservesFiniteLimits`,
> `qcSiteInverseImage_preservesFiniteColimits`); so it defines a morphism of sites, whose morphism
> of topoi `Sh(LC_qc) → Sh(LC_Zar)` is this one.

```lean
noncomputable def qcSiteComparisonMorphism :
    MorphismOfTopoi
      (Sheaf S.qcSite.grothendieckTopology (Type (max u t)))
      (Sheaf S.zariskiTopology (Type (max u t)))
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.opensToSlice_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiSiteComparison.lean#L198). The attribute's comment: “the functor X\_Zar → LC\_Zar/X commutes with fibre products and final object”.

> **The functor `X_Zar → LC_Zar/X` commutes with fibre products and the final object.** The
> functor `U ↦ (U → X)` is representably flat, so it preserves all finite limits; in particular it
> carries intersections of opens to fibre products and `X` to the final object `id : X → X`.

```lean
theorem opensToSlice_preservesFiniteLimits (X : S.category) :
    PreservesFiniteLimits (S.opensToSlice X).1
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffCat.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffCat.lean#L48). The attribute's comment: “the category LC of Hausdorff and locally quasi-compact spaces”.

> The category of Hausdorff, locally quasi-compact topological spaces and continuous
> maps.

```lean
abbrev LocallyQuasiCompactHausdorff
```

**`Stacks.Topology.t2Space_and_locallyCompactSpace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean#L47). The attribute's comment: “Hausdorff and locally quasi-compact is the literature's locally compact”.

> **The convention "Hausdorff and locally quasi-compact".** A topological space is Hausdorff
> and locally quasi-compact (every point has a fundamental system of quasi-compact
> neighbourhoods) if and only if it is *locally compact* in the sense often used in the
> literature: Hausdorff, with every point having a quasi-compact neighbourhood.

```lean
theorem t2Space_and_locallyCompactSpace_iff (X : Type u) [TopologicalSpace X] :
    T2Space X ∧ LocallyCompactSpace X ↔ T2Space X ∧ WeaklyLocallyCompactSpace X
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.isSeparatedMap_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean#L56). The attribute's comment: “any morphism of LC is a separated continuous map”.

> **Morphisms of `LC` are separated.** The source of a morphism of `LC` is Hausdorff, so the
> morphism is a separated continuous map.

```lean
theorem isSeparatedMap_hom {X Y : LocallyQuasiCompactHausdorff.{u}} (f : X ⟶ Y) :
    IsSeparatedMap f.hom
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.isProperMap_iff_isUniversallyClosedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/LocallyQuasiCompactHausdorffProper.lean#L63). The attribute's comment: “a morphism of LC is proper iff it is universally closed”.

> **A morphism of `LC` is proper iff it is universally closed.** Proper means separated and
> universally closed, and every morphism of `LC` is separated.

```lean
theorem isProperMap_iff_isUniversallyClosedMap {X Y : LocallyQuasiCompactHausdorff.{u}}
    (f : X ⟶ Y) :
    StacksDraft.Topology.IsProperMap.{u, u, w} f.hom ↔
      StacksDraft.Topology.IsUniversallyClosedMap.{u, u, w} f.hom
```

## Tag 09WZ, a lemma

[Tag 09WZ](https://stacks.math.columbia.edu/tag/09WZ) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactHausdorff.hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean#L96). The attribute's comment: “fibre\_products”.

> **Stacks 09WZ, the fibre-product clause.** The category of Hausdorff, locally
> quasi-compact spaces has fibre products.

```lean
public noncomputable instance hasPullbacks :
    HasPullbacks (LocallyQuasiCompactHausdorff.{u})
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.hasTerminal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean#L119). The attribute's comment: “final\_object”.

> **Stacks 09WZ, the final-object clause.** The category of Hausdorff, locally
> quasi-compact spaces has a final object.

```lean
public instance hasTerminal : HasTerminal LocallyQuasiCompactHausdorff.{u}
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.hasFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/FiniteLimits.lean#L125). The attribute's comment: “finite\_limits”.

> **Stacks 09WZ, the finite-limits clause.** The category of Hausdorff, locally
> quasi-compact spaces has all finite limits: it has a final object and fibre products.

```lean
public noncomputable instance hasFiniteLimits :
    HasFiniteLimits LocallyQuasiCompactHausdorff.{u}
```

**`Stacks.Topology.LocallyQuasiCompactHausdorff.compactSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcFibreProducts.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcFibreProducts.lean#L95). The attribute's comment: “quasi\_compact”.

> **Stacks 09WZ, the quasi-compactness clause.** Given morphisms `f : X ⟶ Z` and
> `g : Y ⟶ Z` of Hausdorff, locally quasi-compact spaces with `X` and `Y` quasi-compact, the
> fibre product `X ×_Z Y` in `LC` is quasi-compact.

```lean
theorem compactSpace_pullback {X Y Z : LocallyQuasiCompactHausdorff.{u}} (f : X ⟶ Z)
    (g : Y ⟶ Z) [CompactSpace X] [CompactSpace Y] :
    CompactSpace (pullback f g : LocallyQuasiCompactHausdorff.{u})
```

## Tag 09X0, a definition

[Tag 09X0](https://stacks.math.columbia.edu/tag/09X0) in the Stacks Project.

Declarations registered for the tag:

- [`IsQcCovering`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcFibreProducts.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcFibreProducts.lean#L67) (StacksFrontier): “qc coverings of locally quasi-compact Hausdorff spaces”.

## Tag 09X1, a lemma

[Tag 09X1](https://stacks.math.columbia.edu/tag/09X1) in the Stacks Project.

**`isQcCovering_of_homeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean#L122). The attribute's comment: “(1)”.

> **Stacks 09X1** (1). If `X' → X` is an isomorphism in `LC`, that is, a homeomorphism of
> Hausdorff locally quasi-compact spaces, then the singleton family `{X' → X}` is a qc covering.

```lean
theorem isQcCovering_of_homeomorph {X' X : Type*}
    [TopologicalSpace X'] [T2Space X'] [WeaklyLocallyCompactSpace X']
    [TopologicalSpace X] [T2Space X] [WeaklyLocallyCompactSpace X]
    (e : X' ≃ₜ X) :
    IsQcCovering (X := fun _ : Unit => X') (fun _ => (e : X' → X))
```

**`isQcCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean#L142). The attribute's comment: “(2)”.

> **Stacks 09X1** (2). If `f` is a qc covering of `Y` and each `g i` is a qc covering of `X i`,
> then the family of composites `(i, j) ↦ f i ∘ g i j` is a qc covering of `Y`.

```lean
theorem isQcCovering_comp {ι : Type*} {X : ι → Type*} {Y : Type*}
    {J : ι → Type*} {Z : ∀ i, J i → Type*}
    [∀ i, TopologicalSpace (X i)] [TopologicalSpace Y]
    [∀ i, T2Space (X i)] [∀ i, WeaklyLocallyCompactSpace (X i)]
    [T2Space Y] [WeaklyLocallyCompactSpace Y]
    [∀ i j, TopologicalSpace (Z i j)]
    [∀ i j, T2Space (Z i j)] [∀ i j, WeaklyLocallyCompactSpace (Z i j)]
    (f : ∀ i, X i → Y) (hf : ∀ i, Continuous (f i))
    (g : ∀ i (j : J i), Z i j → X i)
    (hcov : IsQcCovering f)
    (hcov' : ∀ i, IsQcCovering (g i)) :
    IsQcCovering (X := fun p : Σ i, J i => Z p.1 p.2)
      (fun p => f p.1 ∘ g p.1 p.2)
```

**`isQcCovering_base_change`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCoveringAxioms.lean#L175). The attribute's comment: “(3)”.

> **Stacks 09X1** (3). If `f` is a qc covering of `Y` and `h : X' → Y` is a morphism of `LC`,
> then the family of projections `pr_{X'} : X' ×_Y X i → X'` is a qc covering of `X'`.

```lean
theorem isQcCovering_base_change {ι : Type*} {X : ι → Type*} {Y X' : Type*}
    [∀ i, TopologicalSpace (X i)] [TopologicalSpace Y] [TopologicalSpace X']
    [∀ i, T2Space (X i)] [∀ i, WeaklyLocallyCompactSpace (X i)]
    [T2Space Y] [WeaklyLocallyCompactSpace Y]
    [T2Space X'] [WeaklyLocallyCompactSpace X']
    (f : ∀ i, X i → Y) (hf : ∀ i, Continuous (f i))
    (h : X' → Y) (hh : Continuous h)
    (hcov : IsQcCovering f) :
    IsQcCovering (X := fun i => FiberProd h (f i))
      (fun i => FiberProd.prX' h (f i))
```

## Tag 09X5, a lemma

[Tag 09X5](https://stacks.math.columbia.edu/tag/09X5) in the Stacks Project.

**`proper_surjective_isQcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperSurjectiveQcCovering.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperSurjectiveQcCovering.lean#L69).

> **Stacks Tag 09X5 / Lemma 21.31.4.** Let `X` and `Y` be Hausdorff and
> locally quasi-compact topological spaces (objects of `LC`) and let `f : X → Y`
> be continuous (a morphism of `LC`). If `f` is proper and surjective, then the
> family `{f : X → Y}` is a qc covering.

```lean
theorem proper_surjective_isQcCovering {X Y : Type*}
    [TopologicalSpace X] [TopologicalSpace Y]
    [T2Space X] [LocallyCompactSpace X] [T2Space Y] [LocallyCompactSpace Y]
    (f : X → Y) (hproper : IsProperMap f)
    (hsurj : Function.Surjective f) :
    IsQuasiCompactCovering f
```

## Tag 09X2, a remark

[Tag 09X2](https://stacks.math.columbia.edu/tag/09X2) in the Stacks Project.

**`Stacks.Topology.exists_boundedLCSubcategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/BoundedSubcategory.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/BoundedSubcategory.lean#L268). The attribute's comment: “the bounded subcategory LC\_α”.

> **Stacks 09X2, the bounded-subcategory clause.** Any prescribed small set of Hausdorff,
> locally quasi-compact spaces is contained in a bounded full subcategory of `LC` which is
> closed under existing countable limits and colimits and under the cardinal bound of
> Equation 046U.

```lean
theorem exists_boundedLCSubcategory
    (S₀ : Set LocallyQuasiCompactHausdorff.{u}) [Small.{u} S₀] :
    Nonempty (BoundedLCSubcategory S₀)
```

**`Stacks.Topology.LocallyQuasiCompactQcSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSite.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSite.lean#L201). The attribute's comment: “the site LC\_qc”.

> **Stacks 09X2, the site clause.** The data defining the big quasi-compact site `LC_qc`.
>
> Its objects form the cardinal-cutoff bounded subcategory supplied by
> `Stacks.Topology.BoundedLCSubcategory`, with an additional representative condition for the
> prescribed cardinal bound. Its chosen pretopology is represented by quasi-compact covering
> families indexed in `Type w`, and every quasi-compact presieve has a combinatorially
> equivalent chosen representative.

```lean
structure LocallyQuasiCompactQcSite
    (initialObjects : Set LocallyQuasiCompactHausdorff.{u})
    (bound : Cardinal.{u} → Cardinal.{u})
```

**`Stacks.Topology.exists_locallyQuasiCompactQcSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSite.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSite.lean#L434). The attribute's comment: “the set of coverings”.

> **Stacks 09X2, the covering-set clause.** On any prescribed bounded subcategory `LC_α` of
> `LC` there is a set of quasi-compact covering families which forms a pretopology and contains a
> combinatorially equivalent representative of every quasi-compact covering family; that is, the
> quasi-compact site `LC_qc` exists on `LC_α`.
>
> The set of coverings is the one generated by *all* quasi-compact families: the three site
> axioms are Stacks 09X1, and the representative condition is satisfied by the family itself,
> which is legitimate because the families on `LC_α` indexed in `Type (u + 1)` already form a
> set.

```lean
theorem exists_locallyQuasiCompactQcSite
    (S₀ : Set LocallyQuasiCompactHausdorff.{u})
    (B : BoundedLCSubcategory S₀) :
    ∃ S : LocallyQuasiCompactQcSite.{u, u + 1} S₀ Cardinal.stacksBound,
      S.boundedSubcategory = B
```

**`Stacks.Topology.LocallyQuasiCompactQcSite.mem_smallPretopology_iff_isQcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L193). The attribute's comment: “the coverings of a small model of LC\_qc are the quasi-compact coverings”.

> **Stacks 09X2, the smallness clause.** The small model really is the quasi-compact site: a
> presieve of it is covering exactly when the sieve it generates, read in `LC_qc`, is refined by a
> quasi-compact covering family.
>
> The pretopology of the small model is the maximal one generating the transported topology, so
> membership in it unwinds to membership of a generated sieve in the topology generated by the
> chosen set `Cov` of quasi-compact coverings, which is `isCovering_iff_isQcCovering`.

```lean
theorem mem_smallPretopology_iff_isQcCovering {Y : S.smallSite} (R : Presieve Y) :
    R ∈ S.smallPretopology Y ↔
      ∃ E : PreZeroHypercover.{u + 1} (S.smallEquivalence.inverse.obj Y),
        S.IsQcCovering E ∧
          E.presieve₀ ≤
            ((Sieve.generate R).functorPushforward S.smallEquivalence.inverse).arrows
```

**`Stacks.Topology.LocallyQuasiCompactQcSite.smallSheafEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L238). The attribute's comment: “LC\_qc and a small model of it have the same topos”.

> **Stacks 09X2, the topos clause.** Sheaves on `LC_qc` and sheaves on its small model are the
> same, at any coefficients. The comparison is a dense subsite inclusion for the transported
> topology, so restriction along it is an equivalence.

```lean
def smallSheafEquiv (A : Type t₁) [Category.{t₂} A] :
    Sheaf S.grothendieckTopology A ≌ Sheaf S.smallTopology A
```

## Tag 09X3, a lemma

[Tag 09X3](https://stacks.math.columbia.edu/tag/09X3) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcDirectImageTopologicalInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean#L87). The attribute's comment: “the identification eps\_\{X,*}a\_X^\{-1} = pi\_X^\{-1} on sheaves of sets”.

> **Stacks 09X3, the identification `ε_{X,*} a_X^{-1} = π_X^{-1}`.** Direct image along the
> change-of-topology morphism undoes quasi-compact sheafification on the Zariski comparison
> inverse images, because those are already quasi-compact sheaves.

```lean
def qcDirectImageTopologicalInverseImageIso (X : S.category) :
    qcTopologicalInverseImage.{u, w, t} S X ⋙ qcDirectImage.{u, w, t} S X ≅
      comparisonInverseImage.{u, w, t} S X
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalInverseImage_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean#L108). The attribute's comment: “full faithfulness of the composite inverse image a\_X^\{-1} on sheaves of sets”.

> **Stacks 09X3, full faithfulness of `a_X^{-1}`.** The inverse image along the comparison
> morphism `a_X = π_X ∘ ε_X : Sh(LC_qc/X) → Sh(X)` is full and faithful on sheaves of sets.
>
> This is the sentence Stacks 0DAG opens with, for the bottom horizontal arrow of the diagram of
> Stacks 0DAF: `(h_{-1})^{-1}` is fully faithful with quasi-inverse `h_{-1,*}`.
>
> Composing with `ε_{X,*}` gives `π_X^{-1}` up to the isomorphism
> `qcDirectImageTopologicalInverseImageIso`; that composite is therefore fully faithful, and
> `ε_{X,*}` is faithful, so `a_X^{-1}` is fully faithful.

```lean
theorem qcTopologicalInverseImage_fullyFaithful (X : S.category) :
    (qcTopologicalInverseImage.{u, w, t} S X).Full ∧
      (qcTopologicalInverseImage.{u, w, t} S X).Faithful
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalAdjunction_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonEmbedding.lean#L129). The attribute's comment: “the unit of a\_X^\{-1} is invertible on sheaves of sets”.

> **Stacks 09X3, the quasi-inverse clause.** The unit of the adjunction
> `a_X^{-1} ⊣ a_{X,*}` of the comparison morphism of topoi is an isomorphism: `a_{X,*}` recovers
> every sheaf on the space from its inverse image.

```lean
theorem qcTopologicalAdjunction_unit_isIso (X : S.category) :
    IsIso (qcTopologicalMorphism.{u, w, t} S X).adj.unit
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isSheaf_qc_germSectionsPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcGermSectionsSheaf.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcGermSectionsSheaf.lean#L208). The attribute's comment: “the qc sheaf condition”.

> The presheaf on the localized quasi-compact site `LC_qc/X'` whose sections over
> `h : W ⟶ X'` are the global sections of the germ-model inverse image `h^{-1}F` is a sheaf.

```lean
theorem isSheaf_qc_germSectionsPresheaf
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X' : S.category)
    (F : Sheaf (Opens.grothendieckTopology X'.obj) (Type (max u t))) :
    Presheaf.IsSheaf (S.qcSite.grothendieckTopology.over X')
      (germSectionsPresheaf S X' F)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isIso_toSheafify_comparisonInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcGermSectionsSheaf.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcGermSectionsSheaf.lean#L296). The attribute's comment: “the composite inverse image”.

> The unit of quasi-compact sheafification is an isomorphism on the comparison inverse image
> `π_{X'}^{-1}F`: `ε_{X'}^{-1}π_{X'}^{-1}F` is `π_{X'}^{-1}F`.

```lean
theorem isIso_toSheafify_comparisonInverseImage
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X' : S.category)
    (F : Sheaf (Opens.grothendieckTopology X'.obj) (Type (max u t))) :
    IsIso (toSheafify (S.qcSite.grothendieckTopology.over X')
      ((comparisonInverseImage.{u, w, t} S X').obj F).obj)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isSheaf_germSectionsPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiGermSectionsSheaf.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiGermSectionsSheaf.lean#L262). The attribute's comment: “the Zariski sheaf condition”.

> **The germ-model sections presheaf is a sheaf.** The presheaf on the localized Zariski site
> `LC_Zar/X'` whose sections over `h : W ⟶ X'` are the global sections of the germ-model inverse
> image `h^{-1}F` satisfies the sheaf condition for the localized Zariski topology: an open covering
> of `W` by objects of the site and a family of germ sections agreeing on the overlaps determine a
> unique germ section on `W`. This is the first assertion of Stacks 09X3.

```lean
theorem isSheaf_germSectionsPresheaf
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X' : S.category)
    (F : Sheaf (Opens.grothendieckTopology X'.obj) (Type (max u t))) :
    Presheaf.IsSheaf (S.zariskiTopology.over X') (germSectionsPresheaf S X' F)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.germSectionsPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiProperBaseChangeClause.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiProperBaseChangeClause.lean#L93). The attribute's comment: “the sections formula on LC\_Zar/X”.

> **The sections formula of Stacks 09X3 for the Zariski site, naturally in the object of the
> localized site.** For an object `X'` of the locally quasi-compact Zariski site and a sheaf of sets
> `F` on its space, the comparison inverse image `π_{X'}^{-1}F` is the germ-model sections presheaf
>
> `(h : W ⟶ X') ↦ Γ(W, h^{-1}F)`,
>
> as presheaves on the localized Zariski site `LC_Zar/X'`.
>
> The identification is read off the universal property rather than computed on either side: the
> germ-model sections sheaf corepresents morphisms out of the comparison inverse image
> (`germSectionsMapOutProperty`), which the comparison inverse image corepresents by its own
> adjunction, so the two agree.

```lean
def germSectionsPresheafIso (X' : S.category)
    (F : Sheaf (Opens.grothendieckTopology X'.obj) (Type (max u t))) :
    ((comparisonInverseImage.{u, w, t} S X').obj F).obj ≅ germSectionsPresheaf S X' F
```

## Tag 0DCU, a lemma

[Tag 0DCU](https://stacks.math.columbia.edu/tag/0DCU) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.properDirectImageComparisonIsoOfProperMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperBaseChangeSurjective.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperBaseChangeSurjective.lean#L603). The attribute's comment: “proper\_direct\_image”.

> **Stacks 0DCU, clause (7a): the proper direct image clause.** For a proper morphism `f` of
> the locally quasi-compact Zariski site, ordinary direct image of sheaves of sets along the
> underlying continuous map commutes with inverse image along the comparison morphisms to the
> Zariski slice topoi:
>
> `π_Y^{-1} ∘ f_* ≅ f_{Zar,*} ∘ π_X^{-1}`.
>
> Properness is the only hypothesis. This is `properDirectImageComparisonIso`, whose hypothesis
> on the `Y`-side counit is discharged by `isIso_properBaseChangeCounit`, which is proper base
> change for sheaves of sets, Stacks 0D90, in the form the Zariski comparison needs.

```lean
def properDirectImageComparisonIsoOfProperMap
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u}
      (((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f) : X.obj → Y.obj)) :
    TopCat.Sheaf.pushforward (Type (max (u + 1) v))
        ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f) ⋙
      S.comparisonInverseImage.{u, w, max (u + 1) v} Y ≅
    S.comparisonInverseImage.{u, w, max (u + 1) v} X ⋙
      (zariskiSliceMorphism.{u, w, max (u + 1) v} S f).pushforward
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.properDerivedImageComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperDerivedImageIso.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperDerivedImageIso.lean#L349). The attribute's comment: “proper\_derived\_image”.

> **[Stacks, Tag 0DCU], the derived clause: the derived Zariski base-change map of a proper
> morphism is an isomorphism.** For `f : X ⟶ Y` a proper morphism of the locally quasi-compact
> Zariski site, the comparison
> `π_Y^{-1} ∘ Rf_* ⟶ Rf_{Zar,*} ∘ π_X^{-1}` of `properDerivedImageComparison` is invertible.
>
> This is `isIso_properDerivedImageComparison_of_locallyZero_cohomologyPresheaf` fed
> `equalizerSieve_mem_over_of_isProperMap`.

```lean
theorem properDerivedImageComparison_isIso
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u}
      (((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f) : X.obj → Y.obj)) :
    IsIso (properDerivedImageComparison.{u, w, v} S f)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.properDerivedImageComparison_isIso_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperDerivedImageIso.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ProperDerivedImageIso.lean#L373). The attribute's comment: “proper\_derived\_image, with the four sheafifications and the three enough-injectives inputs discharged rather than assumed”.

> **[Stacks, Tag 0DCU], the derived clause, with properness as the only hypothesis.** For
> `f : X ⟶ Y` a proper morphism of the locally quasi-compact Zariski site, the comparison
> `π_Y^{-1} ∘ Rf_* ⟶ Rf_{Zar,*} ∘ π_X^{-1}` of `properDerivedImageComparison` is invertible.
>
> The four sheafifications and the three enough-injectives inputs the derived functors are built
> from are not assumed: all four sites are essentially small at this coefficient universe, so
> `hasSheafify_opensSite`, `hasSheafify_zariskiSlice`, `enoughInjectives_spaceSheaf` and
> `enoughInjectives_zariskiSliceSheaf` supply them.

```lean
theorem properDerivedImageComparison_isIso_unconditional
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u}
      (((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f) : X.obj → Y.obj)) :
    letI := hasSheafify_opensSite.{u, w, v} S X
    letI := hasSheafify_opensSite.{u, w, v} S Y
    letI := hasSheafify_zariskiSlice.{u, w, v} S X
    letI := hasSheafify_zariskiSlice.{u, w, v} S Y
    letI := enoughInjectives_spaceSheaf.{u, w, v} S X
    letI := enoughInjectives_spaceSheaf.{u, w, v} S Y
    letI := enoughInjectives_zariskiSliceSheaf.{u, w, v} S X
    IsIso (properDerivedImageComparison.{u, w, v} S f)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiCohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiCohomologyComparison.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiCohomologyComparison.lean#L291). The attribute's comment: “cohomology\_comparison”.

> **The cohomology comparison for the Zariski comparison morphism.** For an abelian sheaf `F`
> on the space of an object `X` of the locally quasi-compact Zariski site, the cohomology of the
> localized Zariski site with coefficients in `π_X^{-1}F` is the cohomology of the space `X` with
> coefficients in `F`:
>
> `H^n_{Zar}(X, π_X^{-1}F) ≅ H^n(X, F)`,
>
> naturally in `F`. This is clause (1) of Stacks 0DCU.

```lean
def zariskiCohomologyComparisonIso (n : ℕ) :
    S.abelianComparisonInverseImage.{u, w, max (u + 1) v} X ⋙
        Sheaf.functorH (S.zariskiTopology.over X) n ≅
      Sheaf.functorH (Opens.grothendieckTopology X.obj) n
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiCohomologyComparisonIso_unconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiCohomologyComparison.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiCohomologyComparison.lean#L327). The attribute's comment: “cohomology\_comparison, with the sheafifications, the injective resolutions and the universe of the Ext-groups discharged rather than assumed”.

> **The cohomology comparison for the Zariski comparison morphism, with no hypothesis.** For
> an abelian sheaf `F` on the space of an object `X` of the locally quasi-compact Zariski site,
>
> `H^n_{Zar}(X, π_X^{-1}F) ≅ H^n(X, F)`,
>
> naturally in `F`. This is clause (1) of Stacks 0DCU.
>
> Nothing is assumed of the two sites: both are essentially small at this coefficient universe, so
> the sheafifications, the injective resolutions and the universe of the `Ext`-groups that
> `Sheaf.functorH` is built from are supplied by `hasSheafify_opensSite`,
> `hasSheafify_zariskiSlice`, `hasInjectiveResolutions_spaceSheaf`,
> `hasInjectiveResolutions_zariskiSliceSheaf`, `hasExt_spaceSheaf` and
> `hasExt_zariskiSliceSheaf`.

```lean
def zariskiCohomologyComparisonIso_unconditional (n : ℕ) :
    letI := hasSheafify_opensSite.{u, w, v} S X
    letI := hasSheafify_zariskiSlice.{u, w, v} S X
    letI := hasExt_spaceSheaf.{u, w, v} S X
    letI := hasExt_zariskiSliceSheaf.{u, w, v} S X
    letI := hasInjectiveResolutions_spaceSheaf.{u, w, v} S X
    letI := hasInjectiveResolutions_zariskiSliceSheaf.{u, w, v} S X
    S.abelianComparisonInverseImage.{u, w, max (u + 1) v} X ⋙
        Sheaf.functorH (S.zariskiTopology.over X) n ≅
      Sheaf.functorH (Opens.grothendieckTopology X.obj) n
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.abelianComparisonAdjunction_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonEmbedding.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonEmbedding.lean#L292). The attribute's comment: “unit\_isomorphism”.

> **Stacks 0DCU, the unit clause.** The unit of the Zariski comparison adjunction on abelian
> sheaves is an isomorphism: the inverse image `π_X^{-1}` is fully faithful, because
> `opensToSlice` is continuous, cocontinuous, full and faithful.

```lean
theorem abelianComparisonAdjunction_unit_isIso
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    (X : S.category) :
    IsIso (S.abelianComparisonAdjunction.{u, w, max (u + 1) v} X).unit
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.abelianComparisonDirectImage_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonExactness.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonExactness.lean#L362). The attribute's comment: “exact\_direct\_image”.

> **Stacks 0DCU, the exact-direct-image clause.** The direct image from the Zariski slice site
> of an object to the Zariski site of its underlying space is exact on abelian sheaves.

```lean
theorem abelianComparisonDirectImage_exact
    {S₀ : Set LocallyQuasiCompactHausdorff.{u}} {Bound : Cardinal.{u} → Cardinal.{u}}
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    (X : S.category) :
    exactFunctor
      (Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})
      (Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v})
      (S.comparisonDirectImage X AddCommGrpCat.{max (u + 1) v})
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiComparisonSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonNaturality.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonNaturality.lean#L398). The attribute's comment: “commutative\_square”.

> **Stacks 0DCU, clause (5): the commutative square of topoi.** The square whose horizontal
> arrows are `f_Zar : Sh(LC_Zar/X) → Sh(LC_Zar/Y)` and `f : Sh(X_Zar) → Sh(Y_Zar)` and whose
> vertical arrows are the comparison morphisms `π_X` and `π_Y` commutes: read on inverse images,
> which is where a morphism of topoi lives, `π_X^{-1} ∘ f^{-1} ≅ f_Zar^{-1} ∘ π_Y^{-1}`.
>
> It is obtained from `zariskiComparisonDirectImageSquareIso` by uniqueness of left adjoints,
> using the specified comparison and slice adjunctions.
>
> The coefficients are types in an arbitrary universe containing the universe of the spaces.

```lean
def zariskiComparisonSquareIso :
    (Opens.map ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f)).sheafPullback
        (Type (max u t))
        (Opens.grothendieckTopology
          ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).obj Y))
        (Opens.grothendieckTopology
          ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).obj X)) ⋙
      comparisonInverseImage.{u, w, t} S X ≅
    comparisonInverseImage.{u, w, t} S Y ⋙ (zariskiSliceMorphism.{u, w, t} S f).inverseImage
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.abelianDerivedComparisonAdjunction_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiDerivedUnit.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiDerivedUnit.lean#L164). The attribute's comment: “derived\_unit”.

> **Stacks 0DCU, the derived-unit clause.** The canonical map from a complex of abelian
> sheaves on the space `X` to the derived direct image of its inverse image on the localized
> Zariski site is an isomorphism, naturally in the complex.

```lean
theorem abelianDerivedComparisonAdjunction_unit_isIso
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    (X : S.category)
    [HasSheafify (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v}]
    [HasSheafify (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v}] :
    IsIso (abelianDerivedComparisonAdjunction.{u, w, v} S X).unit
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.abelianDerivedComparisonAdjunction_unit_isIso_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiDerivedUnit.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiDerivedUnit.lean#L204). The attribute's comment: “derived\_unit, with the two sheafifications discharged rather than assumed”.

> **Stacks 0DCU, the derived-unit clause, with no hypothesis.** The canonical map from a
> complex of abelian sheaves on the space `X` to the derived direct image of its inverse image on
> the localized Zariski site is an isomorphism, naturally in the complex.
>
> The two sheafifications the derived adjunction is built from are not assumed: both sites are
> essentially small at this coefficient universe, so `hasSheafify_opensSite` and
> `hasSheafify_zariskiSlice` supply them.

```lean
theorem abelianDerivedComparisonAdjunction_unit_isIso_unconditional
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    (X : S.category) :
    letI := hasSheafify_opensSite.{u, w, v} S X
    letI := hasSheafify_zariskiSlice.{u, w, v} S X
    IsIso (abelianDerivedComparisonAdjunction.{u, w, v} S X).unit
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.relativeZariskiCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiRelativeCohomology.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiRelativeCohomology.lean#L434). The attribute's comment: “relative\_cohomology”.

> **Stacks 0DCU, clause (6): the relative-cohomology clause.** For a morphism `f : X ⟶ Y` of
> the locally quasi-compact Zariski site and `L ∈ D⁺(Y)`, the cohomology of `π_Y^{-1}L` over the
> object `X/Y` of the localized Zariski site is the cohomology of the space `X` with coefficients
> in `f^{-1}L`:
>
> `H^n_{Zar}(X, π_Y^{-1}L) ≅ H^n(X, f^{-1}L)`,
>
> naturally in `L`.

```lean
def relativeZariskiCohomologyIso
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) {X Y : S.category} (f : X ⟶ Y)
    (n : ℤ)
    [HasSheafify (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v}]
    [HasSheafify (Opens.grothendieckTopology Y.obj) AddCommGrpCat.{max (u + 1) v}]
    [HasSheafify (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v}]
    [HasSheafify (S.zariskiTopology.over Y) AddCommGrpCat.{max (u + 1) v}]
    [EnoughInjectives
      (Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v})]
    [EnoughInjectives
      (Sheaf (Opens.grothendieckTopology Y.obj) AddCommGrpCat.{max (u + 1) v})]
    [EnoughInjectives (Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})]
    [EnoughInjectives (Sheaf (S.zariskiTopology.over Y) AddCommGrpCat.{max (u + 1) v})] :
    (S.abelianComparisonInverseImage.{u, w, max (u + 1) v} Y).rightDerivedFunctorPlus ⋙
        ((sheafSections (S.zariskiTopology.over Y)
            AddCommGrpCat.{max (u + 1) v}).obj (op (Over.mk f))).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max (u + 1) v} n ≅
      ((Opens.map
              ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f)).sheafPullback
            AddCommGrpCat.{max (u + 1) v} (Opens.grothendieckTopology Y.obj)
            (Opens.grothendieckTopology X.obj)).rightDerivedFunctorPlus ⋙
        ((sheafSections (Opens.grothendieckTopology X.obj)
            AddCommGrpCat.{max (u + 1) v}).obj
          (op (⊤ : Opens X.obj))).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max (u + 1) v} n
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.relativeZariskiCohomologyIso_unconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiRelativeCohomology.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiRelativeCohomology.lean#L552). The attribute's comment: “relative\_cohomology, with the four sheafifications and the four enough-injectives inputs discharged rather than assumed”.

> **Stacks 0DCU, clause (6): the relative-cohomology clause, with no hypothesis.** For a
> morphism `f : X ⟶ Y` of the locally quasi-compact Zariski site and `L ∈ D⁺(Y)`,
>
> `H^n_{Zar}(X, π_Y^{-1}L) ≅ H^n(X, f^{-1}L)`,
>
> naturally in `L`.
>
> Nothing is assumed of the two sites. The four sheafifications and the four enough-injectives
> inputs the bounded below right derived functors are built from are supplied by
> `hasSheafify_opensSite`, `hasSheafify_zariskiSlice`, `enoughInjectives_spaceSheaf` and
> `enoughInjectives_zariskiSliceSheaf`, each of which holds because the site in question is
> essentially small at this coefficient universe.

```lean
def relativeZariskiCohomologyIso_unconditional
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) {X Y : S.category} (f : X ⟶ Y)
    (n : ℤ) :
    letI := hasSheafify_opensSite.{u, w, v} S X
    letI := hasSheafify_opensSite.{u, w, v} S Y
    letI := hasSheafify_zariskiSlice.{u, w, v} S X
    letI := hasSheafify_zariskiSlice.{u, w, v} S Y
    letI := enoughInjectives_spaceSheaf.{u, w, v} S X
    letI := enoughInjectives_spaceSheaf.{u, w, v} S Y
    letI := enoughInjectives_zariskiSliceSheaf.{u, w, v} S X
    letI := enoughInjectives_zariskiSliceSheaf.{u, w, v} S Y
    (S.abelianComparisonInverseImage.{u, w, max (u + 1) v} Y).rightDerivedFunctorPlus ⋙
        ((sheafSections (S.zariskiTopology.over Y)
            AddCommGrpCat.{max (u + 1) v}).obj (op (Over.mk f))).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max (u + 1) v} n ≅
      ((Opens.map
              ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f)).sheafPullback
            AddCommGrpCat.{max (u + 1) v} (Opens.grothendieckTopology Y.obj)
            (Opens.grothendieckTopology X.obj)).rightDerivedFunctorPlus ⋙
        ((sheafSections (Opens.grothendieckTopology X.obj)
            AddCommGrpCat.{max (u + 1) v}).obj
          (op (⊤ : Opens X.obj))).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max (u + 1) v} n
```

## Tag 0D92, a lemma

[Tag 0D92](https://stacks.math.columbia.edu/tag/0D92) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.topologyChangeSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L251). The attribute's comment: “change-of-topology square”.

> **Stacks 0D92, the change-of-topology square.** The change-of-topology morphisms commute
> with the morphisms of slice topoi induced by `f`:
> `ε_X^{-1} ∘ f_{Zar}^{-1} ≅ f_{qc}^{-1} ∘ ε_Y^{-1}`.
>
> On direct images the square commutes strictly, because the change-of-topology direct image
> leaves the underlying presheaf unchanged; both sides of the square on inverse images are left
> adjoints of the two sides of that identity, so the isomorphism is the one supplied by uniqueness
> of left adjoints.

```lean
def topologyChangeSquareIso :
    (zariskiSliceMorphism.{u, w, t} S f).inverseImage ⋙ qcInverseImage.{u, w, t} S X ≅
      qcInverseImage.{u, w, t} S Y ⋙ qcSliceInverseImage.{u, w, t} S f
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalComparisonSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L281). The attribute's comment: “topological comparison square”.

> **Stacks 0D92, the topological comparison square.** The comparison morphisms
> `a_X = π_X ∘ ε_X` to sheaves on the underlying spaces commute with the morphisms of slice topoi
> induced by `f`: `a_X^{-1} ∘ g^{-1} ≅ f_{qc}^{-1} ∘ a_Y^{-1}`, where `g` is the underlying
> continuous map of `f`.
>
> It is the Zariski square of Stacks 0DCU followed by the change-of-topology square.

```lean
def qcTopologicalComparisonSquareIso :
    (Opens.map ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).map f)).sheafPullback
        (Type (max u t))
        (Opens.grothendieckTopology
          ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).obj Y))
        (Opens.grothendieckTopology
          ((S.qcSite.inclusion ⋙ locallyQuasiCompactHausdorffToTop).obj X)) ⋙
      qcTopologicalInverseImage.{u, w, t} S X ≅
    qcTopologicalInverseImage.{u, w, t} S Y ⋙ qcSliceInverseImage.{u, w, t} S f
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalProperDirectImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcComparisonNaturality.lean#L395). The attribute's comment: “proper direct image”.

> **Stacks 0D92, the proper direct image clause.** If the underlying continuous map of
> `f : X ⟶ Y` is proper, then direct image of sheaves of sets along it commutes with inverse image
> along the comparison morphisms `a_X`, `a_Y` to sheaves on the underlying spaces:
> `a_Y^{-1} ∘ f_* = f_{qc,*} ∘ a_X^{-1}`.
>
> This is `qcTopologicalBaseChangeMap` with its invertibility supplied by
> `isIso_qcTopologicalBaseChangeMap`.

```lean
def qcTopologicalProperDirectImageIso
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u} ⇑((siteToTop S).map f)) :
    spaceDirectImage S f (Type u) ⋙ qcTopologicalInverseImage.{u, w, u} S Y ≅
      qcTopologicalInverseImage.{u, w, u} S X ⋙ qcSliceDirectImage.{u, w, u} S f
```

## Tag 0EZI, a lemma

[Tag 0EZI](https://stacks.math.columbia.edu/tag/0EZI) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.exists_isPullback_properMorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonSituationData.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonSituationData.lean#L75). The attribute's comment: “condition (0EZ4) of Situation 0EZ3 for the proper maps of LC”.

> A proper arrow of the site admits a base change along an arbitrary arrow, and that base change
> is again proper.

```lean
theorem exists_isPullback_properMorphisms
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    ⦃X Y Y' : S.category⦄ (f : X ⟶ Y) (hf : S.properMorphisms f) (g : Y' ⟶ Y) :
    ∃ (Z : S.category) (q : Z ⟶ X) (p : Z ⟶ Y'),
      IsPullback q p f g ∧ S.properMorphisms p
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiPullbackClass_overMapPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonSituationData.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiComparisonSituationData.lean#L138). The attribute's comment: “condition (0EZ5) of Situation 0EZ3 for the sheaves pulled back from the space”.

> Restriction along an arrow `f : X ⟶ Y` of the site carries the sheaves pulled back from `Y`
> to the sheaves pulled back from `X`: a restriction of `π_Y^{-1}G` is `π_X^{-1}` of the inverse
> image of `G` along the underlying map of `f`.

```lean
theorem zariskiPullbackClass_overMapPullback
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    ⦃X Y : S.category⦄ (f : X ⟶ Y)
    (F : Sheaf (S.zariskiTopology.over Y) AddCommGrpCat.{max (u + 1) v})
    (hF : S.zariskiPullbackClass.{u, w, v} Y F) :
    S.zariskiPullbackClass.{u, w, v} X
      ((S.zariskiTopology.overMapPullback AddCommGrpCat.{max (u + 1) v} f).obj F)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiPullbackClass_rightDerived_overMapPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiHigherDirectImageClass.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiHigherDirectImageClass.lean#L224). The attribute's comment: “condition (4) of Situation 0EZ3 for this situation: all higher direct images along a proper arrow of a sheaf pulled back from the space are again pulled back from the space. This is the field `ComparingTopologies.CohomologyComparison.weakSerre_rightDerived_relocalizationPushforward`, proved outright for every i, with the witness `R^i g_* G` specified rather than obtained from the existential. The five conditions of Situation 0EZ3 are items (1)-(5) of that tag; the `(0EZ4)`/`(0EZ5)`/`(0EZ6)`/`(0EZ7)` names used elsewhere in this directory are this development's own, and this is `(0EZ7)`. ALL FIVE CONDITIONS ARE NOW PROVED: the other four are `morphismProperty_baseChange` and `weakSerre_relocalizationInverseImage` (ZariskiComparisonSituationData.lean), `weakSerre_isSheaf_fine` (`isSheaf_qc_zariskiPullbackClass`, ZariskiPullbackClassQcSheaf.lean) and `covering_refinement` (`exists_zariskiRefinement_properMorphisms`, ZariskiQcCoveringRefinement.lean). SITUATION 0EZ3 IS STILL NOT INSTANTIATED HERE, AND THIS CONDITION IS WHAT BLOCKS IT. The carrier is settled: `CohomologyComparison` is declared for `[SmallCategory C]` with coefficients `Ab` in the carrier's own universe, `S.category` is `Type (u+1)` with morphisms in `Type u`, and the carrier is `CategoryTheory.SmallModel S.category` in `Type u`, `EssentiallySmall.{u} S.category` being the instance `LocallyQuasiCompactQcSite.category_essentiallySmall`. That fixes the coefficients at `AddCommGrpCat.{u}`, where the sheaf condition is proved and where the restriction condition `zariskiPullbackClass_overMapPullback` now also holds, being stated for every `AddCommGrpCat.{max u t}`. THIS condition is stated only at `AddCommGrpCat.{max (u+1) v}`. ONE of the seven inputs of its proof now reaches `AddCommGrpCat.{u}`, being stated for every `AddCommGrpCat.{max u t}`: `abelianComparisonInverseImage_exact` (ZariskiSite.lean). That was the input believed OBSTRUCTED rather than merely unrestated, because it went through `Small.{max (u+1) v} ((S.zariskiTopology.over X).Cover Y)ᵒᵖ` and the slice's covering sieves do live in `Type (u+1)`; it turns out not to need them, and now takes the `essentiallySmall_over` route, its Kan-extension shapes being `u`-small by `small_costructuredArrow_opensToSlice`. The other six still carry `max (u+1) v` -- `topologicalPushforward` and `zariskiBaseChange` (ProperDerivedImage.lean), `isIso_zariskiBaseChange_of_properMap` (AbelianProperDirectImage.lean), `preservesFiniteLimits_zariskiSlicePushforward` (AcyclicityReduction.lean), and `isZero_rightDerived_sliceDirectImage_abelianComparisonInverseImage` with `rightDerivedZariskiBaseChangeIso` here. THE NEXT ONE NEEDS A LEMMA THAT DOES NOT EXIST: restating `preservesFiniteLimits_zariskiSlicePushforward` at `max u t` fails even with both sheafifications built from `essentiallySmall_over`, because `(Over.pullback f).sheafPushforwardContinuous` is a right adjoint only when the left Kan extension along `(Over.pullback f).op` exists, which needs `Small.{max u t} (CostructuredArrow (Over.pullback f).op Z)`. Those comma categories are indexed by `Over Y`, in `Type (u+1)`; at `max (u+1) v` their smallness is free from `Small.{max (u+1) v} α` for every `α : Type (max (u+1) v)` (Sheafification.lean), the one step that really uses `u+1 ≤ max (u+1) v`, and at `max u t` there is no such instance. What is owed is the analogue of `small_costructuredArrow_opensToSlice` for `Over.pullback f`. Past it the rest is RESTATEMENT, made large only because these facts are supplied as INSTANCES and an instance generalized to `max u t` is unusable -- `max u ?t =?= max (u+1) v` is not solvable by instance synthesis -- so each remaining input must take them as local `have`s, across the 32 files here that mention `max (u+1) v`. Transporting the conditions along `equivSmallModel` is also not done”.

> Every higher direct image along a proper arrow `f : X ⟶ Y` of a sheaf pulled back from the
> space `X` is again pulled back from the space `Y`: if `F` lies in `zariskiPullbackClass X` then
> `R^i f_{Zar,*}F` lies in `zariskiPullbackClass Y`, for every `i : ℕ`.

```lean
theorem zariskiPullbackClass_rightDerived_overMapPushforward (hf : S.properMorphisms f)
    (F : Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})
    (hF : S.zariskiPullbackClass.{u, w, v} X F) (i : ℕ) :
    S.zariskiPullbackClass.{u, w, v} Y
      ((((Over.map f).sheafPushforwardCocontinuous AddCommGrpCat.{max (u + 1) v}
        (S.zariskiTopology.over X) (S.zariskiTopology.over Y)).rightDerived i).obj F)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.exists_zariski_properMorphisms_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiProperRefinement.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiProperRefinement.lean#L312). The attribute's comment: “condition (0EZ8) of Situation 0EZ3: a quasi-compact covering is refined by a Zariski covering, then one proper arrow, then a Zariski covering”.

> **Stacks 0EZI**, the refinement condition. Every quasi-compact covering of an object `U` of the
> site is refined in three stages: by a Zariski covering `{V ⟶ U}`, then over each `V` by a single
> proper arrow `f : W ⟶ V` which is itself a quasi-compact covering, and finally by a Zariski
> covering of `W` whose composites factor through the given covering. This is condition (0EZ8) of
> Situation 0EZ3 with the proper arrows as the class `P`, the quasi-compact topology as `τ` and the
> Zariski topology as `τ'`.

```lean
theorem exists_zariski_properMorphisms_refinement
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    (U : S.category) (R : Presieve U) (hR : R ∈ S.qcSite.pretopology U) :
    ∃ T : Presieve U, T ∈ S.zariskiPrecoverage U ∧
      ∀ ⦃V : S.category⦄ (v : V ⟶ U), T v →
        ∃ (W : S.category) (f : W ⟶ V), S.properMorphisms f ∧
          Presieve.singleton f ∈ S.qcSite.pretopology V ∧
            ∃ P : Presieve W, P ∈ S.zariskiPrecoverage W ∧
              P.FactorsThruAlong R (f ≫ v)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isSheaf_qc_zariskiPullbackClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackClassQcSheaf.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackClassQcSheaf.lean#L94). The attribute's comment: “condition (3) of Situation 0EZ3 for this situation: every abelian sheaf on the localized Zariski site that is pulled back from the space satisfies the sheaf condition for quasi-compact coverings. This is the field `ComparingTopologies.CohomologyComparison.weakSerre_isSheaf_fine`, proved outright, with the sheaf on the space and the isomorphism to it taken from the essential image rather than from a choice. The five conditions of Situation 0EZ3 are items (1)-(5) of that tag; the `(0EZ4)`/`(0EZ5)`/`(0EZ6)`/`(0EZ7)` names used elsewhere in this directory are this development's own, and this is `(0EZ6)`. ALL FIVE CONDITIONS ARE NOW PROVED for this situation, but SITUATION 0EZ3 IS STILL NOT INSTANTIATED HERE. `CohomologyComparison` is declared `(C : Type u') [SmallCategory C]` (ChangeOfTopology/ComparisonSituation.lean:117) and takes its coefficients in `Ab.{u'}`, so the carrier's universe fixes the coefficient universe. `S.category` is `Type (u+1)` with morphisms in `Type u`, so `SmallCategory S.category` does not synthesize and the carrier is `CategoryTheory.SmallModel S.category`, in `Type u`; `EssentiallySmall.{u} S.category` IS now an instance, `LocallyQuasiCompactQcSite.category_essentiallySmall`. The coefficients are therefore `AddCommGrpCat.{u}`, which is where this condition is proved and is why the carrier cannot be `AsSmall.{v} S.category`: that one would want `AddCommGrpCat.{max (u+1) v}`, where the germ model this condition is read off cannot even be stated. Condition `(0EZ5)` (`zariskiPullbackClassOfSize_overMapPullback`) is now stated for every `AddCommGrpCat.{max u t}` and so holds at `AddCommGrpCat.{u}`. WHAT BLOCKS THE BRIDGE is condition `(0EZ7)` (`zariskiPullbackClass_rightDerived_overMapPushforward`), still stated only at `AddCommGrpCat.{max (u+1) v}`. ONE of the seven inputs of its proof now reaches `AddCommGrpCat.{u}`: `abelianComparisonInverseImage_exact`, which was the one believed obstructed rather than merely unrestated and turns out not to need the slice's covering sieves at all. The next to move, `preservesFiniteLimits_zariskiSlicePushforward`, needs a lemma the library does not have -- `Small.{max u t} (CostructuredArrow (Over.pullback f).op Z)`, the analogue of `small_costructuredArrow_opensToSlice` for `Over.pullback f`, without which `(Over.pullback f).sheafPushforwardContinuous` is not known to be a right adjoint at `max u t`. Past that the remaining five are a RESTATEMENT rather than new proper-base-change mathematics, made large only because the smallness and sheafification facts are supplied as INSTANCES, which cannot be generalized to `max u t` because `max u ?t =?= max (u+1) v` is not solvable by instance synthesis. See `ZariskiHigherDirectImageClass.lean` for the list. Transport of both precoverages and of the class along `equivSmallModel` is also not done”.

> **Stacks 0EZI.** An abelian sheaf on the localized Zariski site over `X` which is pulled back
> from the space underlying `X` satisfies the sheaf condition for the quasi-compact topology over
> `X`.

```lean
theorem isSheaf_qc_zariskiPullbackClass
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category)
    (G : Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{u})
    (hG : S.zariskiPullbackClassOfSize.{u, w, u} X G) :
    Presheaf.IsSheaf (S.qcSite.grothendieckTopology.over X) G.obj
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiPullbackClass_rightDerived_sliceDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackHigherDirectImage.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackHigherDirectImage.lean#L119). The attribute's comment: “condition (0EZ7) of Situation 0EZ3: higher direct images along a proper arrow stay in the class”.

> **Stacks 0EZI, the condition on higher direct images.** Let `f : X ⟶ Y` be a proper arrow of
> the locally quasi-compact Zariski site and let `G` be an abelian sheaf on the localized Zariski
> site over `X` of the form `π_X^{-1}G₀`. Then for every `i` the higher direct image `R^i f_{Zar,*}G`
> is again of that form: it is `π_Y^{-1}` of the `i`-th higher direct image of `G₀` along the
> continuous map underlying `f`.
>
> This is condition (0EZ7) of Situation 0EZ3 for the data chosen by Stacks 0EZI — the proper arrows
> as the class `P`, the sheaves pulled back from the space as `A'`.

```lean
theorem zariskiPullbackClass_rightDerived_sliceDirectImage
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound)
    ⦃X Y : S.category⦄ (f : X ⟶ Y) (hf : S.properMorphisms f)
    (G : Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})
    (hG : S.zariskiPullbackClass.{u, w, v} X G) (i : ℕ) :
    S.zariskiPullbackClass.{u, w, v} Y
      (((sliceDirectImage S f AddCommGrpCat.{max (u + 1) v}).rightDerived i).obj G)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiPullbackClass_isSheaf_qc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackQcSheaf.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackQcSheaf.lean#L49). The attribute's comment: “condition (0EZ6) of Situation 0EZ3 for the sheaves pulled back from the space”.

> An abelian sheaf on the localized Zariski site over `X` which is pulled back from the space `X`
> is already a sheaf for the quasi-compact topology: `F' = ε_{X,*}ε_X^{-1}F'`.

```lean
theorem zariskiPullbackClass_isSheaf_qc
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category)
    (F : Sheaf (S.zariskiTopology.over X) AddCommGrpCat.{max (u + 1) v})
    (hF : S.zariskiPullbackClass.{u, w, v} X F) :
    Presheaf.IsSheaf (S.qcSite.grothendieckTopology.over X) F.obj
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.zariskiPullbackClass_isWeakSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackWeakSerre.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiPullbackWeakSerre.lean#L149). The attribute's comment: “the class A'\_X of Situation 0EZ3 is a weak Serre class”.

> **Stacks 0EZI, the weak Serre condition on the class `A'_X`.** Situation 0EZ3 requires the
> class it is handed over each object of the site to be a weak Serre subcategory of the abelian
> sheaves on the localized coarse site. For the choice Stacks 0EZI makes — the sheaves of the form
> `π_X^{-1}F` on the localized Zariski site — this holds because `π_X^{-1}` is exact and fully
> faithful and `π_{X,*}` is exact, all three being parts of Stacks 0DCU.

```lean
theorem zariskiPullbackClass_isWeakSerreClass
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category) :
    (S.zariskiPullbackClass.{u, w, v} X).IsWeakSerreClass
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.exists_zariskiRefinement_properMorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiQcCoveringRefinement.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/ZariskiQcCoveringRefinement.lean#L248). The attribute's comment: “condition (5) of Situation 0EZ3 for this situation: the three-stage refinement of a quasi-compact covering, by a Zariski covering, then one proper arrow over each member, then a Zariski covering of its source. This is the field `ComparingTopologies.CohomologyComparison.covering_refinement`, proved outright and carrying no hypothesis beyond the covering itself. The five conditions of Situation 0EZ3 are items (1)-(5) of that tag `(0EZ7)` names used elsewhere in this directory are this development's own. ALL FIVE ARE NOW PROVED for this situation, and Situation 0EZ3 is nevertheless still NOT instantiated here: condition (1) is `morphismProperty_baseChange` (ZariskiComparisonSituationData.lean), condition (2) is `weakSerre_relocalizationInverseImage` (same file), condition (3) is `isSheaf_qc_zariskiPullbackClass` (ZariskiPullbackClassQcSheaf.lean) and condition (4) is `zariskiPullbackClass_rightDerived_overMapPushforward` (ZariskiHigherDirectImageClass.lean). What is missing is one coefficient universe. The carrier of a `CohomologyComparison` has to be `CategoryTheory.SmallModel S.category`, `S.category` having morphisms in `Type u` and only `EssentiallySmall.{u}` `LocallyQuasiCompactQcSite.category_essentiallySmall`, so the small model and `CategoryTheory.equivSmallModel` are available coefficients at `AddCommGrpCat.{u}`. Conditions (1) and (5) are universe-free, (3) is proved there, and (2) now holds at every `AddCommGrpCat.{max u t}`, but (4) is stated only at `AddCommGrpCat.{max (u+1) v}` and every input of its proof carries that universe in its own statement, so it cannot be instantiated at `u` without generalizing the proper-base-change chain. Transporting the five conditions along `equivSmallModel` is also not done”.

> **Stacks 0EZI**, the covering-refinement condition. Every quasi-compact covering `R` of an
> object `U` of the site is refined in three stages: a Zariski covering `Q` of `U`, then over each
> member `v : V ⟶ U` of `Q` a single proper arrow `f : W ⟶ V` which is itself a quasi-compact
> covering of `V`, and then a Zariski covering of `W` all of whose members factor through `R` along
> `f ≫ v`.
>
> The quasi-compact coverings are stated as membership in the underlying precoverage of the site's
> chosen pretopology, which is the same condition.

```lean
theorem exists_zariskiRefinement_properMorphisms
    (U : S.category) (R : Presieve U) (hR : R ∈ S.qcSite.pretopology.toPrecoverage U) :
    ∃ Q : Presieve U, Q ∈ S.zariskiPrecoverage U ∧
      ∀ ⦃V : S.category⦄ (v : V ⟶ U), Q v →
        ∃ (W : S.category) (f : W ⟶ V), S.properMorphisms f ∧
          Presieve.singleton f ∈ S.qcSite.pretopology.toPrecoverage V ∧
          ∃ T : Presieve W, T ∈ S.zariskiPrecoverage W ∧ T.FactorsThruAlong R (f ≫ v)
```

## Tag 0DCY, a lemma

[Tag 0DCY](https://stacks.math.columbia.edu/tag/0DCY) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isIso_qcAbelianComparisonAdjunction_unit_app_and_isZero_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean#L74). The attribute's comment: “clause (1): for `X` in `LC_qc` and an abelian sheaf `F` on `X`, the unit `π_X^{-1}F ⟶ ε_{X,*}a_X^{-1}F` is an isomorphism and `R^i ε_{X,*}(a_X^{-1}F) = 0` for `i > 0`”.

> **Stacks 0DCY (1).** For `X` in `LC_qc` and an abelian sheaf `F` on `X`, the change-of-topology
> unit `π_X^{-1}F ⟶ ε_{X,*}ε_X^{-1}π_X^{-1}F = ε_{X,*}a_X^{-1}F` is an isomorphism, that is
> `ε_{X,*}a_X^{-1}F = π_X^{-1}F`, and `R^i ε_{X,*}(a_X^{-1}F) = 0` for `i > 0`.

```lean
theorem isIso_qcAbelianComparisonAdjunction_unit_app_and_isZero_rightDerived
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category)
    (F : Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v}) :
    IsIso ((qcAbelianComparisonAdjunction.{u, w, v} S X).unit.app
        ((S.abelianComparisonInverseImage.{u, w, max (u + 1) v} X).obj F)) ∧
      ∀ i : ℕ, 0 < i → IsZero (((qcAbelianDirectImage.{u, w, v} S X).rightDerived i).obj
        ((qcTopologicalAbelianInverseImage.{u, w, v} S X).obj F))
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcTopologicalHigherDirectImageIsoOfProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean#L90). The attribute's comment: “clause (2): an isomorphism `a_Y^{-1}(R^i f_* F) ≅ R^i f_{qc,*}(a_X^{-1}F)` for a proper morphism `f : X ⟶ Y` of `LC_qc`, an abelian sheaf `F` on `X` and every `i`”.

> **Stacks 0DCY (2).** For a proper morphism `f : X ⟶ Y` of `LC_qc` and an abelian sheaf `F` on
> `X`, `a_Y^{-1}(R^i f_*F) = R^i f_{qc,*}(a_X^{-1}F)` for every `i`.

```lean
def qcTopologicalHigherDirectImageIsoOfProper
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) {X Y : S.category} (f : X ⟶ Y)
    (hf : S.properMorphisms f) (i : ℕ)
    (F : Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v}) :
    (qcTopologicalAbelianInverseImage.{u, w, v} S Y).obj
        (((spaceDirectImage S f AddCommGrpCat.{max (u + 1) v}).rightDerived i).obj F) ≅
      ((qcAbelianSliceDirectImage.{u, w, v} S f).rightDerived i).obj
        ((qcTopologicalAbelianInverseImage.{u, w, v} S X).obj F)
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isIso_qcDerivedComparisonUnit_app_abelianComparisonInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean#L165). The attribute's comment: “clause (3): for `X` in `LC_qc` and `K` in `D⁺(X)`, the canonical map `π_X^{-1}K ⟶ Rε_{X,*}(a_X^{-1}K)` is an isomorphism”.

> **Stacks 0DCY (3).** For `X` in `LC_qc` and `K` in `D⁺(X)`, the canonical map
> `π_X^{-1}K ⟶ Rε_{X,*}(a_X^{-1}K)` is an isomorphism.

```lean
theorem isIso_qcDerivedComparisonUnit_app_abelianComparisonInverseImage
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) (X : S.category)
    (K : DerivedCategory.Plus
      (Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v})) :
    IsIso ((qcDerivedComparisonUnit.{u, w, v} S X).app
      ((S.abelianComparisonInverseImage.{u, w, max (u + 1) v} X).mapDerivedCategoryPlus.obj
        K))
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isIso_qcTopologicalDerivedBaseChangeMap_app_of_proper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcDerivedComparison.lean#L342). The attribute's comment: “clause (4): for a proper morphism `f : X ⟶ Y` of `LC_qc` and `K` in `D⁺(X)`, the base change map `a_Y^{-1}(Rf_*K) ⟶ Rf_{qc,*}(a_X^{-1}K)` is an isomorphism”.

> **Stacks 0DCY (4).** For a proper morphism `f : X ⟶ Y` of `LC_qc` and `K` in `D⁺(X)`, the
> canonical map `a_Y^{-1}(Rf_*K) ⟶ Rf_{qc,*}(a_X^{-1}K)` is an isomorphism.

```lean
theorem isIso_qcTopologicalDerivedBaseChangeMap_app_of_proper
    (S : LocallyQuasiCompactZariskiSituation.{u, w} S₀ Bound) {X Y : S.category} (f : X ⟶ Y)
    (hf : S.properMorphisms f)
    (K : DerivedCategory.Plus
      (Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v})) :
    IsIso ((qcTopologicalDerivedBaseChangeMap.{u, w, v} S f).app K)
```

## Tag 0D91, a lemma

[Tag 0D91](https://stacks.math.columbia.edu/tag/0D91) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.isIso_qcTopologicalDerivedUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologicalDescent.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologicalDescent.lean#L302). The attribute's comment: “cohomological descent for LC\_qc: for X in LC\_qc and K in D^+(X), the canonical map K -> Ra\_\{X,*}a\_X^\{-1}K is an isomorphism”.

> **Stacks 0D91**: cohomological descent for the quasi-compact site. For `X` an object of
> `LC_qc` and `K` in `D⁺(X)` the canonical map `K ⟶ Ra_{X,*}a_X^{-1}K` is an isomorphism.

```lean
theorem isIso_qcTopologicalDerivedUnit_app
    (K : DerivedCategory.Plus
      (Sheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v})) :
    IsIso ((qcTopologicalDerivedUnit.{u, w, v} S X).app K)
```

## Tag 09X4, a lemma

[Tag 09X4](https://stacks.math.columbia.edu/tag/09X4) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcCohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean#L303). The attribute's comment: “part (1): H^n(X, F) = H^n\_qc(X, a\_X^\{-1}F) for an abelian sheaf F on X, naturally in F, with cohomology read as the right derived functors of global sections”.

> **Stacks 09X4 for abelian sheaves.** For an object `X` of `LC_qc` and an abelian sheaf `F`
> on the space underlying `X`, the cohomology of the localized quasi-compact site with
> coefficients in `a_X^{-1}F` is the cohomology of the space with coefficients in `F`:
>
> `H^n_{qc}(X, a_X^{-1}F) ≅ H^n(X, F)`,
>
> naturally in `F`.

```lean
def qcCohomologyComparisonIso (n : ℕ) :
    qcTopologicalAbelianInverseImage.{u, w, v} S X ⋙
        (qcGlobalSections.{u, w, v} S X).rightDerived n ≅
      (spaceGlobalSections.{u, w, v} S X).rightDerived n
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.constantSheafQcCohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean#L356). The attribute's comment: “the example: H^n(X, A) = H^n\_qc(X, A) for an abelian group A, naturally in A”.

> **Stacks 09X4, the constant-sheaf example.** For an abelian group `A`, the cohomology of the
> space `X` with coefficients in the constant sheaf on `A` is the cohomology of the localized
> quasi-compact site with coefficients in its constant sheaf on `A`:
>
> `H^n(X, A) ≅ H^n_{qc}(X, A)`,
>
> naturally in `A`.

```lean
def constantSheafQcCohomologyComparisonIso (n : ℕ) :
    constantSheaf (Opens.grothendieckTopology X.obj) AddCommGrpCat.{max (u + 1) v} ⋙
        (spaceGlobalSections.{u, w, v} S X).rightDerived n ≅
      constantSheaf (S.qcSite.grothendieckTopology.over X) AddCommGrpCat.{max (u + 1) v} ⋙
        (qcGlobalSections.{u, w, v} S X).rightDerived n
```

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.qcHypercohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcCohomologyComparison.lean#L437). The attribute's comment: “part (2): H^n(X, K) = H^n\_qc(X, a\_X^\{-1}K) for K in D^+(X), naturally in K, with hypercohomology read as the cohomology of the right derived functor of global sections on D^+”.

> **Stacks 09X4 for bounded below complexes.** For an object `X` of `LC_qc` and `K` in
> `D⁺(X)`, the hypercohomology of the space with coefficients in `K` is the hypercohomology of the
> localized quasi-compact site with coefficients in `a_X^{-1}K`:
>
> `H^n(X, K) ≅ H^n_{qc}(X, a_X^{-1}K)`,
>
> naturally in `K`.

```lean
def qcHypercohomologyComparisonIso (n : ℤ) :
    spaceHypercohomology.{u, w, v} S X n ≅
      (qcTopologicalAbelianInverseImage.{u, w, v} S X).mapDerivedCategoryPlus ⋙
        qcHypercohomology.{u, w, v} S X n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.31, Tag 09WY](https://stacks.math.columbia.edu/tag/09WY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
