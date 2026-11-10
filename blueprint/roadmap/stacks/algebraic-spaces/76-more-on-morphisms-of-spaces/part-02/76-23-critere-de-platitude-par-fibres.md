---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_chartPoint_isFibreFlatOnChartSquares_iff_isFibreFlatOverAtGeometricPoint, AlgebraicGeometry.Space.isFibreFlatOverAtGeometricPoint_congr_of_image_eq, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint_of_image_eq, AlgebraicGeometry.Space.isFlatOverAtPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_exists_chartPoint, AlgebraicGeometry.Space.isFlatOnFibreAtFieldValuedPoint_iff_isFibreFlatOverAtGeometricPoint, AlgebraicGeometry.Space.exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint
statement: formalized
proof: formalized
---

# 76.23 Critère de platitude par fibres

Section 76.23 of the Stacks Project, [Tag 05WX](https://stacks.math.columbia.edu/tag/05WX). 8 tags here are carried by 41 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05WY, a lemma

[Tag 05WY](https://stacks.math.columbia.edu/tag/05WY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_chartPoint_isFibreFlatOnChartSquares_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessChartPoint.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessChartPoint.lean#L211). The attribute's comment: “(1) iff (3), with condition (3) carrying a point u of U above x as the source states it rather than a lift of the geometric point; condition (3) read on the local rings of the charts”.

> **Stacks 05WY: condition (3) if and only if condition (1), with condition (3) carrying a
> point of `U` above `x`.**  In Situation 05WX the following are equivalent, for a geometric point
> `x̄` of `X`:
>
> 1. writing `ȳ = f ∘ x̄` and `z̄ = h ∘ ȳ`, the fibre `F_x̄ / 𝔪_z̄ F_x̄` is flat over
>    `𝒪_{Y, ȳ} / 𝔪_z̄ 𝒪_{Y, ȳ}`;
> 3. there is a commuting diagram of schemes `U ⟶ V ⟶ W` étale over `f` and `h`, **and a point
>    `u` of `U` mapping to the image of `x̄` in `|X|`**, at which the fibre of `F|_U` over the
>    fibre of `V` is flat.
>
> This is condition (3) as the source states it: the source picks a diagram *and a point
> `u ∈ U` mapping to `x`*, with no lift of the geometric point chosen.
> `AlgebraicGeometry.Space.exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint` is the
> same equivalence with the point presented as a lift of `x̄` to the chart.
>
> Condition (3) is read on the local rings of the charts rather than on the scheme-theoretic
> fibres `U_w` and `V_w`, through the canonical identifications
> `𝒪_{V_w, v} = 𝒪_{V, v}/𝔪_w 𝒪_{V, v}` and `(F_w)_u = (F|_U)_u/𝔪_w (F|_U)_u` which the source
> records at the start of its proof.

```lean
theorem exists_chartPoint_isFibreFlatOnChartSquares_iff_isFibreFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (xbar : GeometricPoint B S hS X.1) :
    (∃ (U : SmallEtale B S hS X.1) (Vc : SmallEtale B S hS Y.1) (Wc : SmallEtale B S hS Z.1)
        (g₁ : U.obj.left ⟶ Vc.obj.left)
        (_hcomm₁ : U.obj.hom ≫ f.hom = yoneda.map g₁ ≫ Vc.obj.hom)
        (g₂ : Vc.obj.left ⟶ Wc.obj.left)
        (_hcomm₂ : Vc.obj.hom ≫ h.hom = yoneda.map g₂ ≫ Wc.obj.hom)
        (u : chartScheme U),
      ChartPoint B S hS U.obj.left U.obj.hom u xbar.image ∧
        IsFibreFlatOnChartSquares B S hS X.1 X.2 F U Vc Wc g₁ g₂ u) ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar
```

**`AlgebraicGeometry.Space.isFibreFlatOverAtGeometricPoint_congr_of_image_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessChartPoint.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessChartPoint.lean#L243). The attribute's comment: “well-posedness of 'pick a geometric point xbar of X lying over x' in condition (1): the condition at a geometric point depends only on its image in |X|”.

> **The condition of Stacks 05WY at a geometric point depends only on the point of `|X|` it
> lies over.**  For two geometric points `x̄`, `x̄'` of `X` with the same image in `|X|`,
> condition (1) of Stacks 05WY holds at `x̄` exactly when it holds at `x̄'`.

```lean
theorem isFibreFlatOverAtGeometricPoint_congr_of_image_eq {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (h : Y ⟶ Z) (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (xbar xbar' : GeometricPoint B S hS X.1) (himage : xbar.image = xbar'.image) :
    IsFibreFlatOverAtGeometricPoint B S hS f h F xbar ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar'
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean#L477). The attribute's comment: “(1) iff (2): flatness of the pullback of F to the field fibre X_z over Y_z at a geometric point of X_z, read at a geometric point as in Stacks 05VU, iff condition (1) at the image of that point in X”.

> **Stacks 05WY: condition (2) if and only if condition (1).**  In Situation 05WX let `z` be a
> field-valued point of `Z` with field of definition `K`, let `X_z = Spec(K) ×_{z, Z} X` and
> `Y_z = Spec(K) ×_{z, Z} Y` be the field fibres and let `F_z` be the pullback of `F` to `X_z`.
> Then for a geometric point `x̄_z` of `X_z`, the module `F_z` is flat over `Y_z` at `x̄_z` exactly
> when condition (1) of Stacks 05WY holds at the image `x̄` of `x̄_z` in `X`.
>
> This is condition (2) of the source.  Relative flatness at a point is read at a geometric point,
> as condition (2) of Stacks 05VU
> (`AlgebraicGeometry.Space.isFlatOverAt_exists_chartDiagram_iff_isFlatOverAtGeometricPoint`
> identifies that with the chartwise condition of Definition 05VV which the source cites), and the
> statement is at *every* geometric point of `X_z` rather than only at one above the `K`-rational
> point `x` of `X_z` that the source's representative `x : Spec(K) ⟶ X` defines — which is the
> source's condition (2) together with its independence of the choice of representative, since
> condition (1) at the image of `x̄_z` depends only on that image
> (`AlgebraicGeometry.Space.isFibreFlatOverAtGeometricPoint_congr_of_image_eq`).

```lean
theorem isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) (z : FieldValuedPoint B S hS Z.1)
    (xz : GeometricPoint B S hS (fieldFibreSpace (f ≫ h) z).1) :
    IsFlatOverAtGeometricPoint B S hS
        (ObjectProperty.homMk (fieldFibreSourceMap B S hS f.hom h.hom z) :
          fieldFibreSpace (f ≫ h) z ⟶ fieldFibreSpace h z)
        ((modulePullback B S hS (ObjectProperty.homMk
            (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
              fieldFibreSpace (f ≫ h) z ⟶ X)).obj F) xz ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F
        (geometricPointMap (ObjectProperty.homMk
          (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
            fieldFibreSpace (f ≫ h) z ⟶ X).hom xz)
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint_of_image_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean#L505). The attribute's comment: “(1) iff (2) with condition (1) at an arbitrary chosen geometric point of X above the point, as the source states condition (1)”.

> **Stacks 05WY, condition (2) against condition (1) at a chosen geometric point of `X`.**
> Condition (2) at a geometric point `x̄_z` of the field fibre `X_z` holds exactly when
> condition (1) holds at *any* geometric point `x̄` of `X` with the same image in `|X|` as the image
> of `x̄_z`.
>
> This is the form the source's condition (1) takes: "pick a geometric point `x̄` of `X` lying
> over `x`".

```lean
theorem isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint_of_image_eq
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (z : FieldValuedPoint B S hS Z.1)
    (xz : GeometricPoint B S hS (fieldFibreSpace (f ≫ h) z).1)
    (xbar : GeometricPoint B S hS X.1)
    (himage : (geometricPointMap (ObjectProperty.homMk
        (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
          fieldFibreSpace (f ≫ h) z ⟶ X).hom xz).image = xbar.image) :
    IsFlatOverAtGeometricPoint B S hS
        (ObjectProperty.homMk (fieldFibreSourceMap B S hS f.hom h.hom z) :
          fieldFibreSpace (f ≫ h) z ⟶ fieldFibreSpace h z)
        ((modulePullback B S hS (ObjectProperty.homMk
            (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
              fieldFibreSpace (f ≫ h) z ⟶ X)).obj F) xz ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar
```

**`AlgebraicGeometry.Space.isFlatOverAtPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean#L534). The attribute's comment: “(1) iff (2) with condition (2) in the chartwise form of Definition 05VV, which is the predicate the source cites”.

> **Stacks 05WY: condition (2) in the chartwise form of Definition 05VV, if and only if
> condition (1).**  The pullback `F_z` of `F` to the field fibre `X_z` is flat at the image in
> `|X_z|` of a geometric point `x̄_z`, over `Y_z`, in the sense of Definition 05VV, exactly when
> condition (1) of Stacks 05WY holds at the image of `x̄_z` in `X`.
>
> This is condition (2) with flatness at a point spelled by
> `AlgebraicGeometry.Space.IsFlatOverAtPoint`, the predicate of Definition 05VV that the source
> cites, rather than at a geometric point.

```lean
theorem isFlatOverAtPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (z : FieldValuedPoint B S hS Z.1)
    (xz : GeometricPoint B S hS (fieldFibreSpace (f ≫ h) z).1) :
    IsFlatOverAtPoint B S hS (fieldFibreSpace (f ≫ h) z).2
        (ObjectProperty.homMk (fieldFibreSourceMap B S hS f.hom h.hom z) :
          fieldFibreSpace (f ≫ h) z ⟶ fieldFibreSpace h z).hom
        ((modulePullback B S hS (ObjectProperty.homMk
            (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
              fieldFibreSpace (f ≫ h) z ⟶ X)).obj F) xz.image ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F
        (geometricPointMap (ObjectProperty.homMk
          (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
            fieldFibreSpace (f ≫ h) z ⟶ X).hom xz)
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_exists_chartPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean#L564). The attribute's comment: “(2) iff (3), composed through condition (1); condition (3) carrying a point u of U above x as the source states it, read on the local rings of the charts”.

> **Stacks 05WY: condition (2) if and only if condition (3).**  In Situation 05WX, flatness of
> the pullback `F_z` over `Y_z` at a geometric point `x̄_z` of the field fibre `X_z` holds exactly
> when there is a commuting diagram of schemes `U ⟶ V ⟶ W` étale over `f` and `h` and a point `u`
> of `U` above the image of `x̄_z` in `|X|`, at which the fibre of `F|_U` over the fibre of `V` is
> flat.

```lean
theorem isFlatOverAtGeometricPoint_fieldFibreSpace_iff_exists_chartPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (z : FieldValuedPoint B S hS Z.1)
    (xz : GeometricPoint B S hS (fieldFibreSpace (f ≫ h) z).1) :
    IsFlatOverAtGeometricPoint B S hS
        (ObjectProperty.homMk (fieldFibreSourceMap B S hS f.hom h.hom z) :
          fieldFibreSpace (f ≫ h) z ⟶ fieldFibreSpace h z)
        ((modulePullback B S hS (ObjectProperty.homMk
            (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
              fieldFibreSpace (f ≫ h) z ⟶ X)).obj F) xz ↔
      ∃ (U : SmallEtale B S hS X.1) (Vc : SmallEtale B S hS Y.1) (Wc : SmallEtale B S hS Z.1)
          (g₁ : U.obj.left ⟶ Vc.obj.left)
          (_hcomm₁ : U.obj.hom ≫ f.hom = yoneda.map g₁ ≫ Vc.obj.hom)
          (g₂ : Vc.obj.left ⟶ Wc.obj.left)
          (_hcomm₂ : Vc.obj.hom ≫ h.hom = yoneda.map g₂ ≫ Wc.obj.hom)
          (u : chartScheme U),
        ChartPoint B S hS U.obj.left U.obj.hom u
            (geometricPointMap (ObjectProperty.homMk
              (pullback.fst (f.hom ≫ h.hom) (yonedaEquiv.symm z.value)) :
                fieldFibreSpace (f ≫ h) z ⟶ X).hom xz).image ∧
          IsFibreFlatOnChartSquares B S hS X.1 X.2 F U Vc Wc g₁ g₂ u
```

**`AlgebraicGeometry.Space.isFlatOnFibreAtFieldValuedPoint_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldValuedPoint.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldValuedPoint.lean#L703). The attribute's comment: “(1) iff (2), for every geometric point over x and every field-valued representative of x”.

> **Stacks 05WY, (1) `⟺` (2).** Let `f : X ⟶ Y` and `h : Y ⟶ Z` be morphisms of algebraic
> spaces over `S`, let `F` be a quasi-coherent `𝒪_X`-module and let `x` be a point of `|X|`.  For
> every geometric point `x̄` of `X` lying over `x` and every field-valued point
> `x : Spec(K) ⟶ X` in the class of `x`, with `z = h ∘ f ∘ x`, the following are equivalent:
>
> 1. the module `F_{x̄}/𝔪_{z̄} F_{x̄}` is flat over `𝒪_{Y, ȳ}/𝔪_{z̄} 𝒪_{Y, ȳ}`, where `ȳ = f ∘ x̄`
>    and `z̄ = h ∘ ȳ`;
> 2. the pullback `F_z` of `F` to `X_z = Spec(K) ×_{z, Z} X` is flat over
>    `Y_z = Spec(K) ×_{z, Z} Y` at the `K`-rational point of `X_z` determined by `x`, in the sense
>    of Stacks 05VV.
>
> In particular neither condition depends on the choices made.

```lean
theorem isFlatOnFibreAtFieldValuedPoint_iff_isFibreFlatOverAtGeometricPoint
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1)
    (xbar : GeometricPoint B S hS X.1) (hxbar : xbar.LiesOver x)
    (hp : p.class B S hS X.1 = x) :
    IsFlatOnFibreAtFieldValuedPoint B S hS f h p F ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar
```

**`AlgebraicGeometry.Space.exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessGeometricPoint.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessGeometricPoint.lean#L638). The attribute's comment: “(1) iff (3), condition (3) read on the local rings of the charts”.

> **Stacks 05WY: condition (3) if and only if condition (1).** In Situation 05WX — a scheme
> `S`, algebraic spaces `X`, `Y`, `Z` over `S` with `f : X ⟶ Y` and `h : Y ⟶ Z`, a quasi-coherent
> `𝒪_X`-module `F` and a geometric point `x̄` of `X` — the following are equivalent:
>
> 1. writing `ȳ = f ∘ x̄` and `z̄ = h ∘ ȳ`, the fibre `F_x̄ / 𝔪_z̄ F_x̄` is flat over
>    `𝒪_{Y, ȳ} / 𝔪_z̄ 𝒪_{Y, ȳ}`;
> 3. there is a commuting diagram of schemes `U ⟶ V ⟶ W` étale over `f` and `h`, and a point `u`
>    of `U` above the image of `x̄`, at which the fibre of `F|_U` over the fibre of `V` is flat.
>
> Condition (3) of the source reads the second condition on the scheme-theoretic fibres `U_w` and
> `V_w`; here it is read on their local rings, through the canonical identifications
> `𝒪_{V_w, v} = 𝒪_{V, v}/𝔪_w 𝒪_{V, v}` and `(F_w)_u = (F|_U)_u/𝔪_w (F|_U)_u` which the source
> records at the start of its proof. The point `u` above `x̄` is presented as a lift of `x̄` to the
> chart, which is the same data by Stacks 05VN
> (`AlgebraicGeometry.Space.exists_chartLift_of_chartPoint` and
> `AlgebraicGeometry.Space.chartPoint_isChartPoint`).
>
> Condition (2) of the source, flatness of the pullback of `F` to the fibre `X_z` over `Y_z` in
> the sense of Stacks 05VV, is not among the conditions compared here; it is
> `Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_isFibreFlatOverAtGeometricPoint`
> of `StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessFieldFibre.lean`, and
> `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_fieldFibreSpace_iff_exists_chartPoint`
> composes it with this lemma.
>
> Such a diagram always exists (`AlgebraicGeometry.Space.exists_chartSquares`), which is what the
> second direction uses: take `W ⟶ Z` surjective étale, then `V ⟶ W ×_Z Y` and `U ⟶ V ×_Y X`
> surjective étale, and a point of `U` above the image of `x̄`.  Since no diagram is privileged,
> condition (3) in fact holds at *every* diagram as soon as it holds at one, which is
> `AlgebraicGeometry.Space.forall_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint`.

```lean
theorem exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (xbar : GeometricPoint B S hS X.1) :
    (∃ (N : SmallEtaleNeighborhood xbar) (Vc : SmallEtale B S hS Y.1)
        (g₁ : N.chart.obj.left ⟶ Vc.obj.left)
        (hcomm₁ : N.chart.obj.hom ≫ f.hom = yoneda.map g₁ ≫ Vc.obj.hom)
        (Wc : SmallEtale B S hS Z.1) (g₂ : Vc.obj.left ⟶ Wc.obj.left)
        (hcomm₂ : Vc.obj.hom ≫ h.hom = yoneda.map g₂ ≫ Wc.obj.hom),
      Module.FlatQuotSMul
        (((BigFppfOver.toScheme B S hS).map g₁).stalkMap (chartPoint B S hS X.1 N)).hom
        ((maximalIdeal ↥(chartLocalRing B S hS Z.1 (targetNeighborhood B S hS
              (targetNeighborhood B S hS N Vc g₁ hcomm₁) Wc g₂ hcomm₂))).map
          (((BigFppfOver.toScheme B S hS).map g₂).stalkMap
            (chartPoint B S hS Y.1 (targetNeighborhood B S hS N Vc g₁ hcomm₁))).hom)
        (((maximalIdeal ↥(chartLocalRing B S hS Z.1 (targetNeighborhood B S hS
                (targetNeighborhood B S hS N Vc g₁ hcomm₁) Wc g₂ hcomm₂))).map
            (((BigFppfOver.toScheme B S hS).map g₂).stalkMap
              (chartPoint B S hS Y.1 (targetNeighborhood B S hS N Vc g₁ hcomm₁))).hom).map
          (((BigFppfOver.toScheme B S hS).map g₁).stalkMap (chartPoint B S hS X.1 N)).hom)
        rfl ↥(chartZariskiModuleStalk B S hS X.1 X.2 N F)) ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar
```

**`AlgebraicGeometry.Space.forall_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessGeometricPoint.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessGeometricPoint.lean#L682). The attribute's comment: “(1) iff (3) at an arbitrary chosen diagram: the every-diagram reading of condition (3), read on the local rings of the charts”.

> **Stacks 05WY: condition (3) at an arbitrary chosen diagram if and only if condition (1).**
> In Situation 05WX the chart condition (3) of Stacks 05WY holds on *every* pointed pair of
> composable commuting squares of étale scheme charts `U ⟶ V ⟶ W` of `f` and `h` exactly when
> condition (1) holds at `x̄`.
>
> This is the "any choice works" reading of condition (3) the source intends: the source says
> "choose a commutative diagram", so the condition must not depend on the choice.  Together with
> `AlgebraicGeometry.Space.exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint` it says
> that the some-diagram and every-diagram readings of condition (3) agree, a diagram existing by
> `AlgebraicGeometry.Space.exists_chartSquares`.

```lean
theorem forall_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (xbar : GeometricPoint B S hS X.1) :
    (∀ (N : SmallEtaleNeighborhood xbar) (Vc : SmallEtale B S hS Y.1)
        (g₁ : N.chart.obj.left ⟶ Vc.obj.left)
        (hcomm₁ : N.chart.obj.hom ≫ f.hom = yoneda.map g₁ ≫ Vc.obj.hom)
        (Wc : SmallEtale B S hS Z.1) (g₂ : Vc.obj.left ⟶ Wc.obj.left)
        (hcomm₂ : Vc.obj.hom ≫ h.hom = yoneda.map g₂ ≫ Wc.obj.hom),
      Module.FlatQuotSMul
        (((BigFppfOver.toScheme B S hS).map g₁).stalkMap (chartPoint B S hS X.1 N)).hom
        ((maximalIdeal ↥(chartLocalRing B S hS Z.1 (targetNeighborhood B S hS
              (targetNeighborhood B S hS N Vc g₁ hcomm₁) Wc g₂ hcomm₂))).map
          (((BigFppfOver.toScheme B S hS).map g₂).stalkMap
            (chartPoint B S hS Y.1 (targetNeighborhood B S hS N Vc g₁ hcomm₁))).hom)
        (((maximalIdeal ↥(chartLocalRing B S hS Z.1 (targetNeighborhood B S hS
                (targetNeighborhood B S hS N Vc g₁ hcomm₁) Wc g₂ hcomm₂))).map
            (((BigFppfOver.toScheme B S hS).map g₂).stalkMap
              (chartPoint B S hS Y.1 (targetNeighborhood B S hS N Vc g₁ hcomm₁))).hom).map
          (((BigFppfOver.toScheme B S hS).map g₁).stalkMap (chartPoint B S hS X.1 N)).hom)
        rfl ↥(chartZariskiModuleStalk B S hS X.1 X.2 N F)) ↔
      IsFibreFlatOverAtGeometricPoint B S hS f h F xbar
```

## Tag 05WZ, a definition

[Tag 05WZ](https://stacks.math.columbia.edu/tag/05WZ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFlatOnFibreAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean#L121). The attribute's comment: “part (1), defined through the Lemma 05WY notion IsFibreFlatOverAtGeometricPoint (its condition (1)), asked at every geometric point over x; equal to that condition at any one such point by isFlatOnFibreAt_iff_...”.

> **Stacks 05WZ, part (1).** The restriction of an `𝒪_X`-module `F` to its fibre over the
> image `z` of a point `x` of `|X|` is *flat at `x` over the fibre of `Y` over `z`* when the
> condition of Stacks 05WY holds at every geometric point of `X` above `x`.
>
> The source defines this by "the equivalent conditions of Lemma 05WY are satisfied"; the
> condition used is `AlgebraicGeometry.Space.IsFibreFlatOverAtGeometricPoint`, condition (1) of
> that lemma, whose equivalence with condition (3) is
> `AlgebraicGeometry.Space.exists_flatQuotSMul_chart_iff_isFibreFlatOverAtGeometricPoint`.  See
> `AlgebraicGeometry.Space.isFlatOnFibreAt_iff_isFibreFlatOverAtGeometricPoint` for the reading at
> a single chosen geometric point.

```lean
def IsFlatOnFibreAt {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (F : Modules.{u, m} B S hS X.1 X.2) (x : points B S hS X.1) : Prop
```

**`AlgebraicGeometry.Space.IsFlatFibreAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean#L166). The attribute's comment: “part (2), part (1) at F = O_X, hence defined through the Lemma 05WY notion IsFibreFlatOverAtGeometricPoint at every geometric point over x”.

> **Stacks 05WZ, part (2).** The fibre of `X` over the image `z` of a point `x` of `|X|` is
> *flat at `x` over the fibre of `Y` over `z`* when part (1) holds for `F = 𝒪_X`.

```lean
def IsFlatFibreAt {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (x : points B S hS X.1) : Prop
```

**`AlgebraicGeometry.Space.IsFlatFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreFlatnessAtPoint.lean#L174). The attribute's comment: “part (3), part (2) at every point of |X| over z, hence defined through the Lemma 05WY notion IsFibreFlatOverAtGeometricPoint”.

> **Stacks 05WZ, part (3).** The fibre of `X` over a point `z` of `|Z|` is *flat over the
> fibre of `Y` over `z`* when part (2) holds at every point of `|X|` lying over `z`.

```lean
def IsFlatFibre {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (h : Y ⟶ Z)
    (z : points B S hS Z.1) : Prop
```

## Tag 05X0, a theorem

[Tag 05X0](https://stacks.math.columbia.edu/tag/05X0) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_and_isFibreFlat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean#L312). The attribute's comment: “the equivalence of (1) and (2) at a geometric point `x̄`: flatness over `Z` and over `Y` at `x̄` are condition (2) of Stacks 05VU, the fibre condition of (1) is the one of Stacks 05WY named by the source's definition 05WZ, and flatness of `Y` over `Z` at `ȳ` is Space.IsFlatAt at its image point. Hypothesis (2) of the source is read on the Zariski site of every etale chart; the openness assertion is isOpen_setOf_... below.”.

> **Stacks 05X0.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over a
> scheme `S`, let `F` be an `𝒪_X`-module which is quasi-coherent on the small étale site and of
> finite presentation on charts, and let `x̄` be a geometric point of `X` with images `ȳ` and `z̄`.
> Assume `X` is locally of finite presentation over `Z` and `Y` is locally of finite type over
> `Z`, and assume `F_{x̄} ≠ 0`.  Then
>
> 1. `F` is flat over `Z` at `x̄` and the restriction of `F` to its fibre over `z̄` is flat at `x̄`
>    over the fibre of `Y` over `z̄`
>
> holds exactly when
>
> 2. `Y` is flat over `Z` at `ȳ` and `F` is flat over `Y` at `x̄`
>
> holds.  The fibre condition of (1) is the one of Stacks 05WY, as the source's definition
> (Stacks 05WZ) prescribes.

```lean
theorem isFlatOverAtGeometricPoint_and_isFibreFlat_iff {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hp : IsLocallyOfFinitePresentation B S hS (f ≫ g).hom)
    (hq : IsLocallyOfFiniteType B S hS g.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (xbar : GeometricPoint B S hS X.1)
    (hne : Nontrivial (geometricModuleStalk B S hS X xbar F)) :
    (IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar ∧
        IsFibreFlatOverAtGeometricPoint B S hS f g F xbar) ↔
      (IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image ∧
        IsFlatOverAtGeometricPoint B S hS f F xbar)
```

**`AlgebraicGeometry.Space.setOf_isFlatOverAtGeometricPoint_and_isFibreFlat_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean#L478). The attribute's comment: “the openness assertion: the locus where (1) and (2) hold is the support of the module intersected with the locus where the module is flat over both `Z` and `Y`, which is open by Space.isOpen_flatLocus_inter_flatLocus. Conditions (1) and (2) are read at every geometric point above the point of `|X|`, which is no restriction: by Stacks 05VU the conditions do not depend on the geometric point chosen above it.”.

> **Stacks 05X0, the openness assertion.** Under the hypotheses of Stacks 05X0, the set of
> points of `|X|` lying in the support of `F` at which conditions (1) and (2) hold at every
> geometric point above them is the intersection of that support with the open set
> `AlgebraicGeometry.Space.isOpen_flatLocus_inter_flatLocus` is about, namely the locus where `F`
> is flat both over `Z` and over `Y`.  So that set is open in the support of `F`.
>
> A point of the support at which (1) and (2) hold lies in both flat loci by (1) and (2); and at a
> point of the support lying in both loci condition (1) holds, the fibre condition being a base
> change of flatness over `Y`, hence so does condition (2) by the equivalence.

```lean
theorem setOf_isFlatOverAtGeometricPoint_and_isFibreFlat_eq (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hp : IsLocallyOfFinitePresentation B S hS (f ≫ g).hom)
    (hq : IsLocallyOfFiniteType B S hS g.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F) :
    {x : points B S hS X.1 |
        x ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) ∧
        ∀ xbar : GeometricPoint B S hS X.1, xbar.image = x →
          (IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar ∧
              IsFibreFlatOverAtGeometricPoint B S hS f g F xbar) ∧
            (IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image ∧
              IsFlatOverAtGeometricPoint B S hS f F xbar)} =
      (flatLocus B S hS X.2 (f ≫ g).hom F ∩ flatLocus B S hS X.2 f.hom F) ∩
        supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)
```

**`AlgebraicGeometry.Space.isOpen_setOf_isFlatOverAtGeometricPoint_and_isFibreFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleFibreCriterion.lean#L524). The attribute's comment: “the openness assertion, read in the subspace topology of the support: the locus where (1) and (2) hold is open in Supp(F). Conditions (1) and (2) are read at every geometric point above the point of `|X|`, which by Stacks 05VU does not depend on the geometric point chosen. Finite presentation of the module is read on the Zariski site of every etale scheme chart.”.

> **Stacks 05X0, the openness assertion in the subspace of the support.** Under the hypotheses
> of Stacks 05X0 the set of points of the support of `F` at which conditions (1) and (2) hold is
> open in the support.
>
> This is `AlgebraicGeometry.Space.setOf_isFlatOverAtGeometricPoint_and_isFibreFlat_eq` read in
> the subspace topology: the set is the inverse image in the support of the open set of
> `AlgebraicGeometry.Space.isOpen_flatLocus_inter_flatLocus`.

```lean
theorem isOpen_setOf_isFlatOverAtGeometricPoint_and_isFibreFlat (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hp : IsLocallyOfFinitePresentation B S hS (f ≫ g).hom)
    (hq : IsLocallyOfFiniteType B S hS g.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F) :
    IsOpen {x : (supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) :
        Set (points B S hS X.1)) |
      ∀ xbar : GeometricPoint B S hS X.1, xbar.image = (x : points B S hS X.1) →
        (IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar ∧
            IsFibreFlatOverAtGeometricPoint B S hS f g F xbar) ∧
          (IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image ∧
            IsFlatOverAtGeometricPoint B S hS f F xbar)}
```

## Tag 05X1, a lemma

[Tag 05X1](https://stacks.math.columbia.edu/tag/05X1) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_flatFibreCharts_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseFinitePresentation.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseFinitePresentation.lean#L195). The attribute's comment: “the first conclusion: flatness of `f`. Hypotheses (1), (2) and (4) are the library spellings Space.IsLocallyOfFinitePresentation of `f ≫ g`, Space.IsFlat of `f ≫ g` and Space.IsLocallyOfFiniteType of `g`; hypothesis (3) is CARRIED in its every-etale-chart reading Space.HasFlatFibreCharts, as in the locally Noetherian form Space.isFlat_of_flatFibreCharts of Stacks 0APS, the comparison of a fibre of an algebraic space with the scheme-theoretic fibre of a chart being available in this library only for properties of objects (Space.hasEtaleLocalProperty_fiberAt_iff) and not for a property of a morphism between two such fibres.”.

> **Stacks Project, Tag 05X1, the first conclusion.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be
> morphisms of algebraic spaces over a scheme `S`. If `X` is locally of finite presentation over
> `Z`, `X` is flat over `Z`, the fibres of `X` over the points of `Z` are flat over the
> corresponding fibres of `Y` in the chart sense of
> `AlgebraicGeometry.Space.HasFlatFibreCharts`, and `Y` is locally of finite type over `Z`, then
> `f` is flat.

```lean
theorem isFlat_of_flatFibreCharts_finitePresentation
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfp : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hflat : IsFlat B S hS (f ≫ g)) (hft : IsLocallyOfFiniteType B S hS g)
    (hfib : HasFlatFibreCharts B S hS f g) :
    IsFlat B S hS f
```

**`AlgebraicGeometry.Space.isFlat_of_flatFibreCharts_finitePresentation_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseFinitePresentation.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseFinitePresentation.lean#L219). The attribute's comment: “the second conclusion: flatness of `Y` over `Z` for surjective `f`, with surjectivity taken as Space.IsSurjective of Stacks 03ME. Hypotheses (1), (2) and (4) are the library spellings Space.IsLocallyOfFinitePresentation of `f ≫ g`, Space.IsFlat of `f ≫ g` and Space.IsLocallyOfFiniteType of `g`; hypothesis (3) is CARRIED in its every-etale-chart reading Space.HasFlatFibreCharts, as in the locally Noetherian form Space.isFlat_of_flatFibreCharts_of_isSurjective of Stacks 0APS, the comparison of a fibre of an algebraic space with the scheme-theoretic fibre of a chart being available in this library only for properties of objects and not for a property of a morphism between two such fibres.”.

> **Stacks Project, Tag 05X1, the second conclusion.** In the situation of
> `AlgebraicGeometry.Space.isFlat_of_flatFibreCharts_finitePresentation`, if `f` is in addition
> surjective then `Y` is flat over `Z`.

```lean
theorem isFlat_of_flatFibreCharts_finitePresentation_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfp : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hflat : IsFlat B S hS (f ≫ g)) (hft : IsLocallyOfFiniteType B S hS g)
    (hfib : HasFlatFibreCharts B S hS f g) (hfs : IsSurjective B S hS f) :
    IsFlat B S hS g
```

## Tag 05X2, a lemma

[Tag 05X2](https://stacks.math.columbia.edu/tag/05X2) in the Stacks Project.

**`AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_of_isFlatOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeOverBase.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeOverBase.lean#L139). The attribute's comment: “base change: the locus on the base change is the inverse image of the locus downstairs. Hypotheses (1)-(4) of the source are the finite presentation of `X` over `Z`, of the module on the small etale site, the flatness of the module over `Z`, and the finite type of `Y` over `Z`. The openness assertion is Space.isOpen_flatLocus_of_isLocallyOfFinitePresentation_comp.”.

> **Stacks 05X2, the base-change assertion.** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` whose source and target are given over an algebraic space `Z` by `f ≫ q` and
> `q : Y ⟶ Z`, and let `F` be a quasi-coherent `𝒪_X`-module.  Assume `X` is locally of finite
> presentation over `Z`, that `F` is of finite presentation, that `F` is flat over `Z`, and that
> `Y` is locally of finite type over `Z`.  Then for a base change along an arbitrary morphism
> `h : Z' ⟶ Z`, presented by the cartesian squares `Y' = Y ×_Z Z'` and `X' = X ×_Y Y'`, the locus
> of points of `|X'|` at which the inverse image of `F` is flat over `Y'` is the inverse image
> under `|X'| ⟶ |X|` of the locus of points of `|X|` at which `F` is flat over `Y`.

```lean
theorem flatLocus_modulePullback_eq_preimage_of_isFlatOverBase
    {f : X ⟶ Y} {q : Y ⟶ Z} {h : Z' ⟶ Z} {g : Y' ⟶ Y} {q' : Y' ⟶ Z'}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'}
    (sqY : IsPullback g q' q h) (sqX : IsPullback g' f' f g)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hFfp : F.IsFinitePresentation)
    (hp : IsLocallyOfFinitePresentation B S hS (f ≫ q).hom)
    (hq : IsLocallyOfFiniteType B S hS q.hom)
    (hFZ : IsFlatOver B S hS X.2 (f ≫ q).hom F) :
    flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' flatLocus B S hS X.2 f.hom F
```

**`AlgebraicGeometry.Space.isOpen_flatLocus_of_isLocallyOfFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOverBase.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOverBase.lean#L73). The attribute's comment: “openness; hypothesis (3), flatness over the base, is not needed for this half”.

> **Stacks 05X2, the openness assertion.** Let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` whose source and target are given over an algebraic space `Z` by `p : X ⟶ Z` and
> `q : Y ⟶ Z` with `f ≫ q = p`.  If `p` is locally of finite presentation and `q` is locally of
> finite type, then the locus of points of `|X|` at which an `𝒪_X`-module which is quasi-coherent
> of finite presentation on charts is flat over `Y` is open.
>
> The tag sits on
> `AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnSite_comp`, which is this
> assertion with hypothesis (2) of the source read where the source reads it, on the small étale
> site; this form is the special case of it at a module whose finite presentation is available
> only chartwise.

```lean
theorem isOpen_flatLocus_of_isLocallyOfFinitePresentation_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (F : Modules.{u, u} B S hS X hX)
    (hp : IsLocallyOfFinitePresentation B S hS p)
    (hq : IsLocallyOfFiniteType B S hS q)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hfp : IsFinitePresentationOnCharts B S hS hX F) :
    IsOpen (flatLocus B S hS hX f F)
```

**`AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnSite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOverBase.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOverBase.lean#L102). The attribute's comment: “openness; hypothesis (3), flatness over the base, is not needed for this half”.

> **Stacks 05X2, the openness assertion, from finite presentation on the small étale site.**
> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` whose source and target are given
> over an algebraic space `Z` by `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`.  If `p` is locally
> of finite presentation and `q` is locally of finite type, then the locus of points of `|X|` at
> which an `𝒪_X`-module of finite presentation on the small étale site is flat over `Y` is open.
>
> Hypothesis (2) of the source, finite presentation of the module, is Stacks 03DL (7) on the small
> étale site of `X`; the quasi-coherence of the module which the source assumes in its preamble
> follows from it, by `SheafOfModules.isQuasicoherentOnSite_of_isFinitePresentationOnSite`.  Both
> are passed to the charts by
> `AlgebraicGeometry.Space.isFinitePresentationOnCharts_of_isFinitePresentationOnSite` and
> `AlgebraicGeometry.Space.isQuasicoherentOnCharts_of_isFinitePresentationOnSite`, so this form
> asks no chartwise hypothesis and
> `AlgebraicGeometry.Space.isOpen_flatLocus_of_isLocallyOfFinitePresentation_comp` is the special
> case of it at a module whose finite presentation is only available chartwise.

```lean
theorem isOpen_flatLocus_of_isFinitePresentationOnSite_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (F : Modules.{u, u} B S hS X hX)
    (hp : IsLocallyOfFinitePresentation B S hS p)
    (hq : IsLocallyOfFiniteType B S hS q)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite F) :
    IsOpen (flatLocus B S hS hX f F)
```

## Tag 05X3, a lemma

[Tag 05X3](https://stacks.math.columbia.edu/tag/05X3) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_setOf_isFlatAt_of_isLocallyOfFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocus.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocus.lean#L194). The attribute's comment: “openness of the flat locus”. References: SGA 3 VIB (1.3), “more general”; SGA 3 X (4.4), “partial”.

> **Stacks 05X3, the openness assertion.** Let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` whose source and target are given over a third algebraic space `Z` by morphisms
> `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`. If `p` is locally of finite presentation and `q`
> is locally of finite type, then the set of points of `|X|` at which `f` is flat is open.
>
> Flatness of `p`, which the source assumes, is not needed here: the two finiteness hypotheses
> already make `f` locally of finite presentation by Stacks 05WT, so the openness of the flat
> locus of a morphism locally of finite presentation applies to `f` itself. The same reduction
> is how the scheme-level assertion of Stacks 05VK is proved.

```lean
theorem isOpen_setOf_isFlatAt_of_isLocallyOfFinitePresentation_comp
    {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFinitePresentation B S hS p)
    (hq : IsLocallyOfFiniteType B S hS q) :
    IsOpen {x : points B S hS X | IsFlatAt B S hS f x}
```

**`AlgebraicGeometry.Space.flatLocusOpenAndStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusBaseChange.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusBaseChange.lean#L536). The attribute's comment: “openness and base change of the relative flat locus”.

> **Stacks 05X3.** For a commutative triangle of algebraic spaces over `S` given by
> `f : X ⟶ Y`, `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`, with `p` locally of finite
> presentation and flat and `q` locally of finite type, the locus of points of `|X|` at which `f`
> is flat is open and its formation commutes with base change along any morphism `Z' ⟶ Z`.
>
> The openness assertion is
> `AlgebraicGeometry.Space.isOpen_setOf_isFlatAt_of_isLocallyOfFinitePresentation_comp` and the
> base-change assertion is `AlgebraicGeometry.Space.isFlatAt_baseChangeOverBase_iff`.

```lean
theorem flatLocusOpenAndStableUnderBaseChange
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFinitePresentation B S hS p) (hpflat : IsFlat B S hS p)
    (hq : IsLocallyOfFiniteType B S hS q) :
    IsOpen {x : points B S hS X | IsFlatAt B S hS f x} ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Z' →
        ∀ (g : Z' ⟶ Z) (x' : points B S hS (pullback p g)),
          IsFlatAt B S hS (baseChangeOverBase B S hS f p q hfq g) x' ↔
            IsFlatAt B S hS f
              (pointsMap B S hS (pullback p g) (pullback.fst p g) x')
```

## Tag 0CZS, a lemma

[Tag 0CZS](https://stacks.math.columbia.edu/tag/0CZS) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusChartComparison.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusChartComparison.lean#L208). The attribute's comment: “clause (4) in the SMALL-ETALE-SITE reading: the source's Zariski-chart reading of clause (4) at a geometric point xbar implies that the image point of xbar lies in the locus of points of |X| admitting an etale morphism of algebraic spaces a : V -> X through them along which the inverse image of F is finite free in the sense of 03DE(2), which is the locus of Stacks 0CZT”.

> **Clause (4) of Stacks 0CZS in the small-étale-site reading of Stacks 0CZT.**  If a
> quasi-coherent `𝒪_X`-module `M` is finite free in an étale neighbourhood of a geometric point `x̄`
> of `X` in the Zariski-chart sense of `AlgebraicGeometry.Space.IsFiniteFreeNearGeometricPoint` —
> the source's own reading — then the image point of `x̄` lies in the finite-free étale locus
> `AlgebraicGeometry.Space.etaleFiniteFreeLocus`, the locus of Stacks 0CZT.

```lean
theorem mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint
    {X : AlgebraicSpaces B S hS} (M : Modules.{u, u} B S hS X.1 X.2)
    (hM : M.IsQuasicoherentOnSite) (xbar : GeometricPoint B S hS X.1)
    (h : IsFiniteFreeNearGeometricPoint B S hS xbar M) :
    xbar.image ∈ etaleFiniteFreeLocus B S hS M
```

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusChartComparison.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusChartComparison.lean#L248). The attribute's comment: “(1) implies (4) with clause (4) in the SMALL-ETALE-SITE reading, i.e. membership in the locus of Stacks 0CZT; the fibre stalk and its base ring are in the QUOTIENT FORM M_xbar / m_ybar M_xbar over O_{X, xbar} / m_ybar O_{X, xbar}, whose identification with the stalk on the geometric fibre X_ybar is condition (2) of Stacks 05WY and is not available”.

> **Clause (1) implies clause (4), in the small-étale-site reading of Stacks 0CZT.**  Let
> `f : X ⟶ Y` be locally of finite presentation, let `M` be a quasi-coherent `𝒪_X`-module of finite
> presentation on charts and let `x̄` be a geometric point of `X`.  If `M` is flat at `x` over `Y`
> and the geometric fibre stalk `(M_{ȳ})_{x̄}` is a flat `𝒪_{X_{ȳ}, x̄}`-module, then the image point
> of `x̄` lies in the finite-free étale locus of Stacks 0CZT.  The fibre stalk and its base ring are
> in the quotient form `M_{x̄} / 𝔪_{ȳ} M_{x̄}` over `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`.

```lean
theorem mem_etaleFiniteFreeLocus_of_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (M : Modules.{u, u} B S hS X.1 X.2)
    [M.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 M)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f M xbar)
    (hfibre : Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f M xbar)) :
    xbar.image ∈ etaleFiniteFreeLocus B S hS M
```

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_geometricFibre_of_isFiniteFreeNearGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean#L278). The attribute's comment: “(4) implies (3), with the geometric fibre X_ybar formed as the fibre product of f with the geometric point ybar = f o xbar in the category of algebraic spaces over S (02X2), the etale neighbourhood of xbar inside X_ybar read as in the locus of 0CZT, and clause (4) in the source's Zariski-chart reading”.

> **Stacks 0CZS, (4) implies (3).**  If a quasi-coherent `𝒪_X`-module `M` is finite free in an
> étale neighbourhood of a geometric point `x̄` of `X` — clause (4), in the source's Zariski-chart
> reading — then the inverse image of `M` to the geometric fibre `X_ȳ` through `x̄` is finite free in
> an étale neighbourhood of the lift of `x̄` to that fibre, which is clause (3).
>
> The source calls this implication immediate, and so it is: clause (4) puts `x` in the finite-free
> étale locus of `M` on `|X|`
> (`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint`), and that
> locus only grows under an inverse image, the lift of `x̄` lying over `x̄` by
> `AlgebraicGeometry.Space.pointsMap_geometricFibreToSource_geometricFibrePoint`.

```lean
theorem mem_etaleFiniteFreeLocus_geometricFibre_of_isFiniteFreeNearGeometricPoint
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (M : Modules.{u, u} B S hS X.1 X.2)
    (hM : M.IsQuasicoherentOnSite) (xbar : GeometricPoint B S hS X.1)
    (h : IsFiniteFreeNearGeometricPoint B S hS xbar M) :
    (geometricFibrePoint B S hS f xbar).image ∈
      etaleFiniteFreeLocus B S hS ((modulePullback B S hS
        (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj M)
```

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_geometricFibre_of_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean#L304). The attribute's comment: “(1) implies (3), with the geometric fibre X_ybar formed as the fibre product of f with ybar = f o xbar (02X2) and the fibre stalk of clause (1) in the QUOTIENT FORM M_xbar / m_ybar M_xbar over O_{X, xbar} / m_ybar O_{X, xbar}, whose identification with the etale local ring of that fibre is condition (2) of Stacks 05WY and is not available”.

> **Stacks 0CZS, (1) implies (3).**  Let `f : X ⟶ Y` be locally of finite presentation, let `M`
> be a quasi-coherent `𝒪_X`-module of finite presentation on charts and let `x̄` be a geometric point
> of `X`.  If `M` is flat at `x` over `Y` and the geometric fibre stalk `(M_{ȳ})_{x̄}` is a flat
> `𝒪_{X_{ȳ}, x̄}`-module, then the inverse image of `M` to the geometric fibre is finite free in an
> étale neighbourhood of the lift of `x̄`.
>
> This is `(1) ⟹ (4)` followed by `(4) ⟹ (3)`.  The fibre stalk and its base ring are in the
> quotient form `M_{x̄} / 𝔪_{ȳ} M_{x̄}` over `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`, as they are throughout
> this development; the identification of that quotient with the étale local ring of the geometric
> fibre constructed here is condition (2) of Stacks 05WY and is not available.

```lean
theorem mem_etaleFiniteFreeLocus_geometricFibre_of_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (M : Modules.{u, u} B S hS X.1 X.2)
    [M.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 M)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f M xbar)
    (hfibre : Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f M xbar)) :
    (geometricFibrePoint B S hS f xbar).image ∈
      etaleFiniteFreeLocus B S hS ((modulePullback B S hS
        (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj M)
```

**`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_of_isFiniteFreeNearGeometricFibrePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean#L263). The attribute's comment: “(3) implies (1), with the geometric fibre X_ybar formed as the fibre product of f with ybar = f o xbar in the category of algebraic spaces over S (02X2), clause (3) read as finite freeness of the inverse image of F to X_ybar on a Zariski open of an etale SCHEME chart of X_ybar around a point above the canonical lift of xbar, and the fibre stalk of clause (1) in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar}; flatness of F over Y, local finite presentation of f and finite presentation of F are not assumed”.

> **Stacks 0CZS, (3) implies (1).**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`,
> let `F` be a quasi-coherent `𝒪_X`-module and let `x̄` be a geometric point of `X` with image `ȳ`.
> If the inverse image of `F` to the geometric fibre `X_ȳ` is finite free in an étale neighbourhood
> of the lift of `x̄` — clause (3) — then the fibre stalk `(F_ȳ)_x̄` is a flat
> `𝒪_{X_ȳ, x̄}`-module, which is clause (1).
>
> The defining square of `X_ȳ` is cartesian, so clause (1) for `f` at `x̄` and clause (1) for the
> structure morphism `X_ȳ ⟶ Spec(κ(ȳ))` at the lift are the same condition
> (`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_modulePullback_iff`).
> Clause (3) is clause (4) for the inverse image on the fibre, so `(4) ⟹ (2) ⟹ (1)` on the fibre
> gives clause (1) at the lift, and the comparison carries it down.  Condition (2) of Stacks 05WY —
> the identification of the fibre stalk with the stalk on `X_ȳ` — is not used: both sides of the
> comparison are taken in the quotient form.
>
> Neither flatness of `F` over `Y`, nor local finite presentation of `f`, nor finite presentation of
> `F` is assumed, which generalises the source.

```lean
theorem flat_geometricFibreModuleStalk_of_isFiniteFreeNearGeometricFibrePoint
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (xbar : GeometricPoint B S hS X.1)
    (h : IsFiniteFreeNearGeometricPoint B S hS (geometricFibrePoint B S hS f xbar)
      ((modulePullback B S hS
        (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F)) :
    Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)
```

**`AlgebraicGeometry.Space.isFiniteFreeNearGeometricFibrePoint_of_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean#L303). The attribute's comment: “(1) implies (3), with the geometric fibre X_ybar formed as the fibre product of f with ybar = f o xbar in the category of algebraic spaces over S (02X2), the fibre stalk of clause (1) in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar}, and clause (3) read as finite freeness of the inverse image of F to X_ybar on a Zariski open of an etale SCHEME chart of X_ybar around a point above the canonical lift of xbar”.

> **Stacks 0CZS, (1) implies (3).**  Let `f : X ⟶ Y` be locally of finite presentation, let `F`
> be a finitely presented quasi-coherent `𝒪_X`-module and let `x̄` be a geometric point of `X` with
> image `ȳ`.  If `F` is flat at `x` over `Y` and the fibre stalk `(F_ȳ)_x̄` is a flat
> `𝒪_{X_ȳ, x̄}`-module, then the inverse image of `F` to the geometric fibre `X_ȳ` is finite free in
> an étale neighbourhood of the lift of `x̄`, which is clause (3).
>
> Clause (1) at `x̄` is clause (1) for the structure morphism `X_ȳ ⟶ Spec(κ(ȳ))` at the lift, by the
> comparison across the cartesian defining square of `X_ȳ`, and `(1) ⟹ (4)` applied on the fibre is
> clause (3).  Its hypotheses there are the base changes of the hypotheses here: Stacks 03XR for
> local finite presentation of the structure morphism, the inverse image of a finitely presented
> module for finite presentation on charts, and Stacks 05VW (1) for flatness at the lift.

```lean
theorem isFiniteFreeNearGeometricFibrePoint_of_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] [SheafOfModules.IsFinitePresentationOnSite F]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar)
    (hfibre : Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)) :
    IsFiniteFreeNearGeometricPoint B S hS (geometricFibrePoint B S hS f xbar)
      ((modulePullback B S hS
        (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F)
```

**`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_geometricFibre_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean#L368). The attribute's comment: “clauses (1), (2), (3) and (4) are equivalent, under the source's own hypotheses; the geometric fibre X_ybar is formed as the fibre product of f with ybar = f o xbar in the category of algebraic spaces over S (02X2), clauses (3) and (4) are read as finite freeness on a Zariski open of an etale SCHEME chart around a point above the relevant geometric point, and clauses (1) and (2) appear BOTH in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} and in the LITERAL FORM on X_ybar, i.e. the geometric stalk of the inverse image of F at the canonical lift of xbar over the etale local ring of X_ybar there; the agreement of the two forms is a consequence of the equivalence and is NOT condition (2) of Stacks 05WY, which stays unavailable”.

> **Stacks 0CZS, the equivalence of all four clauses.**  Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is locally of finite presentation, let `F` be a finitely presented
> quasi-coherent `𝒪_X`-module and let `x̄` be a geometric point of `X` with image `ȳ`.  If `F` is
> flat at `x` over `Y`, then
>
> 1. `(F_ȳ)_x̄` is a flat `𝒪_{X_ȳ, x̄}`-module,
> 2. `(F_ȳ)_x̄` is a free `𝒪_{X_ȳ, x̄}`-module,
> 3. `F_ȳ` is finite free in an étale neighbourhood of `x̄` in `X_ȳ`,
> 4. `F` is finite free in an étale neighbourhood of `x` in `X`
>
> are equivalent.  Clauses (1) and (2) appear twice: in the quotient form
> `F_x̄ / 𝔪_ȳ F_x̄` over `𝒪_{X, x̄} / 𝔪_ȳ 𝒪_{X, x̄}` in which this development carries them, and in
> the literal form on the geometric fibre `X_ȳ` of
> `StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean` — the honest geometric
> stalk of the inverse image of `F` at the canonical lift of `x̄`, over the honest étale local ring
> of `X_ȳ` there.  The entries are, in order: clause (1) in the quotient form, clause (2) in the
> quotient form, clause (1) in the literal form, clause (2) in the literal form, clause (3), and
> clause (4).
>
> The equivalence of the two forms of clauses (1) and (2) is *not* condition (2) of Stacks 05WY, and
> does not supply it: no identification of the quotient with the stalk on `X_ȳ` is produced, only
> the agreement of the flatness and freeness conditions, which clause (3) mediates.

```lean
theorem flat_geometricFibreModuleStalk_geometricFibre_tfae
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] [SheafOfModules.IsFinitePresentationOnSite F]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar) :
    [Module.Flat (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar),
      Module.Free (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar),
      Module.Flat
        ↥(etaleLocalRing B S hS (geometricFibre B S hS f (geometricPointMap f.hom xbar)).1
          (geometricFibrePoint B S hS f xbar))
        ↥(geometricModuleStalk B S hS (geometricFibre B S hS f (geometricPointMap f.hom xbar))
          (geometricFibrePoint B S hS f xbar)
          ((modulePullback B S hS
            (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F)),
      Module.Free
        ↥(etaleLocalRing B S hS (geometricFibre B S hS f (geometricPointMap f.hom xbar)).1
          (geometricFibrePoint B S hS f xbar))
        ↥(geometricModuleStalk B S hS (geometricFibre B S hS f (geometricPointMap f.hom xbar))
          (geometricFibrePoint B S hS f xbar)
          ((modulePullback B S hS
            (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F)),
      IsFiniteFreeNearGeometricPoint B S hS (geometricFibrePoint B S hS f xbar)
        ((modulePullback B S hS
          (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F),
      IsFiniteFreeNearGeometricPoint B S hS xbar F].TFAE
```

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_mem_etaleFiniteFreeLocus_geometricFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean#L453). The attribute's comment: “(3) implies (4) with BOTH clauses in the SMALL-ETALE-SITE reading, i.e. membership in the locus of Stacks 0CZT on the geometric fibre X_ybar and on X respectively, X_ybar being the fibre product of f with ybar = f o xbar in the category of algebraic spaces over S (02X2); the source's flatness of F over Y at x is STRENGTHENED to flatness of F over Y everywhere, because the Zariski-chart reading upstairs is recovered only at a geometric point chosen over the image of the lift of xbar”.

> **Stacks 0CZS, (3) implies (4), both clauses in the small-étale-site reading of the locus of
> Stacks 0CZT.**  Let `f : X ⟶ Y` be locally of finite presentation, let `F` be a quasi-coherent
> `𝒪_X`-module of finite presentation on charts which is flat over `Y`, and let `x̄` be a geometric
> point of `X` with image `ȳ`.  If the image of the canonical lift of `x̄` lies in the finite-free
> étale locus of the inverse image of `F` to the geometric fibre `X_ȳ`, then the image of `x̄` lies
> in the finite-free étale locus of `F`.
>
> This is the reverse inclusion of the base-change clause of Stacks 0CZT —
> `AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint_modulePullback`
> — at the cartesian defining square of `X_ȳ`, with the Zariski-chart reading upstairs supplied at a
> *chosen* geometric point over the image of the lift
> (`AlgebraicGeometry.Space.exists_isFiniteFreeNearGeometricPoint_of_mem_etaleFiniteFreeLocus`);
> only the image point of the chosen point enters the conclusion, and it is the image of the lift,
> which is the image of `x̄`.
>
> Because the chosen point need not be `x̄`, the source's hypothesis of flatness of `F` over `Y` *at
> `x`* is strengthened here to flatness over `Y` everywhere.  The equivalence
> `AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_geometricFibre_tfae` carries the source's
> own hypothesis, at the Zariski-chart reading of clause (3).

```lean
theorem mem_etaleFiniteFreeLocus_of_mem_etaleFiniteFreeLocus_geometricFibre
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (hF : IsFlatOver B S hS X.2 f.hom F) (xbar : GeometricPoint B S hS X.1)
    (h : (geometricFibrePoint B S hS f xbar).image ∈ etaleFiniteFreeLocus B S hS
      ((modulePullback B S hS
        (geometricFibreToSource B S hS f (geometricPointMap f.hom xbar))).obj F)) :
    xbar.image ∈ etaleFiniteFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.isFiniteFreeNearGeometricPoint_of_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean#L315). The attribute's comment: “(1) implies (4), with the etale neighbourhood of x taken to be a Zariski open of an etale SCHEME chart of X around a point above x and finite freeness read on the Zariski site of that chart (the source's own route through More on Morphisms 080Q); the fibre stalk and its base ring are in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar}, whose identification with the stalk on the geometric fibre X_ybar is condition (2) of Stacks 05WY and is not available”.

> **Stacks 0CZS, (1) implies (4).**  Let `f : X ⟶ Y` be locally of finite presentation, let `F`
> be a quasi-coherent `𝒪_X`-module of finite presentation on charts and let `x̄` be a geometric
> point of `X`.  If `F` is flat at `x` over `Y` and the fibre stalk `(F_{ȳ})_{x̄}` is a flat
> `𝒪_{X_{ȳ}, x̄}`-module, then `F` is finite free in an étale neighbourhood of `x` in `X`.
>
> The route is the source's: clause (1) together with the standing flatness makes the geometric
> stalk `F_{x̄}` free over `𝒪_{X, x̄}`
> (`AlgebraicGeometry.Space.free_geometricModuleStalk_of_flat_geometricFibreModuleStalk`, which is
> Stacks 05X0 at `𝟙 X` over `f`); freeness descends to the Zariski stalk of an étale scheme chart;
> and Stacks 0B8J trivialises the chart restriction on a Zariski open of the chart.  The fibre
> stalk and its base ring are taken in the quotient form `F_{x̄} / 𝔪_{ȳ} F_{x̄}` over
> `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`, as in
> `StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean`.

```lean
theorem isFiniteFreeNearGeometricPoint_of_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar)
    (hfibre : Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)) :
    IsFiniteFreeNearGeometricPoint B S hS xbar F
```

**`AlgebraicGeometry.Space.free_geometricFibreModuleStalk_of_isFiniteFreeNearGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean#L342). The attribute's comment: “(4) implies (2), with the etale neighbourhood of x a Zariski open of an etale SCHEME chart of X and the fibre stalk in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar}; flatness of F over Y, local finite presentation of f and finite presentation of F are not assumed”.

> **Stacks 0CZS, (4) implies (2).**  If `F` is finite free in an étale neighbourhood of `x` in
> `X`, then the fibre stalk `(F_{ȳ})_{x̄}` is a free `𝒪_{X_{ȳ}, x̄}`-module.
>
> The trivialization makes the Zariski stalk of the chart restriction free, freeness ascends to the
> geometric stalk by Stacks 05VP, and the fibre stalk is the reduction of the geometric stalk
> modulo `𝔪_{ȳ} 𝒪_{X, x̄}`.  Neither flatness of `F` over `Y`, nor local finite presentation of
> `f`, nor finite presentation of `F` is used, which generalises the source.

```lean
theorem free_geometricFibreModuleStalk_of_isFiniteFreeNearGeometricPoint
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (xbar : GeometricPoint B S hS X.1)
    (h : IsFiniteFreeNearGeometricPoint B S hS xbar F) :
    Module.Free (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)
```

**`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFiniteFree.lean#L379). The attribute's comment: “clauses (1), (2) and (4) are equivalent, under the source's own hypotheses, with the fibre stalk and its base ring in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} and clause (4) read as finite freeness on a Zariski open of an etale SCHEME chart of X around a point above x”.

> **Stacks 0CZS, the equivalence of clauses (1), (2) and (4).**  Let `f : X ⟶ Y` be a morphism
> of algebraic spaces over `S` which is locally of finite presentation, let `F` be a finitely
> presented quasi-coherent `𝒪_X`-module and let `x̄` be a geometric point of `X` with image `ȳ`.
> If `F` is flat at `x` over `Y`, then
>
> 1. `(F_{ȳ})_{x̄}` is a flat `𝒪_{X_{ȳ}, x̄}`-module,
> 2. `(F_{ȳ})_{x̄}` is a free `𝒪_{X_{ȳ}, x̄}`-module,
> 4. `F` is finite free in an étale neighbourhood of `x` in `X`
>
> are equivalent.  The fibre stalk and its base ring are taken in the quotient form
> `F_{x̄} / 𝔪_{ȳ} F_{x̄}` over `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`, which is how the source's own proof
> reads clause (1), and clause (4) is read on a Zariski open of an étale scheme chart.  Clause (3)
> is not among the entries *here*: it is proved from clause (4) in
> `StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean`, and it is added to the
> equivalence — in its Zariski-chart reading on the geometric fibre, together with clauses (1) and
> (2) in their literal form on that fibre — by
> `AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_geometricFibre_tfae` of
> `StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkClauseThree.lean`.  The source's reverse
> implication `(3) ⟹ (2)` goes through the identification of the stalk on the geometric fibre with
> the quotient, which is condition (2) of Stacks 05WY and is still not available; the equivalence
> does not need it, only the agreement of the two flatness conditions across the cartesian defining
> square of the fibre.

```lean
theorem flat_geometricFibreModuleStalk_tfae
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] [SheafOfModules.IsFinitePresentationOnSite F]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar) :
    [Module.Flat (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar),
      Module.Free (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar),
      IsFiniteFreeNearGeometricPoint B S hS xbar F].TFAE
```

**`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_of_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean#L415). The attribute's comment: “(2) implies (1), with the fibre stalk and its base ring in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} (the geometric fibre X_ybar is not constructed in this library); flatness of F over Y and finite presentation are not assumed”.

> **Stacks 0CZS, (2) implies (1).** A free fibre stalk `(F_{ȳ})_{x̄}` is a flat
> `𝒪_{X_{ȳ}, x̄}`-module.
>
> The fibre stalk and its base ring are taken in the quotient form `F_{x̄} / 𝔪_{ȳ} F_{x̄}` over
> `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`, which is condition (1) of Stacks 05WY for `X ⟶ X ⟶ Y` and is how
> the source's own proof reads clause (1); their identification with the étale local ring and the
> geometric stalk on a geometric fibre `X_{ȳ}` is not available, the fibre of a morphism of
> algebraic spaces over a point of the target not being constructed in this library.  Neither
> flatness of `F` at `x` over `Y`, nor local finite presentation of `f`, nor finite presentation
> of `F` is assumed, which generalises the source.

```lean
theorem flat_geometricFibreModuleStalk_of_free {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, m} B S hS X.1 X.2) (xbar : GeometricPoint B S hS X.1)
    (hfree : Module.Free (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)) :
    Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)
```

**`AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_iff_free_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean#L480). The attribute's comment: “(1) iff (2) under the source's own hypotheses, with the fibre stalk and base ring in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} (the geometric fibre X_ybar is not constructed in this library)”.

> **Stacks 0CZS, (1) is equivalent to (2).** For a finitely presented `𝒪_X`-module `F`,
> flatness and freeness of the fibre stalk `(F_{ȳ})_{x̄}` over the local ring `𝒪_{X_{ȳ}, x̄}` of the
> geometric fibre agree.
>
> The fibre stalk and its base ring are taken in the quotient form `F_{x̄} / 𝔪_{ȳ} F_{x̄}` over
> `𝒪_{X, x̄} / 𝔪_{ȳ} 𝒪_{X, x̄}`, which is condition (1) of Stacks 05WY for `X ⟶ X ⟶ Y` and is how
> the source's own proof reads clause (1); the geometric fibre `X_{ȳ}` itself is not constructed in
> this library.  Neither flatness of `F` at `x` over `Y` nor local finite presentation of `f` is
> assumed, which generalises the source: both clauses are conditions on the fibre stalk alone.

```lean
theorem flat_geometricFibreModuleStalk_iff_free_of_isFinitePresentation
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsFinitePresentationOnSite] (xbar : GeometricPoint B S hS X.1) :
    Module.Flat (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar) ↔
      Module.Free (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar)
```

**`AlgebraicGeometry.Space.exists_chartOpen_over_iso_free_of_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean, line 732](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean#L732). The attribute's comment: “(1) implies (4) under the source's own hypotheses, with clause (1) in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} (the geometric fibre X_ybar is not constructed in this library) and clause (4) in the reading the source's proof produces: an etale SCHEME chart (U, u) over (X, xbar) together with a Zariski open W of U containing u on which the chart restriction phi^* F becomes free on finitely many generators. That W is an etale neighbourhood of xbar in X by chartOpenNeighborhood. The finite freeness is read as freeness of (phi^* F)|_W on the slice of the Zariski site of U at W; identifying that with the chart restriction of F to W read on the Zariski site of W itself is an equivalence of sites and is NOT claimed. Clause (3) is not statable: it needs the geometric fibre X_ybar as an algebraic space.”.

> **Stacks 0CZS, clause (4).**  Let `f : X ⟶ Y` be locally of finite presentation, let `F` be
> a quasi-coherent `𝒪_X`-module of finite presentation on charts and let `x̄` be a geometric point
> of `X`.  If `F` is flat at `x` over `Y` and the fibre stalk `(F_{ȳ})_{x̄}` is a flat
> `𝒪_{X_{ȳ}, x̄}`-module — clause (1) — then `F` is finite free in an étale neighbourhood of `x` in
> `X`: there are an étale scheme chart `φ : (U, u) → (X, x̄)`, a Zariski open `W ⊆ U` containing
> `u` and a rank `r` such that `(φ^* F)|_W` is free on `r` generators.
>
> This is the source's own `(1) ⟹ (4)`, in the reading its proof produces.  Clause (1) makes the
> geometric stalk `F_{x̄}` free over `𝒪_{X, x̄}`
> (`AlgebraicGeometry.Space.free_geometricModuleStalk_of_flat_geometricFibreModuleStalk`, which is
> Stacks 05X0 at `𝟙 X` over `f`); that descends along the faithfully flat comparison of
> Stacks 05VP to freeness of the Zariski stalk `(φ^* F)_u` over `𝒪_{U, u}`
> (`AlgebraicGeometry.Space.free_chartZariskiModuleStalk_of_free_geometricModuleStalk`); and the
> chart restriction is of finite presentation on the Zariski site of `U`, which is what
> `AlgebraicGeometry.Space.IsFinitePresentationOnCharts` says, so Stacks 0B8J spreads a basis of
> that stalk to a trivialization on a Zariski open neighbourhood of `u`.  0B8J is used through
> `Stacks.StalkFiniteType.exists_over_iso_free_of_stalk_basis`, which takes the basis over the
> local ring `𝒪_{U, u}` rather than over the `RingCat`-valued stalk.  The open `W` is itself an
> étale neighbourhood of `x̄` in `X`, by
> `AlgebraicGeometry.Space.chartOpenNeighborhood`.

```lean
theorem exists_chartOpen_over_iso_free_of_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar)
    (hfibre : Module.Flat (geometricFibreLocalRing B S hS f xbar)
      (geometricFibreModuleStalk B S hS f F xbar)) :
    ∃ (N : SmallEtaleNeighborhood xbar) (W : (chartScheme N.chart).Opens)
        (_ : chartPoint B S hS X.1 N ∈ W) (r : ℕ),
      Nonempty ((restrictToChart B S hS X.2 F N.chart).over W ≅
        SheafOfModules.free (ULift.{u} (Fin r)))
```

**`AlgebraicGeometry.Space.exists_chartOpen_over_iso_free_iff_flat_geometricFibreModuleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean, line 858](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreStalkFreeness.lean#L858). The attribute's comment: “(1) iff (4), clause (1) in the QUOTIENT FORM F_xbar / m_ybar F_xbar over O_{X, xbar} / m_ybar O_{X, xbar} (the geometric fibre X_ybar is not constructed in this library) and clause (4) in the reading the source's proof produces: an etale SCHEME chart (U, u) over (X, xbar) with a Zariski open W of U containing u on which phi^* F becomes free on finitely many generators, the finite freeness read on the slice of the Zariski site of U at W. Identifying that slice reading with the chart restriction of F to W read on the Zariski site of W itself is an equivalence of sites and is NOT claimed; neither is the identification of clause (4) with the small-etale reading of the locus of Tag 0CZT. The (4) => (1) direction needs NONE of the source's hypotheses except quasi-coherence of F. Clause (3) is not statable: it needs the geometric fibre X_ybar as an algebraic space.”.

> **Stacks 0CZS, clause (1) if and only if clause (4).**  For `f : X ⟶ Y` locally of finite
> presentation, `F` a quasi-coherent `𝒪_X`-module of finite presentation on charts flat at `x`
> over `Y`, and `x̄` a geometric point of `X`: the fibre stalk `(F_{ȳ})_{x̄}` is a flat
> `𝒪_{X_{ȳ}, x̄}`-module exactly when `F` becomes free on finitely many generators on a Zariski
> open neighbourhood of `u` in some étale scheme chart `(U, u)` of `x̄`.
>
> Clause (4) is read as the source's own proof produces it, on the slice of the Zariski site of
> the chart at the open; identifying that with the chart restriction of `F` read on the Zariski
> site of the open itself is an equivalence of sites and is not claimed.  The reverse implication
> uses only quasi-coherence of `F`.

```lean
theorem exists_chartOpen_over_iso_free_iff_flat_geometricFibreModuleStalk
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (xbar : GeometricPoint B S hS X.1)
    (hflat : IsFlatOverAtGeometricPoint B S hS f F xbar) :
    (∃ (N : SmallEtaleNeighborhood xbar) (W : (chartScheme N.chart).Opens)
        (_ : chartPoint B S hS X.1 N ∈ W) (r : ℕ),
      Nonempty ((restrictToChart B S hS X.2 F N.chart).over W ≅
        SheafOfModules.free (ULift.{u} (Fin r)))) ↔
      Module.Flat (geometricFibreLocalRing B S hS f xbar)
        (geometricFibreModuleStalk B S hS f F xbar)
```

## Tag 0CZT, a lemma

[Tag 0CZT](https://stacks.math.columbia.edu/tag/0CZT) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_etaleFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocus.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocus.lean#L180). The attribute's comment: “openness”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is locally of finite
> presentation and let `F` be a finitely presented `𝒪_X`-module which is flat over `Y`.  Then the
> set of points of `|X|` at which `F` is free in an étale neighbourhood is open in `|X|`.

```lean
theorem isOpen_etaleFreeLocus {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (_hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2)
    [SheafOfModules.IsFinitePresentationOnSite F]
    (_hF : IsFlatOver B S hS X.2 f.hom F) :
    @IsOpen _ (pointTopology B S hS X.1) (etaleFreeLocus B S hS F)
```

**`AlgebraicGeometry.Space.etaleFreeLocus_modulePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusBaseChange.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusBaseChange.lean#L327). The attribute's comment: “the base-change clause: the formation of the locus W commutes with arbitrary base change, as the EQUALITY W((g')^* F) = |g'|^(-1)(W(F)) of subsets of |X'|, at an arbitrary cartesian square of algebraic spaces over S. The openness clause is isOpen_etaleFreeLocus of Spaces/EtaleFreeLocus.lean; the two together are the whole tag. Hypotheses are the source's own and are asked DOWNSTAIRS only, of f and F: f locally of finite presentation, F quasi-coherent, F of finite presentation on the small etale site, and F flat over Y. Nothing is asked of f' or of the inverse image of F, so no stability of the hypotheses under base change is used. The test scheme T of the source is not named: the statement is at a cartesian square, of which the square of a morphism of test schemes is an instance by isPullback_baseChangeMap. Freeness is IsFreeModule, the universal-property reading on the small etale site, at an arbitrary index type.”.

> **Stacks 0CZT, the base-change clause.**  Let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square of algebraic spaces over `S`, let `f` be locally of finite presentation and
> let `F` be a quasi-coherent `𝒪_X`-module of finite presentation on the small étale site which is
> flat over `Y`.  Then the étale free locus of the inverse image of `F` on `X'` is the inverse
> image of the étale free locus of `F`:
>
> ```
> W((g')^* F) = |g'|⁻¹(W(F)).
> ```
>
> The hypotheses are asked of `f` and `F` only, which is what the source asks; nothing is required
> of `f'` or of `(g')^* F`, so no stability of the hypotheses under base change is used.
>
> The inclusion `⊇` is `AlgebraicGeometry.Space.preimage_etaleFreeLocus_subset` and holds for an
> arbitrary morphism with no hypothesis.  The inclusion `⊆` is the source's argument, transporting
> clause (1) of Stacks 0CZS across the square by
> `AlgebraicGeometry.Space.flat_geometricFibreModuleStalk_modulePullback_iff`, between the two ends
> `exists_geometricPoint_flat_geometricFibreModuleStalk_of_mem_etaleFreeLocus` and
> `AlgebraicGeometry.Space.mem_etaleFreeLocus_of_flat_geometricFibreModuleStalk`.

```lean
theorem etaleFreeLocus_modulePullback_eq
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    (hqc : F.IsQuasicoherentOnSite) (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : SheafOfModules.IsFinitePresentationOnSite F)
    (hflat : IsFlatOver B S hS X.2 f.hom F) :
    etaleFreeLocus B S hS ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' etaleFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusBaseChangeReverse.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusBaseChangeReverse.lean#L77). The attribute's comment: “the reverse inclusion W' ⊆ |g'|^{-1}(W) of the base-change clause, with membership in W' read at a geometric point xbar' of X' in the source's own Zariski-chart reading of clause (4) of Stacks 0CZS -- a Zariski open of an etale SCHEME chart of X' on which the chart restriction of (g')^*F is finite free -- and W the locus of points of |X| admitting an etale morphism of algebraic spaces through them along which the inverse image of F is finite free in the sense of 03DE(2)”.

> **The reverse inclusion of the base-change clause.**  Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is locally of finite presentation, let `F` be a quasi-coherent
> `𝒪_X`-module of finite presentation on charts which is flat over `Y`, and let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square.  If the inverse image `(g')^*F` is finite free in an étale neighbourhood of
> a geometric point `x̄'` of `X'` — clause (4) of Stacks 0CZS in the source's Zariski-chart reading —
> then the image of `x̄'` in `|X|` lies in the finite-free étale locus of `F`.

```lean
theorem mem_etaleFiniteFreeLocus_of_isFiniteFreeNearGeometricPoint_modulePullback
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F)
    (hF : IsFlatOver B S hS X.2 f.hom F) (xbar' : GeometricPoint B S hS X'.1)
    (h : IsFiniteFreeNearGeometricPoint B S hS xbar' ((modulePullback B S hS g').obj F)) :
    pointsMap B S hS X'.1 g'.hom xbar'.image ∈ etaleFiniteFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.etaleFreeLocus_modulePullback_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusFinitePresentation.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusFinitePresentation.lean#L331). The attribute's comment: “the base-change clause: the etale free locus of (g')^*F on |X'| is the preimage under |g'| of the etale free locus of F on |X|, at the PLAIN-FREENESS locus the source defines and the openness clause carries, with finite presentation of F read on the small etale site”.

> **The base-change clause for the étale free locus.**  Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is locally of finite presentation, let `F` be a quasi-coherent
> `𝒪_X`-module of finite presentation on charts which is flat over `Y`, and let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square.  Then the étale free locus of the inverse image `(g')^*F` on `|X'|` is the
> inverse image under `|g'|` of the étale free locus of `F` on `|X|`.
>
> The locus is `AlgebraicGeometry.Space.etaleFreeLocus`, the plain-freeness locus by which the
> source defines it, and finite presentation of `F` is taken on the small étale site.

```lean
theorem etaleFreeLocus_modulePullback_eq_preimage_of_isPullback
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    [SheafOfModules.IsFinitePresentationOnSite F]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hF : IsFlatOver B S hS X.2 f.hom F) :
    etaleFreeLocus B S hS ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' etaleFreeLocus B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.23, Tag 05WX](https://stacks.math.columbia.edu/tag/05WX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
