---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.isOpen_smoothBaseLocus, AlgebraicGeometry.CurveFamily.preimage_smoothBaseLocus, AlgebraicGeometry.CurveFamily.exists_isOpenSubspace_smooth, AlgebraicGeometry.curvesSmooth_isStrictlyFull, AlgebraicGeometry.CurvesSmooth, AlgebraicGeometry.isSmoothDimOneFamily_iff_isSmoothFamily_and_isCohenMacaulayDimOneFamily, AlgebraicGeometry.CurveFamily.isOpen_smoothDimOneBaseLocus, AlgebraicGeometry.CurveFamily.isOpen_smoothDimOneBaseLocus_of_isSmoothFamily
statement: formalized
proof: formalized
---

# 109.16 Smooth curves

Section 109.16 of the Stacks Project, [Tag 0DZY](https://stacks.math.columbia.edu/tag/0DZY). 6 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZZ, a lemma

[Tag 0DZZ](https://stacks.math.columbia.edu/tag/0DZZ) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.isOpen_smoothBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L220). The attribute's comment: “the open locus in the base of smoothness”.

> **Stacks 0DZZ.** The locus of points of the base of a family of curves over which the family
> is smooth is open.
>
> The set of points of the total space at which the structure morphism is smooth is open by Tag
> 0DZI, so its complement is closed, and the family is proper, so the image of that complement —
> the complement of the locus in the base — is closed.

```lean
theorem CurveFamily.isOpen_smoothBaseLocus (X : CurveFamily B hZ) :
    IsOpen (CurveFamily.smoothBaseLocus B hZ X)
```

**`AlgebraicGeometry.CurveFamily.preimage_smoothBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L241). The attribute's comment: “base change of the open locus in the base of smoothness”.

> **Stacks 0DZZ.** The open locus in the base over which a family of curves is smooth commutes
> with base change: for a morphism of families of curves, the locus of the source is the inverse
> image of the locus of the target under the morphism of base schemes.

```lean
theorem CurveFamily.preimage_smoothBaseLocus {X Y : CurveFamily B hZ} (φ : X ⟶ Y) :
    Space.pointsMap B integerBase hZ (schemeSpace X.base).obj (schemeSpaceMap φ.baseMap).hom ⁻¹'
        CurveFamily.smoothBaseLocus B hZ Y =
      CurveFamily.smoothBaseLocus B hZ X
```

**`AlgebraicGeometry.CurveFamily.exists_isOpenSubspace_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L274). The attribute's comment: “the open subspace of the base over which a family becomes smooth, compatibly with base change”.

> **Stacks 0DZZ.** The open subspace of the base of a family of curves over which the family
> becomes smooth, in the form the source's proof produces it: for a family of curves `G` there is
> an open subspace `W` of its base such that a family `F` mapping to `G` is smooth exactly when
> the morphism of base schemes factors through `W`.
>
> This is the open `S' ⊂ S` of the source, and the equivalence is its compatibility with arbitrary
> base change: `W` is the open locus of smoothness of `G` in its base, factoring through it is
> having image in that locus, and the locus of `F` is the inverse image of the locus of `G`.

```lean
theorem CurveFamily.exists_isOpenSubspace_smooth (G : CurveFamily B hZ) :
    ∃ W : Subfunctor (schemeSpace G.base).obj,
      Space.IsOpenSubspace B integerBase hZ W ∧
      ∀ (F : CurveFamily B hZ) (a : F ⟶ G),
        IsSmoothFamily B hZ F ↔
          ∃ t : (schemeSpace F.base).obj ⟶ W.toFunctor,
            t ≫ W.ι = (schemeSpaceMap a.baseMap).hom
```

**`AlgebraicGeometry.curvesSmooth_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L317). The attribute's comment: “strict fullness of the smooth subcategory”.

> **Stacks 0DZZ.** The condition that a family of curves be smooth is invariant under
> isomorphism, so `Curves^{smooth}` is a strictly full subcategory of the category of families of
> curves: the first of the three conditions making it an open substack.
>
> An isomorphism of families of curves is a morphism of families, so this is base-change invariance
> of smoothness applied to the inverse isomorphism.

```lean
theorem curvesSmooth_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsSmoothFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.CurvesSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L325). The attribute's comment: “the smooth subcategory of the category of curves”.

> **Stacks 0DZZ.** The subcategory `Curves^{smooth}`: the strictly full subcategory of families
> of curves whose structure morphism is smooth.

```lean
abbrev CurvesSmooth
```

**`AlgebraicGeometry.isSmoothDimOneFamily_iff_isSmoothFamily_and_isCohenMacaulayDimOneFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L347). The attribute's comment: “Curves^{smooth,1} is Curves^{smooth} intersected with Curves^{CM,1}”.

> **Stacks 0DZZ.** `Curves^{smooth,1}` is the intersection of `Curves^{smooth}` with
> `Curves^{CM,1}`: a family of curves is smooth of relative dimension one exactly when it is smooth
> and is Cohen–Macaulay of relative dimension one.

```lean
theorem isSmoothDimOneFamily_iff_isSmoothFamily_and_isCohenMacaulayDimOneFamily
    (X : CurveFamily B hZ) :
    IsSmoothDimOneFamily B hZ X ↔
      IsSmoothFamily B hZ X ∧ IsCohenMacaulayDimOneFamily B hZ X
```

**`AlgebraicGeometry.CurveFamily.isOpen_smoothDimOneBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L364). The attribute's comment: “the open locus in the base of smooth relative dimension one”.

> **Stacks 0DZZ.** For a Cohen–Macaulay family of curves the locus in the base over which the
> family is smooth and has relative dimension one is open: the locus of smoothness is open, and so
> is the locus of relative dimension one by Tag 0E1F.

```lean
theorem CurveFamily.isOpen_smoothDimOneBaseLocus (X : CurveFamily B hZ)
    (hX : IsCohenMacaulayFamily B hZ X) :
    IsOpen (CurveFamily.smoothDimOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.CurveFamily.isOpen_smoothDimOneBaseLocus_of_isSmoothFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L373). The attribute's comment: “the open locus in the base of smooth relative dimension one, for a smooth family”.

> **Stacks 0DZZ.** For a smooth family of curves the locus in the base over which the family is
> smooth and has relative dimension one is open: a smooth family is Cohen–Macaulay.

```lean
theorem CurveFamily.isOpen_smoothDimOneBaseLocus_of_isSmoothFamily (X : CurveFamily B hZ)
    (hX : IsSmoothFamily B hZ X) :
    IsOpen (CurveFamily.smoothDimOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.CurveFamily.isOpen_smoothDimOneBaseLocus_of_any`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L445). The attribute's comment: “the open locus in the base of smooth relative dimension one, for any family”.

> **Stacks 0DZZ.** For any family of curves the locus in the base over which the family is
> smooth and has relative dimension one is open.
>
> This needs no hypothesis on the family: the set of points of the total space at which the
> structure morphism is smooth and has relative dimension one is open, so its complement is
> closed, and the family is proper, so the image of that complement — the complement of the locus
> in the base — is closed.

```lean
theorem CurveFamily.isOpen_smoothDimOneBaseLocus_of_any (X : CurveFamily B hZ) :
    IsOpen (CurveFamily.smoothDimOneBaseLocus B hZ X)
```

**`AlgebraicGeometry.CurveFamily.preimage_smoothDimOneBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L462). The attribute's comment: “base change of the locus in the base of smooth relative dimension one”.

> **Stacks 0DZZ.** The locus in the base over which a family of curves is smooth and has
> relative dimension one commutes with base change: for a morphism of families of curves, the locus
> of the source is the inverse image of the locus of the target under the morphism of base
> schemes.

```lean
theorem CurveFamily.preimage_smoothDimOneBaseLocus {X Y : CurveFamily B hZ} (φ : X ⟶ Y) :
    Space.pointsMap B integerBase hZ (schemeSpace X.base).obj (schemeSpaceMap φ.baseMap).hom ⁻¹'
        CurveFamily.smoothDimOneBaseLocus B hZ Y =
      CurveFamily.smoothDimOneBaseLocus B hZ X
```

**`AlgebraicGeometry.CurveFamily.exists_isOpenSubspace_smoothDimOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L490). The attribute's comment: “the open subspace of the base over which a family becomes smooth of relative dimension one, compatibly with base change”.

> **Stacks 0DZZ.** The open subspace of the base of a family of curves over which the family
> becomes smooth of relative dimension one, in the form the source's proof produces it: for a
> family of curves `G` there is an open subspace `W` of its base such that a family `F` mapping to
> `G` is smooth of relative dimension one exactly when the morphism of base schemes factors
> through `W`.
>
> This is the open `S' ⊂ S` of the source for `Curves^{smooth,1}`, and the equivalence is its
> compatibility with arbitrary base change.

```lean
theorem CurveFamily.exists_isOpenSubspace_smoothDimOne (G : CurveFamily B hZ) :
    ∃ W : Subfunctor (schemeSpace G.base).obj,
      Space.IsOpenSubspace B integerBase hZ W ∧
      ∀ (F : CurveFamily B hZ) (a : F ⟶ G),
        IsSmoothDimOneFamily B hZ F ↔
          ∃ t : (schemeSpace F.base).obj ⟶ W.toFunctor,
            t ≫ W.ι = (schemeSpaceMap a.baseMap).hom
```

**`AlgebraicGeometry.curvesSmooth1_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L529). The attribute's comment: “strict fullness of the smooth subcategory of relative dimension one”.

> **Stacks 0DZZ.** The condition that a family of curves be smooth of relative dimension one is
> invariant under isomorphism, so `Curves^{smooth,1}` is a strictly full subcategory of the category
> of families of curves: the first of the three conditions making it an open substack.

```lean
theorem curvesSmooth1_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsSmoothDimOneFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.CurvesSmooth1`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L537). The attribute's comment: “the smooth subcategory of relative dimension one”.

> **Stacks 0DZZ.** The subcategory `Curves^{smooth,1}`: the strictly full subcategory of
> families of curves whose structure morphism is smooth of relative dimension one.

```lean
abbrev CurvesSmooth1
```

**`AlgebraicGeometry.curvesSmooth1_le_curvesSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L543). The attribute's comment: “the chain of subcategories”.

> **Stacks 0DZZ.** The chain `Curves^{smooth,1} ⊂ Curves^{smooth}`: a family of curves which is
> smooth of relative dimension one is smooth.

```lean
theorem curvesSmooth1_le_curvesSmooth :
    (show ObjectProperty (CurveFamily B hZ) from IsSmoothDimOneFamily B hZ) ≤
      (show ObjectProperty (CurveFamily B hZ) from IsSmoothFamily B hZ)
```

**`AlgebraicGeometry.isSmoothFamily_curveFamilyOfSchemeMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L618). The attribute's comment: “part (2): smoothness of the proper scheme”.

> **Stacks 0DZZ, part (2).** The family of curves attached to a proper flat morphism of schemes
> of finite presentation whose source has dimension at most one is smooth exactly when that morphism
> of schemes is smooth.

```lean
theorem isSmoothFamily_curveFamilyOfSchemeMorphism_iff
    {T U : BigFppfOver B integerBase hZ} (g : T ⟶ U)
    (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
    (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    IsSmoothFamily B hZ
        (curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim) ↔
      Smooth ((BigFppfOver.toScheme B integerBase hZ).map g)
```

**`AlgebraicGeometry.isSmoothDimOneFamily_curveFamilyOfSchemeMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L640). The attribute's comment: “part (2): the proper scheme is smooth and equidimensional of dimension one”.

> **Stacks 0DZZ, part (2).** For a proper flat morphism of schemes of finite presentation with
> nonempty source of dimension at most one onto the spectrum of a field, the attached family of
> curves is smooth of relative dimension one exactly when the source is smooth over the field and
> equidimensional of dimension one.
>
> The source is assumed nonempty because an empty source has relative dimension one vacuously while
> its dimension is `-∞`.

```lean
theorem isSmoothDimOneFamily_curveFamilyOfSchemeMorphism_iff
    {T U : BigFppfOver B integerBase hZ} (g : T ⟶ U)
    (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
    (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (k : Type u) [Field k]
    (hU : (BigFppfOver.toScheme B integerBase hZ).obj U = Spec (.of k))
    (hne : Nonempty ((BigFppfOver.toScheme B integerBase hZ).obj T)) :
    IsSmoothDimOneFamily B hZ
        (curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim) ↔
      (Smooth ((BigFppfOver.toScheme B integerBase hZ).map g) ∧
        Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) =
          (1 : WithBot ℕ∞))
```

**`AlgebraicGeometry.isSmoothDimOneFamily_curveFamilyOfSchemeMorphism_iff_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmooth.lean#L679). The attribute's comment: “part (2): the proper scheme is smooth and every irreducible component of it has dimension one”.

> **Stacks 0DZZ, part (2).** For a proper flat morphism of schemes of finite presentation
> whose source has dimension at most one onto the spectrum of a field, the attached family of
> curves is smooth of relative dimension one exactly when the source is smooth over the field and
> equidimensional of dimension one — that is, every irreducible component of the source has
> dimension one.
>
> This is the whole of part (2) for `Curves^{smooth,1}`, with no hypothesis beyond those of the
> source: "equidimensional of dimension one" is read componentwise, as the definition of Tag 0058
> reads it, and so the equivalence also holds for an empty source, which is smooth of relative
> dimension one and has no irreducible component.

```lean
theorem isSmoothDimOneFamily_curveFamilyOfSchemeMorphism_iff_irreducibleComponents
    {T U : BigFppfOver B integerBase hZ} (g : T ⟶ U)
    (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
    (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (k : Type u) [Field k]
    (hU : (BigFppfOver.toScheme B integerBase hZ).obj U = Spec (.of k)) :
    IsSmoothDimOneFamily B hZ
        (curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim) ↔
      (Smooth ((BigFppfOver.toScheme B integerBase hZ).map g) ∧
        TopologicalSpace.Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ W ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim W = (1 : WithBot ℕ∞))
```

## Tag 0E1N, a lemma

[Tag 0E1N](https://stacks.math.columbia.edu/tag/0E1N) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_isSmoothFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothOverIntegers.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothOverIntegers.lean#L67). The attribute's comment: “Curves^{smooth} → Spec(ℤ) is smooth, on the algebraic stack of curves”.

> The morphism `Curves^{smooth} → Spec(ℤ)` is smooth: the open substack of the algebraic stack
> of curves (Stacks 0D5A) where the family of curves is smooth, followed by the structure morphism
> to `Spec(ℤ)`, is a smooth morphism of algebraic stacks.

```lean
theorem isSmoothOverIntegers_isSmoothFamily :
    IsSmoothOverIntegers B hZ (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
      (isOpenCurvesLocus_isSmoothFamily B hZ)
```

## Tag 0E81, a lemma

[Tag 0E81](https://stacks.math.columbia.edu/tag/0E81) in the Stacks Project.

**`AlgebraicGeometry.curvesSmoothH0_isOpenSubstack_and_factors_iff_and_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothH0Open.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothH0Open.lean#L231). The attribute's comment: “the open substack Curves^{smooth,h0} (the moduli stack M of 0E82), its family characterization (1) and the five equivalent conditions (2) over a field”.

> There is an open substack `Curves^{smooth,h0} ⊂ Curves` — the moduli stack
> `𝓜 = AlgebraicGeometry.moduliSmoothCurves` of Stacks 0E82, the strictly full subcategory of
> families of curves satisfying `AlgebraicGeometry.IsSmoothH0Family`; its inclusion
> `AlgebraicGeometry.moduliSmoothCurvesInclusion` is representable by algebraic spaces and an open
> immersion — such that:
>
> 1. for a family of curves `f : X → S`, classified by a scheme-valued point `y` of `Curves` over
>    `S`, the classifying morphism factors through `Curves^{smooth,h0}` exactly when
>    `f_*𝒪_X = 𝒪_S`, this holding after any base change, and `f` is smooth of relative dimension
>    `1` (`IsSmoothH0Family` of the family `y(S)`);
> 2. for a scheme `X = T` proper over a field `k = W` with `dim X ≤ 1`, classified by `y` over
>    `Spec k`, the following are equivalent: (a) the classifying morphism factors through
>    `Curves^{smooth,h0}`; (b) `X` is smooth, `dim X = 1` and `k = H⁰(X, 𝒪_X)`; (c) `X` is smooth,
>    `dim X = 1` and geometrically connected; (d) `X` is smooth, `dim X = 1` and geometrically
>    integral; (e) `X_{k̄}` is a smooth curve over an algebraic closure `k̄` of `k`.
>
> Part (1)(a) of the source says "factors through `Curves^{smooth}`"; the substack meant is the one
> constructed, `Curves^{smooth,h0}` (see the module documentation).

```lean
theorem curvesSmoothH0_isOpenSubstack_and_factors_iff_and_tfae :
    ((ObjectProperty.IsClosedUnderIsomorphisms (IsSmoothH0Family B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (moduliSmoothCurvesInclusion B hZ).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (moduliSmoothCurvesInclusion B hZ)) ∧
    ∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsSmoothH0Family B hZ),
          z ⋙ ObjectProperty.ι (IsSmoothH0Family B hZ) = y) ↔
        IsSmoothH0Family B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    ∀ {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
      (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
      (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
      (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
      (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
      (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
      (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
      (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
      (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
      (y : BigFppfOver B W.left.1 W.left.2 ⥤ CurveFamily B hZ)
      (_hy : y ⋙ curvesProjectionOver B hZ = Over.map W.hom)
      (_e : y.obj (Over.mk (𝟙 W.left)) ≅
        curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim),
      List.TFAE [
        ∃ z : BigFppfOver B W.left.1 W.left.2 ⥤
            ObjectProperty.FullSubcategory (IsSmoothH0Family B hZ),
          z ⋙ ObjectProperty.ι (IsSmoothH0Family B hZ) = y,
        Smooth ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW) ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫
            ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW).appTop),
        Smooth ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW) ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1 ∧
          GeometricallyConnected ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW),
        Smooth ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW) ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1 ∧
          GeometricallyIntegral ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW),
        Smooth (pullback.snd ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW)
            (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))) ∧
          IsCurve (AlgebraicClosure k)
            (pullback.snd ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW)
              (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))]
```

## Tag 0E82, a definition

[Tag 0E82](https://stacks.math.columbia.edu/tag/0E82) in the Stacks Project.

**`AlgebraicGeometry.moduliSmoothCurves`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliCurves.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliCurves.lean#L79). The attribute's comment: “the moduli stack of smooth proper curves, 𝓜 = Curves^{smooth, h0}”.

> **The moduli stack `𝓜 = Curves^{smooth, h0}` of smooth proper curves**: the substack of the
> stack of curves of the families of curves `f : X → S` which are smooth of relative dimension one
> with `f_*𝒪_X = 𝒪_S`, this holding after any base change (condition (1)(b) of Stacks 0E81), as a
> category fibred in groupoids over the big fppf site of `Spec(ℤ)`.

```lean
def moduliSmoothCurves :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

**`AlgebraicGeometry.moduliSmoothCurvesOfGenus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesOfGenus.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesOfGenus.lean#L85). The attribute's comment: “the moduli stack of smooth proper curves of genus g, 𝓜_g”.

> The moduli stack `𝓜_g` of smooth proper curves of genus `g`: the substack of the stack of
> curves of the families `f : X → S` which are smooth of relative dimension one with
> `f_*𝒪_X = 𝒪_S`, universally, and whose fibre over every point of `S` has genus `g`, as a category
> fibred in groupoids over the big fppf site of `Spec(ℤ)`. It lies in
> `𝓜 = AlgebraicGeometry.moduliSmoothCurves`, and its points are the smooth proper curves of genus
> `g` over fields, as in part (2) of Stacks 0E83.

```lean
def moduliSmoothCurvesOfGenus (g : ℕ) :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

## Tag 0E83, a lemma

[Tag 0E83](https://stacks.math.columbia.edu/tag/0E83) in the Stacks Project.

**`AlgebraicGeometry.moduliSmoothCurves_openClosedDecomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean#L173). The attribute's comment: “the decomposition 𝓜 = ∐_{g ≥ 0} 𝓜_g into open and closed substacks, read on the scheme-valued points of 𝓜”.

> **The decomposition `𝓜 = ∐_{g ≥ 0} 𝓜_g` into open and closed substacks.**
> Let `G` be a family of curves in `𝓜` (`AlgebraicGeometry.moduliSmoothCurves`) over a scheme `S`,
> that is, a scheme-valued point `S → 𝓜`. Then:
>
> * the loci `S_g ⊂ S` of points whose fibre has genus `g` are open and closed in `S`, pairwise
>   disjoint, and cover `S`;
> * for every `g`, `𝓜_g ×_𝓜 S` is the open subscheme `S_g`: there is an open subspace `W` of `S`
>   with points `S_g` such that a family `F` mapping to `G` (a base change of `G` along `T → S`)
>   lies in `𝓜_g` (`AlgebraicGeometry.moduliSmoothCurvesOfGenus`) exactly when `T → S` factors
>   through `W`, exactly when `T → S` maps every point into `S_g`.
>
> So each `𝓜_g ⊂ 𝓜` is an open and closed substack, these substacks are pairwise disjoint, and
> together they cover `𝓜`.

```lean
theorem moduliSmoothCurves_openClosedDecomposition (G : CurveFamily B hZ)
    (hG : IsSmoothH0Family B hZ G) :
    (∀ g : ℕ, IsClopen (CurveFamily.fibreGenusLocus B hZ G g)) ∧
      Pairwise (fun g g' : ℕ => Disjoint (CurveFamily.fibreGenusLocus B hZ G g)
        (CurveFamily.fibreGenusLocus B hZ G g')) ∧
      (⋃ g : ℕ, CurveFamily.fibreGenusLocus B hZ G g) = Set.univ ∧
      ∀ g : ℕ, ∃ W : Subfunctor (schemeSpace G.base).obj,
        Space.IsOpenSubspace B integerBase hZ W ∧
        Set.range (Space.pointsMap B integerBase hZ W.toFunctor W.ι) =
          CurveFamily.fibreGenusLocus B hZ G g ∧
        ∀ (F : CurveFamily B hZ) (a : F ⟶ G),
          (IsSmoothH0FamilyOfFibreGenus B hZ g F ↔
            ∃ t : (schemeSpace F.base).obj ⟶ W.toFunctor,
              t ≫ W.ι = (schemeSpaceMap a.baseMap).hom) ∧
          (IsSmoothH0FamilyOfFibreGenus B hZ g F ↔
            Set.range (Space.pointsMap B integerBase hZ (schemeSpace F.base).obj
              (schemeSpaceMap a.baseMap).hom) ⊆ CurveFamily.fibreGenusLocus B hZ G g)
```

**`AlgebraicGeometry.factors_moduliSmoothCurvesOfGenus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean#L244). The attribute's comment: “part (1), with smooth of relative dimension one in (b): read with smooth of arbitrary relative dimension, (b) ⟹ (a) fails for g = 0, see not_factors_moduliSmoothCurvesOfGenus_zero_of_identity”.

> Let `f : X → S` be a family of curves, classified by a
> scheme-valued point `y` of the stack of curves over `S` with `y(S) ≅ X`. The following are
> equivalent:
>
> * (a) the classifying morphism `S → Curves` factors through `𝓜_g`
>   (`AlgebraicGeometry.moduliSmoothCurvesOfGenus`): `y` lifts to the full subcategory of the
>   families of `𝓜_g`;
> * (b) `X → S` is smooth of relative dimension one, `f_*𝒪_X = 𝒪_S` and this holds after any base
>   change, and `R¹f_*𝒪_X` is a locally free `𝒪_S`-module of rank `g`.
>
> The source writes "smooth" in (b); with no relative dimension (b) ⟹ (a) fails for `g = 0`
> (`AlgebraicGeometry.not_factors_moduliSmoothCurvesOfGenus_zero_of_identity`), and (b) is stated
> with the relative dimension one that membership in `𝓜` (Stacks 0E81) requires.

```lean
theorem factors_moduliSmoothCurvesOfGenus_iff (g : ℕ) (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (_hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom) (X : CurveFamily B hZ)
    (e : y.obj (Over.mk (𝟙 U.left)) ≅ X) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsSmoothH0FamilyOfFibreGenus B hZ g),
        z ⋙ ObjectProperty.ι (IsSmoothH0FamilyOfFibreGenus B hZ g) = y) ↔
      IsSmoothDimOneFamily B hZ X ∧ HasUniversallyBijectiveGlobalFunctions B hZ X ∧
        CurveFamily.HasGenus B hZ X g
```

**`AlgebraicGeometry.factors_moduliSmoothCurvesOfGenus_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesGenusDecomposition.lean#L323). The attribute's comment: “part (2): over a field, (a) the classifying morphism factors through 𝓜_g, (b)-(e) the conditions on X”.

> Let `X` be a scheme proper over a field `k` with `dim(X) ≤ 1`, let `k̄` be an algebraic
> closure of `k` and `g ≥ 0`. The following are equivalent:
>
> * (a) the classifying morphism `Spec(k) → Curves` of `X` factors through `𝓜_g`
>   (`AlgebraicGeometry.moduliSmoothCurvesOfGenus`): a scheme-valued point `y` of `Curves` over `U`
>   with `y(U) ≅ X` lifts to the full subcategory of the families of `𝓜_g`;
> * (b) `X` is smooth, `dim(X) = 1`, `k = H⁰(X, 𝒪_X)`, and `X` has genus `g`;
> * (c) `X` is smooth, `dim(X) = 1`, `X` is geometrically connected, and `X` has genus `g`;
> * (d) `X` is smooth, `dim(X) = 1`, `X` is geometrically integral, and `X` has genus `g`;
> * (e) `X_{k̄}` is a smooth curve of genus `g` over `k̄`.

```lean
theorem factors_moduliSmoothCurvesOfGenus_over_field_iff (g : ℕ) {k : Type u} [Field k]
    (hk : B.Contains (Spec (.of k))) (X : Over (Spec (.of k))) [IsProper X.hom]
    (hdim : topologicalKrullDim X.left ≤ 1) (K : Type u) [Field K] [Algebra k K]
    [IsAlgClosure k K] :
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsSmoothH0FamilyOfFibreGenus B hZ g),
          z ⋙ ObjectProperty.ι (IsSmoothH0FamilyOfFibreGenus B hZ g) = y) ↔
        Smooth X.hom ∧ topologicalKrullDim X.left = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ genus X.hom = g)) ∧
    List.TFAE [
      Smooth X.hom ∧ topologicalKrullDim X.left = 1 ∧
        IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ genus X.hom = g,
      Smooth X.hom ∧ topologicalKrullDim X.left = 1 ∧ GeometricallyConnected X.hom ∧
        genus X.hom = g,
      Smooth X.hom ∧ topologicalKrullDim X.left = 1 ∧ GeometricallyIntegral X.hom ∧
        genus X.hom = g,
      Smooth (pullback.snd X.hom (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ∧
        IsCurve K (pullback.snd X.hom (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ∧
        genus (pullback.snd X.hom (Spec.map (CommRingCat.ofHom (algebraMap k K)))) = g]
```

## Tag 0E84, a lemma

[Tag 0E84](https://stacks.math.columbia.edu/tag/0E84) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_moduliSmoothCurves_and_moduliSmoothCurvesOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesSmoothness.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesSmoothness.lean#L67). The attribute's comment: “both morphisms 𝓜 → Spec(ℤ) and 𝓜_g → Spec(ℤ), for every g”.

> The morphisms `𝓜 → Spec(ℤ)` and, for every `g`, `𝓜_g → Spec(ℤ)` are smooth. Here
> `𝓜 = Curves^{smooth, h0}` and `𝓜_g` are the open substacks of the algebraic stack of curves (Stacks
> 0D5A) of the families smooth of relative dimension one with `f_*𝒪_X = 𝒪_S` universally, and of
> those with moreover all fibres of genus `g`. Both are open substacks of `Curves^{lci+}`, which is
> smooth over `Spec(ℤ)` (Stacks 0DZX).

```lean
theorem isSmoothOverIntegers_moduliSmoothCurves_and_moduliSmoothCurvesOfGenus :
    IsSmoothOverIntegers B hZ (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
        (C1590Private.isOpenCurvesLocus_isSmoothH0Family_of B hZ
          (C1590Private.isOpenCurvesLocus_hasUniversallyBijectiveGlobalFunctions_of
            (C1590Private.isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
              (C1590Private.hasEtaleLocalSchemeCharts B hZ))
            (C1590Private.hasUniversallyBijectiveGlobalFunctions_of
              (C1590Private.hasEtaleLocalSchemeCharts B hZ)))) ∧
      ∀ g : ℕ, IsSmoothOverIntegers B hZ
        (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
        (IsOpenCurvesLocus.of_iff (Q := IsSmoothH0FamilyOfFibreGenus B hZ g)
          (C1590Private.isOpenCurvesLocus_isSmoothH0FamilyOfFibreGenus_of
            (C1590Private.isOpenCurvesLocus_hasUniversallyBijectiveGlobalFunctions_of
              (C1590Private.isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
                (C1590Private.hasEtaleLocalSchemeCharts B hZ))
              (C1590Private.hasUniversallyBijectiveGlobalFunctions_of
                (C1590Private.hasEtaleLocalSchemeCharts B hZ)))
            (C1590Private.prestableGenusLociOpen_of (C1590Private.hasEtaleLocalSchemeCharts B hZ))
            g)
          fun _ => Iff.rfl)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.16, Tag 0DZY](https://stacks.math.columbia.edu/tag/0DZY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
