---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsPrestableCurveFamily, AlgebraicGeometry.factors_curvesPrestable_iff, AlgebraicGeometry.factors_curvesPrestable_over_field_iff, AlgebraicGeometry.curvesPrestable_isOpenSubstack, AlgebraicGeometry.curvesPrestable_isOpenSubstack_and_factors_iff, AlgebraicGeometry.curvesPrestableGenus_isOpenSubstack_and_factors_iff_and_decomposition_and_over_field_iff, AlgebraicGeometry.isSmoothOverIntegers_curvesPrestable, AlgebraicGeometry.isSmoothOverIntegers_curvesPrestableOfGenus
statement: formalized
proof: formalized
---

# 109.20 Prestable curves

Section 109.20 of the Stacks Project, [Tag 0E6S](https://stacks.math.columbia.edu/tag/0E6S). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E6T, a definition

[Tag 0E6T](https://stacks.math.columbia.edu/tag/0E6T) in the Stacks Project.

**`AlgebraicGeometry.IsPrestableCurveFamily`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PrestableCurveFamilies.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PrestableCurveFamilies.lean#L88).

> **Stacks 0E6T.** A family of curves is *prestable* when its structure morphism is
> at-worst-nodal of relative dimension one and the direct image of its structure sheaf is the
> structure sheaf of the base, universally.

```lean
abbrev IsPrestableCurveFamily (X : CurveFamily B hZ) : Prop
```

## Tag 0E6U, a lemma

[Tag 0E6U](https://stacks.math.columbia.edu/tag/0E6U) in the Stacks Project.

**`AlgebraicGeometry.factors_curvesPrestable_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean#L75). The attribute's comment: “part (1)”.

> The classifying morphism of a family of curves `X ⟶ S` factors through the strictly full
> subcategory `Curves^{prestable}` of prestable families (Stacks 0E6T) exactly when `X ⟶ S` is
> prestable: a scheme-valued point `y` of `Curves` over `U` lifts to `Curves^{prestable}` exactly
> when the family `y(U)` it classifies is prestable.

```lean
theorem factors_curvesPrestable_iff (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsPrestableCurveFamily B hZ),
        z ⋙ ObjectProperty.ι (IsPrestableCurveFamily B hZ) = y) ↔
      IsPrestableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left)))
```

**`AlgebraicGeometry.factors_curvesPrestable_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean#L94). The attribute's comment: “part (2)”.

> Let `X` be a proper scheme over a field `k` with `dim(X) ≤ 1` (with `Spec k` in the site, so
> that its classifying morphism `Spec k ⟶ Curves` exists). The classifying morphism of `X` factors
> through `Curves^{prestable}` exactly when the singularities of `X` are at-worst-nodal,
> `dim(X) = 1` and `k = H⁰(X, 𝒪_X)`.

```lean
theorem factors_curvesPrestable_over_field_iff
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
    (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom)
    (e : y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsPrestableCurveFamily B hZ),
        z ⋙ ObjectProperty.ι (IsPrestableCurveFamily B hZ) = y) ↔
      ((letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩;
        Stacks.Curves.HasAtWorstNodalSingularities k X.left) ∧
        topologicalKrullDim X.left = 1 ∧ IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop))
```

**`AlgebraicGeometry.curvesPrestable_isOpenSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean#L143). The attribute's comment: “the open substack Curves^\{prestable} of Curves”.

> `Curves^{prestable}`, the strictly full subcategory of prestable families of curves
> (Stacks 0E6T), is an open substack of `Curves`: prestability is invariant under isomorphism, and
> the inclusion `Curves^{prestable} ⟶ Curves` is representable by algebraic spaces and an open
> immersion.

```lean
theorem curvesPrestable_isOpenSubstack :
    ObjectProperty.IsClosedUnderIsomorphisms (IsPrestableCurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsPrestableCurveFamily B hZ)
          CurveFamily.isPrestableCurveFamily_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsPrestableCurveFamily B hZ)
          CurveFamily.isPrestableCurveFamily_of_hom)
```

**`AlgebraicGeometry.curvesPrestable_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSubstack.lean#L163). The attribute's comment: “the whole statement: the open substack Curves^\{prestable} and parts (1) and (2)”.

> There is an open substack `Curves^{prestable} ⊂ Curves` — the strictly full subcategory of
> prestable families of curves, whose inclusion is representable by algebraic spaces and an open
> immersion — such that
>
> 1. the classifying morphism of a family of curves `X ⟶ S` factors through it exactly when
>    `X ⟶ S` is a prestable family of curves, and
> 2. for a scheme `X` proper over a field `k` with `dim(X) ≤ 1`, the classifying morphism
>    `Spec k ⟶ Curves` of `X` factors through it exactly when the singularities of `X` are
>    at-worst-nodal, `dim(X) = 1` and `k = H⁰(X, 𝒪_X)`.

```lean
theorem curvesPrestable_isOpenSubstack_and_factors_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsPrestableCurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsPrestableCurveFamily B hZ)
          CurveFamily.isPrestableCurveFamily_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsPrestableCurveFamily B hZ)
          CurveFamily.isPrestableCurveFamily_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsPrestableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsPrestableCurveFamily B hZ) = y) ↔
        IsPrestableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsPrestableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsPrestableCurveFamily B hZ) = y) ↔
        ((letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩;
          Stacks.Curves.HasAtWorstNodalSingularities k X.left) ∧
          topologicalKrullDim X.left = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop))))
```

## Tag 0E6V, a lemma

[Tag 0E6V](https://stacks.math.columbia.edu/tag/0E6V) in the Stacks Project.

**`AlgebraicGeometry.curvesPrestableGenus_isOpenSubstack_and_factors_iff_and_decomposition_and_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableGenusDecomposition.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableGenusDecomposition.lean#L229).

> **Stacks 0E6V.** There is a decomposition
> `Curves^{prestable} = ∐_{g ≥ 0} Curves^{prestable}_g` into open and closed substacks, where
> 1. the classifying morphism of a family of curves `f : X → S` factors through
>    `Curves^{prestable}_g` exactly when `f` is a prestable family of curves and `R¹f_*𝒪_X` is a
>    locally free `𝒪_S`-module of rank `g`;
> 2. for a scheme `X` proper over a field `k` with `dim(X) ≤ 1` (a proper morphism `p : T ⟶ W` of
>    the site with `W = Spec k`), the classifying morphism `Spec k → Curves` of `X` factors through
>    `Curves^{prestable}_g` exactly when the singularities of `X` are at-worst-nodal, `dim(X) = 1`,
>    `k = H⁰(X, 𝒪_X)` and the genus of `X` is `g`.
>
> Each `Curves^{prestable}_g` is an open substack of `Curves` contained in `Curves^{prestable}`
> (the first conjunct, with the second), and over every scheme-valued point of
> `Curves^{prestable}` — a prestable family `G` over a scheme `S` — the loci `Ω_g ⊂ S` of the
> `Curves^{prestable}_g` are open and closed, pairwise disjoint and cover `S`, a family mapping to
> `G` lying in `Curves^{prestable}_g` exactly when its base maps into `Ω_g` (the third conjunct):
> this is the decomposition into open and closed substacks.

```lean
theorem curvesPrestableGenus_isOpenSubstack_and_factors_iff_and_decomposition_and_over_field_iff :
    (∀ g : ℕ,
      (ObjectProperty.IsClosedUnderIsomorphisms (IsPrestableGenusCurveFamily B hZ g) ∧
        Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
          (curvesSubstackInclusion B hZ (IsPrestableGenusCurveFamily B hZ g)
            (isOpenCurvesLocus_isPrestableGenusCurveFamily g).prop_of_hom).hom ∧
        Stack.IsOpenImmersion B integerBase hZ
          (curvesSubstackInclusion B hZ (IsPrestableGenusCurveFamily B hZ g)
            (isOpenCurvesLocus_isPrestableGenusCurveFamily g).prop_of_hom)) ∧
      (∀ X : CurveFamily B hZ, IsPrestableGenusCurveFamily B hZ g X →
        IsPrestableCurveFamily B hZ X) ∧
      ∀ (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsPrestableGenusCurveFamily B hZ g),
            z ⋙ ObjectProperty.ι (IsPrestableGenusCurveFamily B hZ g) = y) ↔
          IsPrestableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))) ∧
            RingedSite.IsFiniteLocallyFreeOfRank
              (Space.smallEtaleRingedSite B integerBase hZ
                (schemeSpace (y.obj (Over.mk (𝟙 U.left))).base).1
                (schemeSpace (y.obj (Over.mk (𝟙 U.left))).base).2)
              ((y.obj (Over.mk (𝟙 U.left))).firstDirectImage B hZ) g)) ∧
    (∀ G : CurveFamily B hZ, IsPrestableCurveFamily B hZ G →
      ∃ Ω : ℕ → Set (Space.points B integerBase hZ (schemeSpace G.base).obj),
        (∀ g, IsOpen (Ω g) ∧ IsClosed (Ω g)) ∧ Pairwise (fun g g' => Disjoint (Ω g) (Ω g')) ∧
          (⋃ g, Ω g) = Set.univ ∧
          ∀ (g : ℕ) (F : CurveFamily B hZ) (a : F ⟶ G),
            IsPrestableGenusCurveFamily B hZ g F ↔
              Set.range (Space.pointsMap B integerBase hZ (schemeSpace F.base).obj
                (schemeSpaceMap a.baseMap).hom) ⊆ Ω g) ∧
    (∀ (g : ℕ) (k : Type u) [Field k] {T W : BigFppfOver B integerBase hZ} (p : T ⟶ W)
      (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
      (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map p))
      (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOverFieldOfProper B hZ p k hW hproper hdim) →
      letI : ((BigFppfOver.toScheme B integerBase hZ).obj T).Over (Spec (.of k)) :=
        ⟨(BigFppfOver.toScheme B integerBase hZ).map p ≫ eqToHom hW⟩
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsPrestableGenusCurveFamily B hZ g),
          z ⋙ ObjectProperty.ι (IsPrestableGenusCurveFamily B hZ g) = y) ↔
        (Stacks.Curves.HasAtWorstNodalSingularities k
            ((BigFppfOver.toScheme B integerBase hZ).obj T) ∧
          topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) = 1 ∧
          Function.Bijective
            ((BigFppfOver.toScheme B integerBase hZ).map p ≫ eqToHom hW).appTop ∧
          genus ((BigFppfOver.toScheme B integerBase hZ).map p ≫ eqToHom hW) = g)))
```

## Tag 0E6W, a lemma

[Tag 0E6W](https://stacks.math.columbia.edu/tag/0E6W) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_curvesPrestable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSmooth.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSmooth.lean#L76). The attribute's comment: “the morphism Curves^\{prestable} → Spec(ℤ) is smooth”.

> The morphism `Curves^{prestable} → Spec(ℤ)` is smooth. Here `Curves^{prestable}` is the open
> substack of the algebraic stack of curves (Stacks 0D5A) of the prestable families of curves
> (Stacks 0E6U).

```lean
theorem isSmoothOverIntegers_curvesPrestable :
    IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
      (isOpenCurvesLocus_isPrestableCurveFamily B hZ)
```

**`AlgebraicGeometry.isSmoothOverIntegers_curvesPrestableOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSmooth.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesPrestableSmooth.lean#L86). The attribute's comment: “the morphism Curves^\{prestable}\_g → Spec(ℤ) is smooth, for every g”.

> For every `g`, the morphism `Curves^{prestable}_g → Spec(ℤ)` is smooth. Here
> `Curves^{prestable}_g` is the open substack of the algebraic stack of curves (Stacks 0D5A) of the
> prestable families `f : X → S` with `R¹f_*𝒪_X` locally free of rank `g` (Stacks 0E6V, part (1)).

```lean
theorem isSmoothOverIntegers_curvesPrestableOfGenus (g : ℕ) :
    IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
      (isOpenCurvesLocus_isPrestableGenusCurveFamily (B := B) (hZ := hZ) g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.20, Tag 0E6S](https://stacks.math.columbia.edu/tag/0E6S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
