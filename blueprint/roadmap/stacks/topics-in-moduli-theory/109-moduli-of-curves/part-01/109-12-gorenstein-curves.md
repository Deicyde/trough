---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_gorenstein, AlgebraicGeometry.factorsThrough_curvesSubstack_gorenstein_iff, AlgebraicGeometry.factorsThrough_curvesSubstack_gorenstein_over_field_iff, AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_gorensteinDimOne, AlgebraicGeometry.factorsThrough_curvesSubstack_gorensteinDimOne_iff, AlgebraicGeometry.factorsThrough_curvesSubstack_gorensteinDimOne_over_field_iff
statement: formalized
proof: formalized
---

# 109.12 Gorenstein curves

Section 109.12 of the Stacks Project, [Tag 0E1L](https://stacks.math.columbia.edu/tag/0E1L). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E1M, a lemma

[Tag 0E1M](https://stacks.math.columbia.edu/tag/0E1M) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_gorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean#L84). The attribute's comment: “the inclusion of Curves^{Gorenstein} into Curves is representable by algebraic spaces and an open immersion”.

> **Stacks 0E1M, `Curves^{Gorenstein}` is open in `Curves`.** The inclusion into the category
> fibred in groupoids of families of curves of the full subcategory `Curves^{Gorenstein}` of the
> Gorenstein families is representable by algebraic spaces and an open immersion.

```lean
theorem isOpenImmersion_curvesSubstackInclusion_gorenstein :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGorensteinFamily B hZ)
          (isOpenCurvesLocus_isGorensteinFamily B hZ).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGorensteinFamily B hZ)
          (isOpenCurvesLocus_isGorensteinFamily B hZ).prop_of_hom)
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_gorenstein_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean#L98). The attribute's comment: “part (1)”.

> **Stacks 0E1M, part (1).** Let `X → S` be a family of curves and `z : (Sch/S) → Curves` a
> classifying morphism for it, a scheme-valued point together with an isomorphism `z(S) ≅ X`.
> Then `z` factors through `Curves^{Gorenstein}`, over the site and up to a 2-isomorphism, if and
> only if `X → S` is Gorenstein.

```lean
theorem factorsThrough_curvesSubstack_gorenstein_iff
    (S : BigFppfOver B integerBase hZ)
    (z : BigFppfOver B S.left.1 S.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map S.hom)
    (X : CurveFamily B hZ) (ξ : z.obj (Over.mk (𝟙 S.left)) ≅ X) :
    (∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
          Stack.objectPropertySubcategory B integerBase hZ (curvesFiberedCategory B hZ).val
            (IsGorensteinFamily B hZ),
        Nonempty (g.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsGorensteinFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      Space.IsGorenstein B integerBase hZ X.toBase.hom
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_gorenstein_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinSubstack.lean#L118). The attribute's comment: “part (2)”.

> **Stacks 0E1M, part (2).** Let `g : T ⟶ W` be a morphism of the big fppf site of the integers
> whose target scheme is the spectrum of a field `k`, whose underlying morphism of schemes is
> proper, and whose source scheme `X` has dimension at most one, and let `z : (Sch/Spec(k)) →
> Curves` classify the family of curves of `g`. Then `z` factors through `Curves^{Gorenstein}` if
> and only if `X` is Gorenstein.

```lean
theorem factorsThrough_curvesSubstack_gorenstein_over_field_iff
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
            (IsGorensteinFamily B hZ),
        Nonempty (q.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsGorensteinFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      IsGorenstein ((BigFppfOver.toScheme B integerBase hZ).obj T)
```

## Tag 0E6M, a lemma

[Tag 0E6M](https://stacks.math.columbia.edu/tag/0E6M) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_gorensteinDimOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean#L121). The attribute's comment: “the inclusion of Curves^{Gorenstein,1} into Curves is representable by algebraic spaces and an open immersion”.

> **`Curves^{Gorenstein,1}` is open in `Curves`.** The inclusion into the category fibred in
> groupoids of families of curves of the full subcategory `Curves^{Gorenstein,1}` of the families
> which are Gorenstein of relative dimension one is representable by algebraic spaces and an open
> immersion.

```lean
theorem isOpenImmersion_curvesSubstackInclusion_gorensteinDimOne :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGorensteinDimOneFamily B hZ)
          (isOpenCurvesLocus_isGorensteinDimOneFamily B hZ
            (isOpenCurvesLocus_isGorensteinFamily_and_over_field_iff B hZ)).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsGorensteinDimOneFamily B hZ)
          (isOpenCurvesLocus_isGorensteinDimOneFamily B hZ
            (isOpenCurvesLocus_isGorensteinFamily_and_over_field_iff B hZ)).prop_of_hom)
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_gorensteinDimOne_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean#L144). The attribute's comment: “part (1)”.

> Let `X → S` be a family of curves and `z : (Sch/S) → Curves` a classifying morphism for it, a
> scheme-valued point together with an isomorphism `z(S) ≅ X`. Then `z` factors through
> `Curves^{Gorenstein,1}`, over the site and up to a 2-isomorphism, if and only if `X → S` is
> Gorenstein and has relative dimension one.

```lean
theorem factorsThrough_curvesSubstack_gorensteinDimOne_iff
    (S : BigFppfOver B integerBase hZ)
    (z : BigFppfOver B S.left.1 S.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map S.hom)
    (X : CurveFamily B hZ) (ξ : z.obj (Over.mk (𝟙 S.left)) ≅ X) :
    (∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
          Stack.objectPropertySubcategory B integerBase hZ (curvesFiberedCategory B hZ).val
            (IsGorensteinDimOneFamily B hZ),
        Nonempty (g.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsGorensteinDimOneFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      Space.IsGorenstein B integerBase hZ X.toBase.hom ∧
        Space.HasRelativeDimension 1 B integerBase hZ X.toBase.hom
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_gorensteinDimOne_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGorensteinDimOneSubstack.lean#L165). The attribute's comment: “part (2)”.

> Let `g : T ⟶ W` be a morphism of the big fppf site of the integers whose target scheme is the
> spectrum of a field `k`, whose underlying morphism of schemes is proper, and whose source scheme
> `X` has dimension at most one, and let `z : (Sch/Spec(k)) → Curves` classify the family of curves
> of `g`. Then `z` factors through `Curves^{Gorenstein,1}` if and only if `X` is Gorenstein and
> equidimensional of dimension one, every irreducible component of it having dimension one.

```lean
theorem factorsThrough_curvesSubstack_gorensteinDimOne_over_field_iff
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
            (IsGorensteinDimOneFamily B hZ),
        Nonempty (q.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsGorensteinDimOneFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      (IsGorenstein ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        TopologicalSpace.Equidimensional ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
        ∀ C ∈ irreducibleComponents ((BigFppfOver.toScheme B integerBase hZ).obj T),
          topologicalKrullDim C = (1 : WithBot ℕ∞))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.12, Tag 0E1L](https://stacks.math.columbia.edu/tag/0E1L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
