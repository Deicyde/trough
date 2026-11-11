---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasFiniteRelationFibersAtEveryPoint, AlgebraicGeometry.Space.HasPropertyBeta, AlgebraicGeometry.Space.IsDecent, AlgebraicGeometry.Space.IsReasonable, AlgebraicGeometry.Space.IsVeryReasonable, AlgebraicGeometry.Space.isVeryReasonable_of_isQuasiSeparated, AlgebraicGeometry.Space.isVeryReasonable_of_relativelyRepresentable, AlgebraicGeometry.Space.isDecent_of_isReasonable
statement: formalized
proof: formalized
---

# 68.17 Relative conditions

Section 68.17 of the Stacks Project, [Tag 03KW](https://stacks.math.columbia.edu/tag/03KW). 11 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03KZ, a definition

[Tag 03KZ](https://stacks.math.columbia.edu/tag/03KZ) in the Stacks Project.

**`AlgebraicGeometry.Space.HasFiniteRelationFibersAtEveryPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean#L104). The attribute's comment: “property beta for an algebraic space”.

> **Stacks 03KZ, property `(β)` for an algebraic space.** This is property `(β)` of
> Stacks 03JX: every point of `F` satisfies the equivalent conditions of Stacks 03JU, taken
> here in the form of condition (1), finiteness of one relation fibre in some étale chart.

```lean
abbrev HasFiniteRelationFibersAtEveryPoint : Prop
```

**`AlgebraicGeometry.Space.HasPropertyBeta`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean#L149). The attribute's comment: “property beta for a morphism”.

> **Stacks 03KZ, property `(β)` for a morphism.** A morphism of algebraic spaces over `S`
> has property `(β)` when every base change of it along a morphism from a representable
> presheaf into its target has property `(β)`.

```lean
abbrev HasPropertyBeta (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsDecent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean#L157). The attribute's comment: “decent morphism”.

> **Stacks 03KZ, decent morphism.** A morphism of algebraic spaces over `S` is *decent*
> when every base change of it along a morphism from a representable presheaf into its target
> is a decent algebraic space.

```lean
abbrev IsDecent (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsReasonable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean#L180). The attribute's comment: “reasonable morphism”.

> **Stacks 03KZ, reasonable morphism.** A morphism of algebraic spaces over `S` is
> *reasonable* when every base change of it along a morphism from a representable presheaf
> into its target is a reasonable algebraic space.

```lean
abbrev IsReasonable (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsVeryReasonable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean#L188). The attribute's comment: “very reasonable morphism”.

> **Stacks 03KZ, very reasonable morphism.** A morphism of algebraic spaces over `S` is
> *very reasonable* when every base change of it along a morphism from a representable
> presheaf into its target is a very reasonable algebraic space.

```lean
abbrev IsVeryReasonable (f : X ⟶ Y) : Prop
```

## Tag 03M5, a lemma

[Tag 03M5](https://stacks.math.columbia.edu/tag/03M5) in the Stacks Project.

**`AlgebraicGeometry.Space.isVeryReasonable_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/QuasiSeparatedVeryReasonable.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/QuasiSeparatedVeryReasonable.lean#L84). The attribute's comment: “quasi-separated implies very reasonable”.

> A quasi-separated morphism of algebraic spaces over `S` is very reasonable.

```lean
theorem isVeryReasonable_of_isQuasiSeparated (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y} (hf : IsQuasiSeparated B S hS f) :
    IsVeryReasonable B S hS f
```

**`AlgebraicGeometry.Space.isVeryReasonable_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean#L91). The attribute's comment: “representable implies very reasonable”.

> **Stacks 03M5, representable implies very reasonable.** A representable morphism of
> algebraic spaces over `S` is very reasonable: each of its represented base changes is again a
> representable algebraic space, hence Zariski locally quasi-separated by the implication
> `(θ) ⇒ (ζ)` of Stacks 03JX and very reasonable by `(ζ) ⇒ (ε)`.

```lean
theorem isVeryReasonable_of_relativelyRepresentable (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) : IsVeryReasonable B S hS f
```

**`AlgebraicGeometry.Space.isDecent_of_isReasonable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean#L108). The attribute's comment: “reasonable implies decent”.

> **Stacks 03M5, reasonable implies decent.** A reasonable morphism of algebraic spaces
> over `S` is decent: each of its represented base changes is a reasonable algebraic space,
> hence satisfies property `(γ)` of Stacks 03JX by the implication `(δ) ⇒ (γ)`, which is
> decency.

```lean
theorem isDecent_of_isReasonable (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsReasonable B S hS f) :
    IsDecent B S hS f
```

**`AlgebraicGeometry.Space.hasPropertyBeta_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean#L120). The attribute's comment: “decent implies property (beta)”.

> **Stacks 03M5, decent implies property `(β)`.** A decent morphism of algebraic spaces
> over `S` has property `(β)`: each of its represented base changes is a decent algebraic
> space, hence satisfies property `(β)` of Stacks 03JX by the implication `(γ) ⇒ (β)`.

```lean
theorem hasPropertyBeta_of_isDecent (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsDecent B S hS f) :
    HasPropertyBeta B S hS f
```

**`AlgebraicGeometry.Space.isReasonable_of_isVeryReasonable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableImpliesReasonable.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/VeryReasonableImpliesReasonable.lean#L221). The attribute's comment: “very reasonable implies reasonable”.

> **Stacks 03M5, very reasonable implies reasonable.** A very reasonable morphism of
> algebraic spaces over `S` is reasonable.
>
> Both conditions of Stacks 03KZ are conditions on the represented base changes of the morphism,
> each of which is an algebraic space, so this is the implication
> `AlgebraicGeometry.Space.isReasonableSpace_of_isVeryReasonableSpace` applied base change by
> base change.

```lean
theorem isReasonable_of_isVeryReasonable {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (h : IsVeryReasonable B S hS f) : IsReasonable B S hS f
```

## Tag 0ABX, a lemma

[Tag 0ABX](https://stacks.math.columbia.edu/tag/0ABX) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecent_of_isDecentSpace_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean#L99). The attribute's comment: “decent: a morphism whose source is decent is decent”.

> **Stacks 0ABX, the decent case.** A morphism of algebraic spaces over `S` whose source is
> a decent algebraic space is a decent morphism.
>
> A morphism `g : h_T ⟶ Y` out of a representable presheaf into an algebraic space is
> representable, because the diagonal of `Y` is; hence so is the projection
> `T ×_Y X ⟶ X` of its base change, and decency passes from the target of a representable
> morphism to its source by Stacks 0ABT.

```lean
theorem isDecent_of_isDecentSpace_source (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hdec : IsDecentSpace B S hS X) :
    IsDecent B S hS f
```

**`AlgebraicGeometry.Space.hasMonomorphicFieldRepresentative_pullback_of_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L330). The attribute's comment: “decent, as condition (4) of Stacks 03JU at every represented base change”.

> **Stacks 0ABX, the decent case in the form of condition (4) of Stacks 03JU.** Let
> `f : X ⟶ Y` be a morphism of presheaves on the big fppf site over `S` with `Y` an algebraic
> space. If every point of `X` is the class of a field-valued point presenting it by a
> monomorphism, then so is every point of every base change of `f` along a morphism from a
> representable presheaf into `Y`: that base change is representable over `X`.

```lean
theorem hasMonomorphicFieldRepresentative_pullback_of_source
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hmono : ∀ x : points B S hS X, HasMonomorphicFieldRepresentative B S hS X x)
    (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y)
    (w : points B S hS (pullback g f)) :
    HasMonomorphicFieldRepresentative B S hS (pullback g f) w
```

**`AlgebraicGeometry.Space.hasPropertyBeta_of_hasMonomorphicFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L343). The attribute's comment: “property beta, from condition (4) of Stacks 03JU on the source”.

> **Stacks 0ABX, the case `(β)`.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S`. If every point of `X` is the class of a field-valued point presenting it by a
> monomorphism — condition (4) of Stacks 03JU — then `f` has property `(β)` of Stacks 03JX.

```lean
theorem hasPropertyBeta_of_hasMonomorphicFieldRepresentative
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hmono : ∀ x : points B S hS X, HasMonomorphicFieldRepresentative B S hS X x) :
    HasPropertyBeta B S hS f
```

**`AlgebraicGeometry.Space.hasPropertyBeta_of_hasFiniteRelationFibersAtEveryPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L370). The attribute's comment: “property beta”.

> **Stacks 0ABX, the case `(β)`.** A morphism of algebraic spaces over `S` whose source has
> property `(β)` of Stacks 03JX has property `(β)`.
>
> Property `(β)` of the source is condition (1) of Stacks 03JU at each of its points, which the
> equivalences of that lemma turn into condition (4).

```lean
theorem hasPropertyBeta_of_hasFiniteRelationFibersAtEveryPoint
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hXβ : HasFiniteRelationFibersAtEveryPoint B S hS X) :
    HasPropertyBeta B S hS f
```

**`AlgebraicGeometry.Space.isReasonable_of_isReasonableSpace_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L384). The attribute's comment: “reasonable”.

> **Stacks 0ABX, the reasonable case.** A morphism of algebraic spaces over `S` whose source
> is a reasonable algebraic space is a reasonable morphism.
>
> Each base change of `f` along a morphism from a representable presheaf into `Y` projects to
> `X` by a representable morphism, because the diagonal of `Y` is representable, and
> reasonableness passes to the source of a representable morphism by Stacks 0ABT.

```lean
theorem isReasonable_of_isReasonableSpace_source (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hXr : IsReasonableSpace B S hS X) :
    IsReasonable B S hS f
```

## Tag 03L0, a lemma

[Tag 03L0](https://stacks.math.columbia.edu/tag/03L0) in the Stacks Project.

**`AlgebraicGeometry.Space.hasPropertyBeta_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L277). The attribute's comment: “property beta”.

> **Stacks 03L0, property `(β)`.** Property `(β)` of a morphism of algebraic spaces over `S`
> is preserved by arbitrary base change: a base change of the base change of `f : X ⟶ Y` along
> `g : Y' ⟶ Y` is a base change of `f`.

```lean
theorem hasPropertyBeta_baseChange (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasPropertyBeta B S hS f) : HasPropertyBeta B S hS (pullback.fst g f)
```

**`AlgebraicGeometry.Space.isDecent_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L286). The attribute's comment: “decent”.

> **Stacks 03L0, decent.** Decency of a morphism of algebraic spaces over `S` is preserved
> by arbitrary base change: a base change of the base change of `f : X ⟶ Y` along `g : Y' ⟶ Y`
> is a base change of `f`.

```lean
theorem isDecent_baseChange (f : X ⟶ Y) (g : Y' ⟶ Y) (hf : IsDecent B S hS f) :
    IsDecent B S hS (pullback.fst g f)
```

**`AlgebraicGeometry.Space.isReasonable_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L294). The attribute's comment: “reasonable”.

> **Stacks 03L0, reasonable.** Reasonableness of a morphism of algebraic spaces over `S` is
> preserved by arbitrary base change: a base change of the base change of `f : X ⟶ Y` along
> `g : Y' ⟶ Y` is a base change of `f`.

```lean
theorem isReasonable_baseChange (f : X ⟶ Y) (g : Y' ⟶ Y) (hf : IsReasonable B S hS f) :
    IsReasonable B S hS (pullback.fst g f)
```

## Tag 0ABY, a lemma

[Tag 0ABY](https://stacks.math.columbia.edu/tag/0ABY) in the Stacks Project.

**`AlgebraicGeometry.Space.hasMonomorphicFieldRepresentative_of_target_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L404). The attribute's comment: “property beta, as condition (4) of Stacks 03JU at every point”.

> **Stacks 0ABY, the case `(β)` in the form of condition (4) of Stacks 03JU.** Let
> `f : X ⟶ Y` be a morphism of presheaves on the big fppf site over `S`. If every point of `Y`
> is the class of a field-valued point presenting it by a monomorphism, and if the same holds at
> every point of every base change of `f` along a morphism from a representable presheaf into
> `Y`, then it holds at every point of `X`.
>
> This is the source's argument: a monomorphic representative `Spec k ⟶ Y` of the image of `x`
> is a morphism out of a representable presheaf, the point `x` lifts to the base change
> `Spec k ×_Y X` by Stacks 03H4, and a monomorphic representative there composes with the
> projection — a monomorphism, being a base change of one — to a monomorphic representative
> of `x`.

```lean
theorem hasMonomorphicFieldRepresentative_of_target_of_baseChange (f : X ⟶ Y)
    (hY : ∀ y : points B S hS Y, HasMonomorphicFieldRepresentative B S hS Y y)
    (hf : ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y)
      (w : points B S hS (pullback g f)),
      HasMonomorphicFieldRepresentative B S hS (pullback g f) w)
    (x : points B S hS X) :
    HasMonomorphicFieldRepresentative B S hS X x
```

**`AlgebraicGeometry.Space.isDecentSpace_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean#L102). The attribute's comment: “decent”.

> **Stacks 0ABY, decent.** If a morphism of algebraic spaces over `S` is decent and its
> target is decent, then its source is decent.
>
> A point `x` of the source maps to a point of the target, which decency of the target presents
> by a quasi-compact monomorphism `g : Spec k ⟶ Y`. The point `x` and the tautological point of
> `Spec k` have the same image in `Y`, so they come from a point of `Spec k ×_Y X`; that fibre
> product is decent because the morphism is, so that point is presented by a quasi-compact
> monomorphism, and composing it with the projection to `X` — a base change of `g`, hence again a
> quasi-compact monomorphism — presents `x`.

```lean
theorem isDecentSpace_of_isDecent (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hYdecent : IsDecentSpace B S hS Y) (hfdecent : IsDecent B S hS f) :
    IsDecentSpace B S hS X
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_isReasonable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeReasonablePermanence.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeReasonablePermanence.lean#L250). The attribute's comment: “reasonable”.

> **Stacks 0ABY, reasonable.** If a morphism of algebraic spaces over `S` is reasonable and
> its target is reasonable, then its source is reasonable.
>
> A jointly surjective family of étale charts with universally bounded fibres for the target,
> Stacks 03JT, pulls back to a family of fibre products over the source, each of which is a
> reasonable algebraic space because the morphism is reasonable; a family of charts for each of
> those, composed with the projections to the source, is again jointly surjective and étale,
> and the fibres of the composites remain universally bounded.

```lean
theorem isReasonableSpace_of_isReasonable (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hYr : IsReasonableSpace B S hS Y)
    (hf : IsReasonable B S hS f) :
    IsReasonableSpace B S hS X
```

## Tag 03L1, a lemma

[Tag 03L1](https://stacks.math.columbia.edu/tag/03L1) in the Stacks Project.

**`AlgebraicGeometry.Space.hasPropertyBeta_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L466). The attribute's comment: “property beta”.

> **Stacks 03L1, property `(β)`.** Property `(β)` of a morphism of algebraic spaces over `S`
> is preserved by composition.
>
> The base change of `f ≫ g` along `k : T ⟶ Z` is the base change of `f` along the projection
> `T ×_Z Y ⟶ Y`, viewed over `T ×_Z Y`; that projection has property `(β)` by Stacks 03L0 and
> `T ×_Z Y` has it because `g` does, so Stacks 0ABY applies.

```lean
theorem hasPropertyBeta_comp (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasPropertyBeta B S hS f) (hg : HasPropertyBeta B S hS g) :
    HasPropertyBeta B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isDecent_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditions.lean#L485). The attribute's comment: “decent”.

> **Stacks 03L1, decent.** Decency of a morphism of algebraic spaces over `S` is preserved by
> composition.
>
> The base change of `f ≫ g` along `k : T ⟶ Z` is the base change of `f` along the projection
> `T ×_Z Y ⟶ Y`, viewed over `T ×_Z Y`; that projection is decent by Stacks 03L0 and `T ×_Z Y`
> is decent because `g` is, so Stacks 0ABY applies.

```lean
theorem isDecent_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsDecent B S hS f) (hg : IsDecent B S hS g) :
    IsDecent B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isReasonable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeReasonablePermanence.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeReasonablePermanence.lean#L349). The attribute's comment: “reasonable”.

> **Stacks 03L1, reasonable.** Reasonableness of a morphism of algebraic spaces over `S` is
> preserved by composition.
>
> The base change of `f ≫ g` along `k : T ⟶ Z` is the base change of `f` along the projection
> `T ×_Z Y ⟶ Y`, viewed over `T ×_Z Y`; that projection is reasonable by Stacks 03L0 and
> `T ×_Z Y` is reasonable because `g` is, so Stacks 0ABY applies.

```lean
theorem isReasonable_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsReasonable B S hS f) (hg : IsReasonable B S hS g) :
    IsReasonable B S hS (f ≫ g)
```

## Tag 0ABZ, a lemma

[Tag 0ABZ](https://stacks.math.columbia.edu/tag/0ABZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean#L100). The attribute's comment: “decent”.

> **Stacks 0ABZ, decent.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of algebraic spaces
> over `S`. If `X` and `Z` are decent algebraic spaces, then so is `X ×_Y Z`.
>
> Decency of `X` makes `f` a decent morphism by Stacks 0ABX, its base change `Z ×_Y X ⟶ Z` is
> decent by Stacks 03L0, and decency of `Z` together with that of the base change gives decency
> of `Z ×_Y X` by Stacks 0ABY.

```lean
theorem isDecentSpace_pullback (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hXdec : IsDecentSpace B S hS X) (hZdec : IsDecentSpace B S hS Z) :
    IsDecentSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.Space.isReasonableSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean#L116). The attribute's comment: “reasonable”.

> **Stacks 0ABZ, reasonable.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of algebraic
> spaces over `S`. If `X` and `Z` are reasonable algebraic spaces, then so is `X ×_Y Z`.
>
> Reasonableness of `X` makes `f` a reasonable morphism by Stacks 0ABX, its base change
> `Z ×_Y X ⟶ Z` is reasonable by Stacks 03L0, and reasonableness of `Z` together with that of
> the base change gives reasonableness of `Z ×_Y X` by Stacks 0ABY.

```lean
theorem isReasonableSpace_pullback (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hXr : IsReasonableSpace B S hS X) (hZr : IsReasonableSpace B S hS Z) :
    IsReasonableSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreProductConditions.lean#L133). The attribute's comment: “property beta”.

> **Stacks 0ABZ, property `(β)`.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of algebraic
> spaces over `S`. If `X` and `Z` have property `(β)` of Stacks 03JX, then so does `X ×_Y Z`.
>
> Property `(β)` of `X` makes `f` a morphism with property `(β)` by Stacks 0ABX, its base change
> `Z ×_Y X ⟶ Z` has property `(β)` by Stacks 03L0, and property `(β)` of `Z` together with that
> of the base change gives property `(β)` of `Z ×_Y X` by Stacks 0ABY.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_pullback (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hXβ : HasFiniteRelationFibersAtEveryPoint B S hS X)
    (hZβ : HasFiniteRelationFibersAtEveryPoint B S hS Z) :
    HasFiniteRelationFibersAtEveryPoint B S hS (pullback f g)
```

## Tag 03L2, a lemma

[Tag 03L2](https://stacks.math.columbia.edu/tag/03L2) in the Stacks Project.

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_surjective_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyBetaDescent.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyBetaDescent.lean#L70). The attribute's comment: “property (beta)”.

> **Stacks 03L2, property `(β)`.** Let `f : X ⟶ Y` be a quasi-compact étale morphism of
> algebraic spaces over `S` which is surjective on points. If `X` has property `(β)` of
> Stacks 03JX — every point has a field-valued representative with a finite relation fibre —
> then so does `Y`.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_of_surjective_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hq : IsQuasiCompact B S hS f)
    (he : IsEtale B S hS f) (hs : Function.Surjective (pointsMap B S hS X f))
    (hβ : HasFiniteRelationFibersAtEveryPoint B S hS X) :
    HasFiniteRelationFibersAtEveryPoint B S hS Y
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_surjective_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableEtaleDescent.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableEtaleDescent.lean#L96). The attribute's comment: “reasonable”.

> **Stacks 03L2, reasonable.** Let `f` be a quasi-compact morphism of algebraic spaces over
> `S` which is surjective on points. If its source is reasonable, then so is its target.
>
> An affine étale chart of the target is dominated, after base change along `f`, by an affine
> étale chart of the source, and the bound reasonableness of the source gives the latter bounds
> the degrees of the fibres of the former. Étaleness of `f`, which Stacks 03L2 also assumes, is
> not used.

```lean
theorem isReasonableSpace_of_surjective_isQuasiCompact
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (hsurj : Function.Surjective (pointsMap B S hS X f))
    (hXr : IsReasonableSpace B S hS X) :
    IsReasonableSpace B S hS Y
```

**`AlgebraicGeometry.Space.hasQuasiCompactFieldRepresentative_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean#L151). The attribute's comment: “condition (5) of Stacks 03JV at every point of the target”.

> **Stacks 03L2, condition (5) of Stacks 03JV at every point of the target.** Let `f` be a
> quasi-compact morphism of algebraic spaces over `S` which is surjective on points. If the
> source is decent, then every point of the target has a quasi-compact field-valued
> representative.
>
> A point of the target is the image of a point of the source, which decency of the source
> presents by a quasi-compact morphism from the spectrum of a field; composing it with `f` again
> gives a quasi-compact morphism, and it presents the chosen point of the target.
>
> Decency of the target asks for a representative which is in addition a monomorphism, and
> obtaining one from this is the equivalence of conditions (4) and (5) of Stacks 03JV. Étaleness
> of `f`, which Stacks 03L2 also assumes, is not used.

```lean
theorem hasQuasiCompactFieldRepresentative_of_isDecentSpace (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (hsurj : Function.Surjective (pointsMap B S hS X f))
    (hXdecent : IsDecentSpace B S hS X) (y : points B S hS Y) :
    HasQuasiCompactFieldRepresentative B S hS Y y
```

**`AlgebraicGeometry.Space.isDecentSpace_of_surjective_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeDecency.lean#L171). The attribute's comment: “decent”.

> **Stacks 03L2, decent.** Let `f` be a quasi-compact morphism of algebraic spaces over `S`
> which is surjective on points. If its source is decent, then so is its target.
>
> Every point of the target acquires a quasi-compact field-valued representative by pushing one
> forward along `f`, and the implication from condition (5) to condition (4) of Stacks 03JV
> makes that representative a monomorphism. Étaleness of `f`, which Stacks 03L2 also assumes,
> is not used.

```lean
theorem isDecentSpace_of_surjective_isQuasiCompact (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (hsurj : Function.Surjective (pointsMap B S hS X f))
    (hXdecent : IsDecentSpace B S hS X) :
    IsDecentSpace B S hS Y
```

## Tag 03L3, a lemma

[Tag 03L3](https://stacks.math.columbia.edu/tag/03L3) in the Stacks Project.

**`AlgebraicGeometry.Space.hasPropertyBeta_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L603). The attribute's comment: “property beta”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent:
> `(1)` `f` has property `(β)` in the sense of Stacks 03KZ;
> `(2)` for every affine object `Z` of the site and every `Z ⟶ Y`, the base change
> `Z ×_Y X ⟶ Z` has property `(β)`;
> `(3)` for every such `Z ⟶ Y` the algebraic space `Z ×_Y X` has property `(β)`;
> `(4)` there is a Zariski covering of `Y` by open subspaces `Yᵢ` with every restriction
> `Yᵢ ×_Y X ⟶ Yᵢ` having property `(β)`;
> `(5)` there is a scheme of the site with a surjective étale morphism `V ⟶ Y` such that
> `V ×_Y X ⟶ V` has property `(β)`.

```lean
theorem hasPropertyBeta_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [HasPropertyBeta B S hS f,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            HasPropertyBeta B S hS (pullback.fst g f),
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            HasFiniteRelationFibersAtEveryPoint B S hS (pullback g f),
        ∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, HasPropertyBeta B S hS (pullback.fst (Yᵢ i).ι f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y), IsSurjective B S hS g ∧
          IsEtale B S hS g ∧ HasPropertyBeta B S hS (pullback.fst g f)]
```

**`AlgebraicGeometry.Space.isVeryReasonable_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L630). The attribute's comment: “very reasonable”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent:
> `(1)` `f` is very reasonable in the sense of Stacks 03KZ;
> `(2)` for every affine object `Z` of the site and every `Z ⟶ Y`, the base change
> `Z ×_Y X ⟶ Z` is very reasonable;
> `(3)` for every such `Z ⟶ Y` the algebraic space `Z ×_Y X` is very reasonable;
> `(4)` there is a Zariski covering of `Y` by open subspaces `Yᵢ` with every restriction
> `Yᵢ ×_Y X ⟶ Yᵢ` very reasonable.

```lean
theorem isVeryReasonable_tfae (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsVeryReasonable B S hS f,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsVeryReasonable B S hS (pullback.fst g f),
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsVeryReasonableSpace B S hS (pullback g f),
        ∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, IsVeryReasonable B S hS (pullback.fst (Yᵢ i).ι f)]
```

**`AlgebraicGeometry.Space.isDecent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L652). The attribute's comment: “decent, conditions (1) to (4)”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent:
> `(1)` `f` is decent in the sense of Stacks 03KZ;
> `(2)` for every affine object `Z` of the site and every `Z ⟶ Y`, the base change
> `Z ×_Y X ⟶ Z` is decent;
> `(3)` for every such `Z ⟶ Y` the algebraic space `Z ×_Y X` is decent;
> `(4)` there is a Zariski covering of `Y` by open subspaces `Yᵢ` with every restriction
> `Yᵢ ×_Y X ⟶ Yᵢ` decent.

```lean
theorem isDecent_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsDecent B S hS f,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsDecent B S hS (pullback.fst g f),
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsDecentSpace B S hS (pullback g f),
        ∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, IsDecent B S hS (pullback.fst (Yᵢ i).ι f)]
```

**`AlgebraicGeometry.Space.isDecent_tfae_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 671](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L671). The attribute's comment: “decent”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the four conditions of
> `AlgebraicGeometry.Space.isDecent_tfae` are also equivalent to
> `(5)` there is a scheme of the site with a surjective étale morphism `V ⟶ Y` such that
> `V ×_Y X ⟶ V` is decent.

```lean
theorem isDecent_tfae_etale (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsDecent B S hS f,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsDecent B S hS (pullback.fst g f),
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsDecentSpace B S hS (pullback g f),
        ∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, IsDecent B S hS (pullback.fst (Yᵢ i).ι f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y), IsSurjective B S hS g ∧
          IsEtale B S hS g ∧ IsDecent B S hS (pullback.fst g f)]
```

**`AlgebraicGeometry.Space.isReasonable_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 700](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L700). The attribute's comment: “reasonable”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent:
> `(1)` `f` is reasonable in the sense of Stacks 03KZ;
> `(2)` for every affine object `Z` of the site and every `Z ⟶ Y`, the base change
> `Z ×_Y X ⟶ Z` is reasonable;
> `(3)` for every such `Z ⟶ Y` the algebraic space `Z ×_Y X` is reasonable;
> `(4)` there is a Zariski covering of `Y` by open subspaces `Yᵢ` with every restriction
> `Yᵢ ×_Y X ⟶ Yᵢ` reasonable;
> `(5)` there is a scheme of the site with a surjective étale morphism `V ⟶ Y` such that
> `V ×_Y X ⟶ V` is reasonable.

```lean
theorem isReasonable_tfae (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsReasonable B S hS f,
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsReasonable B S hS (pullback.fst g f),
        ∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
            IsReasonableSpace B S hS (pullback g f),
        ∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, IsReasonable B S hS (pullback.fst (Yᵢ i).ι f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y), IsSurjective B S hS g ∧
          IsEtale B S hS g ∧ IsReasonable B S hS (pullback.fst g f)]
```

## Tag 03L4, a remark

[Tag 03L4](https://stacks.math.columbia.edu/tag/03L4) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isDecent_of_isReasonable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean#L108), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeConditionComparisons.lean#L139) (StacksFrontier): “Remark 68.17.10, which states no proposition of its own: its comparative sentence, that being reasonable is a bit stronger than being decent, is sharp only as the implication `reasonable ⇒ decent` of Stacks 03M5, which is this theorem.”.
- [`AlgebraicGeometry.Space.hasPropertyBeta_tfae`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L603), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 728](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L728) (StacksFrontier): “Remark 68.17.10, which states no proposition of its own: its one mathematical sentence, that a morphism has one of the conditions of Stacks 03KZ when, in the source's words '(very) loosely speaking', the fibres of the morphism do, is disclaimed there as loose and is sharp only as Stacks 03L3 — here the case of property `(β)`.”.
- [`AlgebraicGeometry.Space.isVeryReasonable_tfae`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L630), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L734) (StacksFrontier): “Remark 68.17.10, which states no proposition of its own: its one mathematical sentence, that a morphism has one of the conditions of Stacks 03KZ when, in the source's words '(very) loosely speaking', the fibres of the morphism do, is disclaimed there as loose and is sharp only as Stacks 03L3 — here the case of very reasonableness.”.
- [`AlgebraicGeometry.Space.isDecent_tfae_etale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L671), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L740) (StacksFrontier): “Remark 68.17.10, which states no proposition of its own: its one mathematical sentence, that a morphism has one of the conditions of Stacks 03KZ when, in the source's words '(very) loosely speaking', the fibres of the morphism do, is disclaimed there as loose and is sharp only as Stacks 03L3 — here the case of decency.”.
- [`AlgebraicGeometry.Space.isReasonable_tfae`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L700), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean, line 746](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RelativeLocalCriteria.lean#L746) (StacksFrontier): “Remark 68.17.10, which states no proposition of its own: its one mathematical sentence, that a morphism has one of the conditions of Stacks 03KZ when, in the source's words '(very) loosely speaking', the fibres of the morphism do, is disclaimed there as loose and is sharp only as Stacks 03L3 — here the case of reasonableness.”.

## Tag 03M6, a lemma

[Tag 03M6](https://stacks.math.columbia.edu/tag/03M6) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_iff_valuativeCriterion_existence_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyClosedValuative.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyClosedValuative.lean#L393).

> **Stacks 03M6.** A quasi-compact morphism of algebraic spaces over `S` which is decent as a
> morphism is universally closed exactly when it satisfies the existence part of the valuative
> criterion.
>
> A valuative square for `f` has its bottom edge `Spec R ⟶ Y`, so it is a valuative square for
> the base change `X ×_Y Spec R ⟶ Spec R`, which is quasi-compact and has decent source; that
> base change is universally closed, hence satisfies the existence part by Stacks 03KJ, and a
> dominating extension solving the square there solves the original one after composing the lift
> with the projection to `X`.

```lean
theorem universallyClosed_iff_valuativeCriterion_existence_of_isDecent
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (hdecent : IsDecent B S hS f) :
    UniversallyClosed B S hS f ↔ ValuativeCriterion.Existence f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.17, Tag 03KW](https://stacks.math.columbia.edu/tag/03KW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
