---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isFlat_ambient_of_flatDeformation, AlgebraicGeometry.Stack.isFlatAt_target_of_flatDeformation, AlgebraicGeometry.Stack.isFlat_of_flatDeformation, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient, AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_iff_isSmooth_ambient, AlgebraicGeometry.Stack.AlgebraicStacks.isSyntomic_iff_isSyntomic_ambient, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_iff_isLocallyQuasiFinite_ambient, AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_iff_isMonomorphism_ambient
statement: formalized
proof: formalized
---

# 106.5 Infinitesimal deformations of algebraic stacks

Section 106.5 of the Stacks Project, [Tag 0CJA](https://stacks.math.columbia.edu/tag/0CJA). 2 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CJB, a lemma

[Tag 0CJB](https://stacks.math.columbia.edu/tag/0CJB) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFlat_ambient_of_flatDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformation.lean, line 972](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformation.lean#L972). The attribute's comment: “flatness of the ambient morphism”.

> For a commutative diagram of algebraic stacks over `S` over a thickening `iB : ℬ ⟶ ℬ'` of
> bases, whose cube commutes (`hcoh`), with `𝒴' ⟶ ℬ'` locally of finite type, `𝒳' ⟶ ℬ'` flat and
> locally of finite presentation, the restricted 1-morphism `f` flat, and the two restricted stacks
> the base changes of the ambient ones along `iB`, the ambient 1-morphism `f'` is flat.

```lean
theorem isFlat_ambient_of_flatDeformation
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : AlgebraicStacks.IsLocallyOfFiniteType B S hS pY')
    (hXflat : AlgebraicStacks.IsFlat B S hS pX')
    (hXfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS pX')
    (hfflat : AlgebraicStacks.IsFlat B S hS f) :
    AlgebraicStacks.IsFlat B S hS f'
```

**`AlgebraicGeometry.Stack.isFlatAt_target_of_flatDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformation.lean, line 1004](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformation.lean#L1004). The attribute's comment: “flatness of the target over the base at image points”.

> Under the hypotheses of `AlgebraicGeometry.Stack.isFlat_ambient_of_flatDeformation`, the
> structure 1-morphism `𝒴' ⟶ ℬ'` is flat, in the sense of Stacks 0CID, at every point of `|𝒴'|` in
> the image of `|f'|`.

```lean
theorem isFlatAt_target_of_flatDeformation
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : AlgebraicStacks.IsLocallyOfFiniteType B S hS pY')
    (hXflat : AlgebraicStacks.IsFlat B S hS pX')
    (hXfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS pX')
    (hfflat : AlgebraicStacks.IsFlat B S hS f)
    (x' : AlgebraicStacks.points B S hS 𝒳') :
    AlgebraicStacks.IsFlatAt B S hS pY' (AlgebraicStacks.pointsMap B S hS f' x')
```

**`AlgebraicGeometry.Stack.isFlat_of_flatDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformationCoherence.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningFlatDeformationCoherence.lean#L224).

> **Stacks 0CJB.** Let `iB : ℬ ⟶ ℬ'` be a thickening of algebraic stacks over `S`, let
> `pX' : 𝒳' ⟶ ℬ'` and `pY' : 𝒴' ⟶ ℬ'` be structure 1-morphisms, and let `f' : 𝒳' ⟶ 𝒴'` be a
> 1-morphism over `ℬ'`, by `houter`. Let `PX` and `PY` present the restricted source and target as
> the base changes of `𝒳'` and `𝒴'` along `iB`, and let `f : 𝒳 ⟶ 𝒴` be the restricted 1-morphism
> the universal property of the restricted target induces,
> `AlgebraicGeometry.Stack.restrictedHom`. Assume
>
> 1. `pY'` is locally of finite type,
> 2. `pX'` is flat and locally of finite presentation,
> 3. `f` is flat,
> 4. `𝒳 = ℬ ×_{ℬ'} 𝒳'` and `𝒴 = ℬ ×_{ℬ'} 𝒴'`, i.e. `PX` and `PY` are 2-fibre products.
>
> Then `f'` is flat, and `pY'` is flat — in the sense of **Stacks 0CID** — at every point of `|𝒴'|`
> in the image of `|f'|`.
>
> This is `AlgebraicGeometry.Stack.isFlat_ambient_of_flatDeformation` and
> `AlgebraicGeometry.Stack.isFlatAt_target_of_flatDeformation` with the two 2-cells of the
> commutative diagram and its cube-coherence equation supplied by
> `AlgebraicGeometry.Stack.restrictedIsoFst`, `AlgebraicGeometry.Stack.restrictedIsoSnd` and
> `AlgebraicGeometry.Stack.restrictedHom_coherence` rather than assumed.
>
> The two thickenings `𝒳 ⟶ 𝒳'` and `𝒴 ⟶ 𝒴'` of the source's diagram are not hypotheses: they are
> base changes of `iB` and so are thickenings by **Stacks 0BPR**.

```lean
theorem isFlat_of_flatDeformation
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hYft : AlgebraicStacks.IsLocallyOfFiniteType B S hS pY')
    (hXflat : AlgebraicStacks.IsFlat B S hS pX')
    (hXfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS pX')
    (hfflat : AlgebraicStacks.IsFlat B S hS (restrictedHom B S hS PX PY houter hcartY)) :
    AlgebraicStacks.IsFlat B S hS f' ∧
      ∀ x' : AlgebraicStacks.points B S hS 𝒳',
        AlgebraicStacks.IsFlatAt B S hS pY' (AlgebraicStacks.pointsMap B S hS f' x')
```

## Tag 0CJC, a lemma

[Tag 0CJC](https://stacks.math.columbia.edu/tag/0CJC) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean#L286). The attribute's comment: “flat”.

> For a commutative diagram of thickenings of algebraic stacks over `S` over a thickening
> `iB : ℬ ⟶ ℬ'` of bases, with `𝒴' ⟶ ℬ'` locally of finite type, `𝒳' ⟶ ℬ'` flat and locally of
> finite presentation and the two restricted stacks the base changes of the ambient ones along `iB`,
> the restricted 1-morphism `f` is flat if and only if the ambient 1-morphism `f'` is flat.

```lean
theorem isFlat_iff_isFlat_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsFlat B S hS f ↔ IsFlat B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_iff_isSmooth_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean#L309). The attribute's comment: “smooth”.

> Under the hypotheses of `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`,
> the restricted 1-morphism `f` is smooth if and only if the ambient 1-morphism `f'` is smooth.

```lean
theorem isSmooth_iff_isSmooth_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsSmooth B S hS f ↔ IsSmooth B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSyntomic_iff_isSyntomic_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationProperties.lean#L342). The attribute's comment: “syntomic”.

> Under the hypotheses of `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`,
> and assuming that syntomicity of morphisms of algebraic spaces is local on the source for the
> syntomic precoverage and local on the target for the fpqc precoverage, the restricted 1-morphism
> `f` passes the existential smooth-diagram test at syntomicity of morphisms of algebraic spaces if
> and only if the ambient 1-morphism `f'` does.

```lean
theorem isSyntomic_iff_isSyntomic_ambient
    [MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (k : F ⟶ G) => Space.IsSyntomic B S hS k.hom)
      (Space.Topology.precoverage.{u, u + 1} .syntomic B S hS)]
    [MorphismProperty.IsLocalAtTarget
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (k : F ⟶ G) => Space.IsSyntomic B S hS k.hom)
      (Space.Topology.precoverage.{u, u + 1} .fpqc B S hS)]
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    Stack.HasPropertyOnSomeSmoothDiagram B S hS
        (fun _ _ k => Space.IsSyntomic B S hS k) f.hom ↔
      Stack.HasPropertyOnSomeSmoothDiagram B S hS
        (fun _ _ k => Space.IsSyntomic B S hS k) f'.hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_iff_isLocallyQuasiFinite_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean#L235). The attribute's comment: “locally quasi-finite”.

> **Stacks 0CJC, locally quasi-finite.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`, the restricted 1-morphism
> `f` is locally quasi-finite if and only if the ambient 1-morphism `f'` is locally quasi-finite.
>
> Local quasi-finiteness is by **Stacks 06PU** three conditions, and each is carried separately;
> none of them goes through the smooth-diagram reduction of
> `AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_iff_of_flatDeformation`, local
> quasi-finiteness not being smooth local on the source.
>
> The quasi-DM condition is item (8) of **Stacks 0CJ9**,
> `AlgebraicGeometry.Stack.isQuasiDM_inner_iff_outer`, read on the morphism of thickenings whose
> ambient 1-morphism is `f'` and whose restricted one is `f` — the two thickenings being the base
> changes of `iB`, which are thickenings by **Stacks 0BPR** — and converted to the longhand reading
> of Stacks 04YW by `.isQuasiDMWithRepresentableDiagonal_iff_isQuasiDM`, the representability of a
> relative diagonal being free (**Stacks 04XS**, part (1)).
>
> Local finite type holds for *both* 1-morphisms outright, with no appeal to the thickening: `pX'`
> is locally of finite presentation, hence locally of finite type (**Stacks 0464**), and `houter`
> identifies it with `f' ≫ pY'`, so `f'` is locally of finite type by the cancellation
> **Stacks 06U9** (`.isLocallyOfFiniteType_of_comp`), which needs nothing of `pY'`. For `f` it is
> the base change of that (**Stacks 06FU**), and it is not even needed: it is read off the
> hypothesis in the forward direction and supplied by base change in the converse.
>
> The condition on the fibres is where the thickening enters. `Spec` of a field is reduced, so a
> field-valued point of the ambient target lifts along the thickening `𝒴 ⟶ 𝒴'` by
> `AlgebraicGeometry.Stack.exists_hom_comp_iso_of_isThickening_of_isReducedStack`, and the fibre of
> `f'` over it is the fibre of `f` over the lift by
> `AlgebraicGeometry.Stack.discreteTopology_points_twoFibreProduct_of_isThickening_lift`; the
> reducedness of the field's stack is the scheme case of **Stacks 04YF**.
>
> The converse is base change in one step: **Stacks 06UB**, `.isLocallyQuasiFinite_baseChange`, at
> the cartesian square `AlgebraicGeometry.Stack.restrictedSourceSq`.

```lean
theorem isLocallyQuasiFinite_iff_isLocallyQuasiFinite_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsLocallyQuasiFinite B S hS f ↔ IsLocallyQuasiFinite B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_iff_isMonomorphism_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean#L409). The attribute's comment: “monomorphism”.

> **Item (4) of Stacks 0CJC, monomorphism.** Under the
> hypotheses of `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`, the restricted
> 1-morphism `f` is a monomorphism in the sense of **Stacks 04ZW** if and only if the ambient
> 1-morphism `f'` is.
>
> Being a monomorphism is representability by algebraic spaces together with a condition of Stacks
> 04XB at the monomorphisms of algebraic spaces. The first conjunct transfers by item (12) of
> **Stacks 0CJ9**, `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inner_iff_outer`, read
> on the morphism of thickenings whose ambient 1-morphism is `f'` and whose restricted one is `f`.
> The second is `AlgebraicGeometry.Stack.AlgebraicStacks.hasRelativeProperty_iff_of_pointTest` at
> `CategoryTheory.MorphismProperty.monomorphisms`, whose point test is part (6) of **Stacks 0BPJ**,
> `AlgebraicGeometry.Space.mono_iff_of_cartesianSquareOfThickeningHoms`, which asks no flatness;
> fppf-target-locality of the monomorphisms is **Stacks 042D** and stability under base change an
> instance.
>
> Item (12) of Stacks 0CJ9 is unconditional, so nothing beyond the source's own hypotheses is
> carried in either direction.

```lean
theorem isMonomorphism_iff_isMonomorphism_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : Stack.IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (_hYft : IsLocallyOfFiniteType B S hS pY')
    (_hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsMonomorphism B S hS f ↔ IsMonomorphism B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinite_iff_isFinite_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDeformationPropertiesPointTest.lean#L452). The attribute's comment: “finite”.

> **Item (10) of Stacks 0CJC, finite.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`, the restricted 1-morphism `f`
> is finite in the sense of **Stacks 03ZP** read through Stacks 03YK if and only if the ambient
> 1-morphism `f'` is.
>
> The companion of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_iff_isMonomorphism_ambient` at
> `AlgebraicGeometry.Space.finiteMorphismProperty`, whose point test is part (2) of **Stacks
> 0BPJ**, `AlgebraicGeometry.Space.finiteMorphismProperty_iff_of_cartesianSquareOfThickeningHoms`:
> a morphism of algebraic spaces is finite exactly when it is proper and locally quasi-finite
> (**Stacks 0A4X**), and both of those transfer across a cartesian square of thickenings with
> locally-of-finite-type horizontals, with no flatness. Stability under base change and
> fppf-target-locality (**Stacks 0426**) are both instances.
>
> Representability of the two 1-morphisms comes from item (12) of Stacks 0CJ9 as in that theorem,
> and is unconditional for the same reason.

```lean
theorem isFinite_iff_isFinite_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : Stack.IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (_hYft : IsLocallyOfFiniteType B S hS pY')
    (_hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsFinite B S hS f ↔ IsFinite B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEquivalence_iff_isEquivalence_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean#L170). The attribute's comment: “isomorphism”.

> **Stacks 0CJC, isomorphism.** For a commutative diagram of thickenings of algebraic stacks over
> `S` over a thickening `iB : ℬ ⟶ ℬ'` of bases, with `𝒴' ⟶ ℬ'` locally of finite type, `𝒳' ⟶ ℬ'`
> flat and locally of finite presentation and the two restricted stacks the base changes of the
> ambient ones along `iB`, the restricted 1-morphism `f` is an isomorphism if and only if the
> ambient 1-morphism `f'` is.

```lean
theorem isEquivalence_iff_isEquivalence_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    (CatFiberedInGroupoids.homFunctor f.hom).IsEquivalence ↔
      (CatFiberedInGroupoids.homFunctor f'.hom).IsEquivalence
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_iff_isOpenImmersion_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean#L207). The attribute's comment: “open immersion”.

> **Stacks 0CJC, open immersion.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isEquivalence_iff_isEquivalence_ambient`, the restricted
> 1-morphism `f` is an open immersion if and only if the ambient 1-morphism `f'` is.

```lean
theorem isOpenImmersion_iff_isOpenImmersion_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    IsOpenImmersion B S hS f ↔ IsOpenImmersion B S hS f'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.hasPropertyOnSomeSmoothDiagram_isSyntomic_iff_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningOpenImmersionIsomorphism.lean#L236). The attribute's comment: “syntomic”.

> **Stacks 0CJC, syntomic.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isEquivalence_iff_isEquivalence_ambient`, the restricted
> 1-morphism `f` is syntomic — passes the existential smooth-diagram test of **Stacks 06FN** at
> syntomicity of morphisms of algebraic spaces, which is how the source defines a syntomic
> 1-morphism of algebraic stacks — if and only if the ambient 1-morphism `f'` is.

```lean
theorem hasPropertyOnSomeSmoothDiagram_isSyntomic_iff_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : IsLocallyOfFiniteType B S hS pY')
    (hXflat : IsFlat B S hS pX')
    (hXfp : IsLocallyOfFinitePresentation B S hS pX') :
    Stack.HasPropertyOnSomeSmoothDiagram B S hS
        (fun _ _ k => Space.IsSyntomic B S hS k) f.hom ↔
      Stack.HasPropertyOnSomeSmoothDiagram B S hS
        (fun _ _ k => Space.IsSyntomic B S hS k) f'.hom
```

**`AlgebraicGeometry.Stack.isUnramified_iff_isUnramified_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUnramifiedEtaleIff.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUnramifiedEtaleIff.lean#L41). The attribute's comment: “unramified”.

> **Stacks 0CJC, unramified.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`, the restricted 1-morphism
> `f` is unramified if and only if the ambient 1-morphism `f'` is unramified.

```lean
theorem isUnramified_iff_isUnramified_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : AlgebraicStacks.IsLocallyOfFiniteType B S hS pY')
    (hXflat : AlgebraicStacks.IsFlat B S hS pX')
    (hXfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS pX') :
    IsUnramified B S hS f ↔ IsUnramified B S hS f'
```

**`AlgebraicGeometry.Stack.isEtale_iff_isEtale_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUnramifiedEtaleIff.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUnramifiedEtaleIff.lean#L66). The attribute's comment: “etale”.

> **Stacks 0CJC, étale.** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_iff_isFlat_ambient`, the restricted 1-morphism
> `f` is étale if and only if the ambient 1-morphism `f'` is étale.

```lean
theorem isEtale_iff_isEtale_ambient
    {iB : ℬ ⟶ ℬ'} {pX' : 𝒳' ⟶ ℬ'} {pY' : 𝒴' ⟶ ℬ'}
    {PX : Bicategory.TwoCommSq pX' iB} {PY : Bicategory.TwoCommSq pY' iB}
    {f : PX.pt ⟶ PY.pt} {f' : 𝒳' ⟶ 𝒴'}
    (hiB : IsThickening iB)
    (hcartX : Bicategory.IsTwoFibreProduct PX) (hcartY : Bicategory.IsTwoFibreProduct PY)
    (houter : f' ≫ pY' ≅ pX')
    (hrestrict : f ≫ PY.fst ≅ PX.fst ≫ f')
    (hinner : f ≫ PY.snd ≅ PX.snd)
    (hcoh : Bicategory.whiskerLeft f PY.iso.hom ≫ Bicategory.whiskerRight hinner.hom iB =
      Bicategory.whiskerRight hrestrict.hom pY' ≫
        Bicategory.whiskerLeft PX.fst houter.hom ≫ PX.iso.hom)
    (hYft : AlgebraicStacks.IsLocallyOfFiniteType B S hS pY')
    (hXflat : AlgebraicStacks.IsFlat B S hS pX')
    (hXfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS pX') :
    IsEtale B S hS f ↔ IsEtale B S hS f'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.5, Tag 0CJA](https://stacks.math.columbia.edu/tag/0CJA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
