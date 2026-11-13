---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.ringKrullDim_relation_eq_add_ringKrullDim_sourceFibre, AlgebraicGeometry.Stack.ringKrullDim_chart_add_relation_eq, AlgebraicGeometry.Stack.hasLocalRingDimensionAtEveryChart_of_hasLocalRingDimensionAtSomeChart, AlgebraicGeometry.Stack.hasLocalRingDimensionAtSomeChart_iff_hasLocalRingDimensionAtEveryChart, AlgebraicGeometry.Stack.hasLocalRingDimensionAtSomeChart_of_hasLocalRingDimensionAtEveryChart, AlgebraicGeometry.Stack.hasRelationLocalRingDimension_transport_twoFibreProduct, AlgebraicGeometry.Stack.exists_iff_forall_geometricPoint_hasChartLocalRingDimension, AlgebraicGeometry.Stack.exists_hasChartLocalRingDimension
statement: formalized
proof: formalized
---

# 107.6 The dimension of the local ring

Section 107.6 of the Stacks Project, [Tag 0DS7](https://stacks.math.columbia.edu/tag/0DS7). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DS8, a lemma

[Tag 0DS8](https://stacks.math.columbia.edu/tag/0DS8) in the Stacks Project.

**`AlgebraicGeometry.Stack.ringKrullDim_relation_eq_add_ringKrullDim_sourceFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean#L286). The attribute's comment: “the dimension formula for the source projection”.

> **Stacks 0DS8**, the dimension formula. For a smooth 1-morphism `f : U ⟶ 𝒳` from a scheme to
> a locally Noetherian algebraic stack and a presented self-intersection `R = U ×_𝒳 U` with source
> morphism `s`, the dimension of `𝒪_{R, r}` at a geometric point `r` is the sum of the dimension
> of `𝒪_{U, s(r)}` and the dimension of the fibre `𝒪_{R_{s(r)}, r}`.
>
> The morphism `s` is smooth, hence flat, so `𝒪_{U, s(r)} ⟶ 𝒪_{R, r}` is a flat local
> homomorphism of Noetherian local rings and Stacks 00ON applies.

```lean
theorem ringKrullDim_relation_eq_add_ringKrullDim_sourceFibre
    (hf : AlgebraicStacks.IsSmooth B S hS f) (hsq : Bicategory.IsTwoFibreProduct sq)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳) (hR : IsAlgebraicSpace B S hS R)
    (r : Space.GeometricPoint B S hS R) :
    ringKrullDim (Space.etaleLocalRing B S hS R r) =
      ringKrullDim (chartEtaleLocalRing B S hS U f sq R eU eR r) +
        ringKrullDim (sourceFibreEtaleLocalRing B S hS U f sq R eU eR hR r)
```

**`AlgebraicGeometry.Stack.ringKrullDim_chart_add_relation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean#L329). The attribute's comment: “the dimension-difference identity”.

> **Stacks 0DS8.** The identity
> `dim(𝒪_{U,s(r)}) - dim(𝒪_{R_u,r}) = 2 dim(𝒪_{U,s(r)}) - dim(𝒪_{R,r})`, recorded in the
> subtraction-free form obtained by adding `dim(𝒪_{R_u,r}) + dim(𝒪_{R,r})` to both sides, which is
> equivalent to it wherever the three dimensions are finite — in particular here, all three rings
> being Noetherian local.
>
> The invariant `2 dim(𝒪_{U,s(r)}) - dim(𝒪_{R,r})` of Stacks 0DSA is thus computed by the source
> fibre.

```lean
theorem ringKrullDim_chart_add_relation_eq
    (hf : AlgebraicStacks.IsSmooth B S hS f) (hsq : Bicategory.IsTwoFibreProduct sq)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳) (hR : IsAlgebraicSpace B S hS R)
    (r : Space.GeometricPoint B S hS R) :
    ringKrullDim (chartEtaleLocalRing B S hS U f sq R eU eR r) +
        ringKrullDim (Space.etaleLocalRing B S hS R r) =
      ringKrullDim (chartEtaleLocalRing B S hS U f sq R eU eR r) +
          ringKrullDim (chartEtaleLocalRing B S hS U f sq R eU eR r) +
        ringKrullDim (sourceFibreEtaleLocalRing B S hS U f sq R eU eR hR r)
```

## Tag 0DS9, a lemma

[Tag 0DS9](https://stacks.math.columbia.edu/tag/0DS9) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasLocalRingDimensionAtEveryChart_of_hasLocalRingDimensionAtSomeChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartComparison.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartComparison.lean#L358). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 0DS9, condition (1) implies condition (2).** If some scheme of the site carries a
> smooth 1-morphism to a locally Noetherian algebraic stack `𝒳` and a finite type point above the
> finite type point `x ∈ |𝒳|` at which the invariant of Stacks 0DSA is `d`, then every such
> configuration measures it to be `d`.
>
> This is the chart independence of the invariant,
> `AlgebraicGeometry.Stack.hasChartInvariant_congr_of_isFiniteTypePoint`, read through the
> restatement of the two conditions in terms of
> `AlgebraicGeometry.Stack.HasChartInvariant`.

```lean
theorem hasLocalRingDimensionAtEveryChart_of_hasLocalRingDimensionAtSomeChart
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) (d : ℤ)
    (hd : HasLocalRingDimensionAtSomeChart.{u, w} B S hS 𝒳 h𝒳 x hx d) :
    HasLocalRingDimensionAtEveryChart.{u, w} B S hS 𝒳 h𝒳 x hx d
```

**`AlgebraicGeometry.Stack.hasLocalRingDimensionAtSomeChart_iff_hasLocalRingDimensionAtEveryChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartComparison.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartComparison.lean#L387). The attribute's comment: “the equivalence of the two conditions”.

> **Stacks 0DS9.** For a locally Noetherian algebraic stack `𝒳`, a finite type point
> `x ∈ |𝒳|` and an integer `d`, the two conditions
>
> 1. there *exists* a scheme `U` of the site, a smooth 1-morphism `U ⟶ 𝒳` and a finite type point
>    `u ∈ U` above `x` with `2 dim(𝒪_{U,ū}) - dim(𝒪_{R, e(ū)}) = d`, where `R = U ×_𝒳 U`, and
> 2. *every* such `U`, smooth 1-morphism and finite type point above `x` satisfies that identity
>
> are equivalent. Condition (1) is `AlgebraicGeometry.Stack.HasLocalRingDimensionAtSomeChart`,
> which is also the definition of Stacks 0DSA, and condition (2) is
> `AlgebraicGeometry.Stack.HasLocalRingDimensionAtEveryChart`.
>
> Condition (2) implies condition (1) because the range of the two quantifiers is nonempty, by
> **Stacks 06FX**. The converse is the chart independence of the invariant, which is the content of
> the source's proof.

```lean
theorem hasLocalRingDimensionAtSomeChart_iff_hasLocalRingDimensionAtEveryChart
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) (d : ℤ) :
    HasLocalRingDimensionAtSomeChart.{u, w} B S hS 𝒳 h𝒳 x hx d ↔
      HasLocalRingDimensionAtEveryChart.{u, w} B S hS 𝒳 h𝒳 x hx d
```

**`AlgebraicGeometry.Stack.hasLocalRingDimensionAtSomeChart_of_hasLocalRingDimensionAtEveryChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartIndependence.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionChartIndependence.lean#L493). The attribute's comment: “condition (2) implies condition (1)”.

> **Stacks 0DS9, condition (2) implies condition (1).** If every smooth chart of a locally
> Noetherian algebraic stack `𝒳` carrying a finite type point above `x` measures the invariant of
> Stacks 0DSA to be `d`, then some one does — because, by **Stacks 06FX**, there is one.
>
> This direction of the equivalence is exactly the non-emptiness of the range of the two
> quantifiers, supplied by
> `AlgebraicGeometry.Stack.exists_smoothChart_presentation_of_isFiniteTypePoint`.

```lean
theorem hasLocalRingDimensionAtSomeChart_of_hasLocalRingDimensionAtEveryChart
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) (d : ℤ)
    (h : HasLocalRingDimensionAtEveryChart.{u, w} B S hS 𝒳 h𝒳 x hx d) :
    HasLocalRingDimensionAtSomeChart.{u, w} B S hS 𝒳 h𝒳 x hx d
```

**`AlgebraicGeometry.Stack.hasRelationLocalRingDimension_transport_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionSquareIndependence.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionSquareIndependence.lean#L248). The attribute's comment: “the invariant of the two conditions does not depend on the presented self-intersection”.

> **The invariant of Stacks 0DSA does not depend on the presented self-intersection.** Let a
> smooth chart `g : V ⟶ 𝒳` be given, and let its self-intersection be presented twice over — by a
> 2-fibre product square `T` for the cospan `(g, g)`, an algebraic space `Q` presenting its apex
> through `eQ` and a mediating morphism `δ`, and by `T'`, `Q'`, `eQ'`, `δ'`. Then at one and the
> same point `ν` of the chart the two presentations measure the invariant to be the same integer.
>
> The point of the chart does *not* move: the comparison of the two presentations is an
> isomorphism `Q ≅ Q'` of the two representing presheaves of the relation, which carries the
> diagonal image of `ν` for the first presentation to the diagonal image of `ν` for the second and
> leaves `ν` alone. The chart dimension entering the invariant is read at `ν` itself
> (`AlgebraicGeometry.Stack.hasRelationLocalRingDimension_diagonal_iff`), so it is untouched, and
> the dimension of the relation is unchanged under an isomorphism of presheaves
> (`AlgebraicGeometry.Space.localRingDimension_pointsMap_of_isIso`).
>
> This is one half of the presentation quantifier of condition (2) of **Stacks 0DS9**; the other
> half, the comparison equivalence of the chart, is
> `AlgebraicGeometry.Stack.hasRelationLocalRingDimension_transport_equivalence`, and the two are
> combined in
> `AlgebraicGeometry.Stack.forall_hasRelationLocalRingDimension_transport_presentation`.

```lean
theorem hasRelationLocalRingDimension_transport_twoFibreProduct
    (δ : Bicategory.TwoCommSq.PreHom (selfIntersectionDiagonalSquare B S hS V g) T)
    (δ' : Bicategory.TwoCommSq.PreHom (selfIntersectionDiagonalSquare B S hS V g) T')
    (ν : Space.points B S hS (yoneda.obj V)) (d : ℤ) :
    HasRelationLocalRingDimension B S hS V g T Q eV eQ
        (Space.pointsMap B S hS (yoneda.obj V)
          (selfIntersectionDiagonalMap B S hS V g T Q eV eQ δ) ν) d ↔
      HasRelationLocalRingDimension B S hS V g T' Q' eV eQ'
        (Space.pointsMap B S hS (yoneda.obj V)
          (selfIntersectionDiagonalMap B S hS V g T' Q' eV eQ' δ') ν) d
```

**`AlgebraicGeometry.Stack.exists_iff_forall_geometricPoint_hasChartLocalRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean#L394). The attribute's comment: “the two conditions, over the geometric point above a point of the relation”.

> **Stacks 0DS9, for the choice of geometric point.** The existential and the universal
> condition over the geometric points above a point `ρ` of the relation are equivalent: some
> geometric point above `ρ` measures the invariant to be `d` exactly when every one does.
>
> Forward this is
> `AlgebraicGeometry.Stack.hasChartLocalRingDimension_iff_hasRelationLocalRingDimension`; backward
> it is the existence of a geometric point above `ρ`.

```lean
theorem exists_iff_forall_geometricPoint_hasChartLocalRingDimension
    (hR : IsAlgebraicSpace B S hS R) (ρ : Space.points B S hS R) (d : ℤ) :
    (∃ r : Space.GeometricPoint B S hS R, r.LiesOver ρ ∧
        HasChartLocalRingDimension B S hS U f sq R eU eR r d) ↔
      ∀ r : Space.GeometricPoint B S hS R, r.LiesOver ρ →
        HasChartLocalRingDimension B S hS U f sq R eU eR r d
```

**`AlgebraicGeometry.Stack.exists_hasChartLocalRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean#L419). The attribute's comment: “the invariant of the two conditions is a well-defined integer at a smooth chart”.

> **Stacks 0DS9, well-definedness of the invariant.** At a geometric point of a presented
> self-intersection of a smooth chart of a locally Noetherian algebraic stack the invariant
> `2 dim(𝒪_{U,s(r)}) - dim(𝒪_{R,r})` of Stacks 0DSA is realized by an integer: both local rings are
> Noetherian local rings, so Krull's height theorem makes both dimensions finite.
>
> This is what lets the conditions of Stacks 0DS9 be read at a `d ∈ ℤ`; the integer is unique by
> `AlgebraicGeometry.Stack.hasChartLocalRingDimension_unique`.

```lean
theorem exists_hasChartLocalRingDimension
    (hf : AlgebraicStacks.IsSmooth B S hS f) (hsq : Bicategory.IsTwoFibreProduct sq)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳) (hR : IsAlgebraicSpace B S hS R)
    (r : Space.GeometricPoint B S hS R) :
    ∃ d : ℤ, HasChartLocalRingDimension B S hS U f sq R eU eR r d
```

## Tag 0DSA, a definition

[Tag 0DSA](https://stacks.math.columbia.edu/tag/0DSA) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasLocalRingDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationLocalRingDimension.lean#L478).

> **Stacks 0DSA.** The dimension of the local ring of a locally Noetherian algebraic stack `𝒳`
> at a finite type point `x ∈ |𝒳|` *is* the integer `d` when condition (1) of Stacks 0DS9 holds:
> some scheme `U` of the site carries a smooth 1-morphism `f : U ⟶ 𝒳` and a finite type point `u`
> of `U` above `x` at which a presented self-intersection `R = U ×_𝒳 U`, with diagonal `e`, has
> `2 dim(𝒪_{U,ū}) - dim(𝒪_{R, e(ū)}) = d`.
>
> The source phrases the dimension as a relation between `x` and `d ∈ ℤ`, not as a function of `x`,
> and so does this: the value is pinned down by Stacks 0DS9, whose independence of the chart is not
> available here. Negative values occur (Stacks 0DS5), whence `ℤ`.

```lean
def HasLocalRingDimension (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (_h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (_hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) (d : ℤ) : Prop
```

## Tag 0DSB, a lemma

[Tag 0DSB](https://stacks.math.columbia.edu/tag/0DSB) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasLocalRingDimensionAtSomeChart_iff_of_versalCogroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionVersalChart.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalRingDimensionVersalChart.lean#L134).

> **Stacks 0DSB.** Let `𝒳` be an algebraic stack, locally of finite type over a locally
> Noetherian scheme `S` (Situation 0DQU), and let `x₀ : Spec k ⟶ 𝒳` be a morphism, `k` a field of
> finite type over `S`, with `Spec Λ ⊆ S` an affine open through which `Spec k ⟶ S` factors with
> `Λ → k` finite (Section 07T2). Represent `𝓕_{𝒳,k,x₀}` as in Remark 0DR3 by a cogroupoid
> `(A, B, s, t, c)` of Noetherian complete local `Λ`-algebras with residue field `k`: a versal formal
> object `ξ` over `A` and a representable presentation `P` on `𝒞^_Λ` with objects `P.objects = A`,
> arrows `P.arrows = B`, source and target `s = P.source`, `t = P.target` and comultiplication
> `c = P.comultiplication`, whose restriction to `𝒞_Λ` is the groupoid in functors
> `(A|_{𝒞_Λ}, A|_{𝒞_Λ} ×_{ξ, 𝓕, ξ} A|_{𝒞_Λ})` of `ξ` (this is the representation produced by
> `AlgebraicGeometry.Stack.exists_versalCogroupoid_predeformationCategory`). Then the dimension of
> the local ring of `𝒳` at the point of `x₀` (Stacks 0DSA, the single integer of Stacks 0DS9) is
> `2 dim A - dim B`: an integer `d` satisfies condition (1) of Stacks 0DS9
> (`AlgebraicGeometry.Stack.HasLocalRingDimensionAtSomeChart`) at that point exactly when
> `d = 2 dim A - dim B`.
>
> Every such representation is allowed, so the statement holds for all of them; the two dimensions
> are finite and are recorded as natural numbers before the difference is taken, as in Stacks
> 0DSA.

```lean
theorem hasLocalRingDimensionAtSomeChart_iff_of_versalCogroupoid (D : VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let C := Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀
    letI := C.category
    let hp := Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property
    ∀ (ξ : Deformation.FormalObject C.projection) (_ : Deformation.IsVersal hp.cofibered ξ)
      (P : Deformation.RepresentablePresentation.{_, u, u}
        (Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)),
      P.objects = ξ.base →
      Nonempty (Deformation.versalGroupoid C.projection hp ξ ≅
        Deformation.GroupoidInFunctors.restrict P.groupoidInFunctors
          Deformation.artinianToComplete) →
      ∃ m n : ℕ, ringKrullDim P.objects = m ∧ ringKrullDim P.arrows = n ∧
        ∀ d : ℤ, HasLocalRingDimensionAtSomeChart D.B D.S D.hS D.𝒳
          (isLocallyNoetherianStack_of_versalSituation D) (objectPoint D.B D.S D.hS iΛ x₀ hx₀)
          (isFiniteTypePoint_objectPoint D iΛ hiΛ x₀ hx₀ hfinite) d ↔
            d = 2 * (m : ℤ) - (n : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 107.6, Tag 0DS7](https://stacks.math.columbia.edu/tag/0DS7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
