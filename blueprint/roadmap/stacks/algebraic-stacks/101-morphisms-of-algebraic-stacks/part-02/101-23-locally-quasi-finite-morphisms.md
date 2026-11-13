---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyOfFiniteType_and_discreteTopology_of_isLocallyQuasiFinite, AlgebraicGeometry.Stack.isLocallyQuasiFinite_of_isLocallyOfFiniteType_of_discreteTopology, AlgebraicGeometry.Stack.isLocallyQuasiFinite_iff_isLocallyOfFiniteType_and_discreteTopology, AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyQuasiFinite, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_field, AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_fieldPoint, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_comp
statement: formalized
proof: formalized
---

# 101.23 Locally quasi-finite morphisms

Section 101.23 of the Stacks Project, [Tag 06PT](https://stacks.math.columbia.edu/tag/06PT). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06UA, a lemma

[Tag 06UA](https://stacks.math.columbia.edu/tag/06UA) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_and_discreteTopology_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L186). The attribute's comment: “(1) implies (2)”.

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

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_of_isLocallyOfFiniteType_of_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L308). The attribute's comment: “(2) implies (1)”.

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

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_iff_isLocallyOfFiniteType_and_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRepresentable.lean#L362).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyQuasiFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteAlgebraicStack.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteAlgebraicStack.lean#L87).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteBaseChange.lean#L111).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverField.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverField.lean#L314).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.locallyQuasiFinite_of_isLocallyQuasiFinite_over_fieldPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverFieldPoint.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteOverFieldPoint.lean#L351). The attribute's comment: “at a field-valued point of a general base scheme”.

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteComposition.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteComposition.lean#L500).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_tfae_hasQuasiFiniteFlatSpaceCover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentationUnconditional.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMRelativePresentationUnconditional.lean#L82). The attribute's comment: “All three conditions, with no hypothesis beyond the source's. The implication (1) implies (2) uses Tag 06MF through hasQuasiDMPresentation\_of\_isAbsolutelyQuasiDM, and the terminal scheme that Tag 050D part (6) needs lies in the site by AlgebraicGeometry.BigFppfSite.contains\_terminal”.

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteRelativePresentationUnconditional.lean#L440).

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_of_comp_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteCancellation.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocallyQuasiFiniteCancellation.lean#L105).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
