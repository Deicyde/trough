---
declaration: section
origin: cited
lean: AlgebraicGeometry.curvesH01_isOpenSubstack_and_factors_iff_and_over_field_iff, AlgebraicGeometry.curvesH01_isOpenSubstack_and_factors_iff_and_properOverField_iff, AlgebraicGeometry.CurveFamily.isCohenMacaulayDimOneFamily_of_hasUniversallyBijectiveGlobalFunctions, AlgebraicGeometry.CurveFamily.isIso_structureSharp_and_baseChange_of_residueField, AlgebraicGeometry.CurveFamily.isFiniteLocallyFreeOnSite_firstDirectImage_of_residueField, AlgebraicGeometry.CurveFamily.isIso_firstDirectImageBaseChangeMap_of_residueField, AlgebraicGeometry.curvesGenus_isOpenSubstack_and_factors_iff_and_decomposition
statement: formalized
proof: formalized
---

# 109.9 Curves of a given genus

Section 109.9 of the Stacks Project, [Tag 0E6H](https://stacks.math.columbia.edu/tag/0E6H). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E6I, a lemma

[Tag 0E6I](https://stacks.math.columbia.edu/tag/0E6I) in the Stacks Project.

**`AlgebraicGeometry.curvesH01_isOpenSubstack_and_factors_iff_and_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesH01OpenSubstack.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesH01OpenSubstack.lean#L68).

> There is an open substack `Curves^{h0,1} ⊂ Curves` of the stack of curves — the strictly full
> subcategory of families with `f_*𝒪_X = 𝒪_S` universally and fibres of dimension `1` is invariant
> under isomorphism and its inclusion is representable by algebraic spaces and an open immersion —
> such that
> 1. the classifying morphism of a family of curves `f : X → S` factors through `Curves^{h0,1}`
>    exactly when `f_*𝒪_X = 𝒪_S`, this holds after arbitrary base change, and the fibres of `f`
>    have dimension `1`;
> 2. for a scheme `X` proper over a field `k` with `dim(X) ≤ 1`, the classifying morphism
>    `Spec k → Curves` of `X` factors through `Curves^{h0,1}` exactly when `H⁰(X, 𝒪_X) = k` and
>    `dim(X) = 1`.

```lean
theorem curvesH01_isOpenSubstack_and_factors_iff_and_over_field_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsH01CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          (CurveFamily.isOpenCurvesLocus_isH01CurveFamily (B := B) (hZ := hZ)).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          (CurveFamily.isOpenCurvesLocus_isH01CurveFamily (B := B) (hZ := hZ)).prop_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsH01CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsH01CurveFamily B hZ) = y) ↔
        IsH01CurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
      (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
      (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
      (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅
        curveFamilyOfSchemeMorphism B hZ g (flat_of_eq_spec_field _ k hW) hproper
          (locallyOfFinitePresentation_of_eq_spec_field _ k hW)
          (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
          ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
          ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance) hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsH01CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsH01CurveFamily B hZ) = y) ↔
        Function.Bijective ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW).appTop ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1))
```

**`AlgebraicGeometry.curvesH01_isOpenSubstack_and_factors_iff_and_properOverField_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesH01Unconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesH01Unconditional.lean#L69). The attribute's comment: “the open substack Curves^\{h0,1} of Curves (closed under isomorphisms, inclusion representable by algebraic spaces and an open immersion), with (1) for a family of curves f : X → S, the classifying morphism factors through it iff f\_*O\_X = O\_S, universally, and the fibres have dimension 1, and (2) for a scheme X proper over a field k with dim(X) ≤ 1, the classifying morphism Spec(k) → Curves factors through it iff H^0(X, O\_X) = k and dim(X) = 1. Unconditional: 0E0R at i = 0 and 0E6B (a) are proved, not assumed”.

> `Curves^{h0,1}`, the strictly full subcategory of `Curves` of families of curves `f : X → S`
> with `f_*𝒪_X = 𝒪_S`, this holding after arbitrary base change, and whose fibres have dimension `1`
> (`AlgebraicGeometry.IsH01CurveFamily`), is an open substack of `Curves`: it is closed under
> isomorphisms and its inclusion `curvesSubstackInclusion` is representable by algebraic spaces and
> an open immersion. Moreover
> 1. for a family of curves over a scheme `S = U`, classified by `y` (a morphism over `U` from the
>    site of `U` to `Curves`), the classifying morphism factors through `Curves^{h0,1}` if and only
>    if the family `y(U)` has `f_*𝒪_X = 𝒪_S`, universally, and fibres of dimension `1`;
> 2. for a scheme `X = T` proper over a field `k` (the scheme of `W` being `Spec k`) with
>    `dim(X) ≤ 1`, and `y` a classifying morphism `Spec(k) → Curves` of the attached family of
>    curves, `y` factors through `Curves^{h0,1}` if and only if `k ⟶ H⁰(X, 𝒪_X)` is bijective and
>    `dim(X) = 1`.

```lean
theorem curvesH01_isOpenSubstack_and_factors_iff_and_properOverField_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsH01CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsH01CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsH01CurveFamily B hZ) = y) ↔
        IsH01CurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
      (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
      (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
      (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
      (y : BigFppfOver B W.left.1 W.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map W.hom →
      (y.obj (Over.mk (𝟙 W.left)) ≅ curveFamilyOfProperOverFieldEqSpec B hZ g k hW hproper hdim) →
      ((∃ z : BigFppfOver B W.left.1 W.left.2 ⥤
          ObjectProperty.FullSubcategory (IsH01CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsH01CurveFamily B hZ) = y) ↔
        Function.Bijective ((Scheme.ΓSpecIso (.of k)).inv ≫
            ((BigFppfOver.toScheme B integerBase hZ).map g ≫ eqToHom hW).appTop) ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1))
```

## Tag 0E6J, a lemma

[Tag 0E6J](https://stacks.math.columbia.edu/tag/0E6J) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.isCohenMacaulayDimOneFamily_of_hasUniversallyBijectiveGlobalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesH01.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesH01.lean#L469). The attribute's comment: “the objects of Curves^\{h0,1} (f\_*O\_X = O\_S universally and fibres of dimension 1) lie in Curves^\{CM,1} (Cohen-Macaulay of relative dimension 1)”.

> **Stacks 0E6J.** `Curves^{h0,1} ⊂ Curves^{CM,1}`: a family of curves `f : X ⟶ S` with
> `f_*𝒪_X = 𝒪_S`, universally, and all of whose fibres have dimension one is Cohen–Macaulay of
> relative dimension one.
>
> At a point of `X` the family is the base change of the family over the spectrum of a field
> representing the image point; that family is again of this kind, and is Cohen–Macaulay of
> relative dimension one by Tag 0BY5
> (`AlgebraicGeometry.CurveFamily.isCohenMacaulayDimOneFamily_of_base_eq_spec`). Both properties at a
> point are read off a base change along the cartesian square (Tags 0E10 and 04NS).

```lean
theorem CurveFamily.isCohenMacaulayDimOneFamily_of_hasUniversallyBijectiveGlobalFunctions
    (X : CurveFamily B hZ) (hΓ : HasUniversallyBijectiveGlobalFunctions B hZ X)
    (hdim : ∀ y, Space.fiberDimension B integerBase hZ X.toBase.hom y = 1) :
    IsCohenMacaulayDimOneFamily B hZ X
```

## Tag 0E1J, a lemma

[Tag 0E1J](https://stacks.math.columbia.edu/tag/0E1J) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.isIso_structureSharp_and_baseChange_of_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean#L192). The attribute's comment: “(1)”.

> Let `f : X → S` be a family of curves with `κ(s) = H⁰(X_s, 𝒪_{X_s})` for every point `s ∈ S`.
> Then `f_*𝒪_X = 𝒪_S` — the structure map `𝒪_S ⟶ f_*𝒪_X` is an isomorphism — and this holds
> universally: the same is true of the base change of `f` along every morphism `Y ⟶ S` from an
> algebraic space.

```lean
theorem isIso_structureSharp_and_baseChange_of_residueField (X : CurveFamily B hZ)
    (h : X.HasResidueFieldGlobalFunctions) :
    IsIso (Space.structureSharp B integerBase hZ X.toBase) ∧
      ∀ (Y : AlgebraicSpaces B integerBase hZ) (g : Y ⟶ schemeSpace X.base),
        IsIso (Space.structureSharp B integerBase hZ (pullback.snd X.toBase g))
```

**`AlgebraicGeometry.CurveFamily.isFiniteLocallyFreeOnSite_firstDirectImage_of_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean#L205). The attribute's comment: “(2)”.

> Let `f : X → S` be a family of curves with `κ(s) = H⁰(X_s, 𝒪_{X_s})` for every point `s ∈ S`.
> Then `R¹f_*𝒪_X` is a finite locally free `𝒪_S`-module: every object of the small étale site of
> `S` has a covering on whose members it is finite free (Stacks 03DL (2)).

```lean
theorem isFiniteLocallyFreeOnSite_firstDirectImage_of_residueField (X : CurveFamily B hZ)
    (h : X.HasResidueFieldGlobalFunctions) :
    SheafOfModules.IsFiniteLocallyFreeOnSite (X.firstDirectImage B hZ)
```

**`AlgebraicGeometry.CurveFamily.isIso_firstDirectImageBaseChangeMap_of_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyFirstHigherDirectImage.lean#L217). The attribute's comment: “(3)”.

> Let `f : X → S` be a family of curves with `κ(s) = H⁰(X_s, 𝒪_{X_s})` for every point `s ∈ S`.
> For every morphism `h : S' → S`, with `f' : X' → S'` the base change — that is, for every
> morphism of families of curves `a : X' ⟶ X`, whose square is cartesian, over `h = a.baseMap` —
> the base change map `h^*(R¹f_*𝒪_X) ⟶ R¹f'_*𝒪_{X'}`
> (`AlgebraicGeometry.CurveFamily.firstDirectImageBaseChangeMap`) is an isomorphism.

```lean
theorem isIso_firstDirectImageBaseChangeMap_of_residueField (X : CurveFamily B hZ)
    (h : X.HasResidueFieldGlobalFunctions) (F : CurveFamily B hZ) (a : F ⟶ X) :
    IsIso (firstDirectImageBaseChangeMap a)
```

## Tag 0E6K, a lemma

[Tag 0E6K](https://stacks.math.columbia.edu/tag/0E6K) in the Stacks Project.

**`AlgebraicGeometry.curvesGenus_isOpenSubstack_and_factors_iff_and_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGenusDecomposition.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesGenusDecomposition.lean#L144).

> **Stacks 0E6K.** There is a decomposition into open and closed substacks
> `Curves^{h0,1} = ∐_{g ≥ 0} Curves_g`, where
> (1) the classifying morphism of a family of curves `f : X → S` factors through `Curves_g` exactly
> when `f_*𝒪_X = 𝒪_S`, this holds after arbitrary base change, the fibres of `f` have dimension `1`,
> and `R¹f_*𝒪_X` is a locally free `𝒪_S`-module of rank `g`; and
> (2) for a scheme `X` proper over a field `k` with `dim(X) ≤ 1`, the classifying morphism
> `Spec(k) → Curves` factors through `Curves_g` exactly when `dim(X) = 1`, `k = H⁰(X, 𝒪_X)` and the
> genus of `X` is `g`.
>
> In the statement: `Curves^{h0,1}` and each `Curves_g` are open substacks of `Curves` (strictly full
> subcategories whose inclusions are representable by algebraic spaces and open immersions), each
> `Curves_g` lies in `Curves^{h0,1}`, parts (1) and (2) are the factorization criteria, and the
> decomposition is read on every family `G` over a scheme `S` in `Curves^{h0,1}`: the loci in `|S|`
> of the `Curves_g` are open and closed, pairwise disjoint and cover `|S|`.

```lean
theorem curvesGenus_isOpenSubstack_and_factors_iff_and_decomposition :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsH01CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom)) ∧
    (∀ g : ℕ,
      (ObjectProperty.IsClosedUnderIsomorphisms (IsGenusCurveFamily B hZ g) ∧
        Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
          (curvesSubstackInclusion B hZ (IsGenusCurveFamily B hZ g)
            (isGenusCurveFamily_of_hom g)).hom ∧
        Stack.IsOpenImmersion B integerBase hZ
          (curvesSubstackInclusion B hZ (IsGenusCurveFamily B hZ g)
            (isGenusCurveFamily_of_hom g))) ∧
      (∀ X : CurveFamily B hZ, IsGenusCurveFamily B hZ g X → IsH01CurveFamily B hZ X) ∧
      (∀ (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsGenusCurveFamily B hZ g),
            z ⋙ ObjectProperty.ι (IsGenusCurveFamily B hZ g) = y) ↔
          IsGenusCurveFamily B hZ g (y.obj (Over.mk (𝟙 U.left))))) ∧
      (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
        (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
        (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsGenusCurveFamily B hZ g),
            z ⋙ ObjectProperty.ι (IsGenusCurveFamily B hZ g) = y) ↔
          (topologicalKrullDim X.left = 1 ∧ Function.Bijective X.hom.appTop) ∧
            genus X.hom = g))) ∧
    ∀ G : CurveFamily B hZ, IsH01CurveFamily B hZ G →
      ∃ Ω : ℕ → Set (Space.points B integerBase hZ (schemeSpace G.base).obj),
        (∀ g, IsOpen (Ω g) ∧ IsClosed (Ω g)) ∧ Pairwise (fun g g' => Disjoint (Ω g) (Ω g')) ∧
          (⋃ g, Ω g) = Set.univ ∧
          ∀ (g : ℕ) (F : CurveFamily B hZ) (a : F ⟶ G),
            IsGenusCurveFamily B hZ g F ↔
              Set.range (Space.pointsMap B integerBase hZ (schemeSpace F.base).obj
                (schemeSpaceMap a.baseMap).hom) ⊆ Ω g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.9, Tag 0E6H](https://stacks.math.columbia.edu/tag/0E6H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
