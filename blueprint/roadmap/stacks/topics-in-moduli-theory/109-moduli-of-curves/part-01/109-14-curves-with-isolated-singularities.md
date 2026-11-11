---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurvesWithFiniteNonSmoothLocus, AlgebraicGeometry.curvesWithFiniteNonSmoothLocusProjection, AlgebraicGeometry.CurvesPlus, AlgebraicGeometry.CurveFamily.isFiniteNonSmoothLocus_iff_forall_isClosedSubspace, AlgebraicGeometry.CurveFamily.isFiniteNonSmoothLocus_iff_exists_isClosedSubspace, AlgebraicGeometry.curvesPlus_isOpenSubstack, AlgebraicGeometry.curvesPlus_classifying_factors_iff, AlgebraicGeometry.curvesPlus_classifying_factors_iff_of_field
statement: formalized
proof: formalized
---

# 109.14 Curves with isolated singularities

Section 109.14 of the Stacks Project, [Tag 0E0K](https://stacks.math.columbia.edu/tag/0E0K). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZW, a lemma

[Tag 0DZW](https://stacks.math.columbia.edu/tag/0DZW) in the Stacks Project.

**`AlgebraicGeometry.CurvesWithFiniteNonSmoothLocus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesIsolatedSingularities.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesIsolatedSingularities.lean#L79). The attribute's comment: “the substack of curves with isolated singularities”.

> **Stacks 0DZW.** The strictly full subcategory `Curves⁺ ⊂ Curves` of the families of
> curves whose non-smooth locus, with its reduced closed subspace structure, is finite over
> the base.

```lean
abbrev CurvesWithFiniteNonSmoothLocus
```

**`AlgebraicGeometry.curvesWithFiniteNonSmoothLocusProjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesIsolatedSingularities.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesIsolatedSingularities.lean#L84). The attribute's comment: “the projection of the substack”.

> **Stacks 0DZW.** The projection taking a family of curves with isolated singularities to
> its base scheme, which is how `Curves⁺` is regarded as a category over the big fppf site.

```lean
abbrev curvesWithFiniteNonSmoothLocusProjection :
    CurvesWithFiniteNonSmoothLocus B hZ ⥤ B.Schemes
```

**`AlgebraicGeometry.CurvesPlus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesFiniteSingularities.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesFiniteSingularities.lean#L81). The attribute's comment: “the\_substack\_curves”.

> **Stacks 0DZW.** The substack `Curves⁺`: the strictly full subcategory of families of
> curves whose reduced non-smooth locus is finite over the base.

```lean
abbrev CurvesPlus
```

**`AlgebraicGeometry.CurveFamily.isFiniteNonSmoothLocus_iff_forall_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenLocus.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenLocus.lean#L225). The attribute's comment: “part (1), condition (b) with 'any': every closed subspace structure on the singular locus is finite over the base”.

> **Stacks 0DZW, part (1), condition (b) with "any".** A family of curves `X → S` lies in
> `Curves⁺` exactly when *every* closed subspace `Z ⊂ X` whose set of points is the singular locus
> of `X → S` is finite over `S`.

```lean
theorem CurveFamily.isFiniteNonSmoothLocus_iff_forall_isClosedSubspace (X : CurveFamily B hZ) :
    IsFiniteNonSmoothLocus B hZ X ↔
      ∀ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z →
        Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
          CurveFamily.nonSmoothLocus B hZ X →
        Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom)
```

**`AlgebraicGeometry.CurveFamily.isFiniteNonSmoothLocus_iff_exists_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenLocus.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenLocus.lean#L242). The attribute's comment: “part (1), condition (b) with 'some': some closed subspace structure on the singular locus is finite over the base”.

> **Stacks 0DZW, part (1), condition (b) with "some".** A family of curves `X → S` lies in
> `Curves⁺` exactly when *some* closed subspace `Z ⊂ X` whose set of points is the singular locus of
> `X → S` is finite over `S`.

```lean
theorem CurveFamily.isFiniteNonSmoothLocus_iff_exists_isClosedSubspace (X : CurveFamily B hZ) :
    IsFiniteNonSmoothLocus B hZ X ↔
      ∃ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z ∧
        Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
          CurveFamily.nonSmoothLocus B hZ X ∧
        Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom)
```

**`AlgebraicGeometry.curvesPlus_isOpenSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean#L102). The attribute's comment: “Curves⁺ is an open substack of Curves: a strictly full subcategory whose inclusion is representable by algebraic spaces and an open immersion”.

> **Stacks 0DZW, the open substack.** `Curves⁺` is an open substack of the stack of curves: it
> is a strictly full subcategory, and its inclusion into `Curves` is representable by algebraic
> spaces and an open immersion.

```lean
theorem curvesPlus_isOpenSubstack :
    (show ObjectProperty (CurveFamily B hZ) from
        IsFiniteNonSmoothLocus B hZ).IsClosedUnderIsomorphisms ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ (curvesPlusInclusion B hZ).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (curvesPlusInclusion B hZ)
```

**`AlgebraicGeometry.curvesPlus_classifying_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean#L173). The attribute's comment: “part (1): for every family of curves X → S, the classifying morphism factors through Curves⁺ iff the singular locus with some, equivalently any, closed subspace structure is finite over S”.

> **Stacks 0DZW, part (1).** For a family of curves `X → S` and its classifying morphism
> `S → Curves`, the classifying morphism factors through `Curves⁺` exactly when *some* closed
> subspace structure on the singular locus of `X → S` is finite over `S`, and exactly when *every*
> closed subspace structure on it is.

```lean
theorem curvesPlus_classifying_factors_iff (X : CurveFamily B hZ)
    (y : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ (curvesFiberedCategory B hZ).val)
    (hy : IsClassifyingMorphism B hZ X y) :
    ((∃ g : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ
          (curvesPlusFiberedCategory B hZ).val,
        Nonempty (g.comp (curvesPlusInclusion B hZ).hom ≅ y)) ↔
      ∃ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z ∧
        Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
          CurveFamily.nonSmoothLocus B hZ X ∧
        Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom)) ∧
    ((∃ g : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ
          (curvesPlusFiberedCategory B hZ).val,
        Nonempty (g.comp (curvesPlusInclusion B hZ).hom ≅ y)) ↔
      ∀ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z →
        Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
          CurveFamily.nonSmoothLocus B hZ X →
        Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom))
```

**`AlgebraicGeometry.curvesPlus_classifying_factors_iff_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean#L284). The attribute's comment: “part (2): for a proper scheme X of dimension at most one over a field k, the classifying morphism Spec(k) → Curves factors through Curves⁺ iff X → Spec(k) is smooth except at finitely many points”.

> **Stacks 0DZW, part (2).** Let `X` be a proper scheme of dimension at most one over a field
> `k`. The classifying morphism `Spec(k) → Curves` of the attached family of curves factors through
> `Curves⁺` exactly when `X → Spec(k)` is smooth except at finitely many points.

```lean
theorem curvesPlus_classifying_factors_iff_of_field
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (y : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ (curvesFiberedCategory B hZ).val)
    (hy : IsClassifyingMorphism B hZ (curveFamilyOfProperOverField B hZ k g e hproper hdim) y) :
    (∃ g' : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ (curvesPlusFiberedCategory B hZ).val,
        Nonempty (g'.comp (curvesPlusInclusion B hZ).hom ≅ y)) ↔
      {x : (BigFppfOver.toScheme B integerBase hZ).obj T |
        ¬ InfinitesimalLifting.SmoothAt ((BigFppfOver.toScheme B integerBase hZ).map g) x}.Finite
```

**`AlgebraicGeometry.exists_curvesPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusOpenSubstack.lean#L311). The attribute's comment: “the open substack Curves⁺ ⊂ Curves together with parts (1) and (2)”.

> **Stacks 0DZW.** There is an open substack `Curves⁺` of the stack of curves — a strictly full
> subcategory whose inclusion is representable by algebraic spaces and an open immersion — such that
>
> 1. for every family of curves `X → S` and its classifying morphism, the classifying morphism
>    factors through `Curves⁺` iff the singular locus of `X → S` with some closed subspace
>    structure is finite over `S`, iff it is finite over `S` with every closed subspace structure;
> 2. for every proper scheme `X` of dimension at most one over a field `k`, the classifying morphism
>    `Spec(k) → Curves` factors through `Curves⁺` iff `X → Spec(k)` is smooth except at finitely
>    many points.

```lean
theorem exists_curvesPlus :
    ∃ (P : ObjectProperty (CurveFamily B hZ))
        (hP : ∀ {F G : CurveFamily B hZ}, (F ⟶ G) → P G → P F),
      P.IsClosedUnderIsomorphisms ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ (curvesSubInclusion B hZ P hP).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (curvesSubInclusion B hZ P hP) ∧
      (∀ (X : CurveFamily B hZ)
        (y : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ (curvesFiberedCategory B hZ).val),
        IsClassifyingMorphism B hZ X y →
          ((∃ g : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ
                (curvesSubFiberedCategory B hZ P hP).val,
              Nonempty (g.comp (curvesSubInclusion B hZ P hP).hom ≅ y)) ↔
            ∃ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z ∧
              Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
                CurveFamily.nonSmoothLocus B hZ X ∧
              Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom)) ∧
          ((∃ g : BasedCategory.ofFunctor (Over.map X.base.hom) ⥤ᵇ
                (curvesSubFiberedCategory B hZ P hP).val,
              Nonempty (g.comp (curvesSubInclusion B hZ P hP).hom ≅ y)) ↔
            ∀ Z : Subfunctor X.total.1, Space.IsClosedSubspace B integerBase hZ Z →
              Set.range (Space.pointsMap B integerBase hZ Z.toFunctor Z.ι) =
                CurveFamily.nonSmoothLocus B hZ X →
              Space.IsFinite B integerBase hZ (Z.ι ≫ X.toBase.hom))) ∧
      (∀ (k : Type u) [Field k] {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W)
        (e : (BigFppfOver.toScheme B integerBase hZ).obj W ≅ Spec (.of k))
        (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
        (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
        (y : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ (curvesFiberedCategory B hZ).val),
        IsClassifyingMorphism B hZ (curveFamilyOfProperOverField B hZ k g e hproper hdim) y →
          ((∃ g' : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ
                (curvesSubFiberedCategory B hZ P hP).val,
              Nonempty (g'.comp (curvesSubInclusion B hZ P hP).hom ≅ y)) ↔
            {x : (BigFppfOver.toScheme B integerBase hZ).obj T |
              ¬ InfinitesimalLifting.SmoothAt
                ((BigFppfOver.toScheme B integerBase hZ).map g) x}.Finite))
```

**`AlgebraicGeometry.curvesPlus_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusStrictlyFull.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesPlusStrictlyFull.lean#L233). The attribute's comment: “open\_substack”.

> **Stacks 0DZW.** Membership in the subcategory `Curves⁺` of families of curves whose
> reduced non-smooth locus is finite over the base is invariant under isomorphism, so `Curves⁺`
> is a strictly full subcategory.

```lean
theorem curvesPlus_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsFiniteNonSmoothLocus B hZ).IsClosedUnderIsomorphisms
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.14, Tag 0E0K](https://stacks.math.columbia.edu/tag/0E0K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
