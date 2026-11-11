---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.associatedAffineChaoticTopology, AlgebraicGeometry.Stack.sheafAssociatedAffineChaoticEquivalence, AlgebraicGeometry.Stack.AffineCategory, AlgebraicGeometry.Stack.AffineCategory.isStronglyCartesian_toAffine, AlgebraicGeometry.Stack.associatedAffineTopology, AlgebraicGeometry.Stack.generate_mem_associatedAffineTopology, AlgebraicGeometry.Stack.AffineCategory.isFiberedInGroupoids_toAffine, AlgebraicGeometry.Stack.AffineCategory.isCoverDense_inclusion
statement: formalized
proof: formalized
---

# 96.24 Restricting to affines

Section 96.24 of the Stacks Project, [Tag 0H08](https://stacks.math.columbia.edu/tag/0H08). 4 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H09, a definition

[Tag 0H09](https://stacks.math.columbia.edu/tag/0H09) in the Stacks Project.

**`AlgebraicGeometry.Stack.associatedAffineChaoticTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L167).

> **Stacks 0H09.** The associated affine site of a category `p : 𝒳 ⥤ (Sch/S)_{fppf}`: the
> affine subcategory `𝒳_{affine}` carrying the chaotic topology, in which the maximal sieve is
> the only covering sieve.

```lean
abbrev associatedAffineChaoticTopology : GrothendieckTopology (AffineCategory B S hS p)
```

**`AlgebraicGeometry.Stack.sheafAssociatedAffineChaoticEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L173). The attribute's comment: “sheaves are presheaves”.

> **Stacks 0H09.** Sheaves on the associated affine site are the same as presheaves on the
> affine subcategory: the forgetful functor from sheaves to presheaves is an equivalence.

```lean
def sheafAssociatedAffineChaoticEquivalence (A : Type*) [Category A] :
    Sheaf (associatedAffineChaoticTopology B S hS p) A ≌ (AffineCategory B S hS p)ᵒᵖ ⥤ A
```

## Tag 0H0A, a definition

[Tag 0H0A](https://stacks.math.columbia.edu/tag/0H0A) in the Stacks Project.

**`AlgebraicGeometry.Stack.AffineCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L102). The attribute's comment: “the affine subcategory”.

> **Stacks 0H0A.** The affine subcategory of a category over the big fppf category of `S`:
> the full subcategory of the objects lying over an affine scheme.

```lean
abbrev AffineCategory
```

**`AlgebraicGeometry.Stack.AffineCategory.isStronglyCartesian_toAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L117). The attribute's comment: “arrows are strongly cartesian”.

> **Stacks 0H0A.** Every arrow between affine objects of a category fibred in groupoids is
> strongly cartesian for the restricted structure functor.

```lean
theorem isStronglyCartesian_toAffine (hp : p.IsFiberedInGroupoids)
    {x y : AffineCategory B S hS p} (φ : y ⟶ x) :
    (toAffine B S hS p).IsStronglyCartesian ((toAffine B S hS p).map φ) φ
```

**`AlgebraicGeometry.Stack.associatedAffineTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L142). The attribute's comment: “the associated affine topology”.

> **Stacks 0H0A.** The associated affine site of a category `p : 𝒳 ⥤ (Sch/S)_{fppf}` and a
> topology `τ` on the affine schemes over `S`: the topology the affine subcategory inherits
> from `τ`.
>
> The five associated affine sites of the source — Zariski, étale, smooth, syntomic and fppf —
> are the values of this at the five big affine topologies.

```lean
abbrev associatedAffineTopology (τ : GrothendieckTopology (BigAffineFppf B S hS)) :
    GrothendieckTopology (AffineCategory B S hS p)
```

**`AlgebraicGeometry.Stack.generate_mem_associatedAffineTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSite.lean#L153). The attribute's comment: “the covering families”.

> **Stacks 0H0A.** A family in the affine subcategory of a category fibred in groupoids whose
> image in the affine schemes over `S` generates a covering sieve generates a covering sieve for
> the associated affine topology.
>
> This is the description of the coverings of `𝒳_{affine, τ}` in the paragraph following the
> source's definition.

```lean
theorem generate_mem_associatedAffineTopology (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology (BigAffineFppf B S hS))
    (E : Covering.{v, w, u + 1} (AffineCategory B S hS p))
    (hE : Sieve.generate (E.2.map (AffineCategory.toAffine B S hS p)).presieve₀ ∈
      τ ((AffineCategory.toAffine B S hS p).obj E.1)) :
    Sieve.generate E.2.presieve₀ ∈ associatedAffineTopology B S hS p τ E.1
```

## Tag 0H0B, a lemma

[Tag 0H0B](https://stacks.math.columbia.edu/tag/0H0B) in the Stacks Project.

**`AlgebraicGeometry.Stack.AffineCategory.isFiberedInGroupoids_toAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean#L168). The attribute's comment: “the affine structure functor is fibred in groupoids”.

> **Stacks 0H0B.** The structure functor of the affine subcategory of a category fibred in
> groupoids is again fibred in groupoids, over the big affine fppf category of `S`.

```lean
theorem isFiberedInGroupoids_toAffine (hp : p.IsFiberedInGroupoids) :
    (toAffine B S hS p).IsFiberedInGroupoids
```

**`AlgebraicGeometry.Stack.AffineCategory.isCoverDense_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean#L205). The attribute's comment: “cover density”.

> **Stacks 0H0B.** The affine inclusion of a category fibred in groupoids is cover dense for
> the inherited topology, as soon as the affine inclusion of the big fppf category over `S` is
> cover dense.

```lean
theorem isCoverDense_inclusion (hp : p.IsFiberedInGroupoids)
    (K : GrothendieckTopology (BigFppfOver B S hS))
    (hj : (BigAffineFppf.inclusion B S hS).IsCoverDense K) :
    (inclusion B S hS p).IsCoverDense (p.inheritedTopology K)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean#L235).

> **Stacks 0H0B.** The inclusion of the affine subcategory of a category fibred in groupoids
> is a special cocontinuous functor from the associated affine site to the associated site, for
> any topology on the big affine fppf category of `S` and any topology on the big fppf category
> over `S` for which the affine inclusion downstairs is a dense subsite inclusion.
>
> Consequently the inclusion induces an equivalence of sheaf topoi. The five topologies of the
> source are the five instances.

```lean
theorem inclusion_isSpecialCocontinuous (hp : p.IsFiberedInGroupoids)
    (J : GrothendieckTopology (BigAffineFppf B S hS))
    (K : GrothendieckTopology (BigFppfOver B S hS))
    (hbase : (BigAffineFppf.inclusion B S hS).IsDenseSubsite J K) :
    IsSpecialCocontinuous (associatedAffineTopology B S hS p J) (p.inheritedTopology K)
      (inclusion B S hS p)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEquivalence.lean#L267). The attribute's comment: “the fppf topology”.

> **Stacks 0H0B** for the fppf topology: the inclusion of the affine subcategory into a
> category fibred in groupoids is special cocontinuous from the associated affine fppf site to
> the associated fppf site, and so induces an equivalence of the sheaf topoi.

```lean
theorem inclusion_isSpecialCocontinuous_fppf (hp : p.IsFiberedInGroupoids) :
    IsSpecialCocontinuous
      (associatedAffineTopology B S hS p (BigAffineFppf.topology B S hS))
      (associatedTopology B S hS p B.topology) (inclusion B S hS p)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEtaleSmooth.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEtaleSmooth.lean#L60). The attribute's comment: “the étale topology”.

> **Stacks 0H0B** for the étale topology: the inclusion of the affine subcategory into a
> category fibred in groupoids is special cocontinuous from the associated affine étale site to
> the associated étale site, and so induces an equivalence of the sheaf topoi.

```lean
theorem inclusion_isSpecialCocontinuous_etale (hp : p.IsFiberedInGroupoids) :
    IsSpecialCocontinuous
      (associatedAffineTopology B S hS p (BigAffineEtale.topology B.toBigEtaleSite S hS))
      (p.inheritedTopology (BigEtaleOver.topology B.toBigEtaleSite S hS))
      (inclusion B S hS p)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEtaleSmooth.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteEtaleSmooth.lean#L72). The attribute's comment: “the smooth topology”.

> **Stacks 0H0B** for the smooth topology: the inclusion of the affine subcategory into a
> category fibred in groupoids is special cocontinuous from the associated affine smooth site to
> the associated smooth site, and so induces an equivalence of the sheaf topoi.

```lean
theorem inclusion_isSpecialCocontinuous_smooth (hp : p.IsFiberedInGroupoids) :
    IsSpecialCocontinuous
      (associatedAffineTopology B S hS p (BigAffineSmooth.topology B.toBigSmoothSite S hS))
      (p.inheritedTopology (BigSmoothOver.topology B.toBigSmoothSite S hS))
      (inclusion B S hS p)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteZariskiSyntomic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteZariskiSyntomic.lean#L56). The attribute's comment: “the Zariski topology”.

> **Stacks 0H0B** for the Zariski topology: the inclusion of the affine subcategory into a
> category fibred in groupoids is special cocontinuous from the associated affine Zariski site to
> the associated Zariski site, and so induces an equivalence of the sheaf topoi.

```lean
theorem inclusion_isSpecialCocontinuous_zariski (hp : p.IsFiberedInGroupoids) :
    IsSpecialCocontinuous
      (associatedAffineTopology B S hS p (BigAffineZariski.topology B.toBigZariskiSite S hS))
      (p.inheritedTopology (BigZariskiOver.topology B.toBigZariskiSite S hS))
      (inclusion B S hS p)
```

**`AlgebraicGeometry.Stack.AffineCategory.inclusion_isSpecialCocontinuous_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteZariskiSyntomic.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineSiteZariskiSyntomic.lean#L68). The attribute's comment: “the syntomic topology”.

> **Stacks 0H0B** for the syntomic topology: the inclusion of the affine subcategory into a
> category fibred in groupoids is special cocontinuous from the associated affine syntomic site to
> the associated syntomic site, and so induces an equivalence of the sheaf topoi.

```lean
theorem inclusion_isSpecialCocontinuous_syntomic (hp : p.IsFiberedInGroupoids) :
    IsSpecialCocontinuous
      (associatedAffineTopology B S hS p (BigAffineSyntomic.topology B.toBigSyntomicSite S hS))
      (p.inheritedTopology (BigSyntomicOver.topology B.toBigSyntomicSite S hS))
      (inclusion B S hS p)
```

## Tag 0H0C, an equation

[Tag 0H0C](https://stacks.math.columbia.edu/tag/0H0C) in the Stacks Project.

**`AlgebraicGeometry.Stack.affineToFull`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean#L168). The attribute's comment: “the morphism of ringed topoi”.

> The morphism of ringed topoi induced by the inclusion of the affine subsite: its underlying
> morphism of topoi is the equivalence of Stacks 0H0B and its structure morphism is the adjunct of
> the identification of the inverse image of the structure sheaf with its restriction.

```lean
noncomputable def affineToFull
    (O : Sheaf (associatedTopology B S hS p τ) CommRingCat.{max u v w}) :
    AlgebraicGeometry.RingedToposHom (affineRingedTopos B S hS p τ J O)
      (fullRingedTopos B S hS p τ O)
```

**`AlgebraicGeometry.Stack.isIso_affineToFull_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean#L186). The attribute's comment: “the structure morphism is an isomorphism”.

> The structure morphism of `affineToFull` is an isomorphism.

```lean
theorem isIso_affineToFull_fSharpInverseImage
    (O : Sheaf (associatedTopology B S hS p τ) CommRingCat.{max u v w}) :
    IsIso (affineToFull B S hS p τ J O).fSharpInverseImage
```

**`AlgebraicGeometry.Stack.isEquivalence_affineToFull_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean#L194). The attribute's comment: “the inverse image is an equivalence”.

> The inverse image of `affineToFull` is an equivalence.

```lean
theorem isEquivalence_affineToFull_inverseImage
    (O : Sheaf (associatedTopology B S hS p τ) CommRingCat.{max u v w}) :
    (affineToFull B S hS p τ J O).toToposHom.inverseImage.IsEquivalence
```

**`AlgebraicGeometry.Stack.affineToFullFppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedTopos.lean#L224). The attribute's comment: “the fppf topology”.

> The inclusion of the affine subsite of the associated fppf site of a category fibred in
> groupoids, as a morphism of ringed topoi for the lifted structure sheaf of Stacks 06TV.

```lean
noncomputable def affineToFullFppf (hp : p.IsFiberedInGroupoids) :
    letI : (AffineCategory.inclusion B S hS p).IsDenseSubsite
        (associatedAffineTopology B S hS p (BigAffineFppf.topology B S hS))
        (associatedTopology B S hS p B.topology) :=
      isDenseSubsite_affineInclusion_fppf B S hS p hp
    AlgebraicGeometry.RingedToposHom
      (affineRingedTopos B S hS p B.topology (BigAffineFppf.topology B S hS)
        (liftedStructureSheaf B S hS p B.topology hp le_rfl))
      (fullRingedTopos B S hS p B.topology
        (liftedStructureSheaf B S hS p B.topology hp le_rfl))
```

**`AlgebraicGeometry.Stack.affineToFullZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean#L135). The attribute's comment: “the Zariski topology”.

> The inclusion of the affine subsite of the associated Zariski site of a category fibred in
> groupoids, as a morphism of ringed topoi for the lifted structure sheaf of Stacks 06TV. Its
> inverse image is an equivalence and its structure morphism is an isomorphism, by
> `AlgebraicGeometry.Stack.isEquivalence_affineToFull_inverseImage` and
> `AlgebraicGeometry.Stack.isIso_affineToFull_fSharpInverseImage`.

```lean
noncomputable def affineToFullZariski (hp : p.IsFiberedInGroupoids) :
    letI : (AffineCategory.inclusion B S hS p).IsDenseSubsite
        (associatedAffineTopology B S hS p
          (BigAffineZariski.topology B.toBigZariskiSite S hS))
        (associatedTopology B S hS p B.zariskiTopology) :=
      isDenseSubsite_affineInclusion_zariski B S hS p hp
    AlgebraicGeometry.RingedToposHom
      (affineRingedTopos B S hS p B.zariskiTopology
        (BigAffineZariski.topology B.toBigZariskiSite S hS)
        (liftedStructureSheaf B S hS p B.zariskiTopology hp (zariskiTopology_le_topology B)))
      (fullRingedTopos B S hS p B.zariskiTopology
        (liftedStructureSheaf B S hS p B.zariskiTopology hp
          (zariskiTopology_le_topology B)))
```

**`AlgebraicGeometry.Stack.affineToFullEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean#L159). The attribute's comment: “the étale topology”.

> The inclusion of the affine subsite of the associated étale site of a category fibred in
> groupoids, as a morphism of ringed topoi for the lifted structure sheaf of Stacks 06TV. Its
> inverse image is an equivalence and its structure morphism is an isomorphism, by
> `AlgebraicGeometry.Stack.isEquivalence_affineToFull_inverseImage` and
> `AlgebraicGeometry.Stack.isIso_affineToFull_fSharpInverseImage`.

```lean
noncomputable def affineToFullEtale (hp : p.IsFiberedInGroupoids) :
    letI : (AffineCategory.inclusion B S hS p).IsDenseSubsite
        (associatedAffineTopology B S hS p (BigAffineEtale.topology B.toBigEtaleSite S hS))
        (associatedTopology B S hS p B.etaleTopology) :=
      isDenseSubsite_affineInclusion_etale B S hS p hp
    AlgebraicGeometry.RingedToposHom
      (affineRingedTopos B S hS p B.etaleTopology
        (BigAffineEtale.topology B.toBigEtaleSite S hS)
        (liftedStructureSheaf B S hS p B.etaleTopology hp (etaleTopology_le_topology B)))
      (fullRingedTopos B S hS p B.etaleTopology
        (liftedStructureSheaf B S hS p B.etaleTopology hp (etaleTopology_le_topology B)))
```

**`AlgebraicGeometry.Stack.affineToFullSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean#L180). The attribute's comment: “the smooth topology”.

> The inclusion of the affine subsite of the associated smooth site of a category fibred in
> groupoids, as a morphism of ringed topoi for the lifted structure sheaf of Stacks 06TV. Its
> inverse image is an equivalence and its structure morphism is an isomorphism, by
> `AlgebraicGeometry.Stack.isEquivalence_affineToFull_inverseImage` and
> `AlgebraicGeometry.Stack.isIso_affineToFull_fSharpInverseImage`.

```lean
noncomputable def affineToFullSmooth (hp : p.IsFiberedInGroupoids) :
    letI : (AffineCategory.inclusion B S hS p).IsDenseSubsite
        (associatedAffineTopology B S hS p (BigAffineSmooth.topology B.toBigSmoothSite S hS))
        (associatedTopology B S hS p B.smoothTopology) :=
      isDenseSubsite_affineInclusion_smooth B S hS p hp
    AlgebraicGeometry.RingedToposHom
      (affineRingedTopos B S hS p B.smoothTopology
        (BigAffineSmooth.topology B.toBigSmoothSite S hS)
        (liftedStructureSheaf B S hS p B.smoothTopology hp (smoothTopology_le_topology B)))
      (fullRingedTopos B S hS p B.smoothTopology
        (liftedStructureSheaf B S hS p B.smoothTopology hp (smoothTopology_le_topology B)))
```

**`AlgebraicGeometry.Stack.affineToFullSyntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/AffineRingedToposTopologies.lean#L201). The attribute's comment: “the syntomic topology”.

> The inclusion of the affine subsite of the associated syntomic site of a category fibred in
> groupoids, as a morphism of ringed topoi for the lifted structure sheaf of Stacks 06TV. Its
> inverse image is an equivalence and its structure morphism is an isomorphism, by
> `AlgebraicGeometry.Stack.isEquivalence_affineToFull_inverseImage` and
> `AlgebraicGeometry.Stack.isIso_affineToFull_fSharpInverseImage`.

```lean
noncomputable def affineToFullSyntomic (hp : p.IsFiberedInGroupoids) :
    letI : (AffineCategory.inclusion B S hS p).IsDenseSubsite
        (associatedAffineTopology B S hS p
          (BigAffineSyntomic.topology B.toBigSyntomicSite S hS))
        (associatedTopology B S hS p B.syntomicTopology) :=
      isDenseSubsite_affineInclusion_syntomic B S hS p hp
    AlgebraicGeometry.RingedToposHom
      (affineRingedTopos B S hS p B.syntomicTopology
        (BigAffineSyntomic.topology B.toBigSyntomicSite S hS)
        (liftedStructureSheaf B S hS p B.syntomicTopology hp
          (syntomicTopology_le_topology B)))
      (fullRingedTopos B S hS p B.syntomicTopology
        (liftedStructureSheaf B S hS p B.syntomicTopology hp
          (syntomicTopology_le_topology B)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.24, Tag 0H08](https://stacks.math.columbia.edu/tag/0H08)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
