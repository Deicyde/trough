---
declaration: section
origin: cited
lean: Deformation.Examples.SchemeMorphismFamily, Deformation.Examples.SchemeMorphismFamily.Hom, Deformation.Examples.schemeMorphismFamilyFunctor, Deformation.Examples.schemeMorphismDeformationCategory, Deformation.Examples.schemeMorphismFamilyFunctor_cofiberedInGroupoids, Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategory, Deformation.Examples.satisfiesRS_schemeMorphismFamilyFunctor, Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategoryProjection
statement: formalized
proof: formalized
---

# 93.10 Morphisms of Schemes

Section 93.10 of the Stacks Project, [Tag 0E3S](https://stacks.math.columbia.edu/tag/0E3S). 6 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E3T, an example

[Tag 0E3T](https://stacks.math.columbia.edu/tag/0E3T) in the Stacks Project.

**`Deformation.Examples.SchemeMorphismFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean#L68). The attribute's comment: “deformation\_category\_of\_a\_scheme\_morphism”.

> A flat family of morphisms of schemes over an object of `𝒞_Λ`.

```lean
structure SchemeMorphismFamily (Λ : Type u) (k : Type v) [CommRing Λ] [Field k]
    [Algebra Λ k]
```

**`Deformation.Examples.SchemeMorphismFamily.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean#L94). The attribute's comment: “deformation\_category\_of\_a\_scheme\_morphism”.

> A cartesian morphism of flat families of morphisms of schemes, directed covariantly on the
> bases.

```lean
structure Hom (P Q : SchemeMorphismFamily.{u, v} Λ k)
```

**`Deformation.Examples.schemeMorphismFamilyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean#L133). The attribute's comment: “deformation\_category\_of\_a\_scheme\_morphism”.

> The functor sending a flat family of morphisms of schemes to its object of `𝒞_Λ`.

```lean
def schemeMorphismFamilyFunctor :
    SchemeMorphismFamily.{u, v} Λ k ⥤ ArtinianLocalAlgCat.{u, v, v} Λ k
```

**`Deformation.Examples.schemeMorphismDeformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean#L183). The attribute's comment: “deformation\_category\_of\_a\_scheme\_morphism”.

> Deformations of a fixed morphism of schemes over the residue field.

```lean
abbrev schemeMorphismDeformationCategory {X Y : Scheme.{v}} (f : X ⟶ Y)
    (pX : X ⟶ baseSpec (residueFieldBase Λ k))
    (pY : Y ⟶ baseSpec (residueFieldBase Λ k))
    (hf : f ≫ pY = pX)
```

**`Deformation.Examples.schemeMorphismFamilyFunctor_cofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphisms.lean#L298).

> The category of flat families of morphisms of schemes is cofibered in groupoids over
> `𝒞_Λ`.

```lean
theorem schemeMorphismFamilyFunctor_cofiberedInGroupoids
    {Λ : Type u} {k : Type v} [CommRing Λ] [Field k] [Algebra Λ k] :
    IsCofiberedInGroupoids (schemeMorphismFamilyFunctor.{u, v} (Λ := Λ) (k := k))
```

## Tag 0E3U, a lemma

[Tag 0E3U](https://stacks.math.columbia.edu/tag/0E3U) in the Stacks Project.

**`Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessinger.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessinger.lean#L101). The attribute's comment: “the in-particular assertion only: granting (RS) for Example 0E3T as the hypothesis hRS, the deformation category Def\_\{X ⟶ Y} of a morphism of schemes X ⟶ Y over k is a deformation category. (RS) for Example 0E3T itself is NOT proved here”.

> The second assertion of Stacks Tag 0E3U. Granting the Rim-Schlessinger condition for the
> category of all flat families of morphisms of schemes over `𝒞_Λ`, the deformation category of
> a fixed morphism `X ⟶ Y` of schemes over the residue field is a deformation category: a
> predeformation category satisfying (RS).

```lean
theorem isDeformationCategory_schemeMorphismDeformationCategory
    (hRS : SatisfiesRS (schemeMorphismFamilyFunctor.{u, v} (Λ := Λ) (k := k)))
    {X Y : Scheme.{v}} (f : X ⟶ Y)
    (pX : X ⟶ baseSpec (residueFieldBase Λ k))
    (pY : Y ⟶ baseSpec (residueFieldBase Λ k))
    (hf : f ≫ pY = pX) :
    IsDeformationCategory (schemeMorphismDeformationCategoryProjection f pX pY hf)
```

**`Deformation.Examples.satisfiesRS_schemeMorphismFamilyFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessingerSquares.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessingerSquares.lean#L183). The attribute's comment: “condition (RS) for the category of all flat families of morphisms of schemes of Example 0E3T -- the first assertion -- with nothing assumed. The two gluing facts it rests on are the last assertion of Tag 07RV and the equivalence assertion of the closing paragraph of Tag 07RX, both proved in this repository: Stacks.Pushout.isPullback\_of\_isPushout\_glued and Stacks.Pushout.isPushout\_restrictions\_of\_flat. The pushout of spectra, the existence of the glued family, the flatness of its two structure morphisms and both halves of the universal property are proved as well. The in-particular assertion, that the deformation category of a fixed morphism of schemes over k is a deformation category, is Deformation.Examples.isDeformationCategory\_schemeMorphismDeformationCategoryProjection”.

> **Stacks Project, Tag 0E3U, first assertion.**  The category of flat families of morphisms
> of schemes over `𝒞_Λ` of Example 0E3T satisfies the Rim-Schlessinger condition (RS), with no
> hypothesis.
>
> The fibre product of a cospan of families over a surjection of bases is glued twice over the
> one cocartesian square of spectra that the surjection produces: the sources are glued, the
> targets are glued, and the morphism between the two glued schemes is the descent of the two
> given morphisms along the pushout of the sources.

```lean
theorem satisfiesRS_schemeMorphismFamilyFunctor :
    SatisfiesRS (schemeMorphismFamilyFunctor.{u, v} (Λ := Λ) (k := k))
```

**`Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategoryProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessingerUnconditional.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsRimSchlessingerUnconditional.lean#L73). The attribute's comment: “the in-particular assertion, with nothing assumed: the deformation category Def\_\{X ⟶ Y} of a morphism of schemes X ⟶ Y over k is a deformation category, by the localization argument of Tag 06JC. Condition (RS) for the category of all flat families of morphisms of schemes of Example 0E3T -- the first assertion -- is Deformation.Examples.satisfiesRS\_schemeMorphismFamilyFunctor, proved by gluing the sources and the targets over one cocartesian square of spectra”.

> **Stacks Project, Tag 0E3U, second assertion.** The deformation category of a fixed morphism
> `X ⟶ Y` of schemes over the residue field is a deformation category: a predeformation category
> satisfying the Rim-Schlessinger condition (RS), with no hypothesis.
>
> This is `Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategory` with its
> hypothesis supplied by `Deformation.Examples.satisfiesRS_schemeMorphismFamilyFunctor`.

```lean
theorem isDeformationCategory_schemeMorphismDeformationCategoryProjection {X Y : Scheme.{v}}
    (f : X ⟶ Y)
    (pX : X ⟶ baseSpec (residueFieldBase Λ k))
    (pY : Y ⟶ baseSpec (residueFieldBase Λ k))
    (hf : f ≫ pY = pX) :
    IsDeformationCategory (schemeMorphismDeformationCategoryProjection f pX pY hf)
```

## Tag 0E3V, a lemma

[Tag 0E3V](https://stacks.math.columbia.edu/tag/0E3V) in the Stacks Project.

**`Deformation.Examples.schemeMorphismTargetForgetful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L124). The attribute's comment: “the target-forgetting functor Def\_\{X ⟶ Y} ⟶ Def\_Y, one half of the morphism of deformation categories Def\_\{X ⟶ Y} ⟶ Def\_X × Def\_Y of the source's proof”.

> The functor from deformations of a morphism `f : X ⟶ Y` of schemes over the residue field
> to deformations of its target `Y`, keeping the family that deforms `Y` together with its
> identification of the fibre over the closed point and forgetting the family that deforms
> `X`.

```lean
def schemeMorphismTargetForgetful :
    schemeMorphismDeformationCategory f pX pY hf ⥤
      SchemeDeformationCategory (Λ := Λ) (k := k) (Over.mk pY)
```

**`Deformation.Examples.schemeMorphismTargetForgetful_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L163). The attribute's comment: “that the target-forgetting functor is a morphism of deformation categories over the base category”.

> The target-forgetful functor commutes with the projections of the two deformation
> categories to `𝒞_Λ`, so it is a morphism of categories over the base category.

```lean
theorem schemeMorphismTargetForgetful_comp_projection :
    schemeMorphismTargetForgetful f pX pY hf ⋙
        schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY) =
      schemeMorphismDeformationCategoryProjection f pX pY hf
```

**`Deformation.Examples.schemeMorphismSourceBased`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L203). The attribute's comment: “the source component of the morphism Def\_\{X → Y} → Def\_X × Def\_Y”.

> The source-forgetful functor `Def_{X ⟶ Y} ⟶ Def_X`, as a morphism of categories over
> `𝒞_Λ`.

```lean
def schemeMorphismSourceBased :
    BasedCategory.ofFunctor (schemeMorphismDeformationCategoryProjection f pX pY hf) ⥤ᵇ
      BasedCategory.ofFunctor
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))
```

**`Deformation.Examples.schemeMorphismTargetBased`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L213). The attribute's comment: “the target component of the morphism Def\_\{X → Y} → Def\_X × Def\_Y”.

> The target-forgetful functor `Def_{X ⟶ Y} ⟶ Def_Y`, as a morphism of categories over
> `𝒞_Λ`.

```lean
def schemeMorphismTargetBased :
    BasedCategory.ofFunctor (schemeMorphismDeformationCategoryProjection f pX pY hf) ⥤ᵇ
      BasedCategory.ofFunctor
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))
```

**`Deformation.Examples.schemeMorphismInfinitesimalPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L227). The attribute's comment: “the arrow Inf(Def\_\{X → Y}) → Inf(Def\_X × Def\_Y), as the pair of the maps induced on infinitesimal automorphisms by the two endpoint-forgetting 1-morphisms”.

> **Stacks 0E3V**, the arrow `Inf(Def_{X ⟶ Y}) → Inf(Def_X × Def_Y)`: the pair of the
> `k`-linear maps on infinitesimal automorphisms induced by the two endpoint-forgetting morphisms
> of deformation categories.

```lean
def schemeMorphismInfinitesimalPair
    (hM : SatisfiesRS (schemeMorphismDeformationCategoryProjection f pX pY hf))
    (hX : SatisfiesRS (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)))
    (hY : SatisfiesRS (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
    {x₀ : schemeMorphismDeformationCategory f pX pY hf}
    (PM : ChosenPushforwardsAt (schemeMorphismDeformationCategoryProjection f pX pY hf) x₀)
    (QX : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))
      ((schemeMorphismSourceForgetful f pX pY hf).obj x₀))
    (QY : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))
      ((schemeMorphismTargetForgetful f pX pY hf).obj x₀)) :
    letI := naturalLocalizedTangentAddCommGroup PM hM
    letI := naturalLocalizedTangentModule PM hM
    letI := naturalLocalizedTangentAddCommGroup QX hX
    letI := naturalLocalizedTangentModule QX hX
    letI := naturalLocalizedTangentAddCommGroup QY hY
    letI := naturalLocalizedTangentModule QY hY
    localizedAutomorphismFunctorTangent PM →ₗ[k]
      localizedAutomorphismFunctorTangent QX × localizedAutomorphismFunctorTangent QY
```

**`Deformation.Examples.injective_schemeMorphismInfinitesimalPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L266). The attribute's comment: “exactness at the first spot: the arrow Inf(Def\_\{X → Y}) → Inf(Def\_X × Def\_Y) is injective”.

> **Stacks 0E3V, exactness at the first spot.** The arrow
> `Inf(Def_{X ⟶ Y}) → Inf(Def_X × Def_Y)` is injective, so the sequence
> `0 → Inf(Def_{X ⟶ Y}) → Inf(Def_X × Def_Y)` is exact: an infinitesimal automorphism of a
> deformation of `f` is a pair of infinitesimal automorphisms of the two endpoint deformations
> compatible with the arrow, and such a pair determines it.

```lean
theorem injective_schemeMorphismInfinitesimalPair
    (hM : SatisfiesRS (schemeMorphismDeformationCategoryProjection f pX pY hf))
    (hX : SatisfiesRS (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)))
    (hY : SatisfiesRS (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
    {x₀ : schemeMorphismDeformationCategory f pX pY hf}
    (PM : ChosenPushforwardsAt (schemeMorphismDeformationCategoryProjection f pX pY hf) x₀)
    (QX : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))
      ((schemeMorphismSourceForgetful f pX pY hf).obj x₀))
    (QY : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))
      ((schemeMorphismTargetForgetful f pX pY hf).obj x₀)) :
    letI := naturalLocalizedTangentAddCommGroup PM hM
    letI := naturalLocalizedTangentModule PM hM
    letI := naturalLocalizedTangentAddCommGroup QX hX
    letI := naturalLocalizedTangentModule QX hX
    letI := naturalLocalizedTangentAddCommGroup QY hY
    letI := naturalLocalizedTangentModule QY hY
    Function.Injective (schemeMorphismInfinitesimalPair f pX pY hf hM hX hY PM QX QY)
```

**`Deformation.Examples.schemeMorphismTangentPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L296). The attribute's comment: “the arrow T Def\_\{X → Y} → T(Def\_X × Def\_Y), as the pair of the maps induced on tangent modules by the two endpoint-forgetting 1-morphisms”.

> **Stacks 0E3V**, the arrow `T Def_{X ⟶ Y} → T(Def_X × Def_Y)`: the pair of the `k`-linear
> maps on tangent modules induced by the two endpoint-forgetting morphisms of deformation
> categories.

```lean
def schemeMorphismTangentPair
    (hM : IsDeformationCategory.{u, u, u}
      (schemeMorphismDeformationCategoryProjection f pX pY hf))
    (hX : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)))
    (hY : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
    (M : FGModuleCat.{u} k) :
    ↥(tangentModuleAt.{u, u, u}
        (BasedCategory.ofFunctor (schemeMorphismDeformationCategoryProjection f pX pY hf))
        hM M) →ₗ[k]
      ↥(tangentModuleAt.{u, u, u} (BasedCategory.ofFunctor
          (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))) hX M) ×
        ↥(tangentModuleAt.{u, u, u} (BasedCategory.ofFunctor
          (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))) hY M)
```

**`Deformation.Examples.exists_schemeMorphismTangentPair_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L357). The attribute's comment: “the image of the arrow T Def\_\{X → Y} → T(Def\_X × Def\_Y): a pair of first-order deformations of X and of Y is hit exactly when f deforms along it. The identification of the obstruction with a class in Ext^1(Lf^* NL\_\{Y/k}, O\_X) is NOT proved”.

> **Stacks 0E3V**, the image of the arrow `T Def_{X ⟶ Y} → T(Def_X × Def_Y)`. A pair of
> first-order deformations `X_ε` of `X` and `Y_ε` of `Y` is in the image exactly when `f` deforms
> along it, that is, when some first-order deformation of `f` has the two given deformations as
> its endpoints up to isomorphism in the fibre. This is the content of the last paragraph of the
> source's proof; the identification of the obstruction to such a deformation with a class in
> `Ext¹_{𝒪_X}(Lf^*NL_{Y/k}, 𝒪_X)` is not proved here.

```lean
theorem exists_schemeMorphismTangentPair_eq_iff
    (hM : IsDeformationCategory.{u, u, u}
      (schemeMorphismDeformationCategoryProjection f pX pY hf))
    (hX : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)))
    (hY : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
    (M : FGModuleCat.{u} k)
    (xε : (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)).Fiber
      ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M))
    (yε : (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)).Fiber
      ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)) :
    (∃ t, schemeMorphismTangentPair f pX pY hf hM hX hY M t =
        (tangentClassAt.{u, u, u} (BasedCategory.ofFunctor
            (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))) hX M xε,
          tangentClassAt.{u, u, u} (BasedCategory.ofFunctor
            (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))) hY M yε)) ↔
      ∃ mε : (schemeMorphismDeformationCategoryProjection f pX pY hf).Fiber
          ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M),
        IsIsomorphic ((fiberFunctor (schemeMorphismSourceBased f pX pY hf)
            ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)).obj mε) xε ∧
          IsIsomorphic ((fiberFunctor (schemeMorphismTargetBased f pX pY hf)
            ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)).obj mε) yε
```

**`Deformation.Examples.schemeMorphismDeformation_endpointArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismEndpoints.lean#L421). The attribute's comment: “PARTIAL. Of the six-term exact sequence this establishes: the arrow Inf(Def\_\{X → Y}) → Inf(Def\_X × Def\_Y) and the arrow T Def\_\{X → Y} → T(Def\_X × Def\_Y), both as the pairs of the maps induced by the source- and target-forgetting 1-morphisms Def\_\{X → Y} → Def\_X and Def\_\{X → Y} → Def\_Y; exactness at the FIRST spot, i.e. exactness of 0 → Inf(Def\_\{X → Y}) → Inf(Def\_X × Def\_Y); and the description of the IMAGE of T Def\_\{X → Y} → T(Def\_X × Def\_Y) as the pairs of first-order deformations of X and Y along which f deforms. NOT established: the terms Der\_k(O\_Y, f\_*O\_X) and Ext^1(Lf^* NL\_\{Y/k}, O\_X), the three arrows Inf(Def\_X × Def\_Y) → Der\_k(O\_Y, f\_*O\_X), Der\_k(O\_Y, f\_*O\_X) → T Def\_\{X → Y} and T(Def\_X × Def\_Y) → Ext^1(Lf^* NL\_\{Y/k}, O\_X), and exactness at the second, third and fourth spots. Hypotheses carried rather than proved: condition (RS) for Example 0E3T, and that Def\_X and Def\_Y are deformation categories”.

> **Stacks 0E3V, the part of the six-term exact sequence that this file establishes.**
>
> For a morphism `f : X ⟶ Y` of schemes over `k`, the morphism of deformation categories
> `Def_{X ⟶ Y} ⟶ Def_X × Def_Y` of the source's proof induces two of the six arrows of the
> source's sequence, and the package records them together with what is proved about exactness:
>
> 1. the sequence `0 → Inf(Def_{X ⟶ Y}) → Inf(Def_X × Def_Y)` is exact, i.e. the arrow on
>    infinitesimal automorphisms is injective;
> 2. the arrow on tangent spaces is the pair of the maps induced by the two forgetful morphisms;
> 3. a pair of first-order deformations of `X` and of `Y` is in the image of that arrow exactly
>    when `f` deforms along it.
>
> The three remaining arrows of the source's sequence — the two involving
> `Der_k(𝒪_Y, f_*𝒪_X)` and the obstruction map into
> `Ext¹_{𝒪_X}(Lf^*NL_{Y/k}, 𝒪_X)` — and exactness at the second, third and fourth spots are not
> proved; see the implementation notes of this file.
>
> The deformation hypothesis on `Def_{X ⟶ Y}` is supplied by
> `Deformation.Examples.isDeformationCategory_schemeMorphismDeformationCategory` from condition
> (RS) for the category of all flat families of morphisms of schemes.

```lean
theorem schemeMorphismDeformation_endpointArrows
    (hM : IsDeformationCategory.{u, u, u}
      (schemeMorphismDeformationCategoryProjection f pX pY hf))
    (hX : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)))
    (hY : IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
    {x₀ : schemeMorphismDeformationCategory f pX pY hf}
    (PM : ChosenPushforwardsAt (schemeMorphismDeformationCategoryProjection f pX pY hf) x₀)
    (QX : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))
      ((schemeMorphismSourceForgetful f pX pY hf).obj x₀))
    (QY : ChosenPushforwardsAt
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY))
      ((schemeMorphismTargetForgetful f pX pY hf).obj x₀))
    (M : FGModuleCat.{u} k) :
    letI := naturalLocalizedTangentAddCommGroup PM hM.satisfiesRS
    letI := naturalLocalizedTangentModule PM hM.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup QX hX.satisfiesRS
    letI := naturalLocalizedTangentModule QX hX.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup QY hY.satisfiesRS
    letI := naturalLocalizedTangentModule QY hY.satisfiesRS
    Function.Injective (schemeMorphismInfinitesimalPair f pX pY hf hM.satisfiesRS
        hX.satisfiesRS hY.satisfiesRS PM QX QY) ∧
      (∀ t, schemeMorphismTangentPair f pX pY hf hM hX hY M t =
        (tangentMapAt.{u, u, u} hM hX (schemeMorphismSourceBased f pX pY hf) M t,
          tangentMapAt.{u, u, u} hM hY (schemeMorphismTargetBased f pX pY hf) M t)) ∧
      ∀ (xε : (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX)).Fiber
          ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M))
        (yε : (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)).Fiber
          ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)),
        (∃ t, schemeMorphismTangentPair f pX pY hf hM hX hY M t =
            (tangentClassAt.{u, u, u} (BasedCategory.ofFunctor
                (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX))) hX M xε,
              tangentClassAt.{u, u, u} (BasedCategory.ofFunctor
                (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pY)))
                hY M yε)) ↔
          ∃ mε : (schemeMorphismDeformationCategoryProjection f pX pY hf).Fiber
              ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M),
            IsIsomorphic ((fiberFunctor (schemeMorphismSourceBased f pX pY hf)
                ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)).obj mε) xε ∧
              IsIsomorphic ((fiberFunctor (schemeMorphismTargetBased f pX pY hf)
                ((squareZeroExtensionArtinian.{u, u, u} Λ k).obj M)).obj mε) yε
```

**`Deformation.Examples.schemeMorphismDeformation_sixTermExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSixTermExact.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSixTermExact.lean#L234). The attribute's comment: “the canonical exact sequence of k-vector spaces 0 -> Inf(Def\_\{X -> Y}) -> Inf(Def\_X x Def\_Y) -> Der\_k(O\_Y, f\_*O\_X) -> T Def\_\{X -> Y} -> T(Def\_X x Def\_Y) -> Ext^1\_\{O\_X}(Lf^* NL\_\{Y/k}, O\_X) for a morphism of schemes f : X -> Y over k: its five k-linear maps and exactness at all five spots”.

> Let `f : X → Y` be a morphism of schemes over `k` (Example 0DY7). There is a canonical exact
> sequence of `k`-vector spaces
>
> `0 → Inf(Def_{X → Y}) → Inf(Def_X × Def_Y) → Der_k(𝒪_Y, f_*𝒪_X) → T Def_{X → Y}`
> `  → T(Def_X × Def_Y) → Ext¹_{𝒪_X}(Lf^*NL_{Y/k}, 𝒪_X)`.
>
> The six terms are `localizedAutomorphismFunctorTangent` of the fixed pushforwards
> `schemeMorphismTrivialPushforwards f pX pY hf` (`Inf(Def_{X → Y})`), the product of those of
> `schemeMorphismSourcePushforwards f pX pY hf` and `schemeMorphismTargetPushforwards f pX pY hf`
> (`Inf(Def_X × Def_Y)`), `schemeMorphismDerivations f pY` (`Der_k(𝒪_Y, f_*𝒪_X)`), the tangent
> module of `Def_{X → Y}` over `k[ε]` (`T Def_{X → Y}`), the product of the tangent modules of
> `Def_X` and `Def_Y` over `k[ε]` (`T(Def_X × Def_Y)`), and `schemeMorphismObstructionExt f pY`
> (`Ext¹_{𝒪_X}(Lf^*NL_{Y/k}, 𝒪_X)`), each with its `k`-vector space structure. The products are
> the source's `Def_X × Def_Y`: for the 2-fibre product `schemeEndpointsProduct pX pY` over `𝒞_Λ`
> (a deformation category, `isDeformationCategory_schemeEndpointsProduct`), the projections induce
> `k`-linear equivalences `schemeEndpointsProductInfEquiv` (`Inf(Def\_X × Def\_Y) ≃ Inf(Def\_X) ×
> Inf(Def\_Y)`) and `schemeEndpointsProductTangentEquiv` (`T(Def\_X × Def\_Y) ≃ T Def\_X × T Def\_Y`),
> and the arrows `a` and `d` below are the maps induced by `Def_{X → Y} → Def_X × Def_Y`
> (`schemeMorphismEndpointsBased`) followed by these equivalences
> (`schemeMorphismInfinitesimalPair'_canonical_eq`, `schemeMorphismTangentPair'_eq`).
>
> The five arrows are `a = schemeMorphismInfinitesimalPair'` and `d = schemeMorphismTangentPair'`,
> induced by the endpoint-forgetting morphisms; `b = schemeMorphismSixTermConjugationArrow`,
> `(α, β) ↦` the derivation by which `β⁻¹ ∘ f' ∘ α` differs from the trivial lift
> `f' = f × id`; `c = schemeMorphismDerivationTangentLinearMap`, `D ↦` the class of `D ⬝ f'`; and
> `e = schemeMorphismObstructionLinearMap`, `(X', Y') ↦ Push(Y') − Pull(X')`, the obstruction of
> Tag 08U8. The statement: `a` is injective (exactness at `Inf(Def_{X → Y})`) and the sequence is
> exact at `Inf(Def_X × Def_Y)`, `Der_k(𝒪_Y, f_*𝒪_X)`, `T Def_{X → Y}` and `T(Def_X × Def_Y)`.

```lean
theorem schemeMorphismDeformation_sixTermExact :
    letI := naturalLocalizedTangentAddCommGroup (schemeMorphismTrivialPushforwards f pX pY hf)
      (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY hf).satisfiesRS
    letI := naturalLocalizedTangentModule (schemeMorphismTrivialPushforwards f pX pY hf)
      (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY hf).satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup (schemeMorphismSourcePushforwards f pX pY
        hf) (isDeformationCategory_schemeDeformationCategoryProjection (Over.mk pX)).satisfiesRS
    letI := naturalLocalizedTangentModule (schemeMorphismSourcePushforwards f pX pY
        hf) (isDeformationCategory_schemeDeformationCategoryProjection (Over.mk pX)).satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup (schemeMorphismTargetPushforwards f pX pY
        hf) (isDeformationCategory_schemeDeformationCategoryProjection (Over.mk pY)).satisfiesRS
    letI := naturalLocalizedTangentModule (schemeMorphismTargetPushforwards f pX pY
        hf) (isDeformationCategory_schemeDeformationCategoryProjection (Over.mk pY)).satisfiesRS
    letI := schemeMorphismDerivationsModule f pY
      (SheafOfModules.unit (structureSheafRing X.toRingedSpace))
    letI := schemeMorphismObstructionExtModule f pY
    Function.Injective (schemeMorphismInfinitesimalPair' f pX pY hf
        (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
        hf).satisfiesRS (schemeMorphismTrivialPushforwards f pX pY hf)
            (schemeMorphismSourcePushforwards f pX pY hf) (schemeMorphismTargetPushforwards f pX pY
            hf)) ∧
      Function.Exact (schemeMorphismInfinitesimalPair' f pX pY hf
          (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
          hf).satisfiesRS (schemeMorphismTrivialPushforwards f pX pY hf)
              (schemeMorphismSourcePushforwards f pX pY hf) (schemeMorphismTargetPushforwards f pX
              pY hf)) (schemeMorphismSixTermConjugationArrow f pX pY hf) ∧
      Function.Exact (schemeMorphismSixTermConjugationArrow f pX pY hf)
        (schemeMorphismDerivationTangentLinearMap f pX pY hf) ∧
      Function.Exact (schemeMorphismDerivationTangentLinearMap f pX pY hf)
        (schemeMorphismTangentPair' f pX pY hf
            (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
            hf) (FGModuleCat.of k (ULift.{u} k))) ∧
      Function.Exact (schemeMorphismTangentPair' f pX pY hf
            (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
            hf) (FGModuleCat.of k (ULift.{u} k)))
        (schemeMorphismObstructionLinearMap f pX pY hf)
```

## Tag 0E3W, a lemma

[Tag 0E3W](https://stacks.math.columbia.edu/tag/0E3W) in the Stacks Project.

**`Deformation.Examples.isFiniteDimensionalDeformationCategory_schemeMorphismDeformationCategoryProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsFiniteDimensional.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsFiniteDimensional.lean#L87). The attribute's comment: “for a morphism f : X -> Y of schemes over k with X and Y both proper over k, Inf(Def\_\{X -> Y}) and T Def\_\{X -> Y} are finite dimensional; stated as condition (4) of Deformation.IsFiniteDimensionalDeformationCategory: the tangent space, and the infinitesimal automorphisms at every point over k and every choice of pushforwards, are finite dimensional”.

> **Stacks Project, Tag 0E3W.** In the setting of Tag 0E3V — a morphism `f : X → Y` of schemes
> over the field `k` — if `X` and `Y` are both proper over `k`, then `Inf(Def_{X → Y})` and
> `T Def_{X → Y}` are finite dimensional.
>
> The statement is condition (4) of `Deformation.IsFiniteDimensionalDeformationCategory` for the
> deformation category `Def_{X → Y}` of Example 0E3T: it is a deformation category, its tangent
> space `T Def_{X → Y}` (isomorphism classes over the dual numbers, with the vector space structure
> of Tag 06IH) is finite dimensional, and its infinitesimal automorphisms are finite dimensional at
> every point over `k` and every choice of pushforwards.

```lean
theorem isFiniteDimensionalDeformationCategory_schemeMorphismDeformationCategoryProjection
    [IsProper pX] [IsProper pY] :
    IsFiniteDimensionalDeformationCategory
      (schemeMorphismDeformationCategoryProjection f pX pY hf)
```

## Tag 0ET6, a lemma

[Tag 0ET6](https://stacks.math.columbia.edu/tag/0ET6) in the Stacks Project.

**`Deformation.Examples.exists_hull_schemeMorphismIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsHull.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsHull.lean#L120). The attribute's comment: “the functor of isomorphism classes of Def\_\{X -> Y} has a hull”. References: SGA 7 VI (4.9), “(a)”.

> **Stacks 0ET6, the hull.** Let `Λ` be a complete local ring with residue field `k` and let
> `f : X ⟶ Y` be a morphism of proper `k`-schemes. Then the functor
> `A ↦ Ob(Def_{X → Y}(A))/≅` of isomorphism classes of deformations of `f` has a hull: a versal
> formal object whose differential is bijective.

```lean
theorem exists_hull_schemeMorphismIsomorphismClasses (hΛ : IsClassical Λ k)
    [IsProper pX] [IsProper pY] :
    let G := isomorphismClasses
      (BasedCategory.ofFunctor (schemeMorphismDeformationCategoryProjection f pX pY hf))
      (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
        hf).predeformation.cofibered
    ∃ ξ : FormalObject (CategoryOfElements.π G),
      IsHull (categoryOfElements_projection_isCofibered G) ξ
```

**`Deformation.Examples.isProrepresentableULift_schemeMorphismIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsHull.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismsHull.lean#L139). The attribute's comment: “if Der\_k(O\_X, O\_X) = Der\_k(O\_Y, O\_Y) = 0, the functor of isomorphism classes of Def\_\{X -> Y} is prorepresentable”.

> **Stacks 0ET6, prorepresentability.** Let `Λ` be a complete local ring with residue field
> `k` and let `f : X ⟶ Y` be a morphism of proper `k`-schemes with
> `Der_k(𝒪_X, 𝒪_X) = Der_k(𝒪_Y, 𝒪_Y) = 0`. Then the functor `A ↦ Ob(Def_{X → Y}(A))/≅` of
> isomorphism classes of deformations of `f` is prorepresentable.

```lean
theorem isProrepresentableULift_schemeMorphismIsomorphismClasses (hΛ : IsClassical Λ k)
    [IsProper pX] [IsProper pY]
    (hX : ∀ D : schemeMorphismDerivations (Λ := Λ) (k := k) (𝟙 X) pX, D = 0)
    (hY : ∀ D : schemeMorphismDerivations (Λ := Λ) (k := k) (𝟙 Y) pY, D = 0) :
    IsProrepresentableULift (isomorphismClasses
      (BasedCategory.ofFunctor (schemeMorphismDeformationCategoryProjection f pX pY hf))
      (isDeformationCategory_schemeMorphismDeformationCategoryProjection f pX pY
        hf).predeformation.cofibered)
```

## Tag 0E3X, a lemma

[Tag 0E3X](https://stacks.math.columbia.edu/tag/0E3X) in the Stacks Project.

**`Deformation.Examples.schemeMorphismSourceForgetful_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSource.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSource.lean#L221). The attribute's comment: “morphism of deformation categories”.

> The source-forgetful functor commutes with the projections of the two deformation
> categories to `𝒞_Λ`, so it is a morphism of categories over the base category: this is the
> morphism of deformation categories `Def_{X ⟶ Y} ⟶ Def_X`.

```lean
theorem schemeMorphismSourceForgetful_comp_projection :
    schemeMorphismSourceForgetful f pX pY hf ⋙
        schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk pX) =
      Over.forget (schemeMorphismFamilySpecialFiber f pX pY hf) ⋙
        schemeMorphismFamilyFunctor
```

**`Deformation.Examples.schemeMorphismSourceForgetful_reflectsIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSource.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSource.lean#L232). The attribute's comment: “reflects isomorphisms”.

> The source-forgetful functor reflects isomorphisms: an arrow of deformations of `f`
> whose source component is invertible has invertible component on bases, and an arrow of
> flat families over an isomorphism of bases is an isomorphism.

```lean
instance schemeMorphismSourceForgetful_reflectsIsomorphisms :
    (schemeMorphismSourceForgetful f pX pY hf).ReflectsIsomorphisms
```

**`Deformation.Examples.schemeMorphismSourceForgetful_isEquivalence_of_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSourceEquivalence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeMorphismSourceEquivalence.lean#L123).

> Let `f : X ⟶ Y` be a morphism of schemes over the residue field `k` such that the canonical
> map `𝒪_Y ⟶ f_*𝒪_X` is an isomorphism and `R¹f_*𝒪_X` vanishes. Then the functor forgetting the
> target of a deformation of `f` is an equivalence from the deformation category of `f` to the
> deformation category of `X`.

```lean
theorem schemeMorphismSourceForgetful_isEquivalence_of_specialFibre
    (h0 : IsIso (C := Y.Modules) (Scheme.Modules.unitToPushforwardUnit f))
    (hR : IsZero (((Scheme.Modules.pushforward f).rightDerived 1).obj
      (SheafOfModules.unit X.ringCatSheaf))) :
    (schemeMorphismSourceForgetful f pX pY hf).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.10, Tag 0E3S](https://stacks.math.columbia.edu/tag/0E3S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
