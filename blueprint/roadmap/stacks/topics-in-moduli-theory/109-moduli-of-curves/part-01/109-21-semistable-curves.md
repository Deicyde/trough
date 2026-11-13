---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.hasNoRationalTailFibre_iff_isCounitSurjectiveAbove, AlgebraicGeometry.IsSemistableCurveFamily, AlgebraicGeometry.curvesSemistable_isOpenSubstack_and_factors_iff, AlgebraicGeometry.curvesSemistableOfGenus_isOpenSubstack_and_factors_iff, AlgebraicGeometry.factors_curvesSemistableOfGenus_over_field_iff_noRationalTail_and_globallyGenerated, AlgebraicGeometry.isSmoothOverIntegers_curvesSemistable_and_curvesSemistableOfGenus
statement: formalized
proof: formalized
---

# 109.21 Semistable curves

Section 109.21 of the Stacks Project, [Tag 0E6X](https://stacks.math.columbia.edu/tag/0E6X). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E6Y, a lemma

[Tag 0E6Y](https://stacks.math.columbia.edu/tag/0E6Y) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.hasNoRationalTailFibre_iff_isCounitSurjectiveAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NoRationalTailDualizingPowerCounit.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NoRationalTailDualizingPowerCounit.lean#L149).

> Let `f : X → S` be a prestable family of curves of genus `g ≥ 1`, with relative dualizing
> complex `ω^•_{X/S}` and relative dualizing sheaf `ω_{X/S} = H^{-1}(ω^•_{X/S})`. Let `s ∈ S` and
> `m ≥ 2`. The fibre `X_s` has no rational tail if and only if `f^*f_*ω_{X/S}^{⊗ m} ⟶ ω_{X/S}^{⊗ m}`
> is surjective over `f⁻¹(U)` for some open `U ∋ s`.

```lean
theorem hasNoRationalTailFibre_iff_isCounitSurjectiveAbove (X : CurveFamily B hZ)
    (hX : IsPrestableCurveFamily B hZ X) {g : ℕ} (hg : X.HasGenus B hZ g) (hg1 : 1 ≤ g)
    (D : Space.RelativeDualizingComplex B.contains_terminal X.toBase X.proper X.flat
      X.finitePresentation)
    (s : (BigFppfOver.toScheme B integerBase hZ).obj X.base) {m : ℕ} (hm : 2 ≤ m) :
    X.HasNoRationalTailFibre B hZ (X.residueFieldPoint s) ↔
      X.IsCounitSurjectiveAbove
        (@Space.invertibleTensorPower B integerBase hZ X.total.1 X.total.2
          (X.dualizingSheafOfComplex D) (isInvertible_dualizingSheafOfComplex hX D) m) s
```

## Tag 0E6Z, a definition

[Tag 0E6Z](https://stacks.math.columbia.edu/tag/0E6Z) in the Stacks Project.

**`AlgebraicGeometry.IsSemistableCurveFamily`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/SemistableCurveFamilies.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/SemistableCurveFamilies.lean#L78).

> **Stacks 0E6Z.** A family of curves is *semistable* when it is prestable and, for every
> point of the base, its fibre there has genus at least one and no rational tail.

```lean
abbrev IsSemistableCurveFamily (X : CurveFamily B hZ) : Prop
```

## Tag 0E70, a lemma

[Tag 0E70](https://stacks.math.columbia.edu/tag/0E70) in the Stacks Project.

**`AlgebraicGeometry.curvesSemistable_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableSubstack.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableSubstack.lean#L97). The attribute's comment: “the whole statement: the open substack Curves^\{semistable} and parts (1) and (2)”.

> There is an open substack `Curves^{semistable} ⊂ Curves` — the strictly full subcategory of
> semistable families of curves (Stacks 0E6Z), whose inclusion is representable by algebraic spaces
> and an open immersion — such that
>
> 1. the classifying morphism of a family of curves `X ⟶ S` factors through it exactly when
>    `X ⟶ S` is a semistable family of curves, and
> 2. for a scheme `X` proper over a field `k` with `dim(X) ≤ 1` (with `Spec k` in the site, so that
>    its classifying morphism `Spec k ⟶ Curves` exists), the classifying morphism of `X` factors
>    through it (a) exactly when (b) the singularities of `X` are at-worst-nodal, `dim(X) = 1`,
>    `k = H⁰(X, 𝒪_X)`, the genus of `X` is at least one and `X` has no rational tail, and (a)
>    exactly when (c) the singularities of `X` are at-worst-nodal, `dim(X) = 1`,
>    `k = H⁰(X, 𝒪_X)` and `ω_X^{⊗ m}` is globally generated for every `m ≥ 2`.

```lean
theorem curvesSemistable_isOpenSubstack_and_factors_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsSemistableCurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsSemistableCurveFamily B hZ)
          (CurveFamily.isSemistableCurveFamily_of_hom B hZ)).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsSemistableCurveFamily B hZ)
          (CurveFamily.isSemistableCurveFamily_of_hom B hZ))) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsSemistableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsSemistableCurveFamily B hZ) = y) ↔
        IsSemistableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsSemistableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsSemistableCurveFamily B hZ) = y) ↔
        letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ 1 ≤ genus X.hom ∧
            ∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsSemistableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsSemistableCurveFamily B hZ) = y) ↔
        letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
        ∃ (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X.left)
          (hdim1 : topologicalKrullDim X.left = 1)
          (hΓ : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop)),
          haveI : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X.left ↘ Spec (.of k)).appTop) := hΓ
          haveI := connectedSpace_of_isIso_globalSections k (X.left ↘ Spec (.of k))
          letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X.left
            hdim1 hnodal
          ∀ m : ℕ, 2 ≤ m → SheafOfModules.IsGeneratedByGlobalSections
            (tensorPower X.left.presheaf X.left.ringCatSheaf.2
              (Stacks.Duality.dualizingSheafOverField (X.left ↘ Spec (.of k))) m)))
```

## Tag 0E71, a lemma

[Tag 0E71](https://stacks.math.columbia.edu/tag/0E71) in the Stacks Project.

**`AlgebraicGeometry.curvesSemistableOfGenus_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableGenusDecomposition.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableGenusDecomposition.lean#L93). The attribute's comment: “the decomposition Curves^\{semistable} = ∐\_\{g ≥ 1} Curves^\{semistable}\_g into open and closed substacks, and part (1)”.

> For every `g`, `Curves^{semistable}_g` is an open substack of `Curves` contained in
> `Curves^{semistable}`: its inclusion is representable by algebraic spaces and an open immersion.
> Part (1): the classifying morphism of a family of curves `f : X → S` factors through
> `Curves^{semistable}_g` exactly when `f` is semistable and `R¹f_*𝒪_X` is a locally free
> `𝒪_S`-module of rank `g`. Over every semistable family with base `S`, the loci of the
> `Curves^{semistable}_g` are open and closed subsets of `S`, pairwise disjoint, empty for `g = 0`
> and covering `S` for `g ≥ 1`: so `Curves^{semistable} = ∐_{g ≥ 1} Curves^{semistable}_g` as open
> and closed substacks.

```lean
theorem curvesSemistableOfGenus_isOpenSubstack_and_factors_iff :
    (∀ g : ℕ,
      ((show ObjectProperty (CurveFamily B hZ) from
          IsSemistableCurveFamilyOfFibreGenus B hZ g).IsClosedUnderIsomorphisms ∧
        Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
          (curvesSubstackInclusion B hZ (IsSemistableCurveFamilyOfFibreGenus B hZ g)
            (isOpenCurvesLocus_isSemistableCurveFamilyOfFibreGenus
              (isOpenCurvesLocus_isSemistableCurveFamily_of
                (isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
                  (hasEtaleLocalSchemeCharts B hZ))
                (hasUniversallyBijectiveGlobalFunctions_of (hasEtaleLocalSchemeCharts B hZ))
                (prestableSemistableFibresOpen B hZ))
              (prestableGenusLociOpen_of (hasEtaleLocalSchemeCharts B hZ)) g).prop_of_hom).hom ∧
        Stack.IsOpenImmersion B integerBase hZ
          (curvesSubstackInclusion B hZ (IsSemistableCurveFamilyOfFibreGenus B hZ g)
            (isOpenCurvesLocus_isSemistableCurveFamilyOfFibreGenus
              (isOpenCurvesLocus_isSemistableCurveFamily_of
                (isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
                  (hasEtaleLocalSchemeCharts B hZ))
                (hasUniversallyBijectiveGlobalFunctions_of (hasEtaleLocalSchemeCharts B hZ))
                (prestableSemistableFibresOpen B hZ))
              (prestableGenusLociOpen_of (hasEtaleLocalSchemeCharts B hZ)) g).prop_of_hom)) ∧
      (∀ X : CurveFamily B hZ,
        IsSemistableCurveFamilyOfFibreGenus B hZ g X → IsSemistableCurveFamily B hZ X) ∧
      ∀ (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsSemistableCurveFamilyOfFibreGenus B hZ g),
            z ⋙ ObjectProperty.ι (IsSemistableCurveFamilyOfFibreGenus B hZ g) = y) ↔
          IsSemistableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))) ∧
            CurveFamily.HasGenus B hZ (y.obj (Over.mk (𝟙 U.left))) g)) ∧
    ∀ G : CurveFamily B hZ, IsSemistableCurveFamily B hZ G →
      ∃ Ω : ℕ → Set ((BigFppfOver.toScheme B integerBase hZ).obj G.base),
        (∀ g, IsOpen (Ω g) ∧ IsClosed (Ω g)) ∧ Pairwise (fun g g' => Disjoint (Ω g) (Ω g')) ∧
          Ω 0 = ∅ ∧ ⋃ (g : ℕ) (_ : 1 ≤ g), Ω g = Set.univ ∧
          ∀ (g : ℕ) (F : CurveFamily B hZ) (a : F ⟶ G),
            IsSemistableCurveFamilyOfFibreGenus B hZ g F ↔
              Set.range ((BigFppfOver.toScheme B integerBase hZ).map a.baseMap) ⊆ Ω g
```

**`AlgebraicGeometry.factors_curvesSemistableOfGenus_over_field_iff_noRationalTail_and_globallyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableGenusDecomposition.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableGenusDecomposition.lean#L146). The attribute's comment: “part (2): (a) ⇔ (b) and (a) ⇔ (c), for a proper scheme of dimension at most one over a field”.

> Let `g ≥ 1` and let `X` be a proper scheme of dimension at most one over a field `k` (with
> `Spec k` in the site, so that the classifying morphism `Spec k ⟶ Curves` of `X` exists). The
> classifying morphism of `X` factors through `Curves^{semistable}_g` (a) exactly when (b) the
> singularities of `X` are at-worst-nodal, `dim X = 1`, `k = H⁰(X, 𝒪_X)`, the genus of `X` is `g`
> and `X` has no rational tail, and (a) exactly when (c) the singularities of `X` are
> at-worst-nodal, `dim X = 1`, `k = H⁰(X, 𝒪_X)`, the genus of `X` is `g` and `ω_X^{⊗m}` is globally
> generated for every `m ≥ 2`.

```lean
theorem factors_curvesSemistableOfGenus_over_field_iff_noRationalTail_and_globallyGenerated
    {g : ℕ} (hg : 1 ≤ g)
    {k : Type u} [Field k] (X : Over (Spec (.of k))) [IsProper X.hom]
    (hk : B.Contains (Spec (.of k))) (hdim : topologicalKrullDim X.left ≤ 1)
    (U : BigFppfOver B integerBase hZ) (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom)
    (e : y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) :
    ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsSemistableCurveFamilyOfFibreGenus B hZ g),
        z ⋙ ObjectProperty.ι (IsSemistableCurveFamilyOfFibreGenus B hZ g) = y) ↔
      letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
      Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
        IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ genus X.hom = g ∧
          ∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
    ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        ObjectProperty.FullSubcategory (IsSemistableCurveFamilyOfFibreGenus B hZ g),
        z ⋙ ObjectProperty.ι (IsSemistableCurveFamilyOfFibreGenus B hZ g) = y) ↔
      letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
      haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
      ∃ (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X.left)
        (hdim1 : topologicalKrullDim X.left = 1)
        (hΓ : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop)),
        haveI : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X.left ↘ Spec (.of k)).appTop) := hΓ
        haveI := connectedSpace_of_isIso_globalSections k (X.left ↘ Spec (.of k))
        letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X.left
          hdim1 hnodal
        genus X.hom = g ∧ ∀ m : ℕ, 2 ≤ m → SheafOfModules.IsGeneratedByGlobalSections
          (tensorPower X.left.presheaf X.left.ringCatSheaf.2
            (Stacks.Duality.dualizingSheafOverField (X.left ↘ Spec (.of k))) m))
```

## Tag 0E72, a lemma

[Tag 0E72](https://stacks.math.columbia.edu/tag/0E72) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_curvesSemistable_and_curvesSemistableOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableSmoothness.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesSemistableSmoothness.lean#L64). The attribute's comment: “both morphisms Curves^\{semistable} → Spec(ℤ) and Curves^\{semistable}\_g → Spec(ℤ), for every g”.

> The morphisms `Curves^{semistable} → Spec(ℤ)` and, for every `g`,
> `Curves^{semistable}_g → Spec(ℤ)` are smooth. Here `Curves^{semistable}` and
> `Curves^{semistable}_g` are the open substacks of the algebraic stack of curves (Stacks 0D5A) of
> the semistable families and of the semistable families with all fibres of genus `g`.

```lean
theorem isSmoothOverIntegers_curvesSemistable_and_curvesSemistableOfGenus :
    IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
        (isOpenCurvesLocus_isSemistableCurveFamily_of
          (isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
            (hasEtaleLocalSchemeCharts B hZ))
          (hasUniversallyBijectiveGlobalFunctions_of (hasEtaleLocalSchemeCharts B hZ))
          (prestableSemistableFibresOpen B hZ)) ∧
      ∀ g : ℕ, IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
        (isOpenCurvesLocus_isSemistableCurveFamilyOfFibreGenus
          (isOpenCurvesLocus_isSemistableCurveFamily_of
            (isOpenCurvesLocus_hasBijectiveGlobalFunctionsOnFieldFibres_of
              (hasEtaleLocalSchemeCharts B hZ))
            (hasUniversallyBijectiveGlobalFunctions_of (hasEtaleLocalSchemeCharts B hZ))
            (prestableSemistableFibresOpen B hZ))
          (prestableGenusLociOpen_of (hasEtaleLocalSchemeCharts B hZ)) g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.21, Tag 0E6X](https://stacks.math.columbia.edu/tag/0E6X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
