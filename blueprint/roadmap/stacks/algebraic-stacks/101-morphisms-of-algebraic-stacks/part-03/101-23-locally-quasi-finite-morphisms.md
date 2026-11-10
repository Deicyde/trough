---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyOfFiniteType_and_discreteTopology_of_isLocallyQuasiFinite, AlgebraicGeometry.Stack.isLocallyQuasiFinite_of_isLocallyOfFiniteType_of_discreteTopology, AlgebraicGeometry.Stack.isLocallyQuasiFinite_iff_isLocallyOfFiniteType_and_discreteTopology, AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyQuasiFinite, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_field, AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_fieldPoint, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_comp
statement: formalized
proof: formalized
---

# 101.23 Locally quasi-finite morphisms

Section 101.23 of the Stacks Project, [Tag 06PT](https://stacks.math.columbia.edu/tag/06PT). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06UA, a lemma

[Tag 06UA](https://stacks.math.columbia.edu/tag/06UA) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_and_discreteTopology_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L186). The attribute's comment: “(1) implies (2)”.

> **Stacks 06UA, the implication (1) ⟹ (2).** A 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces and locally quasi-finite in the sense of **Stacks 04XB** is
> locally of finite type, and the fibre of it over every field-valued point of the target has
> discrete space of points.

```lean
theorem isLocallyOfFiniteType_and_discreteTopology_of_isLocallyQuasiFinite
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (h : IsLocallyQuasiFinite B S hS f.hom) :
    AlgebraicStacks.IsLocallyOfFiniteType B S hS f ∧
      ∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
        (toBase : Spec (.of k) ⟶ S)
        (g : schemeStack.{u, w} B S hS (Over.mk (⟨toBase⟩ : B.obj hk ⟶ B.obj hS)) ⟶ 𝒴),
        DiscreteTopology
          (points B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
            (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.property)
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_of_isLocallyOfFiniteType_of_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L308). The attribute's comment: “(2) implies (1)”.

> **Stacks 06UA, the implication (2) ⟹ (1).** A 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces, locally of finite type, and whose fibre over every field-valued
> point of the target has discrete space of points, is locally quasi-finite in the sense of
> **Stacks 04XB**.
>
> One scheme atlas of `𝒴` suffices by **Stacks 04XD**, and for the base change of `f` along it the
> criterion of **Stacks 06RW** applies: it is locally of finite type by **Stacks 04XC** and its
> field-valued fibres are fibres of `f`.

```lean
theorem isLocallyQuasiFinite_of_isLocallyOfFiniteType_of_discreteTopology
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hft : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hfib : ∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
      (toBase : Spec (.of k) ⟶ S)
      (g : schemeStack.{u, w} B S hS (Over.mk (⟨toBase⟩ : B.obj hk ⟶ B.obj hS)) ⟶ 𝒴),
      DiscreteTopology
        (points B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
          (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.property)) :
    IsLocallyQuasiFinite B S hS f.hom
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_iff_isLocallyOfFiniteType_and_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L362).

> **Stacks 06UA.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` which is representable
> by algebraic spaces is locally quasi-finite in the sense of **Stacks 04XB** exactly when it is
> locally of finite type and for every field-valued point of `𝒴` the fibre of `f` over it has
> discrete space of points.
>
> The right-hand side is the conjunction of the second and third clauses of **Stacks 06PU**.

```lean
theorem isLocallyQuasiFinite_iff_isLocallyOfFiniteType_and_discreteTopology
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    IsLocallyQuasiFinite B S hS f.hom ↔
      (AlgebraicStacks.IsLocallyOfFiniteType B S hS f ∧
        ∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
          (toBase : Spec (.of k) ⟶ S)
          (g : schemeStack.{u, w} B S hS (Over.mk (⟨toBase⟩ : B.obj hk ⟶ B.obj hS)) ⟶ 𝒴),
          DiscreteTopology
            (points B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
              (twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.property))
```

## Tag 06PU, a definition

[Tag 06PU](https://stacks.math.columbia.edu/tag/06PU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyQuasiFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteAlgebraicStack.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteAlgebraicStack.lean#L87).

> **Stacks 06PU.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is locally
> quasi-finite* when it is quasi-DM (**Stacks 04YW**), locally of finite type (**Stacks 06FS**,
> part (1)), and for every field-valued point of `𝒴` the fibre of `f` over it has discrete space of
> points.
>
> A field-valued point is a field `k` contained in the site together with a structure morphism
> `Spec(k) ⟶ S` and a 1-morphism from the algebraic stack `Spec(k)` represents to `𝒴`; the fibre is
> the apex of the canonical 2-fibre-product square of that 1-morphism with `f`, and its points
> carry the topology of **Stacks 04XL**.

```lean
abbrev IsLocallyQuasiFinite {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06UB, a lemma

[Tag 06UB](https://stacks.math.columbia.edu/tag/06UB) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteBaseChange.lean#L111).

> **Stacks 06UB.** A base change of a locally quasi-finite 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over `S` is locally quasi-finite: the first projection of any 2-fibre product of the
> cospan `(g, f)` is locally quasi-finite as soon as `f` is.
>
> The quasi-DM conjunct is **Stacks 050F** at the exchanged square and local finite type is
> **Stacks 06FU**. For the fibre conjunct, a field-valued point `g'` of `𝒴'` gives the outer point
> `g' ≫ g` of `𝒴`, and the fibre of the base change over `g'` is by **Stacks 02XD** a 2-fibre
> product of the cospan `(f, g' ≫ g)`, whose fibre the hypothesis says has discrete space of
> points.

```lean
theorem isLocallyQuasiFinite_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsLocallyQuasiFinite B S hS f) :
    IsLocallyQuasiFinite B S hS P.fst
```

## Tag 06UC, a lemma

[Tag 06UC](https://stacks.math.columbia.edu/tag/06UC) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverField.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverField.lean#L314).

> Let `𝒳 ⟶ Spec(k)` be a locally quasi-finite 1-morphism, where `𝒳` is an
> algebraic stack over the field `k`, and let `f : V ⟶ 𝒳` be a locally quasi-finite 1-morphism out
> of the algebraic stack represented by a scheme `V` of the site with structure morphism
> `g : V ⟶ Spec(k)`. Then `g` is locally quasi-finite: it is locally of finite type and locally
> quasi-finite as a morphism of schemes.

```lean
theorem locallyQuasiFinite_of_isLocallyQuasiFinite_over_field
    (B : BigFppfSite.{u}) (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    {𝒳 : Stack.AlgebraicStacks.{u, w} B (Spec (.of k)) hk}
    (p : 𝒳 ⟶ Stack.schemeStack.{u, w} B (Spec (.of k)) hk (Over.mk (𝟙 (B.obj hk))))
    (hp : IsLocallyQuasiFinite B (Spec (.of k)) hk p)
    (V : Scheme.{u}) (hV : B.Contains V) (g : V ⟶ Spec (.of k))
    (f : Stack.schemeStack.{u, w} B (Spec (.of k)) hk
      (Over.mk (⟨g⟩ : B.obj hV ⟶ B.obj hk)) ⟶ 𝒳)
    (hf : IsLocallyQuasiFinite B (Spec (.of k)) hk f) :
    LocallyOfFiniteType g ∧ LocallyQuasiFinite g
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_fieldPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverFieldPoint.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverFieldPoint.lean#L351). The attribute's comment: “at a field-valued point of a general base scheme”.

> **Stacks 06UC at a field-valued point of a general base scheme, for the Stacks 06PU notion
> of local quasi-finiteness of the chart.** This is
> `locallyQuasiFinite_siteMap_of_isLocallyQuasiFinite_fieldPoint` with local quasi-finiteness of
> `c` read in the sense of **Stacks 06PU**, which is what the source's statement uses; it implies
> the **Stacks 04XB** notion by **Stacks 06UA**, since `c` is representable by algebraic
> spaces.

```lean
theorem locallyQuasiFinite_of_isLocallyQuasiFinite_over_fieldPoint
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k))) (toBase : Spec (.of k) ⟶ S)
    {𝒴₀ : Stack.AlgebraicStacks.{u, w} B S hS} (W : BigFppfOver B S hS)
    (q : 𝒴₀ ⟶ Stack.schemeStack.{u, w} B S hS (Over.mk (⟨toBase⟩ : B.obj hk ⟶ B.obj hS)))
    (c : Stack.schemeStack.{u, w} B S hS W ⟶ 𝒴₀)
    (hq : IsLocallyQuasiFinite B S hS q) (hc : IsLocallyQuasiFinite B S hS c) :
    LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map (siteMap B S hS (c ≫ q))) ∧
      LocallyQuasiFinite ((BigFppfOver.toScheme B S hS).map (siteMap B S hS (c ≫ q)))
```

## Tag 06UD, a lemma

[Tag 06UD](https://stacks.math.columbia.edu/tag/06UD) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteComposition.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteComposition.lean#L500).

> **Stacks 06UD.** A composite of locally quasi-finite 1-morphisms of algebraic stacks over
> `S` is locally quasi-finite.
>
> The quasi-DM condition composes by **Stacks 050K** and local finite type by **Stacks 06FT**. For
> the third condition, the fibre of `f ≫ g` over a field-valued point `p` of `𝒵` is by
> **Stacks 02XD** a 2-fibre product of the cospan `(f, 𝒴_k ⟶ 𝒴)`, where `𝒴_k` is the fibre of `g`
> over `p`; both `𝒳 ×_𝒴 𝒴_k ⟶ 𝒴_k` and `𝒴_k ⟶ Spec(k)` are locally quasi-finite by
> **Stacks 06UB**, so the discreteness is the case of a target locally quasi-finite over a
> field.

```lean
theorem isLocallyQuasiFinite_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsLocallyQuasiFinite B S hS f) (hg : IsLocallyQuasiFinite B S hS g) :
    IsLocallyQuasiFinite B S hS (f ≫ g)
```

## Tag 06UE, a lemma

[Tag 06UE](https://stacks.math.columbia.edu/tag/06UE) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_tfae_hasQuasiFiniteFlatSpaceCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentation.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentation.lean#L203). The attribute's comment: “granted the substantial direction of Tag 06MF, the quasi-DM presentation theorem, as the hypothesis `hPresentation`, and granted the containment of the terminal scheme in the site as the hypothesis `hZ`, which the absolute quasi-DM condition of Tag 050D part (6) needs. Only (1) implies (2) uses `hPresentation`”.

> **Stacks 06UE.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following
> are equivalent: `f` is quasi-DM; every base change of `f` along an algebraic space over `𝒴` has
> a surjective, flat, locally finitely presented, locally quasi-finite cover by an algebraic
> space; and some algebraic space surjective, flat and locally of finite presentation over `𝒴`
> carries a base change of `f` with such a cover.
>
> The hypothesis `hPresentation` is the substantial direction of **Stacks 06MF**, carried in this
> library; it is used only for (1) ⟹ (2).

```lean
theorem isQuasiDM_tfae_hasQuasiFiniteFlatSpaceCover
    (hPresentation : Stack.ExistsQuasiDMPresentationOfIsAbsolutelyQuasiDM.{u, w} B S hS hZ)
    (f : 𝒳 ⟶ 𝒴) :
    [IsQuasiDM B S hS f,
      HasQuasiFiniteFlatSpaceCoverOnEveryBaseChange B S hS f,
      HasQuasiFiniteFlatSpaceCoverOnSomeFlatBaseChange B S hS f].TFAE
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_tfae_hasQuasiFiniteFlatSpaceCover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentationUnconditional.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentationUnconditional.lean#L83). The attribute's comment: “unconditional. The implication (1) implies (2) uses the substantial direction of Tag 06MF, the quasi-DM presentation theorem hasQuasiDMPresentation\_of\_isAbsolutelyQuasiDM, which is proved; the containment of the terminal scheme in the site that the absolute quasi-DM condition of Tag 050D part (6) needs is discharged by AlgebraicGeometry.BigFppfSite.contains\_terminal”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are equivalent: `f`
> is quasi-DM; every base change of `f` along an algebraic space over `𝒴` has a surjective, flat,
> locally finitely presented, locally quasi-finite cover by an algebraic space; and some algebraic
> space surjective, flat and locally of finite presentation over `𝒴` carries a base change of `f`
> with such a cover.

```lean
theorem isQuasiDM_tfae_hasQuasiFiniteFlatSpaceCover_unconditional (f : 𝒳 ⟶ 𝒴) :
    [IsQuasiDM B S hS f,
      HasQuasiFiniteFlatSpaceCoverOnEveryBaseChange B S hS f,
      HasQuasiFiniteFlatSpaceCoverOnSomeFlatBaseChange B S hS f].TFAE
```

## Tag 06UF, a lemma

[Tag 06UF](https://stacks.math.columbia.edu/tag/06UF) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_and_transfersLocalQuasiFiniteness_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean#L186). The attribute's comment: “the implication (1) => (2)”.

> **Stacks 06UF, (1) ⟹ (2).** A locally quasi-finite 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over `S` is quasi-DM, and for every algebraic space `𝒱` over `𝒴` a locally quasi-finite
> 1-morphism `𝒰 ⟶ 𝒳 ×_𝒴 𝒱` out of an algebraic space has locally quasi-finite composite
> `𝒰 ⟶ 𝒱`.
>
> The quasi-DM conjunct is the first conjunct of **Stacks 06PU**. For the second, the projection
> `𝒳 ×_𝒴 𝒱 ⟶ 𝒱` is a base change of `f` and so locally quasi-finite by **Stacks 06UB**, and
> **Stacks 06UD** composes it with the given 1-morphism.

```lean
theorem isQuasiDM_and_transfersLocalQuasiFiniteness_of_isLocallyQuasiFinite
    (f : 𝒳 ⟶ 𝒴) (hf : IsLocallyQuasiFinite B S hS f) :
    IsQuasiDM B S hS f ∧ TransfersLocalQuasiFinitenessOnSpaceBaseChanges B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFiniteCoverOnEverySpaceBaseChange_of_isQuasiDM_of_transfers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean#L212). The attribute's comment: “the implication (2) => (3), granted the substantial direction of Tag 06MF as `hPresentation`, which is how Tag 06UE is carried in this library”.

> **Stacks 06UF, (2) ⟹ (3).** If `f` is quasi-DM and transfers local quasi-finiteness to the
> projections of its algebraic-space base changes, then each of those base changes has a
> surjective, flat, locally finitely presented and locally quasi-finite cover by an algebraic
> space which is locally quasi-finite over the base.
>
> The cover is the one **Stacks 06UE** produces from the quasi-DM condition; it is locally
> quasi-finite in the sense of Properties of Stacks, Section 04XB, hence in the sense of
> **Stacks 06PU** by **Stacks 06UA**, and the second conjunct of clause (2) then makes its
> composite to the base locally quasi-finite.

```lean
theorem locallyQuasiFiniteCoverOnEverySpaceBaseChange_of_isQuasiDM_of_transfers
    (hPresentation : Stack.ExistsQuasiDMPresentationOfIsAbsolutelyQuasiDM.{u, w} B S hS
      (BigFppfSite.contains_terminal B))
    (f : 𝒳 ⟶ 𝒴) (hf : IsQuasiDM B S hS f)
    (htr : TransfersLocalQuasiFinitenessOnSpaceBaseChanges B S hS f) :
    LocallyQuasiFiniteCoverOnEverySpaceBaseChange B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange_of_onEverySpaceBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean#L231). The attribute's comment: “the implication (3) => (4), unconditionally”.

> **Stacks 06UF, (3) ⟹ (4).** Every algebraic stack has a smooth surjective chart by a scheme
> of the site, and a smooth 1-morphism is flat and locally of finite presentation, so the
> universal clause (3) applied to that chart is clause (4).

```lean
theorem locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange_of_onEverySpaceBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : LocallyQuasiFiniteCoverOnEverySpaceBaseChange B S hS f) :
    LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentation.lean#L250). The attribute's comment: “the quasi-DM conjunct of the conclusion of (4) => (1), unconditionally. The local finite type and field-valued-fibre conjuncts of (4) => (1) are NOT carried”.

> **Stacks 06UF, the quasi-DM conjunct of (4) ⟹ (1).** A locally quasi-finite flat cover of
> `𝒳 ×_𝒴 𝒱` by an algebraic space over one algebraic space `𝒱` surjective, flat and locally of
> finite presentation over `𝒴` makes `f` quasi-DM.
>
> The cover is locally quasi-finite in the sense of **Stacks 06PU**, hence in the sense of
> Properties of Stacks, Section 04XB by **Stacks 06UA**, which is clause (3) of **Stacks 06UE**;
> that lemma's implication (3) ⟹ (1) is the conclusion.

```lean
theorem isQuasiDM_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f) :
    IsQuasiDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFiniteCoverOnEverySpaceBaseChange_of_isQuasiDM_of_transfers_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L160). The attribute's comment: “the implication (2) => (3)”.

> **Stacks 06UF, (2) ⟹ (3).** If `f` is quasi-DM and transfers local quasi-finiteness to the
> projections of its algebraic-space base changes, then each of those base changes has a
> surjective, flat, locally finitely presented and locally quasi-finite cover by an algebraic
> space which is locally quasi-finite over the base.
>
> This is
> `...AlgebraicStacks.locallyQuasiFiniteCoverOnEverySpaceBaseChange_of_isQuasiDM_of_transfers`
> with its hypothesis, the substantial direction of **Stacks 06MF**, discharged by
> `AlgebraicGeometry.Stack.hasQuasiDMPresentation_of_isAbsolutelyQuasiDM`.

```lean
theorem locallyQuasiFiniteCoverOnEverySpaceBaseChange_of_isQuasiDM_of_transfers_unconditional
    (f : 𝒳 ⟶ 𝒴) (hf : IsQuasiDM B S hS f)
    (htr : TransfersLocalQuasiFinitenessOnSpaceBaseChanges B S hS f) :
    LocallyQuasiFiniteCoverOnEverySpaceBaseChange B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L240). The attribute's comment: “the local finite type conjunct of the conclusion of (4) => (1)”.

> **Stacks 06UF, the local finite type conjunct of (4) ⟹ (1).** A locally quasi-finite flat
> cover of `𝒳 ×_𝒴 𝒱` by an algebraic space over one algebraic space `𝒱` surjective, flat and
> locally of finite presentation over `𝒴` makes `f` locally of finite type.
>
> The composite `𝒰 ⟶ 𝒱` is locally quasi-finite, hence locally of finite type, and `𝒰` covers
> `𝒳 ×_𝒴 𝒱` by a surjective flat 1-morphism locally of finite presentation, so the projection
> `𝒳 ×_𝒴 𝒱 ⟶ 𝒱` is locally of finite type by **Stacks 06U8**; that projection is the base change
> of `f` along `𝒱 ⟶ 𝒴`, so **Stacks 06U7** descends local finite type to `f`.

```lean
theorem isLocallyOfFiniteType_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.discreteTopology_points_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L351). The attribute's comment: “the field-valued-fibre conjunct of the conclusion of (4) => (1)”.

> **Stacks 06UF, the field-valued-fibre conjunct of (4) ⟹ (1).** A locally quasi-finite flat
> cover of `𝒳 ×_𝒴 𝒱` by an algebraic space over one algebraic space `𝒱` surjective, flat and
> locally of finite presentation over `𝒴` makes the fibre of `f` over *every* field-valued point of
> `𝒴` have discrete space of points.
>
> This is the source's reduction of the third condition of **Stacks 06PU** to a field-valued point
> which lifts to the chart. The chart being surjective, the fibre `𝒱 ×_𝒴 Spec(k)` has a point, and a
> point of an algebraic stack is an equivalence class of field-valued points, so some field
> extension `k'/k` carries `v : Spec(k') ⟶ 𝒱` and `e : Spec(k') ⟶ Spec(k)` with `v ≫ g`
> 2-isomorphic to `e ≫ y`. Over `v` the fibre is discrete, which is
> `discreteTopology_points_twoFibreProduct_of_hasLocallyQuasiFiniteFlatSpaceCoverOver`; changing the
> cospan leg by that 2-isomorphism (`CategoryTheory.Bicategory.isTwoFibreProduct_reindexSnd`) and
> pasting (**Stacks 02XD**) identify the fibre over `v ≫ g` with `(𝒳 ×\_𝒴 Spec(k)) ×\_\{Spec(k)}
> Spec(k')`, and that maps onto `𝒳 ×\_𝒴 Spec(k)` by a base change of `e`.
>
> `e` is surjective by `AlgebraicGeometry.Stack.isSurjective_of_fieldSpectrum`, the spectrum of a
> field having exactly one point, and it is universally open because its target is the algebraic
> stack of the spectrum of a field (**Stacks 06DN** through
> `universallyOpen_to_fieldSpectrumStack`), so its base change is open on points by **Stacks 06U1**.
> No finiteness of `k'/k` is needed: the source gets openness from flatness and local finite
> presentation of a *finite* extension, and universal openness over a field spectrum gives it for
> an arbitrary one.

```lean
theorem discreteTopology_points_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f)
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k))) (toBase : Spec (.of k) ⟶ S)
    (y : Stack.schemeStack.{u, w} B S hS (Over.mk (⟨toBase⟩ : B.obj hk ⟶ B.obj hS)) ⟶ 𝒴) :
    @DiscreteTopology
      (Stack.points B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.val
        (Stack.twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.property)
      (Stack.pointTopology B S hS
        (Stack.twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L419). The attribute's comment: “the implication (4) => (1)”.

> **Stacks 06UF, (4) ⟹ (1).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` admitting
> one algebraic space `𝒱` surjective, flat and locally of finite presentation over `𝒴` whose base
> change `𝒳 ×_𝒴 𝒱` has a surjective, flat, locally finitely presented and locally quasi-finite
> cover by an algebraic space locally quasi-finite over `𝒱` is locally quasi-finite.
>
> The three conjuncts of **Stacks 06PU** are the three preceding theorems.

```lean
theorem isLocallyQuasiFinite_of_locallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L443).

> **Stacks 06UF.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
>
> 1. `f` is locally quasi-finite (**Stacks 06PU**);
> 2. `f` is quasi-DM (**Stacks 04YW**) and for every algebraic space `𝒱` over `𝒴` every locally
>    quasi-finite 1-morphism `𝒰 ⟶ 𝒳 ×_𝒴 𝒱` out of an algebraic space has locally quasi-finite
>    composite `𝒰 ⟶ 𝒱`;
> 3. for every algebraic space `𝒱` over `𝒴` there is a surjective, flat, locally finitely presented
>    and locally quasi-finite 1-morphism `𝒰 ⟶ 𝒳 ×_𝒴 𝒱` out of an algebraic space whose composite
>    `𝒰 ⟶ 𝒱` is locally quasi-finite;
> 4. there are algebraic spaces `𝒰` and `𝒱`, a surjective, flat and locally finitely presented
>    1-morphism `𝒱 ⟶ 𝒴`, and a surjective, flat, locally finitely presented and locally
>    quasi-finite 1-morphism `𝒰 ⟶ 𝒳 ×_𝒴 𝒱` whose composite `𝒰 ⟶ 𝒱` is locally quasi-finite.

```lean
theorem isLocallyQuasiFinite_tfae (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [IsLocallyQuasiFinite B S hS f,
        IsQuasiDM B S hS f ∧ TransfersLocalQuasiFinitenessOnSpaceBaseChanges B S hS f,
        LocallyQuasiFiniteCoverOnEverySpaceBaseChange B S hS f,
        LocallyQuasiFiniteCoverOnSomeFlatSpaceBaseChange B S hS f]
```

## Tag 06UG, a lemma

[Tag 06UG](https://stacks.math.columbia.edu/tag/06UG) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_of_comp_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteCancellation.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteCancellation.lean#L105).

> **Stacks 06UG.** If a composite of 1-morphisms of algebraic stacks over `S` is locally
> quasi-finite and its second factor is quasi-DM, then its first factor is locally quasi-finite.
>
> `f` is 2-isomorphic to its graph over `𝒵` followed by the second projection of the canonical
> 2-fibre product of the cospan `(f ≫ g, g)`. The graph is locally quasi-finite because `g` is
> quasi-DM (**Stacks 050I** part (3) and **Stacks 06UA**), the projection is a base change of
> `f ≫ g` and so is locally quasi-finite by **Stacks 06UB**, and **Stacks 06UD** composes the
> two.

```lean
theorem isLocallyQuasiFinite_of_comp_of_isQuasiDM
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsLocallyQuasiFinite B S hS (f ≫ g)) (hg : IsQuasiDM B S hS g) :
    IsLocallyQuasiFinite B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.23, Tag 06PT](https://stacks.math.columbia.edu/tag/06PT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
