---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.isOpen_cohenMacaulayBaseLocus, AlgebraicGeometry.CurveFamily.preimage_cohenMacaulayBaseLocus, AlgebraicGeometry.curvesCM_isStrictlyFull, AlgebraicGeometry.CurvesCM, AlgebraicGeometry.exists_cohenMacaulayCurves_openSubstack, AlgebraicGeometry.CurveFamily.preimage_cohenMacaulayDimOneBaseLocus, AlgebraicGeometry.CurveFamily.isOpen_relativeDimensionOneBaseLocus, AlgebraicGeometry.CurveFamily.isOpen_cohenMacaulayDimOneBaseLocus
statement: formalized
proof: formalized
---

# 109.8 Cohen-Macaulay curves

Section 109.8 of the Stacks Project, [Tag 0E0H](https://stacks.math.columbia.edu/tag/0E0H). 2 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E0I, a lemma

[Tag 0E0I](https://stacks.math.columbia.edu/tag/0E0I) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.isOpen_cohenMacaulayBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L169). The attribute's comment: “the open locus in the base”.

> **Stacks 0E0I.** The locus of points of the base of a family of curves over which the
> family is Cohen–Macaulay is open.
>
> The family is flat and locally of finite presentation, so its Cohen–Macaulay locus in the
> total space is open by Tag 0E10, and it is proper, so the image of the complement of that
> locus is closed in the base.

```lean
theorem CurveFamily.isOpen_cohenMacaulayBaseLocus (X : CurveFamily B hZ) :
    IsOpen (Space.cohenMacaulayBaseLocus B integerBase hZ X.toBase.hom)
```

**`AlgebraicGeometry.CurveFamily.preimage_cohenMacaulayBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L179). The attribute's comment: “base change of the open locus in the base”. References: EGA IV (6.8.2), “partial”.

> **Stacks 0E0I.** The open locus in the base over which a family of curves is
> Cohen–Macaulay commutes with base change: for a morphism of families of curves, the locus of
> the source is the inverse image of the locus of the target under the morphism of base
> schemes.

```lean
theorem CurveFamily.preimage_cohenMacaulayBaseLocus {X Y : CurveFamily B hZ} (φ : X ⟶ Y) :
    Space.pointsMap B integerBase hZ (schemeSpace X.base).obj (schemeSpaceMap φ.baseMap).hom ⁻¹'
        Space.cohenMacaulayBaseLocus B integerBase hZ Y.toBase.hom =
      Space.cohenMacaulayBaseLocus B integerBase hZ X.toBase.hom
```

**`AlgebraicGeometry.curvesCM_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L212). The attribute's comment: “strict fullness of the Cohen–Macaulay subcategory”.

> **Stacks 0E0I.** The condition that a family of curves be Cohen–Macaulay is invariant under
> isomorphism, so `Curves^{CM}` is a strictly full subcategory of the category of families of
> curves: the first of the three conditions making it an open substack.
>
> An isomorphism of families of curves is a morphism of families, so this is base-change
> invariance of Cohen–Macaulayness applied to the inverse isomorphism.

```lean
theorem curvesCM_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsCohenMacaulayFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.CurvesCM`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L220). The attribute's comment: “the Cohen–Macaulay subcategory of the category of curves”.

> **Stacks 0E0I.** The subcategory `Curves^{CM}`: the strictly full subcategory of families
> of curves whose structure morphism is Cohen–Macaulay.

```lean
abbrev CurvesCM
```

**`AlgebraicGeometry.exists_cohenMacaulayCurves_openSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayOverField.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayOverField.lean#L152).

> There is an open substack `Curves^{CM} ⊂ Curves` such that
>
> 1. for a family of curves `X → S`, the classifying morphism `S → Curves` factors through
>    `Curves^{CM}` if and only if `X → S` is Cohen–Macaulay;
> 2. for a scheme `X` proper over a field `k` with `dim(X) ≤ 1`, the classifying morphism
>    `Spec(k) → Curves` factors through `Curves^{CM}` if and only if `X` is Cohen–Macaulay.
>
> `Curves` is the category fibred in groupoids of families of curves of Stacks 0D4Z,
> `AlgebraicGeometry.curvesFiberedCategory`, over the big fppf site of `Spec(ℤ)`, and an open
> substack is an `AlgebraicGeometry.Stack.FiberedOpenSubstack`: a strictly full subcategory, fibred
> in groupoids (so closed under base change), whose inclusion is representable by algebraic spaces
> and an open immersion. That is Stacks 04YM without its clause "`Curves^{CM}` is an algebraic
> stack", which for an algebraic `Curves` follows from the others by Stacks 05UM, so that the two
> notions agree there (`AlgebraicGeometry.Stack.openSubstackEquivFibered`); the source produces the
> open substack by the method of Section 109.6, which only uses the open locus in the base and its
> compatibility with base change, and nothing here depends on `Curves` being algebraic (Stacks
> 0D5A).
>
> The classifying morphism of a family `F` factoring through `Curves^{CM}` is `F` lying in the image
> on objects of the inclusion `Curves^{CM} → Curves`; in part (2) the family is
> `AlgebraicGeometry.curveFamilyOfProperOverFieldEqSpec`, the family `X → Spec(k)` attached to a
> proper morphism `g` of the site onto the spectrum of a field, and dimension is topological Krull
> dimension.

```lean
theorem exists_cohenMacaulayCurves_openSubstack :
    ∃ U : Stack.FiberedOpenSubstack (curvesFiberedCategory B hZ),
      (∀ F : CurveFamily B hZ,
        (∃ Y : U.toFibered.val.obj, (CatFiberedInGroupoids.homFunctor U.inclusion).obj Y = F) ↔
          IsCohenMacaulayFamily B hZ F) ∧
      (∀ {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
          (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
          (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
          (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1),
        (∃ Y : U.toFibered.val.obj, (CatFiberedInGroupoids.homFunctor U.inclusion).obj Y =
            curveFamilyOfProperOverFieldEqSpec B hZ g k hW hproper hdim) ↔
          IsCohenMacaulay ((BigFppfOver.toScheme B integerBase hZ).obj T))
```

## Tag 0E1F, a lemma

[Tag 0E1F](https://stacks.math.columbia.edu/tag/0E1F) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.preimage_cohenMacaulayDimOneBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L347). The attribute's comment: “base change of the locus in the base of Cohen–Macaulay relative dimension one”.

> **Stacks 0E1F.** The locus in the base over which a family of curves is Cohen–Macaulay and
> has relative dimension one commutes with base change: for a morphism of families of curves, the
> locus of the source is the inverse image of the locus of the target under the morphism of base
> schemes.

```lean
theorem CurveFamily.preimage_cohenMacaulayDimOneBaseLocus {X Y : CurveFamily B hZ} (φ : X ⟶ Y) :
    Space.pointsMap B integerBase hZ (schemeSpace X.base).obj (schemeSpaceMap φ.baseMap).hom ⁻¹'
        CurveFamily.cohenMacaulayDimOneBaseLocus B hZ Y =
      CurveFamily.cohenMacaulayDimOneBaseLocus B hZ X
```

**`AlgebraicGeometry.CurveFamily.isOpen_relativeDimensionOneBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L380). The attribute's comment: “the open locus in the base of relative dimension one, for a Cohen–Macaulay family”.

> **Stacks 0E1F.** For a Cohen–Macaulay family of curves the locus in the base over which the
> family has relative dimension one is open.
>
> By Tag 0E11 the total space is the disjoint union of open-and-closed subspaces of constant
> relative dimension, and since relative dimension at a point is unique the locus of relative
> dimension one in the total space is the point set of the piece of relative dimension one. That
> set is open, so its complement is closed, and the family is proper, so the image of that
> complement — the complement of the locus in the base — is closed.

```lean
theorem CurveFamily.isOpen_relativeDimensionOneBaseLocus (X : CurveFamily B hZ)
    (hX : IsCohenMacaulayFamily B hZ X) :
    IsOpen (CurveFamily.relativeDimensionOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.CurveFamily.isOpen_cohenMacaulayDimOneBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L422). The attribute's comment: “the open locus in the base of Cohen–Macaulay relative dimension one, for a CM family”.

> **Stacks 0E1F.** For a Cohen–Macaulay family of curves the locus in the base over which the
> family is Cohen–Macaulay and has relative dimension one is open: the Cohen–Macaulay locus is
> then the whole base.

```lean
theorem CurveFamily.isOpen_cohenMacaulayDimOneBaseLocus (X : CurveFamily B hZ)
    (hX : IsCohenMacaulayFamily B hZ X) :
    IsOpen (CurveFamily.cohenMacaulayDimOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.curvesCM1_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L464). The attribute's comment: “strict fullness of the Cohen–Macaulay subcategory of relative dimension one”.

> **Stacks 0E1F.** The condition that a family of curves be Cohen–Macaulay of relative
> dimension one is invariant under isomorphism, so `Curves^{CM,1}` is a strictly full subcategory
> of the category of families of curves: the first of the three conditions making it an open
> substack.
>
> An isomorphism of families of curves is a morphism of families, so this is base-change
> invariance of the condition applied to the inverse isomorphism.

```lean
theorem curvesCM1_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsCohenMacaulayDimOneFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.CurvesCM1`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulay.lean#L472). The attribute's comment: “the Cohen–Macaulay subcategory of relative dimension one”.

> **Stacks 0E1F.** The subcategory `Curves^{CM,1}`: the strictly full subcategory of families
> of curves whose structure morphism is Cohen–Macaulay of relative dimension one.

```lean
abbrev CurvesCM1
```

**`AlgebraicGeometry.CurveFamily.cohenMacaulayDimOneBaseLocus_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean#L113). The attribute's comment: “the open locus in the base of Cohen–Macaulay relative dimension one, for an arbitrary family”.

> **The locus of Cohen–Macaulay relative dimension one is open.** For every family of curves
> `f : X → S`, the set of points of `S` over which `f` is Cohen–Macaulay and has relative
> dimension one is open.
>
> The set of points of the total space at which `f` is Cohen–Macaulay of relative dimension one is
> open (Tags 0E10 and 0E11), and `f` is proper, so the image of its complement — the complement
> of the locus — is closed.

```lean
theorem CurveFamily.cohenMacaulayDimOneBaseLocus_isOpen (X : CurveFamily B hZ) :
    IsOpen (CurveFamily.cohenMacaulayDimOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.isOpenCurvesLocus_isCohenMacaulayDimOneFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean#L128). The attribute's comment: “condition (o) of 0E0E: the open locus in the base, for an arbitrary family”.

> **Condition (o) of Section 0E0E for `Curves^{CM,1}`.** For every family of curves `X → S`
> there is an open subset `S'` of the base such that a family of curves mapping to `X → S` is
> Cohen–Macaulay of relative dimension one exactly when its base maps into `S'`: the locus of
> Cohen–Macaulay relative dimension one, which is open for every family and commutes with base
> change.

```lean
theorem isOpenCurvesLocus_isCohenMacaulayDimOneFamily :
    IsOpenCurvesLocus B hZ (IsCohenMacaulayDimOneFamily B hZ)
```

**`AlgebraicGeometry.isCohenMacaulayDimOneFamily_curveFamilyOfSchemeMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOne.lean#L158). The attribute's comment: “part (2), on the family of curves of the proper scheme: Cohen–Macaulay and equidimensional of dimension one”.

> **Part (2) of Stacks 0E1F, on the family.** Let `g : T ⟶ U` be a morphism of the big fppf
> site of the integers whose target scheme is the spectrum of a field `k`, whose underlying
> morphism of schemes is proper, and whose source scheme has dimension at most one. Then the
> family of curves of `g` is Cohen–Macaulay of relative dimension one exactly when the source
> scheme is Cohen–Macaulay and equidimensional of dimension one, every irreducible component of it
> having dimension one.

```lean
theorem isCohenMacaulayDimOneFamily_curveFamilyOfSchemeMorphism_iff
    {T U : BigFppfOver B integerBase hZ} (g : T ⟶ U) (k : Type u) [Field k]
    (hU : (BigFppfOver.toScheme B integerBase hZ).obj U = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    IsCohenMacaulayDimOneFamily B hZ
        (curveFamilyOfSchemeMorphism B hZ g
          (flat_of_eq_spec_field _ k hU) hproper
          (locallyOfFinitePresentation_of_eq_spec_field _ k hU)
          (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
          ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
          ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
          hdim) ↔
      (IsCohenMacaulay ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        TopologicalSpace.Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ W ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim W = (1 : WithBot ℕ∞))
```

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_cohenMacaulayDimOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean#L89). The attribute's comment: “the inclusion of Curves^\{CM,1} into Curves is representable by algebraic spaces and an open immersion”.

> **Stacks 0E1F, `Curves^{CM,1}` is open in `Curves`.** The inclusion into the category fibred
> in groupoids of families of curves of the full subcategory `Curves^{CM,1}` of the families which
> are Cohen–Macaulay of relative dimension one is representable by algebraic spaces and an open
> immersion.

```lean
theorem isOpenImmersion_curvesSubstackInclusion_cohenMacaulayDimOne :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsCohenMacaulayDimOneFamily B hZ)
          (isOpenCurvesLocus_isCohenMacaulayDimOneFamily B hZ).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsCohenMacaulayDimOneFamily B hZ)
          (isOpenCurvesLocus_isCohenMacaulayDimOneFamily B hZ).prop_of_hom)
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_cohenMacaulayDimOne_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean#L103). The attribute's comment: “part (1)”.

> **Stacks 0E1F, part (1).** Let `X → S` be a family of curves and `z : (Sch/S) → Curves` a
> classifying morphism for it, a scheme-valued point together with an isomorphism `z(S) ≅ X`.
> Then `z` factors through `Curves^{CM,1}`, over the site and up to a 2-isomorphism, if and only if
> `X → S` is Cohen–Macaulay and has relative dimension one.

```lean
theorem factorsThrough_curvesSubstack_cohenMacaulayDimOne_iff
    (S : BigFppfOver B integerBase hZ)
    (z : BigFppfOver B S.left.1 S.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map S.hom)
    (X : CurveFamily B hZ) (ξ : z.obj (Over.mk (𝟙 S.left)) ≅ X) :
    (∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
          Stack.objectPropertySubcategory B integerBase hZ (curvesFiberedCategory B hZ).val
            (IsCohenMacaulayDimOneFamily B hZ),
        Nonempty (g.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsCohenMacaulayDimOneFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      Space.IsCohenMacaulay B integerBase hZ X.toBase.hom ∧
        Space.HasRelativeDimension 1 B integerBase hZ X.toBase.hom
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_cohenMacaulayDimOne_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesCohenMacaulayDimOneSubstack.lean#L126). The attribute's comment: “part (2)”.

> **Stacks 0E1F, part (2).** Let `g : T ⟶ W` be a morphism of the big fppf site of the integers
> whose target scheme is the spectrum of a field `k`, whose underlying morphism of schemes is
> proper, and whose source scheme `X` has dimension at most one, and let `z : (Sch/Spec(k)) →
> Curves` classify the family of curves of `g`. Then `z` factors through `Curves^\{CM,1}` if and only
> if `X` is Cohen–Macaulay and equidimensional of dimension one, every irreducible component of it
> having dimension one.

```lean
theorem factorsThrough_curvesSubstack_cohenMacaulayDimOne_over_field_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
    (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (z : BigFppfOver B W.left.1 W.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map W.hom)
    (ξ : z.obj (Over.mk (𝟙 W.left)) ≅ curveFamilyOfSchemeMorphism B hZ g
      (flat_of_eq_spec_field _ k hW) hproper
      (locallyOfFinitePresentation_of_eq_spec_field _ k hW)
      (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
      ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
      ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance) hdim) :
    (∃ q : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ
          Stack.objectPropertySubcategory B integerBase hZ (curvesFiberedCategory B hZ).val
            (IsCohenMacaulayDimOneFamily B hZ),
        Nonempty (q.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsCohenMacaulayDimOneFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      (IsCohenMacaulay ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        TopologicalSpace.Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ C ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim C = (1 : WithBot ℕ∞))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.8, Tag 0E0H](https://stacks.math.columbia.edu/tag/0E0H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
