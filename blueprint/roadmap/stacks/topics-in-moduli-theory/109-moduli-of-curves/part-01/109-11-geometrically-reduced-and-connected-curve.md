---
declaration: section
origin: cited
lean: AlgebraicGeometry.curvesGrc1_isOpenSubstack, AlgebraicGeometry.factors_curvesGrc1_iff, AlgebraicGeometry.factors_curvesGrc1_over_field_iff, AlgebraicGeometry.curvesGrc1_isOpenSubstack_and_factors_iff, AlgebraicGeometry.curvesGrc1_le_curvesH01_isOpenSubstack_and_firstHigherDirectImage, AlgebraicGeometry.curvesGrcDimOne_genus_decomposition
statement: formalized
proof: formalized
---

# 109.11 Geometrically reduced and connected curves

Section 109.11 of the Stacks Project, [Tag 0E1H](https://stacks.math.columbia.edu/tag/0E1H). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E1I, a lemma

[Tag 0E1I](https://stacks.math.columbia.edu/tag/0E1I) in the Stacks Project.

**`AlgebraicGeometry.curvesGrc1_isOpenSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean#L101). The attribute's comment: “the open substack Curves^{grc,1} of Curves”.

> **Stacks 0E1I, the open substack.** `Curves^{grc,1}`, the strictly full subcategory of
> families of curves whose geometric fibres are reduced, connected and of dimension `1`, is an open
> substack of `Curves`: its inclusion is representable by algebraic spaces and an open
> immersion.

```lean
theorem curvesGrc1_isOpenSubstack :
    ObjectProperty.IsClosedUnderIsomorphisms (IsGrc1CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom)
```

**`AlgebraicGeometry.factors_curvesGrc1_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean#L116). The attribute's comment: “part (1): the classifying morphism of a family of curves factors through Curves^{grc,1} iff its geometric fibres are reduced, connected and of dimension 1”.

> **Stacks 0E1I, part (1).** The classifying morphism of a family of curves `X ⟶ S` factors
> through `Curves^{grc,1}` exactly when the geometric fibres of `X ⟶ S` are reduced, connected and
> of dimension `1`.

```lean
theorem factors_curvesGrc1_iff (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsGrc1CurveFamily B hZ),
        z ⋙ ObjectProperty.ι (IsGrc1CurveFamily B hZ) = y) ↔
      IsGrc1CurveFamily B hZ (y.obj (Over.mk (𝟙 U.left)))
```

**`AlgebraicGeometry.factors_curvesGrc1_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean#L133). The attribute's comment: “part (2): for a proper scheme of dimension at most one over a field, the classifying morphism factors through Curves^{grc,1} iff the scheme is geometrically reduced, geometrically connected and of dimension 1”.

> **Stacks 0E1I, part (2).** Let `X` be a proper scheme of dimension at most one over a field
> `k` (with `Spec k` in the site, so that the classifying morphism `Spec k ⟶ Curves` of `X`
> exists), and let `y` be a scheme-valued point of `Curves` over `U` classifying the family of
> curves of `X`. Then `y` factors through `Curves^{grc,1}` exactly when `X` is geometrically
> reduced over `k`, geometrically connected over `k`, and of dimension `1`.

```lean
theorem factors_curvesGrc1_over_field_iff (k : Type u) [Field k]
    (hk : B.Contains (Spec (.of k))) (X : Over (Spec (.of k))) [IsProper X.hom]
    (hdim : topologicalKrullDim X.left ≤ 1) (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom)
    (e : y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsGrc1CurveFamily B hZ),
        z ⋙ ObjectProperty.ι (IsGrc1CurveFamily B hZ) = y) ↔
      GeometricallyReduced X.hom ∧ GeometricallyConnected X.hom ∧
        topologicalKrullDim X.left = 1
```

**`AlgebraicGeometry.curvesGrc1_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1OpenSubstack.lean#L164). The attribute's comment: “the whole statement: the open substack Curves^{grc,1} and parts (1) and (2)”.

> **Stacks 0E1I.** There is an open substack `Curves^{grc,1} ⊂ Curves` — the strictly full
> subcategory of families of curves whose geometric fibres are reduced, connected and of dimension
> `1`, whose inclusion is representable by algebraic spaces and an open immersion — such that
> (1) the classifying morphism of a family of curves `X ⟶ S` factors through it exactly when the
> geometric fibres of `X ⟶ S` are reduced, connected and of dimension `1`, and (2) for a proper
> scheme `X` of dimension at most one over a field `k`, the classifying morphism of `X` factors
> through it exactly when `X` is geometrically reduced, geometrically connected and of
> dimension `1`.

```lean
theorem curvesGrc1_isOpenSubstack_and_factors_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsGrc1CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsGrc1CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsGrc1CurveFamily B hZ) = y) ↔
        IsGrc1CurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k))) (X : Over (Spec (.of k)))
      [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1) (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsGrc1CurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsGrc1CurveFamily B hZ) = y) ↔
        GeometricallyReduced X.hom ∧ GeometricallyConnected X.hom ∧
          topologicalKrullDim X.left = 1))
```

## Tag 0E6L, a lemma

[Tag 0E6L](https://stacks.math.columbia.edu/tag/0E6L) in the Stacks Project.

**`AlgebraicGeometry.curvesGrc1_le_curvesH01_isOpenSubstack_and_firstHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1H01OpenSubstacks.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGrc1H01OpenSubstacks.lean#L51).

> `Curves^{grc,1}` and `Curves^{h0,1}` are open substacks of `Curves` (each is closed under
> isomorphisms, and its inclusion into `Curves` is representable by algebraic spaces and an open
> immersion), and `Curves^{grc,1} ⊂ Curves^{h0,1}`. In particular, for a family of curves `f : X → S`
> whose geometric fibres are reduced, connected and of dimension `1`, `R¹f_*𝒪_X` is a finite locally
> free `𝒪_S`-module whose formation commutes with arbitrary base change: for every morphism
> `h : S' → S` of base schemes, `h^*(R¹f_*𝒪_X) ≅ R¹f'_*𝒪_{X'}` where `f' : X' → S'` is the base
> change.
>
> The conclusions are stated for the defining properties of the substacks:
> `IsGrc1CurveFamily` and `IsH01CurveFamily`, the strictly full subcategories of `Curves` they
> cut out, and `curvesSubstackInclusion` their inclusions.

```lean
theorem curvesGrc1_le_curvesH01_isOpenSubstack_and_firstHigherDirectImage :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsGrc1CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGrc1CurveFamily B hZ)
          isOpenCurvesLocus_isGrc1CurveFamily.prop_of_hom)) ∧
    (ObjectProperty.IsClosedUnderIsomorphisms (IsH01CurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsH01CurveFamily B hZ)
          CurveFamily.isOpenCurvesLocus_isH01CurveFamily.prop_of_hom)) ∧
    IsGrc1CurveFamily B hZ ≤ IsH01CurveFamily B hZ ∧
    ∀ X : CurveFamily B hZ, IsGrc1CurveFamily B hZ X →
      X.HasFiniteLocallyFreeFirstHigherDirectImage ∧
        X.FirstHigherDirectImageCommutesWithBaseChange
```

## Tag 0E1K, a lemma

[Tag 0E1K](https://stacks.math.columbia.edu/tag/0E1K) in the Stacks Project.

**`AlgebraicGeometry.curvesGrcDimOne_genus_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesReducedConnectedGenusDecomposition.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesReducedConnectedGenusDecomposition.lean#L454). The attribute's comment: “the decomposition Curves^{grc,1} = ∐_g Curves^{grc,1}_g into open and closed substacks (each inclusion representable, an open and a closed immersion; on the base of every object the genus loci are clopen, disjoint and covering), with the characterizations (1) and (2)”.

> **Stacks 0E1K.** There is a decomposition into open and closed substacks
> `Curves^{grc,1} = ∐_{g ≥ 0} Curves^{grc,1}_g`, where `Curves^{grc,1}` is the stack of families
> of curves whose geometric fibres are reduced, connected and of dimension `1`
> (`AlgebraicGeometry.curvesGrcDimOne`) and `Curves^{grc,1}_g` its full subcategory
> `AlgebraicGeometry.curvesGrcDimOneOfGenus`:
>
> * each `Curves^{grc,1}_g ⊂ Curves^{grc,1}` is an open and closed substack — strictly full, with
>   inclusion representable by algebraic spaces, an open immersion and a closed immersion;
> * they decompose `Curves^{grc,1}`: over the base `S` of every family in `Curves^{grc,1}` their
>   loci are open and closed, pairwise disjoint and cover `S`, and a family mapping to it lies in
>   `Curves^{grc,1}_g` exactly when its base maps into the locus of `g`;
> * (1) the classifying morphism `S → Curves` of a family of curves `f : X → S` factors through
>   `Curves^{grc,1}_g` exactly when the geometric fibres of `f` are reduced, connected, of
>   dimension `1` and `R¹f_*𝒪_X` is a locally free `𝒪_S`-module of rank `g`;
> * (2) for a proper scheme `X` over a field `k` with `dim(X) ≤ 1`, the classifying morphism
>   `Spec(k) → Curves` factors through `Curves^{grc,1}_g` exactly when `X` is geometrically
>   reduced, geometrically connected, of dimension `1` and of genus `g`.

```lean
theorem curvesGrcDimOne_genus_decomposition :
    (∀ g : ℕ, (IsGrcDimOneFibreGenus B hZ g).IsClosedUnderIsomorphisms ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesGrcDimOneOfGenusInclusion B hZ g).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (curvesGrcDimOneOfGenusInclusion B hZ g) ∧
      Stack.IsClosedImmersion B integerBase hZ (curvesGrcDimOneOfGenusInclusion B hZ g)) ∧
    (∀ X : (IsGrcDimOneFamily B hZ).FullSubcategory,
      (∀ g, IsClopen (CurveFamily.fibreGenusLocus B hZ X.obj g)) ∧
      Pairwise (fun g g' => Disjoint (CurveFamily.fibreGenusLocus B hZ X.obj g)
        (CurveFamily.fibreGenusLocus B hZ X.obj g')) ∧
      (⋃ g, CurveFamily.fibreGenusLocus B hZ X.obj g) = Set.univ ∧
      ∀ (g : ℕ) (F : (IsGrcDimOneFamily B hZ).FullSubcategory) (a : F ⟶ X),
        (IsGrcDimOneFibreGenus B hZ g F ↔
          Set.range (Space.pointsMap B integerBase hZ (schemeSpace F.obj.base).obj
            (schemeSpaceMap a.hom.baseMap).hom) ⊆ CurveFamily.fibreGenusLocus B hZ X.obj g)) ∧
    (∀ (g : ℕ) (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤ (IsGrcDimOneFibreGenus B hZ g).FullSubcategory,
          z ⋙ (IsGrcDimOneFibreGenus B hZ g).ι ⋙ (IsGrcDimOneFamily B hZ).ι = y) ↔
        IsGrcDimOneFamily B hZ (y.obj (Over.mk (𝟙 U.left))) ∧
          CurveFamily.HasGenus B hZ (y.obj (Over.mk (𝟙 U.left))) g)) ∧
    (∀ (g : ℕ) (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤ (IsGrcDimOneFibreGenus B hZ g).FullSubcategory,
          z ⋙ (IsGrcDimOneFibreGenus B hZ g).ι ⋙ (IsGrcDimOneFamily B hZ).ι = y) ↔
        IsGeometricallyReducedOver X.hom ∧ GeometricallyConnected X.hom ∧
          topologicalKrullDim X.left = 1 ∧ genus X.hom = g))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.11, Tag 0E1H](https://stacks.math.columbia.edu/tag/0E1H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
