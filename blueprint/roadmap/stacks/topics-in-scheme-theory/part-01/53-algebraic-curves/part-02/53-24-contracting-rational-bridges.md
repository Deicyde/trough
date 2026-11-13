---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsRationalBridge, Stacks.Curves.exists_isProper_structureMorphism_and_genus_eq_contraction_bridge, Stacks.Curves.hasAtWorstNodalSingularities_pushoutScheme_bridge, Stacks.Curves.isField_globalSections_bridge, Stacks.Curves.isNode_of_mem_intersection_bridge, Stacks.Curves.moduleFinite_and_isSeparable_globalSections_bridge, Stacks.Curves.isField_and_isSeparable_or_algEquiv_prod_intersectionSections_bridge, Stacks.Curves.exists_ringEquiv_completedLocalRing_contraction_bridge
statement: formalized
proof: formalized
---

# 53.24 Contracting rational bridges

Section 53.24 of the Stacks Project, [Tag 0E7M](https://stacks.math.columbia.edu/tag/0E7M). 6 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E3M, an example

[Tag 0E3M](https://stacks.math.columbia.edu/tag/0E3M) in the Stacks Project.

**`AlgebraicGeometry.IsRationalBridge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Basic.lean#L48). The attribute's comment: “rational\_bridge”.

> An integral irreducible component is a rational bridge if the closure of its complement is
> nonempty, the intersection has degree two over its global functions, and its genus is zero.

```lean
def IsRationalBridge (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))] (C : X.IdealSheafData) : Prop
```

**`Stacks.Curves.exists_isProper_structureMorphism_and_genus_eq_contraction_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/ContractionGenus.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/ContractionGenus.lean#L112). The attribute's comment: “Y is proper over k of dimension one with H⁰(Y, 𝒪\_Y) = k and the genus of X”.

> **The target of a contraction of a rational bridge is a proper scheme over `k` of dimension
> one with `H⁰(Y, 𝒪_Y) = k` and the genus of `X`.** That is, there is a morphism
> `g : Y ⟶ Spec k` with `c ≫ g` the structure morphism of `X` which has these properties.

```lean
theorem exists_isProper_structureMorphism_and_genus_eq_contraction_bridge
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C)
    {Y : Scheme.{u}} (c : X ⟶ Y) (hc : IsContractionOfRationalBridge hC c) :
    ∃ g : Y ⟶ Spec (.of k), c ≫ g = X ↘ Spec (.of k) ∧ IsProper g ∧
      topologicalKrullDim Y = 1 ∧ IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ g.appTop) ∧
      genus g = genus (X ↘ Spec (.of k))
```

**`Stacks.Curves.hasAtWorstNodalSingularities_pushoutScheme_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/ContractionNodal.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/ContractionNodal.lean#L382). The attribute's comment: “the singularities of Y are at-worst-nodal”.

> The singularities of the contraction `Y` of a rational bridge, the pushout
> `AlgebraicGeometry.pushoutScheme` of `Stacks.Curves.bridgePushoutSituation` over `k` by
> `AlgebraicGeometry.pushoutToBase`, are at-worst-nodal.

```lean
theorem hasAtWorstNodalSingularities_pushoutScheme_bridge
    (hdim : topologicalKrullDim X = 1)
    (hnodal : HasAtWorstNodalSingularities k X)
    {C : X.IdealSheafData} (hC : IsRationalBridge k X C) :
    letI : (pushoutScheme (bridgePushoutSituation hdim hnodal hC)).Over (Spec (.of k)) :=
      ⟨pushoutToBase (bridgePushoutSituation hdim hnodal hC)⟩
    HasAtWorstNodalSingularities k (pushoutScheme (bridgePushoutSituation hdim hnodal hC))
```

**`Stacks.Curves.isField_globalSections_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Intersection.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Intersection.lean#L76). The attribute's comment: “k' = H⁰(C, 𝒪\_C) is a field”.

> **The ring of global functions on a rational bridge is a field**: the bridge is an integral
> scheme proper over `k`, so its global functions form a field ([Stacks, Tag 0BUG]).

```lean
theorem isField_globalSections_bridge (k : Type u) [Field k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    (_hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (_hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    IsField Γ(C.subscheme, ⊤)
```

**`Stacks.Curves.isNode_of_mem_intersection_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Intersection.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Intersection.lean#L106). The attribute's comment: “the points of C ∩ X' are nodes of X”.

> **Every point of the intersection of a rational bridge with the closure of its complement is
> a node of the ambient curve.**  At least two irreducible components of `X` pass through each
> such point, so [Stacks, Tag 0E38] applies.

```lean
theorem isNode_of_mem_intersection_bridge (k : Type u) [Field k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C)
    (w : intersectionWithComplementaryCurve C) :
    IsNode k X ((intersectionWithComplementaryCurveIdeal C).subschemeι.base w)
```

**`Stacks.Curves.moduleFinite_and_isSeparable_globalSections_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/IntersectionSections.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/IntersectionSections.lean#L415). The attribute's comment: “k'/k is a finite separable extension of fields”.

> **The field of global functions on a rational bridge is a finite separable extension of the
> base field.**  This is the assertion "`k'/k` is a finite separable extension of fields" of
> [Stacks, Tag 0E3M], for `C ⊆ X` a rational bridge of a proper one-dimensional at-worst-nodal
> curve over `k` with only constant global functions and `k' = Γ(C, 𝒪_C)`.
>
> Finiteness is clause (1) of [Stacks, Tag 0BUG]
> (`Stacks.AlgebraicGeometry.ProperSectionsGeom.moduleFinite_globalSections_of_isProper`): the
> bridge is a closed subscheme of `X`, hence proper over `k`.  Separability is the source's appeal
> to [Stacks, Tag 0C4D] at a point `w` of `C ∩ X'`, which is nonempty
> (`Stacks.Curves.nonempty_intersection_bridge`): that point is a node of `X`, so the residue field
> there is separable over `k`
> (`Stacks.Curves.isSeparableExtension_residueField_intersection_bridge`), hence geometrically
> reduced over `k` by Tag 030W; the evaluation of global functions of the bridge at `w` embeds `k'`
> in that residue field, `k'` being a field, so `k'` is geometrically reduced over `k` too and
> therefore separable, which for the finite extension `k'/k` is separability in the sense of
> `Algebra.IsSeparable`.

```lean
theorem moduleFinite_and_isSeparable_globalSections_bridge
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    letI : IsIntegral C.subscheme := hC.isIntegral
    letI : Field Γ(C.subscheme, ⊤) :=
      (isField_of_universallyClosed k (C.subschemeι ≫ (X ↘ Spec (.of k)))).toField
    letI : Algebra k Γ(C.subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫
        (C.subschemeι ≫ (X ↘ Spec (.of k))).appTop).hom.toAlgebra
    Module.Finite k Γ(C.subscheme, ⊤) ∧ Algebra.IsSeparable k Γ(C.subscheme, ⊤)
```

**`Stacks.Curves.isField_and_isSeparable_or_algEquiv_prod_intersectionSections_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/IntersectionSections.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/IntersectionSections.lean#L476). The attribute's comment: “k''/k' is either a degree two separable extension of fields or k'' = k' × k'”.

> **The degree two extension `k''/k'` of [Stacks, Tag 0E3M] is either a separable field
> extension or the square of `k'`.**  Here `C ⊆ X` is a rational bridge of a proper one-dimensional
> at-worst-nodal curve over `k` with only constant global functions, `X'` is the scheme-theoretic
> closure of `X \ C`, and `k' = Γ(C, 𝒪_C)`, `k'' = Γ(C ∩ X', 𝒪)`.
>
> The intersection is geometrically reduced over `k`
> (`Stacks.Curves.geometricallyReduced_intersection_bridge`), so `k''` is a finite etale
> `k`-algebra, and the degree of `k''` over `k'` is two by the defining condition of a rational
> bridge; the dichotomy is then
> `Stacks.Curves.isField_and_isSeparable_or_algEquiv_prod_of_etale_of_finrank_eq_two`.

```lean
theorem isField_and_isSeparable_or_algEquiv_prod_intersectionSections_bridge
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    letI : IsIntegral C.subscheme := hC.isIntegral
    letI : Field Γ(C.subscheme, ⊤) :=
      (isField_of_universallyClosed k (C.subschemeι ≫ (X ↘ Spec (.of k)))).toField
    letI : Algebra Γ(C.subscheme, ⊤) Γ(intersectionWithComplementaryCurve C, ⊤) :=
      (Scheme.IdealSheafData.inclusion
        (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C)).appTop.hom.toAlgebra
    (IsField Γ(intersectionWithComplementaryCurve C, ⊤) ∧
          Module.finrank Γ(C.subscheme, ⊤) Γ(intersectionWithComplementaryCurve C, ⊤) = 2 ∧
          Algebra.IsSeparable Γ(C.subscheme, ⊤) Γ(intersectionWithComplementaryCurve C, ⊤)) ∨
        Nonempty (Γ(intersectionWithComplementaryCurve C, ⊤) ≃ₐ[Γ(C.subscheme, ⊤)]
          (Γ(C.subscheme, ⊤) × Γ(C.subscheme, ⊤)))
```

**`Stacks.Curves.exists_ringEquiv_completedLocalRing_contraction_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/PushoutCompletionShape.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/PushoutCompletionShape.lean#L145). The attribute's comment: “𝒪^∧\_\{Y,y} ≅ \{f ∈ k''[[s]] : f(0) ∈ k'}, and ≅ k'[[s,t]]/(st) when k'' = k' × k'”.

> **The completed local ring of the contraction of a rational bridge at the image of
> `Spec k'`.**  Let `k` be a field, `X` a proper scheme over `k` of dimension one with
> `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and `C ⊆ X` a rational bridge; let `X'` be the
> scheme-theoretic closure of `X \ C`, `k' = Γ(C, 𝒪_C)`, `k'' = Γ(C ∩ X', 𝒪)` and `Y` the pushout
> of `C ∩ X' ⟶ X'` along `C ∩ X' ⟶ Spec k'`.  Let `y ∈ Y` be the image of `Spec k'`, the image of
> every point of that spectrum.  Then
> ```
> 𝒪^∧_{Y, y} ≅ {f ∈ k''⟦s⟧ : f(0) ∈ k'},
> ```
> and `𝒪^∧_{Y, y} ≅ k'⟦s, t⟧/(st)` when `C ∩ X'` has two points, that is when `k'' = k' × k'`.

```lean
theorem exists_ringEquiv_completedLocalRing_contraction_bridge
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    letI : IsIntegral C.subscheme := hC.isIntegral
    letI : Field Γ(C.subscheme, ⊤) :=
      (isField_of_universallyClosed k (C.subschemeι ≫ (X ↘ Spec (.of k)))).toField
    letI : Algebra Γ(C.subscheme, ⊤) Γ(intersectionWithComplementaryCurve C, ⊤) :=
      (Scheme.IdealSheafData.inclusion
        (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C)).appTop.hom.toAlgebra
    ∃ y : pushoutScheme (bridgePushoutSituation hdim hnodal hC),
      (∀ p : (bridgePushoutSituation hdim hnodal hC).Y,
          pushoutInr (bridgePushoutSituation hdim hnodal hC) p = y) ∧
        Nonempty (Scheme.completedLocalRing
            (pushoutScheme (bridgePushoutSituation hdim hnodal hC)) y ≃+*
          ↥(PowerSeries.constantCoeffInBase (Γ(C.subscheme, ⊤) : Type u)
            (Γ(intersectionWithComplementaryCurve C, ⊤) : Type u))) ∧
        (Nonempty (Γ(intersectionWithComplementaryCurve C, ⊤) ≃ₐ[(Γ(C.subscheme, ⊤) : Type u)]
            ((Γ(C.subscheme, ⊤) : Type u) × (Γ(C.subscheme, ⊤) : Type u))) →
          Nonempty (Scheme.completedLocalRing
              (pushoutScheme (bridgePushoutSituation hdim hnodal hC)) y ≃+*
            (MvPowerSeries (Fin 2) (Γ(C.subscheme, ⊤) : Type u) ⧸
              Ideal.span {(MvPowerSeries.X 0 :
                              MvPowerSeries (Fin 2) (Γ(C.subscheme, ⊤) : Type u)) *
                            MvPowerSeries.X 1})))
```

**`Stacks.Curves.exists_pushout_contraction_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/PushoutContraction.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/PushoutContraction.lean#L326). The attribute's comment: “the pushout Y along C ∩ X' ⟶ Spec k' exists and receives the contraction c : X ⟶ Y”.

> **The pushout of a rational bridge exists and carries a contraction of the bridge.**  The
> pushout square
> ```
> C ∩ X' ⟶ X'
>   ↓        ↓ a
> Spec k' ⟶  Y
> ```
> is [Stacks, Tag 0E25] applied to `Stacks.Curves.bridgePushoutSituation`, and the contraction is
> the one produced by `Stacks.Curves.exists_contraction_pushoutScheme_bridge`.

```lean
theorem exists_pushout_contraction_bridge
    (hdim : topologicalKrullDim X = 1)
    (hnodal : HasAtWorstNodalSingularities k X)
    {C : X.IdealSheafData} (hC : IsRationalBridge k X C) :
    ∃ (Y : Scheme.{u}) (c : X ⟶ Y), IsContractionOfRationalBridge hC c
```

**`Stacks.Curves.smoothAt_bridge_and_complementaryCurve_of_mem_intersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/SmoothIntersection.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/SmoothIntersection.lean#L275). The attribute's comment: “the points of C ∩ X' are smooth points of C and of X'”.

> **The points of `C ∩ X'` are smooth points on both `C` and `X'`.** This is the clause of
> [Stacks, Tag 0E3M] which the source draws from [Stacks, Tag 0E38] after observing that the
> points of the intersection are nodes of `X`: a node has two branches, and here they are the
> bridge and the closure of the complement, each smooth at the point.

```lean
theorem smoothAt_bridge_and_complementaryCurve_of_mem_intersection
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C)
    (w : intersectionWithComplementaryCurve C) :
    InfinitesimalLifting.SmoothAt (C.subschemeι ≫ (X ↘ Spec (.of k)))
        ((Scheme.IdealSheafData.inclusion
          (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C)).base w) ∧
      InfinitesimalLifting.SmoothAt (complementaryCurveι C ≫ (X ↘ Spec (.of k)))
        ((Scheme.IdealSheafData.inclusion
          (le_sup_right : complementaryCurveIdeal C ≤
            intersectionWithComplementaryCurveIdeal C)).base w)
```

**`Stacks.Curves.isIso_structureSheafToPushforward_and_isZero_rightDerived_one_contraction_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/StructurePushforward.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/StructurePushforward.lean#L249). The attribute's comment: “c\_*𝒪\_X = 𝒪\_Y and R¹c\_*𝒪\_X = 0”.

> **The direct images of `𝒪_X` along a contraction of a rational bridge**: the canonical map
> `𝒪_Y ⟶ c_* 𝒪_X` is an isomorphism and `R ¹ c_* 𝒪_X = 0`. This is the clause of
> [Stacks, Tag 0E3M] that reads "we claim that `c_* 𝒪_X = 𝒪_Y` and `R ¹ c_* 𝒪_X = 0`".

```lean
theorem isIso_structureSheafToPushforward_and_isZero_rightDerived_one_contraction_bridge
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C)
    {Y : Scheme.{u}} (c : X ⟶ Y) (hc : IsContractionOfRationalBridge hC c) :
    IsIso (structureSheafToPushforward c) ∧
      IsZero (((Scheme.Modules.pushforward c).rightDerived 1).obj (structureSheafModule X))
```

## Tag 0E64, a lemma

[Tag 0E64](https://stacks.math.columbia.edu/tag/0E64) in the Stacks Project.

**`AlgebraicGeometry.invertibleCurveDegree_pullback_dualizingSheafOverField_eq_zero_of_isRationalBridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingSheafDegree.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingSheafDegree.lean#L39).

> Let `X` be a proper scheme of dimension one over a field `k` with `H⁰(X, 𝒪_X) = k` and
> at-worst-nodal singularities, and let `C ⊆ X` be a rational bridge. Then `deg(ω_X|_C) = 0`, where
> `ω_X` is invertible by `isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities`.

```lean
theorem invertibleCurveDegree_pullback_dualizingSheafOverField_eq_zero_of_isRationalBridge
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI hω := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim
      hnodal
    letI := Stacks.AlgebraicGeometry.Tag09NY.isInvertible_modulePullback C.subschemeι
      (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) hω
    invertibleCurveDegree k (C.subschemeι ≫ (X ↘ Spec (.of k)))
        (Stacks.Curves.topologicalKrullDim_subscheme_eq_one_of_isRationalBridge k X hdim hC).le
        ((Scheme.Modules.pullback C.subschemeι).obj
          (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)))) = 0
```

## Tag 0E65, a lemma

[Tag 0E65](https://stacks.math.columbia.edu/tag/0E65) in the Stacks Project.

**`AlgebraicGeometry.exists_finset_isRationalBridge_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/BaseChangeUnion.lean, line 841](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/BaseChangeUnion.lean#L841). The attribute's comment: “Corrected statement. Stacks asserts that C\_K is a finite DISJOINT union of rational bridges; that is false as printed: for the rational bridge C = V(T₀² + T₁²) of X = V(T₂(T₀² + T₁²)) ⊂ P²\_ℝ, the base change C\_ℂ is two lines meeting in a point, connected and reducible (`Stacks.Curves.DegenerateConic.not_exists_iso_sigma_isRationalBridge_degenerateConic`). Proved here at the tag's own hypotheses, for every field extension K/k, with disjoint union replaced by union: C\_K is the scheme-theoretic union of finitely many rational bridges of X\_K, the reduced irreducible components of X\_K over C.”.

> **[Stacks, Tag 0E65] in the union form.** Let `X` be a proper one-dimensional scheme over a
> field `k` with `H⁰(X, 𝒪_X) = k` and at worst nodal singularities, and let `C ⊆ X` be a rational
> bridge. For an arbitrary field extension `K/k` — no normality, separability, algebraicity or
> finiteness is assumed — the inverse image of `C` in the base change `X_K` is the
> scheme-theoretic *union* of a finite set of rational bridges of `X_K`, namely of the reduced
> structures on the irreducible components of `X_K` lying over `C`.
>
> The tag asserts a *disjoint* union, which is false as printed: over `k = ℝ` the component
> `C = V(T₀² + T₁²)` of the plane cubic `X = V(T₂(T₀² + T₁²)) ⊂ P²_ℝ` is a rational bridge, while
> `C_ℂ = V(T₀ + iT₁) ∪ V(T₀ - iT₁)` is connected and reducible, so it is not a disjoint union of
> integral schemes;
> `Stacks.Curves.DegenerateConic.not_exists_iso_sigma_isRationalBridge_degenerateConic` refutes
> the disjoint conclusion for this conic. This statement is the corrected tag: the same hypotheses,
> with "finite disjoint union" replaced by "finite union". The disjoint form holds when the bridge
> is moreover geometrically integral over its field of global functions `k' = Γ(C, 𝒪_C)`, and is
> `AlgebraicGeometry.exists_iso_sigma_isRationalBridge_baseChange`.
>
> The dichotomy behind the repair is this: a rational bridge is either geometrically integral over
> `k'`, and then `C_K` really is a disjoint union of `[k' ⊗_k K : K]`-many bridges, or it acquires
> two geometric components, meeting in one point and carrying one point of `C ∩ X'` each. In the
> second case the two components of `C_K` meet, so no disjoint decomposition exists, while the
> union form is still correct and is what this statement proves.
>
> What makes each component come out with complementary degree exactly two is a symmetry: over a
> separably closed extension the components of `C_Ω` all have the same image in `X` and are
> therefore conjugate, so their complementary degrees agree
> (`Stacks.Curves.finrank_sup_complementaryCurveIdeal_eq_of_image_eq`). The counting identity
> `Stacks.Curves.sum_finrank_sup_complementaryCurveIdeal_eq` alone does not suffice: it only says
> that the complementary degrees sum to twice the number of components, which a chain of three
> components with degrees `(1, 4, 1)` satisfies just as well.

```lean
theorem exists_finset_isRationalBridge_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalBridge k X C) :
    letI : (pullback (C := Scheme.{u}) (X ↘ Spec (.of k))
        (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).Over (Spec (.of K)) :=
      ⟨pullback.snd _ _⟩
    letI : IsProper ((pullback (C := Scheme.{u}) (X ↘ Spec (.of k))
        (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}) ↘ Spec (.of K)) :=
      inferInstanceAs (IsProper (pullback.snd (X ↘ Spec (.of k))
        (Spec.map (CommRingCat.ofHom (algebraMap k K)))))
    ∃ Λ : Finset (Set (pullback (C := Scheme.{u}) (X ↘ Spec (.of k))
        (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})),
      (∀ Z ∈ Λ, IsRationalBridge K (pullback (C := Scheme.{u}) (X ↘ Spec (.of k))
          (Spec.map (CommRingCat.ofHom (algebraMap k K))))
          (Scheme.IdealSheafData.vanishingIdeal
            (TopologicalSpace.Closeds.closure Z))) ∧
        C.comap (pullback.fst (X ↘ Spec (.of k))
            (Spec.map (CommRingCat.ofHom (algebraMap k K))))
          = Λ.inf fun Z => Scheme.IdealSheafData.vanishingIdeal
              (TopologicalSpace.Closeds.closure Z)
```

## Tag 0E3N, a lemma

[Tag 0E3N](https://stacks.math.columbia.edu/tag/0E3N) in the Stacks Project.

**`Stacks.Curves.nonempty_pullback_dualizingSheafOverField_iso_contraction_bridge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingSheafPullback.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingSheafPullback.lean#L145).

> Let `k` be a field, let `X` be a proper scheme over `k` of dimension one with
> `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, let `C ⊆ X` be a rational bridge and let
> `c : X ⟶ Y` be the contraction of `C`, with `Y` over `k` through `g`, compatibly with `c`. Then
> `c^* ω_Y ≅ ω_X`.

```lean
theorem nonempty_pullback_dualizingSheafOverField_iso_contraction_bridge
    (hdim : topologicalKrullDim X = 1) (hnodal : HasAtWorstNodalSingularities k X)
    {C : X.IdealSheafData} {hC : IsRationalBridge k X C} {Y : Scheme.{u}} {c : X ⟶ Y}
    (hc : IsContractionOfRationalBridge hC c) (g : Y ⟶ Spec (.of k))
    (hcg : c ≫ g = X ↘ Spec (.of k)) :
    haveI := isProper_structureMorphism_of_isContractionOfRationalBridge hdim hnodal hc hcg
    Nonempty ((Scheme.Modules.pullback c).obj (Stacks.Duality.dualizingSheafOverField g) ≅
      Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)))
```

## Tag 0E3P, a lemma

[Tag 0E3P](https://stacks.math.columbia.edu/tag/0E3P) in the Stacks Project.

**`AlgebraicGeometry.isAmple_dualizingSheafOverField_of_hasAtWorstNodalSingularities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingAmple.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/DualizingAmple.lean#L41).

> Let `k` be a field and let `X` be a proper scheme over `k` of dimension one with
> `H⁰(X, 𝒪_X) = k`. If the singularities of `X` are at worst nodal, `X` has no rational tail and no
> rational bridge, and the genus of `X` is at least two, then `ω_X` is an invertible `𝒪_X`-module
> and it is ample.

```lean
theorem isAmple_dualizingSheafOverField_of_hasAtWorstNodalSingularities
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hbridge : ∀ C : X.IdealSheafData, ¬ IsRationalBridge k X C)
    (hg : 2 ≤ genus (X ↘ Spec (.of k))) :
    ∃ _ : SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property
        (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))),
      Scheme.Modules.IsAmple X (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)))
```

## Tag 0E3Q, a lemma

[Tag 0E3Q](https://stacks.math.columbia.edu/tag/0E3Q) in the Stacks Project.

**`AlgebraicGeometry.IsIteratedContractionOfRationalBridges.isStableContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Terminal.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Terminal.lean#L270). The attribute's comment: “ω\_\{X'} is ample”.

> **Stacks Project, Tag 0E3Q: `ω_{X'}` is ample.** Let `X` be a proper scheme over a field `k`
> of dimension one with `H⁰(X, 𝒪_X) = k`, genus `g ≥ 2`, at-worst-nodal singularities and no
> rational tails, and let `c : X ⟶ X'` be the composite of a sequence of contractions of rational
> bridges (Tag 0E3M) such that `X'` has no rational bridge. Then `ω_{X'}` is invertible and ample;
> more precisely `c` satisfies the conditions of Tag 0E7Q: `X'` is proper of dimension one with
> at-worst-nodal singularities, `𝒪_{X'} = c_* 𝒪_X`, `R¹ c_* 𝒪_X = 0`, and `ω_{X'}` is ample.
>
> The target has no rational tails
> (`Stacks.Curves.forall_not_isRationalTail_of_pullback_dualizingSheafOverField_iso`, from
> `c^* ω_{X'} ≅ ω_X`), so Tag 0E3P applies to it.

```lean
theorem isStableContraction
    (htail : letI : X.Over (Spec (.of k)) := ⟨fX⟩
      ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hg : 2 ≤ genus fX)
    (hterminal : ∀ C : Y.IdealSheafData,
      letI : Y.Over (Spec (.of k)) := ⟨fY⟩
      ∀ _ : IsProper (Y ↘ Spec (.of k)), ¬ IsRationalBridge k Y C) :
    Stacks.Curves.StableModel.IsStableContraction fX fY c
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalBridges.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Terminal.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/Terminal.lean#L309). The attribute's comment: “the morphism X ⟶ X' is independent of choices”.

> **Stacks Project, Tag 0E3Q: the morphism `X ⟶ X'` is independent of choices.** Under the
> hypotheses of `AlgebraicGeometry.IsIteratedContractionOfRationalBridges.isStableContraction`, if
> `c₂ : X ⟶ X'₂` is the composite of a second sequence of contractions of rational bridges such that
> `X'₂` has no rational bridge, then there is a unique isomorphism `e : X' ≅ X'₂` with
> `c ≫ e.hom = c₂`. Both composites are stable contractions pulling the dualizing sheaves back to
> `ω_X` (Tag 0E3N along each chain), so
> `Stacks.Curves.StableModel.existsUnique_iso_of_pullback_dualizingSheafOverField_iso` applies.

```lean
theorem existsUnique_iso
    (htail : letI : X.Over (Spec (.of k)) := ⟨fX⟩
      ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hg : 2 ≤ genus fX)
    (hterminal : ∀ C : Y.IdealSheafData,
      letI : Y.Over (Spec (.of k)) := ⟨fY⟩
      ∀ _ : IsProper (Y ↘ Spec (.of k)), ¬ IsRationalBridge k Y C)
    {Y₂ : Scheme.{u}} {fY₂ : Y₂ ⟶ Spec (.of k)} {c₂ : X ⟶ Y₂}
    (hseq₂ : IsIteratedContractionOfRationalBridges k fX fY₂ c₂)
    (hterminal₂ : ∀ C : Y₂.IdealSheafData,
      letI : Y₂.Over (Spec (.of k)) := ⟨fY₂⟩
      ∀ _ : IsProper (Y₂ ↘ Spec (.of k)), ¬ IsRationalBridge k Y₂ C) :
    ∃! e : Y ≅ Y₂, c ≫ e.hom = c₂
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalBridges.existsUnique_iso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/TerminalBaseChange.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalBridges/TerminalBaseChange.lean#L239). The attribute's comment: “formation of the morphism X ⟶ X' commutes with base field extensions”.

> Formation of the contraction `c : X ⟶ Y` commutes with base field extensions: under the
> hypotheses of `AlgebraicGeometry.IsIteratedContractionOfRationalBridges.isStableContraction`, let
> `K/k` be a field extension, `X_K = X ×_k K` and `Y_K = Y ×_k K` over `K`, and `c_K : X_K ⟶ Y_K` the
> base change of `c`. For every sequence `d : X_K ⟶ Z` of contractions of rational bridges of `X_K`
> over `K` such that `Z` has no rational bridge, there is a unique isomorphism `e : Y_K ≅ Z` with
> `c_K ≫ e.hom = d`: the morphism the construction produces for `X_K` is the base change of the one
> for `X`.

```lean
theorem existsUnique_iso_baseChange
    (htail : letI : X.Over (Spec (.of k)) := ⟨fX⟩
      ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hg : 2 ≤ genus fX)
    (hterminal : ∀ C : Y.IdealSheafData,
      letI : Y.Over (Spec (.of k)) := ⟨fY⟩
      ∀ _ : IsProper (Y ↘ Spec (.of k)), ¬ IsRationalBridge k Y C)
    (K : Type u) [Field K] [Algebra k K] {Z : Scheme.{u}} {fZ : Z ⟶ Spec (.of K)}
    {d : pullback fX (Spec.map (CommRingCat.ofHom (algebraMap k K))) ⟶ Z}
    (hd : IsIteratedContractionOfRationalBridges K
      (pullback.snd fX (Spec.map (CommRingCat.ofHom (algebraMap k K)))) fZ d)
    (hdterminal : ∀ C : Z.IdealSheafData,
      letI : Z.Over (Spec (.of K)) := ⟨fZ⟩
      ∀ _ : IsProper (Z ↘ Spec (.of K)), ¬ IsRationalBridge K Z C) :
    ∃! e : pullback fY (Spec.map (CommRingCat.ofHom (algebraMap k K))) ≅ Z,
      pullback.map fX (Spec.map (CommRingCat.ofHom (algebraMap k K))) fY
          (Spec.map (CommRingCat.ofHom (algebraMap k K))) c (𝟙 _) (𝟙 _)
          (by rw [Category.comp_id, hseq.comp_structureMorphism]) (by simp) ≫ e.hom = d
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.24, Tag 0E7M](https://stacks.math.columbia.edu/tag/0E7M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
