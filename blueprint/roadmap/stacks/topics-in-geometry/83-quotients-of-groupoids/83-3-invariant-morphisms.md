---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsInvariant, AlgebraicGeometry.Space.IsGroupInvariant, AlgebraicGeometry.Space.invariant_iff_factors_through_quotientSheaf, AlgebraicGeometry.GroupoidInAlgebraicSpaces.overInvariantTarget, AlgebraicGeometry.GroupoidInAlgebraicSpaces.baseChangedPreRelation_isBaseChange, AlgebraicGeometry.Space.exists_inducedAction_of_baseChangedPreRelation, AlgebraicGeometry.Space.baseChangedPreRelation, AlgebraicGeometry.Space.isPreEquivalenceRelation_baseChangedPreRelation
statement: formalized
proof: formalized
---

# 83.3 Invariant morphisms

Section 83.3 of the Stacks Project, [Tag 048D](https://stacks.math.columbia.edu/tag/048D). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 048E, a definition

[Tag 048E](https://stacks.math.columbia.edu/tag/048E) in the Stacks Project.

**`AlgebraicGeometry.Space.IsInvariant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean#L93). The attribute's comment: “R-invariant”.

> A morphism `φ` out of `U` is *invariant* under a pre-relation `j : R ⟶ U ×_Z U` when it
> identifies the target and the source of every arrow of `j`.

```lean
noncomputable abbrev IsInvariant {C : Type*} [Category C] {Z : C}
    [HasBinaryProducts (Over Z)] {R U : Over Z} {X : C}
    (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsGroupInvariant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean#L101). The attribute's comment: “G-invariant”. References: SGA 3 IV (3.2.1), “special case”.

> A morphism `φ` out of an object `U` carrying an action of a group algebraic space `G` is
> *invariant* when acting does not change its value.

```lean
noncomputable abbrev IsGroupInvariant
    (G : Over B.obj) {U X : Over B.obj} [GrpObj G] [ModObj G U]
    (φ : U ⟶ X) : Prop
```

## Tag 048F, a lemma

[Tag 048F](https://stacks.math.columbia.edu/tag/048F) in the Stacks Project.

**`AlgebraicGeometry.Space.invariant_iff_factors_through_quotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientSheafBaseChange.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientSheafBaseChange.lean#L75).

> **Stacks 048F.** A morphism from `U` to a sheaf is invariant under a pre-relation `j` if
> and only if it factors through the canonical projection of `U` onto the quotient sheaf
> `U/R`.

```lean
theorem invariant_iff_factors_through_quotientSheaf (j : PreRelation R U)
    (hX : Presheaf.IsSheaf (BigFppfOver.topology site S hS) X) (φ : U.left ⟶ X) :
    IsInvariant j φ ↔
      ∃ d : quotientSheaf j ⟶ baseSheaf hX, toQuotientSheaf j ≫ d.hom = φ
```

## Tag 048G, a lemma

[Tag 048G](https://stacks.math.columbia.edu/tag/048G) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.overInvariantTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupoidBaseChange.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupoidBaseChange.lean#L76). The attribute's comment: “groupoid\_over\_x”.

> **Stacks 048G.** A morphism out of the object space of a groupoid in algebraic spaces
> which is invariant under the pre-relation of the groupoid makes the groupoid a groupoid over
> its target: the object and arrow spaces, the source, the target and the composition are
> unchanged, and the new structure morphism on objects is the invariant morphism itself.

```lean
noncomputable def overInvariantTarget (G : GroupoidInAlgebraicSpaces C S hS B)
    {X : AlgebraicSpaces C S hS} (XtoB : X ⟶ B) (φ : G.objects ⟶ X)
    (_hφB : φ ≫ XtoB = G.objectsToBase)
    (hφ : Space.IsInvariant (Space.groupoidPreRelation G) φ.hom) :
    { H : GroupoidInAlgebraicSpaces C S hS X //
      H.toGroupoidInFunctors = G.toGroupoidInFunctors ∧
      ∃ hobj : H.objects = G.objects, eqToHom hobj.symm ≫ H.objectsToBase = φ }
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.baseChangedPreRelation_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupoidBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupoidBaseChange.lean#L214). The attribute's comment: “base\_changed\_groupoid\_relation”.

> **Stacks 048G.** The base change of the pre-relation of a groupoid in algebraic spaces
> along a morphism to an invariant target is the pre-relation of the base change of the
> groupoid over that target: the object and the arrow spaces agree, canonically through the two
> projections of the pullbacks, and the identifications intertwine the source and the target
> maps.

```lean
theorem baseChangedPreRelation_isBaseChange (G : GroupoidInAlgebraicSpaces C S hS B)
    {X X' : AlgebraicSpaces C S hS} (XtoB : X ⟶ B) (φ : G.objects ⟶ X)
    (hφB : φ ≫ XtoB = G.objectsToBase)
    (hφ : Space.IsInvariant (Space.groupoidPreRelation G) φ.hom)
    (f : X' ⟶ X) :
    let H := (overInvariantTarget G XtoB φ hφB hφ).val
    let bc := Space.baseChange H f
    let j := Space.groupoidPreRelation G
    let j' := (Space.baseChangedPreRelation j φ.hom f.hom hφ).val
    ∃ (hobj : H.objects = G.objects) (harr : H.arrows = G.arrows)
      (α : (Space.baseChangedObject (U := Over.mk G.objectsToBase.hom) φ.hom f.hom).left ≅
          bc.groupoid.objects.obj)
      (β : (Space.baseChangedArrows j φ.hom f.hom).left ≅ bc.groupoid.arrows.obj),
      (α.hom ≫ bc.groupoid.objectsToBase.hom = pullback.fst f.hom φ.hom) ∧
      (β.hom ≫ bc.groupoid.arrowsToBase.hom =
        pullback.fst f.hom (j.target.left ≫ φ.hom)) ∧
      (α.hom ≫ bc.projection.mapObjects ≫ (eqToHom hobj).hom =
        pullback.snd f.hom φ.hom) ∧
      (β.hom ≫ bc.projection.mapArrows ≫ (eqToHom harr).hom =
        pullback.snd f.hom (j.target.left ≫ φ.hom)) ∧
      (j'.source.left ≫ α.hom = β.hom ≫ bc.groupoid.source.hom) ∧
      (j'.target.left ≫ α.hom = β.hom ≫ bc.groupoid.target.hom)
```

**`AlgebraicGeometry.Space.exists_inducedAction_of_baseChangedPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InducedGroupAction.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InducedGroupAction.lean#L75). The attribute's comment: “induced\_group\_action”.

> An invariant base change of an action pre-relation is again an action
> pre-relation. The comparison of arrow spaces respects the original arrows and
> both endpoints, while the induced action fixes the new-base coordinate.

```lean
theorem exists_inducedAction_of_baseChangedPreRelation
    (hsource : j.source = snd G U) (htarget : j.target = γ[G,U])
    (hφ : IsInvariant j φ) :
    ∃ action : ModObj G (baseChangedObject φ f),
      letI : ModObj G (baseChangedObject φ f) := action
      let U' := baseChangedObject φ f
      let R' := baseChangedArrows j φ f
      let j' := (baseChangedPreRelation j φ f hφ).val
      let q : U' ⟶ U := Over.homMk (pullback.snd f φ) (by rfl)
      let toOriginal : G ⊗ U' ⟶ G ⊗ U :=
        lift (fst G U') (snd G U' ≫ q)
      ((γ[G, U']).left ≫ pullback.fst f φ =
        (snd G U').left ≫ pullback.fst f φ) ∧
      (γ[G, U'] ≫ q = toOriginal ≫ γ[G,U]) ∧
    ∃ e : G ⊗ U' ≅ R',
        (e.hom.left ≫ pullback.snd f (j.target.left ≫ φ) = toOriginal.left) ∧
        (e.hom ≫ j'.source = snd G U') ∧
        (e.hom ≫ j'.target = γ[G, U'])
```

**`AlgebraicGeometry.Space.baseChangedPreRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L134). The attribute's comment: “base\_changed\_pre\_relation”.

> **Stacks 048G** and **Stacks 048H.** The canonical pre-relation on the base changes of the
> object and of the arrow space of an invariant pre-relation. Its target and source maps are
> fixed by their composites with the two projections of the pullbacks: both preserve the
> component in `X'`, and on the component in `U` they are the target and the source of `j`.

```lean
noncomputable def baseChangedPreRelation (j : PreRelation R U) (φ : U.left ⟶ X) (f : X' ⟶ X)
    (hφ : IsInvariant j φ) :
    { j' : PreRelation (baseChangedArrows j φ f) (baseChangedObject φ f) //
      ((j'.target.left ≫ pullback.fst f φ =
          pullback.fst f (j.target.left ≫ φ)) ∧
        (j'.target.left ≫ pullback.snd f φ =
          pullback.snd f (j.target.left ≫ φ) ≫ j.target.left)) ∧
      ((j'.source.left ≫ pullback.fst f φ =
          pullback.fst f (j.target.left ≫ φ)) ∧
        (j'.source.left ≫ pullback.snd f φ =
          pullback.snd f (j.target.left ≫ φ) ≫ j.source.left)) }
```

**`AlgebraicGeometry.Space.isPreEquivalenceRelation_baseChangedPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L319). The attribute's comment: “pre\_equivalence\_preserved”.

> **Stacks 048G.** Base change along an invariant morphism preserves the pointwise
> equivalence property of a pre-relation.

```lean
theorem isPreEquivalenceRelation_baseChangedPreRelation (j : PreRelation R U)
    (φ : U.left ⟶ X) (f : X' ⟶ X) (hφ : IsInvariant j φ)
    (hj : IsPreEquivalenceRelation j) :
    IsPreEquivalenceRelation (baseChangedPreRelation j φ f hφ).val
```

**`AlgebraicGeometry.Space.mono_baseChangedPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L332). The attribute's comment: “relation\_preserved”.

> **Stacks 048G.** Base change along an invariant morphism preserves relations, that is
> monomorphy of the map to the product.

```lean
theorem mono_baseChangedPreRelation (j : PreRelation R U) (φ : U.left ⟶ X) (f : X' ⟶ X)
    (hφ : IsInvariant j φ) [Mono j] :
    Mono (baseChangedPreRelation j φ f hφ).val
```

**`AlgebraicGeometry.Space.isEquivalenceRelation_baseChangedPreRelation`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L344). The attribute's comment: “equivalence\_preserved”.

> **Stacks 048G.** Base change along an invariant morphism preserves equivalence relations:
> the base-changed pre-relation of an invariant equivalence relation is again an internal
> categorical equivalence relation.

```lean
instance isEquivalenceRelation_baseChangedPreRelation (j : PreRelation R U) (φ : U.left ⟶ X)
    (f : X' ⟶ X) (hφ : IsInvariant j φ)
    [IsEquivalenceRelation j.target j.source] :
    IsEquivalenceRelation
      (PreRelation.target (baseChangedPreRelation j φ f hφ).val)
      (PreRelation.source (baseChangedPreRelation j φ f hφ).val)
```

## Tag 048H, a definition

[Tag 048H](https://stacks.math.columbia.edu/tag/048H) in the Stacks Project.

**`AlgebraicGeometry.Space.baseChangedPreRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L134). The attribute's comment: “base change of the pre-relation”.

> **Stacks 048G** and **Stacks 048H.** The canonical pre-relation on the base changes of the
> object and of the arrow space of an invariant pre-relation. Its target and source maps are
> fixed by their composites with the two projections of the pullbacks: both preserve the
> component in `X'`, and on the component in `U` they are the target and the source of `j`.

```lean
noncomputable def baseChangedPreRelation (j : PreRelation R U) (φ : U.left ⟶ X) (f : X' ⟶ X)
    (hφ : IsInvariant j φ) :
    { j' : PreRelation (baseChangedArrows j φ f) (baseChangedObject φ f) //
      ((j'.target.left ≫ pullback.fst f φ =
          pullback.fst f (j.target.left ≫ φ)) ∧
        (j'.target.left ≫ pullback.snd f φ =
          pullback.snd f (j.target.left ≫ φ) ≫ j.target.left)) ∧
      ((j'.source.left ≫ pullback.fst f φ =
          pullback.fst f (j.target.left ≫ φ)) ∧
        (j'.source.left ≫ pullback.snd f φ =
          pullback.snd f (j.target.left ≫ φ) ≫ j.source.left)) }
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.IsFlat`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantBaseChange.lean#L360) (StacksFrontier): “flat base change”.

## Tag 0DTF, a lemma

[Tag 0DTF](https://stacks.math.columbia.edu/tag/0DTF) in the Stacks Project.

**`AlgebraicGeometry.Space.quotientSheaf_isPullback_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientSheafBaseChange.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientSheafBaseChange.lean#L250).

> **Stacks 0DTF.** The quotient sheaf of the base change of an invariant pre-relation along
> `f : X' ⟶ X` is the fibre product of `X'` and the original quotient sheaf over `X`. The three
> canonical maps are specified by their composites with the quotient projections.

```lean
theorem quotientSheaf_isPullback_baseChange (j : PreRelation R U)
    (hX : Presheaf.IsSheaf (BigFppfOver.topology site S hS) X)
    (hX' : Presheaf.IsSheaf (BigFppfOver.topology site S hS) X')
    (φ : U.left ⟶ X) (f : X' ⟶ X) (hφ : IsInvariant j φ) :
    let j' := (baseChangedPreRelation j φ f hφ).val
    ∃ (qToX : quotientSheaf j ⟶ baseSheaf hX)
      (q'ToX' : quotientSheaf j' ⟶ baseSheaf hX')
      (q'ToQ : quotientSheaf j' ⟶ quotientSheaf j),
      (toQuotientSheaf j ≫ qToX.hom = φ) ∧
      (toQuotientSheaf j' ≫ q'ToX'.hom = pullback.fst f φ) ∧
      (toQuotientSheaf j' ≫ q'ToQ.hom = pullback.snd f φ ≫ toQuotientSheaf j) ∧
      IsPullback q'ToX' q'ToQ ⟨f⟩ qToX
```

## Tag 0DTG, a lemma

[Tag 0DTG](https://stacks.math.columbia.edu/tag/0DTG) in the Stacks Project.

**`AlgebraicGeometry.Stack.baseChangeQuotientStackSquare_isTwoFibreProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/BaseChangeQuotientStackComparisonFibreFull.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/BaseChangeQuotientStackComparisonFibreFull.lean#L356).

> **Stacks 0DTG, the 2-fibre product.** For a groupoid in algebraic spaces `(U, R, s, t, c)`
> over an algebraic space `B` over a scheme `S` of a big fppf site, an `R`-invariant morphism
> `φ : U ⟶ X` of algebraic spaces over `B` and a morphism `g : X' ⟶ X` of algebraic spaces over
> `B`, the 2-commutative square
>
>     [U'/R'] ---> [U/R]
>       |            |
>       v            v
>      𝒮_{X'} ---> 𝒮_X
>
> of `AlgebraicGeometry.Stack.baseChangeQuotientStackSquare` is a 2-fibre product (Stacks 003Q),
> where `(U', R', s', t', c')` is the base change of Stacks 048G.
>
> Its comparison 1-morphism is faithful by
> `AlgebraicGeometry.Stack.faithful_comparison`, locally essentially surjective on fibres by
> `AlgebraicGeometry.Stack.locallyEssSurjOnFibers_baseChangeQuotientStackComparison` and full by
> `AlgebraicGeometry.Stack.full_baseChangeQuotientStackComparison`.

```lean
noncomputable def baseChangeQuotientStackSquare_isTwoFibreProduct :
    Bicategory.IsTwoFibreProduct
      (baseChangeQuotientStackSquare.{u, w} G XtoB X'toB g hg φ hφB hφ)
```

**`AlgebraicGeometry.Stack.baseChangeQuotientStackSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/BaseChangeQuotientStackSquare.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/BaseChangeQuotientStackSquare.lean#L257). The attribute's comment: “the displayed square and its 2-commutativity”.

> **Stacks 0DTG, the displayed square.** For a groupoid in algebraic spaces `(U, R, s, t, c)`
> over an algebraic space `B` over a scheme `S` of a big fppf site, an `R`-invariant morphism
> `φ : U ⟶ X` of algebraic spaces over `B` and a morphism `g : X' ⟶ X` of algebraic spaces over
> `B`, the square
>
>     [U'/R'] ---> [U/R]
>       |            |
>       v            v
>      𝒮_{X'} ---> 𝒮_X
>
> of stacks in groupoids over the big fppf site 2-commutes, where `(U', R', s', t', c')` is the
> base change of Stacks 048G. It is a 2-commutative diagram over the cospan in the sense of
> Stacks 003O, with its filling 2-isomorphism an identity.
>
> The further assertion of Stacks 0DTG, that this square is a 2-fibre product, is
> `AlgebraicGeometry.Stack.baseChangeQuotientStackSquare_isTwoFibreProduct`; hence the qualifier on
> the tag here.

```lean
noncomputable def baseChangeQuotientStackSquare :
    let J := BigFppfOver.topology C S hS
    let Q : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨quotientStack (invariantTargetGroupoid G XtoB φ hφB hφ),
        isStackInGroupoids_quotientStack _⟩
    let SX : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory X, isStackInGroupoids_liftedFibredCategory X⟩
    let SX' : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory X', isStackInGroupoids_liftedFibredCategory X'⟩
    Bicategory.TwoCommSq
      (Bicategory.InducedBicategory.mkHom
        (liftedQuotientStackToBase (invariantTargetGroupoid G XtoB φ hφB hφ)) : Q ⟶ SX)
      (Bicategory.InducedBicategory.mkHom (liftedAssociatedMap g) : SX' ⟶ SX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.3, Tag 048D](https://stacks.math.columbia.edu/tag/048D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
