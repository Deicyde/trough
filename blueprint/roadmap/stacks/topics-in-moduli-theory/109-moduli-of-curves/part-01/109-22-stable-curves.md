---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.hasNoRationalTailNoRationalBridge_iff_exists_isAffineOpen_isRelativelyAmple, AlgebraicGeometry.IsStableCurveFamily, AlgebraicGeometry.curvesStable_isOpenSubstack_and_factors_iff, AlgebraicGeometry.moduliStableCurves, AlgebraicGeometry.moduliStableCurvesOfGenus, AlgebraicGeometry.moduliStableCurves_decomposition_moduliStableCurvesOfGenus, AlgebraicGeometry.isSmoothOverIntegers_moduliStableCurves_and_moduliStableCurvesOfGenus, AlgebraicGeometry.curvesSmall.moduliStableCurves_isOpenSubstack_curvesDM
statement: formalized
proof: formalized
---

# 109.22 Stable curves

Section 109.22 of the Stacks Project, [Tag 0E73](https://stacks.math.columbia.edu/tag/0E73). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E74, a lemma

[Tag 0E74](https://stacks.math.columbia.edu/tag/0E74) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.hasNoRationalTailNoRationalBridge_iff_exists_isAffineOpen_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StableFamilyRelativeDualizingAmple.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StableFamilyRelativeDualizingAmple.lean#L403).

> Let `f : X → S` be a prestable family of curves of genus `g ≥ 2` (genus `g` read as in
> Stacks 0E6V: `R¹f_*𝒪_X` finite locally free of rank `g`) and let `s ∈ S`. The following are
> equivalent:
>
> 1. the fibre `X_s` has no rational tail and no rational bridge (Stacks 0E3H, 0E3M); the fibre is
>    presented by a scheme `V` of the site with a cartesian square over `Spec κ(s) → S`, as in
>    Stacks 0E75;
> 2. for some affine open `U ∋ s`, the relative dualizing sheaf `ω_{f⁻¹(U)/U}`
>    (`AlgebraicGeometry.CurveFamily.relativeDualizingSheafOver`) is ample on `f⁻¹(U)` relative to
>    `U`, for every presentation `X₁ = f⁻¹(U)` of the restricted family by a cartesian square.

```lean
theorem hasNoRationalTailNoRationalBridge_iff_exists_isAffineOpen_isRelativelyAmple
    (X : CurveFamily B hZ) (hX : IsPrestableCurveFamily B hZ X) (g : ℕ)
    (hgen : CurveFamily.HasGenus B hZ X g) (hg : 2 ≤ g)
    (s : (BigFppfOver.toScheme B integerBase hZ).obj X.base) :
    (∃ (V : BigFppfOver B integerBase hZ) (v : V ⟶ X.residuePoint B hZ s)
        (q : yoneda.obj V ⟶ X.total.obj),
        X.IsFibrePresentation B hZ s v q ∧
          HasNoRationalTailNoRationalBridge
            (((BigFppfOver.toScheme B integerBase hZ).obj X.base).residueField s)
            (X.fibreMap B hZ s v)) ↔
      ∃ U : ((BigFppfOver.toScheme B integerBase hZ).obj X.base).Opens,
        ∃ hU : IsAffineOpen U, s ∈ U ∧
        ∀ ⦃X₁ : AlgebraicSpaces B integerBase hZ⦄ (p₁ : X₁ ⟶ X.total)
          (f₁ : X₁ ⟶ schemeSpace (Space.openSub X.base U))
          (h : IsPullback p₁ f₁ X.toBase (schemeSpaceMap (Space.openSubHom X.base U))),
            Space.IsRelativelyAmple B integerBase hZ f₁ (X.relativeDualizingSheafOver hU h)
```

## Tag 0E75, a definition

[Tag 0E75](https://stacks.math.columbia.edu/tag/0E75) in the Stacks Project.

**`AlgebraicGeometry.IsStableCurveFamily`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StableCurveFamilies.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StableCurveFamilies.lean#L108). References: SGA 7 I (5.1), “special case”.

> **Stacks 0E75.** A family of curves is *stable* when it is prestable and, for every point
> of the base, its fibre there has genus at least two and has neither a rational tail nor a
> rational bridge.
>
> The constituents. The family is an `AlgebraicGeometry.CurveFamily`: flat, proper, of finite
> presentation and of relative dimension at most one, from an algebraic space to a scheme of the
> site. Prestability is `AlgebraicGeometry.IsPrestableCurveFamily`. A point of the base is an
> `AlgebraicGeometry.Space.FieldValuedPoint`, a field `p.carrier` together with a morphism from
> its spectrum to the base, and the `CategoryTheory.IsPullback` clause exhibits the scheme `V` of
> the site as the fibre of the family over that point. The conditions on the fibre are collected
> in `AlgebraicGeometry.HasGenusTwoNoRationalTailNoRationalBridge`: its
> `AlgebraicGeometry.genus` over `p.carrier` is at least two, no ideal sheaf of `V` satisfies
> `AlgebraicGeometry.IsRationalTail`, and none satisfies
> `AlgebraicGeometry.IsRationalBridge`.

```lean
abbrev IsStableCurveFamily (X : CurveFamily B hZ) : Prop
```

## Tag 0E76, a lemma

[Tag 0E76](https://stacks.math.columbia.edu/tag/0E76) in the Stacks Project.

**`AlgebraicGeometry.curvesStable_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesStableOpenSubstack.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesStableOpenSubstack.lean#L191).

> There is an open substack `Curves^{stable} ⊂ Curves` — the strictly full
> subcategory of stable families of curves (Stacks 0E75), invariant under isomorphism, whose
> inclusion into `Curves` is representable by algebraic spaces and an open immersion — such that
>
> 1. given a family of curves `f : X → U`, the classifying morphism `U → Curves` factors through
>    `Curves^{stable}` if and only if `X → U` is a stable family of curves: a scheme-valued point
>    `y` of `Curves` over `U` lifts to `Curves^{stable}` exactly when the family `y(U)` it
>    classifies is stable;
> 2. given a scheme `X` proper over a field `k` with `dim(X) ≤ 1`, the following are equivalent:
>    * (a) the classifying morphism `Spec(k) → Curves` of `X` factors through `Curves^{stable}`
>      (every scheme-valued point `y` with `y(U) ≅ X` lifts);
>    * (b) the singularities of `X` are at-worst-nodal, `dim(X) = 1`, `k = H⁰(X, 𝒪_X)`, the genus
>      of `X` is at least two, and `X` has no rational tails and no rational bridges;
>    * (c) the singularities of `X` are at-worst-nodal, `dim(X) = 1`, `k = H⁰(X, 𝒪_X)`, and the
>      dualizing sheaf `ω_X` is ample.

```lean
theorem curvesStable_isOpenSubstack_and_factors_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsStableCurveFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsStableCurveFamily B hZ)
          CurveFamily.isStableCurveFamily_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsStableCurveFamily B hZ)
          CurveFamily.isStableCurveFamily_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsStableCurveFamily B hZ),
          z ⋙ ObjectProperty.ι (IsStableCurveFamily B hZ) = y) ↔
        IsStableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    ∀ {k : Type u} [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1),
      (∀ (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsStableCurveFamily B hZ),
            z ⋙ ObjectProperty.ι (IsStableCurveFamily B hZ) = y) ↔
          letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
          haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
          Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
            IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ 2 ≤ genus X.hom ∧
            (∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
            ∀ C : X.left.IdealSheafData, ¬ IsRationalBridge k X.left C)) ∧
      ((letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
        Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ 2 ≤ genus X.hom ∧
          (∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
          ∀ C : X.left.IdealSheafData, ¬ IsRationalBridge k X.left C) ↔
        letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
        ∃ (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X.left)
          (hdim1 : topologicalKrullDim X.left = 1)
          (hH0 : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X.left ↘ Spec (.of k)).appTop)),
            haveI := hH0
            haveI := connectedSpace_of_isIso_globalSections k (X.left ↘ Spec (.of k))
            letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X.left
              hdim1 hnodal
            Scheme.Modules.IsAmple X.left
              (Stacks.Duality.dualizingSheafOverField (X.left ↘ Spec (.of k))))
```

## Tag 0E77, a definition

[Tag 0E77](https://stacks.math.columbia.edu/tag/0E77) in the Stacks Project.

**`AlgebraicGeometry.moduliStableCurves`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliCurves.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ModuliCurves.lean#L91). The attribute's comment: “the moduli stack of stable curves, 𝓜̄ = Curves^\{stable}”.

> **The moduli stack `𝓜̄ = Curves^{stable}` of stable curves**: the substack of the stack of
> curves of the families of curves which are stable (Stacks 0E75), as a category fibred in groupoids
> over the big fppf site of `Spec(ℤ)`.

```lean
def moduliStableCurves :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

**`AlgebraicGeometry.moduliStableCurvesOfGenus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOfGenus.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOfGenus.lean#L143). The attribute's comment: “the moduli stack of stable curves of genus g, 𝓜̄\_g”.

> **Stacks 0E77, `𝓜̄_g`.** The moduli stack `𝓜̄_g` of stable curves of genus `g`: the substack of
> the stack of curves of the families `f : X → S` which are stable (Stacks 0E75) and whose fibre
> over every point of `S` has genus `g`, as a category fibred in groupoids over the big fppf site of
> `Spec(ℤ)`. It lies in `𝓜̄ = AlgebraicGeometry.moduliStableCurves`, and its points are the stable
> curves of genus `g` over fields, as in part (2) of Stacks 0E78.

```lean
def moduliStableCurvesOfGenus (g : ℕ) :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

## Tag 0E78, a lemma

[Tag 0E78](https://stacks.math.columbia.edu/tag/0E78) in the Stacks Project.

**`AlgebraicGeometry.moduliStableCurves_decomposition_moduliStableCurvesOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesGenusDecomposition.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesGenusDecomposition.lean#L130). The attribute's comment: “the decomposition of the moduli stack of stable curves into the open and closed substacks of stable curves of genus g >= 2, read on the scheme-valued points of the moduli stack, together with parts (1) and (2)”. References: SGA 7 I (5.1), “(2), special case”.

> **The decomposition of `𝓜̄` by the genus.** The moduli stack of stable curves decomposes into
> open and closed substacks `𝓜̄ = ∐_{g ≥ 2} 𝓜̄_g` (`AlgebraicGeometry.moduliStableCurves`,
> `AlgebraicGeometry.moduliStableCurvesOfGenus`), and:
>
> * **Decomposition.** For every scheme-valued point of `𝓜̄`, that is every stable family of curves
>   `G` over a scheme `S`, the loci `fibreGenusLocus G g` of the points of `S` whose fibre has genus
>   `g` are open and closed in `S`; for `g ≥ 2` they are pairwise disjoint and cover `S`; and an
>   object `F ⟶ G` of `𝓜̄` over `S` lies in `𝓜̄_g` exactly when its base lands in the locus of `g`.
>   So `𝓜̄_g ×_{𝓜̄} S` is the open and closed subscheme of `S` on that locus.
> * **(1)** Given a family of curves `f : X → U`, its classifying morphism `U → Curves` factors
>   through `𝓜̄_g` if and only if `X → U` is a stable family of curves and `R¹f_*𝒪_X` is a locally
>   free `𝒪_U`-module of rank `g`.
> * **(2)** Given a proper scheme `X` over a field `k` with `dim(X) ≤ 1`, the following are
>   equivalent: (a) the classifying morphism `Spec(k) → Curves` factors through `𝓜̄_g`; (b) the
>   singularities of `X` are at-worst-nodal, `dim(X) = 1`, `k = H⁰(X, 𝒪_X)`, the genus of `X` is
>   `g`, and `X` has no rational tails or bridges; (c) the singularities of `X` are at-worst-nodal,
>   `dim(X) = 1`, `k = H⁰(X, 𝒪_X)`, the genus of `X` is `g`, and `ω_X` is ample.

```lean
theorem moduliStableCurves_decomposition_moduliStableCurvesOfGenus :
    (∀ G : CurveFamily B hZ, IsStableCurveFamily B hZ G →
      (∀ g : ℕ, IsClopen (CurveFamily.fibreGenusLocus B hZ G g)) ∧
        Pairwise (Function.onFun Disjoint
          fun g : {g : ℕ // 2 ≤ g} => CurveFamily.fibreGenusLocus B hZ G g) ∧
        ⋃ g : {g : ℕ // 2 ≤ g}, CurveFamily.fibreGenusLocus B hZ G g = Set.univ ∧
        ∀ (g : ℕ) (F : CurveFamily B hZ) (a : F ⟶ G),
          (IsStableCurveFamilyOfFibreGenus B hZ g F ↔
            Set.range (Space.pointsMap B integerBase hZ (schemeSpace F.base).obj
              (schemeSpaceMap a.baseMap).hom) ⊆ CurveFamily.fibreGenusLocus B hZ G g)) ∧
    (∀ (g : ℕ) (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          ObjectProperty.FullSubcategory (IsStableCurveFamilyOfFibreGenus B hZ g),
          z ⋙ ObjectProperty.ι (IsStableCurveFamilyOfFibreGenus B hZ g) = y) ↔
        IsStableCurveFamily B hZ (y.obj (Over.mk (𝟙 U.left))) ∧
          CurveFamily.HasGenus B hZ (y.obj (Over.mk (𝟙 U.left))) g)) ∧
    ∀ {g : ℕ} (_hg : 2 ≤ g) {k : Type u} [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1),
      (∀ (U : BigFppfOver B integerBase hZ)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
        y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
        (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
        ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
            ObjectProperty.FullSubcategory (IsStableCurveFamilyOfFibreGenus B hZ g),
            z ⋙ ObjectProperty.ι (IsStableCurveFamilyOfFibreGenus B hZ g) = y) ↔
          letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
          haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
          Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
            IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ genus X.hom = g ∧
            (∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
            ∀ C : X.left.IdealSheafData, ¬ IsRationalBridge k X.left C)) ∧
      ((letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
        Stacks.Curves.HasAtWorstNodalSingularities k X.left ∧ topologicalKrullDim X.left = 1 ∧
          IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop) ∧ genus X.hom = g ∧
          (∀ C : X.left.IdealSheafData, ¬ IsRationalTail k X.left C) ∧
          ∀ C : X.left.IdealSheafData, ¬ IsRationalBridge k X.left C) ↔
        letI : X.left.Over (Spec (.of k)) := ⟨X.hom⟩
        haveI : IsProper (X.left ↘ Spec (.of k)) := inferInstanceAs (IsProper X.hom)
        ∃ (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X.left)
          (hdim1 : topologicalKrullDim X.left = 1)
          (hH0 : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X.left ↘ Spec (.of k)).appTop)),
          genus X.hom = g ∧
            haveI := hH0
            haveI := connectedSpace_of_isIso_globalSections k (X.left ↘ Spec (.of k))
            letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X.left
              hdim1 hnodal
            Scheme.Modules.IsAmple X.left
              (Stacks.Duality.dualizingSheafOverField (X.left ↘ Spec (.of k))))
```

## Tag 0E79, a lemma

[Tag 0E79](https://stacks.math.columbia.edu/tag/0E79) in the Stacks Project.

**`AlgebraicGeometry.isSmoothOverIntegers_moduliStableCurves_and_moduliStableCurvesOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StableCurvesSmoothOverSpecZ.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StableCurvesSmoothOverSpecZ.lean#L118). The attribute's comment: “both morphisms: 𝓜̄ → Spec(ℤ) (first conjunct) and 𝓜̄\_g → Spec(ℤ) for every g (second conjunct, for 𝓜̄\_g cut out by R¹f\_*𝒪\_X locally free of rank g as in 0E78 (1), and by all fibres of genus g as in 0E77) are smooth”.

> **Stacks 0E79.** The morphisms `𝓜̄ → Spec(ℤ)` and, for every `g`, `𝓜̄_g → Spec(ℤ)` are smooth.
> Here `𝓜̄` is the open substack of the algebraic stack of curves (Stacks 0D5A) of the stable
> families (Stacks 0E76), and `𝓜̄_g` is its open substack of the stable families of genus `g`. The
> second conjunct states smoothness of `𝓜̄_g` in both forms of its families: stable with `R¹f_*𝒪_X`
> locally free of rank `g` (part (1) of Stacks 0E78, `AlgebraicGeometry.IsStableCurveFamilyOfGenus`),
> and stable with every fibre of genus `g` (Stacks 0E77,
> `AlgebraicGeometry.IsStableCurveFamilyOfFibreGenus`); the two properties of families agree
> (`AlgebraicGeometry.isStableCurveFamilyOfFibreGenus_iff_isStableCurveFamilyOfGenus`),
> so they cut out the same open substack. Both `𝓜̄` and `𝓜̄_g` are open substacks of
> `Curves^{nodal}`, which is smooth over `Spec(ℤ)` (Stacks 0E00).
>
> The statement assumes nothing beyond the site `B` containing `Spec(ℤ)`; the algebraicity
> of `Curves` (Stacks 0D5A), its limit preservation (Stacks 0D55) and the openness of `𝓜̄` and
> `𝓜̄_g` are all proved.

```lean
theorem isSmoothOverIntegers_moduliStableCurves_and_moduliStableCurvesOfGenus :
    IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
        (isOpenCurvesLocus_isStableCurveFamily B hZ) ∧
      ∀ g : ℕ,
        IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
            (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_fibreGenus B hZ g) ∧
          IsSmoothOverIntegers B hZ (isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)
            (isOpenCurvesLocus_isStableCurveFamilyOfFibreGenus B hZ g)
```

## Tag 0E7A, a lemma

[Tag 0E7A](https://stacks.math.columbia.edu/tag/0E7A) in the Stacks Project.

**`AlgebraicGeometry.curvesSmall.moduliStableCurves_isOpenSubstack_curvesDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOpenInCurvesDM.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOpenInCurvesDM.lean#L54).

> The stacks `𝓜̄` and `𝓜̄_g` are open substacks of `Curves^{DM}`; in particular they are DM
> (Stacks 050D) and Deligne–Mumford stacks (Stacks 03YO).
>
> In the statement, `Curves` is the algebraic stack `AlgebraicGeometry.curvesAlgebraicStack` (the
> small model of the stack of curves, equivalent over the site to the category of families of
> curves through `AlgebraicGeometry.curvesSmallEquivalence`), algebraic by Stacks 0D5A
> (`AlgebraicGeometry.curvesFiberedCategory_isAlgebraicStack`). `W` is `Curves^{DM}`: the open
> substack whose objects are those of the Deligne–Mumford locus `Stack.dmLocus` (Stacks 0DSW), and
> it is DM. `M` is `𝓜̄`: an open substack of `Curves` whose objects are exactly the stable families
> of curves (Stacks 0E75), the families of `AlgebraicGeometry.moduliStableCurves`; `M_g` is `𝓜̄_g`:
> an open substack whose objects are exactly the stable families whose fibre over every point has
> genus `g`, the families of `AlgebraicGeometry.moduliStableCurvesOfGenus` (Stacks 0E77, 0E78).
> Both are contained in `W` (an open substack of `Curves` contained in the open substack `W` is an
> open substack of `W`), DM, and Deligne–Mumford stacks.
>
> The statement holds for every `g`, not only in the range `g ≥ 2` of Stacks 0E77.

```lean
theorem moduliStableCurves_isOpenSubstack_curvesDM (g : ℕ) :
    ∃ W M Mg : Stack.OpenSubstack
        (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)),
      (W.property =
          Stack.dmLocus B integerBase hZ B.contains_terminal
            (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)) ∧
        Stack.AlgebraicStacks.IsAbsolutelyDM B integerBase hZ B.contains_terminal
          W.toAlgebraicStack) ∧
      ((∀ F : CurveFamily B hZ,
          M.property ((curvesSmallEquivalence B hZ
            (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).functor.obj F) ↔
            IsStableCurveFamily B hZ F) ∧
        M.property ≤ W.property ∧
        Stack.AlgebraicStacks.IsAbsolutelyDM B integerBase hZ B.contains_terminal
          M.toAlgebraicStack ∧
        Stack.IsDeligneMumfordStack.{u, w} B integerBase hZ M.toAlgebraicStack.val.val) ∧
      ((∀ F : CurveFamily B hZ,
          Mg.property ((curvesSmallEquivalence B hZ
            (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).functor.obj F) ↔
            IsStableCurveFamilyOfFibreGenus B hZ g F) ∧
        Mg.property ≤ W.property ∧
        Stack.AlgebraicStacks.IsAbsolutelyDM B integerBase hZ B.contains_terminal
          Mg.toAlgebraicStack ∧
        Stack.IsDeligneMumfordStack.{u, w} B integerBase hZ Mg.toAlgebraicStack.val.val)
```

## Tag 0E87, a lemma

[Tag 0E87](https://stacks.math.columbia.edu/tag/0E87) in the Stacks Project.

**`AlgebraicGeometry.curvesPointSet_moduliSmoothOfGenus_isOpen_dense_in_stableOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesOpenDense.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ModuliSmoothCurvesOpenDense.lean#L323).

> Let `g ≥ 2`. The inclusion `|𝓜_g| ⊂ |𝓜̄_g|` is that of an open dense
> subset.
>
> `𝓜_g` is the substack of the stack of curves of families `f : X → S` which are smooth of relative
> dimension one with `f_*𝒪_X = 𝒪_S` universally and `R¹f_*𝒪_X` locally free of rank `g`
> (Stacks 0E83), and `𝓜̄_g` that of stable families with `R¹f_*𝒪_X` locally free of rank `g`
> (Stacks 0E78); `|𝓜_g|` and `|𝓜̄_g|` are their images in `|Curves|`, with the topology of
> Stacks 04Y8, and `|𝓜̄_g|` carries the subspace topology.

```lean
theorem curvesPointSet_moduliSmoothOfGenus_isOpen_dense_in_stableOfGenus
    (g : ℕ) (hg : 2 ≤ g) :
    curvesPointSet B hZ (fun F => IsSmoothH0Family B hZ F ∧ CurveFamily.HasGenus B hZ F g) ⊆
        curvesPointSet B hZ (IsStableCurveFamilyOfGenus B hZ g) ∧
      IsOpen (Subtype.val ⁻¹' curvesPointSet B hZ
          (fun F => IsSmoothH0Family B hZ F ∧ CurveFamily.HasGenus B hZ F g) :
        Set (curvesPointSet B hZ (IsStableCurveFamilyOfGenus B hZ g))) ∧
      Dense (Subtype.val ⁻¹' curvesPointSet B hZ
          (fun F => IsSmoothH0Family B hZ F ∧ CurveFamily.HasGenus B hZ F g) :
        Set (curvesPointSet B hZ (IsStableCurveFamilyOfGenus B hZ g)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.22, Tag 0E73](https://stacks.math.columbia.edu/tag/0E73)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
