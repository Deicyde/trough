---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_isAlgebraicSpace, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_isPullback, AlgebraicGeometry.Space.isSheaf_of_isRepresentableByAlgebraicSpaces, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_diagonal, AlgebraicGeometry.Space.isAlgebraicSpaceULift_of_isRepresentable_uliftYoneda, AlgebraicGeometry.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces, AlgebraicGeometry.Space.isAlgebraicSpaceULift_pullback_of_isRepresentableULift
statement: formalized
proof: formalized
---

# 80.3 Morphisms representable by algebraic spaces

Section 80.3 of the Stacks Project, [Tag 02YP](https://stacks.math.columbia.edu/tag/02YP). 11 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02YQ, a definition

[Tag 02YQ](https://stacks.math.columbia.edu/tag/02YQ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean#L85).

> **Stacks Project, Tag 02YQ.** A morphism of presheaves is representable by algebraic
> spaces if its pullback to every scheme over the base is an algebraic space.

```lean
abbrev IsRepresentableByAlgebraicSpaces (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) : Prop
```

## Tag 03BN, a lemma

[Tag 03BN](https://stacks.math.columbia.edu/tag/03BN) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean#L93).

> **Stacks 03BN.** A morphism between algebraic spaces over `S` is representable by
> algebraic spaces: its base change along a scheme-valued point of its target is a fibre
> product of three algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_of_isAlgebraicSpace
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsRepresentableByAlgebraicSpaces B S hS f
```

## Tag 03Y0, a lemma

[Tag 03Y0](https://stacks.math.columbia.edu/tag/03Y0) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean#L222).

> **Stacks Project, Tag 03Y0.** A cartesian base change of a morphism representable by
> algebraic spaces is representable by algebraic spaces.

```lean
lemma isRepresentableByAlgebraicSpaces_of_isPullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G G' H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (p : H ⟶ F) (a' : H ⟶ G') (a : F ⟶ G) (g : G' ⟶ G)
    (h : IsPullback p a' a g)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a) :
    IsRepresentableByAlgebraicSpaces B S hS a'
```

## Tag 02YR, a lemma

[Tag 02YR](https://stacks.math.columbia.edu/tag/02YR) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheaf_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableByAlgebraicSpaces.lean#L157).

> **Stacks Project, Tag 02YR.** A transformation representable by algebraic spaces has a
> sheaf as its source if its target is a sheaf.

```lean
theorem isSheaf_of_isRepresentableByAlgebraicSpaces
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hG : Presheaf.IsSheaf (BigFppfOver.topology B S hS) G) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS) F
```

## Tag 05LA, a lemma

[Tag 05LA](https://stacks.math.columbia.edu/tag/05LA) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableDiagonal.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RepresentableDiagonal.lean#L62).

> **Stacks Project, Tag 05LA.** The relative diagonal of a transformation representable
> by algebraic spaces is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_diagonal
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (ha : IsRepresentableByAlgebraicSpaces B S hS a) :
    IsRepresentableByAlgebraicSpaces B S hS (pullback.diagonal a)
```

## Tag 02YS, a lemma

[Tag 02YS](https://stacks.math.columbia.edu/tag/02YS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpaceULift_of_isRepresentable_uliftYoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperLocality.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperLocality.lean#L104). The attribute's comment: “representable target, arbitrary value universe”.

> The source of a morphism of presheaves with values in `Type (max w u)` which is
> representable by algebraic spaces and whose target is isomorphic to the universe-lifted Yoneda
> presheaf of an object of the big fppf site of `S` is an algebraic space over `S`.

```lean
theorem isAlgebraicSpaceULift_of_isRepresentable_uliftYoneda
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)} {U : BigFppfOver B S hS} (a : F ⟶ G)
    (e : G ≅ (uliftYoneda.{w}).obj U)
    (ha : IsRepresentableByAlgebraicSpacesULift.{w} B S hS a) :
    IsAlgebraicSpaceULift.{w} B S hS F
```

**`AlgebraicGeometry.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableByAlgebraicSpaces.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableByAlgebraicSpaces.lean#L187).

> **Stacks 02YS.** A transformation representable by algebraic spaces to an algebraic space over
> `S` has an algebraic space over `S` as its source.
>
> The three clauses of `AlgebraicGeometry.IsAlgebraicSpace` are verified as in Stacks 02WY. The
> sheaf clause is Stacks 02YR. The diagonal clause is the composite
> `Δ_F = Δ_{F/G} ≫ (F ×_G F ⟶ F × F)`, representable because `Δ_{F/G}` is — this is Stacks 05LA in
> the strengthened form above — and because the second factor is a base change of `Δ_G`. For the
> atlas clause, base-changing a scheme atlas of `G` along `a` gives a surjective étale morphism to
> `F` from an *algebraic space*, and composing it with a scheme atlas of that algebraic space gives
> a scheme atlas of `F`.

```lean
theorem isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (ha : Space.IsRepresentableByAlgebraicSpaces B S hS a)
    (hG : IsAlgebraicSpace B S hS G) :
    IsAlgebraicSpace B S hS F
```

## Tag 03XY, a lemma

[Tag 03XY](https://stacks.math.columbia.edu/tag/03XY) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpaceULift_pullback_of_isRepresentableULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L404). The attribute's comment: “in an arbitrary value universe”.

> The fibre product of an algebraic space over `S` with the source of a
> morphism representable by algebraic spaces, over the target of that morphism, is an algebraic
> space over `S`, for presheaves on the big fppf site of `S` with values in `Type (max w u)`.

```lean
theorem isAlgebraicSpaceULift_pullback_of_isRepresentableULift
    {F G X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)} (a : F ⟶ G) (f : X ⟶ G)
    (ha : IsRepresentableByAlgebraicSpacesULift.{w} B S hS a)
    (hX : IsAlgebraicSpaceULift.{w} B S hS X) :
    IsAlgebraicSpaceULift.{w} B S hS (pullback f a)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_pullback_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean#L103).

> **Stacks 03XY.** The fibre product of an algebraic space over `S` with the source of a
> morphism representable by algebraic spaces, over the target of that morphism, is an
> algebraic space over `S`.

```lean
theorem isAlgebraicSpace_pullback_of_isRepresentableByAlgebraicSpaces
    {F G X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (f : X ⟶ G)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hX : IsAlgebraicSpace B S hS X) :
    IsAlgebraicSpace B S hS (pullback f a)
```

## Tag 03Y1, a lemma

[Tag 03Y1](https://stacks.math.columbia.edu/tag/03Y1) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean#L118).

> **Stacks 03Y1.** A composite of morphisms of presheaves on the big fppf site of `S`
> representable by algebraic spaces is representable by algebraic spaces.
>
> The base change of `a ≫ b` along `ξ` is the base change of `a` along the second projection
> of the base change of `b` along `ξ`, which is an algebraic space by Stacks 03XY.

```lean
theorem isRepresentableByAlgebraicSpaces_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : G ⟶ H)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hb : IsRepresentableByAlgebraicSpaces B S hS b) :
    IsRepresentableByAlgebraicSpaces B S hS (a ≫ b)
```

## Tag 046D, a lemma

[Tag 046D](https://stacks.math.columbia.edu/tag/046D) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_prod_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean#L132).

> **Stacks 046D.** The product of two morphisms of presheaves on the big fppf site of `S`
> representable by algebraic spaces is representable by algebraic spaces.
>
> The product `a₁ ⨯ a₂` is the composite of `a₁ ⨯ 𝟙` with `𝟙 ⨯ a₂`, and each of these is a
> base change of one of the two factors along a projection.

```lean
lemma isRepresentableByAlgebraicSpaces_prod_map
    {F₁ F₂ G₁ G₂ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a₁ : F₁ ⟶ G₁) (a₂ : F₂ ⟶ G₂)
    (h₁ : IsRepresentableByAlgebraicSpaces B S hS a₁)
    (h₂ : IsRepresentableByAlgebraicSpaces B S hS a₂) :
    IsRepresentableByAlgebraicSpaces B S hS (prod.map a₁ a₂)
```

## Tag 0AMN, a lemma

[Tag 0AMN](https://stacks.math.columbia.edu/tag/0AMN) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L417). The attribute's comment: “representable by algebraic spaces in an arbitrary value universe”.

> If the relative diagonal of `b` and the composite `a ≫ b` are
> representable by algebraic spaces, then so is `a`, for presheaves on the big fppf site of `S`
> with values in `Type (max w u)`.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)} (a : F ⟶ G) (b : G ⟶ H)
    (hdiag : IsRepresentableByAlgebraicSpacesULift.{w} B S hS (pullback.diagonal b))
    (hcomp : IsRepresentableByAlgebraicSpacesULift.{w} B S hS (a ≫ b)) :
    IsRepresentableByAlgebraicSpacesULift.{w} B S hS a
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Stability.lean#L153).

> **Stacks 0AMN.** If the relative diagonal of `b` and the composite `a ≫ b` are
> representable by algebraic spaces, then so is `a`.
>
> The base change of `a` along `ξ` is the base change of the relative diagonal of `b` along
> the canonical morphism from the base change of `a ≫ b` along `ξ ≫ b` to `pullback b b`.

```lean
theorem isRepresentableByAlgebraicSpaces_of_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : G ⟶ H)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (pullback.diagonal b))
    (hcomp : IsRepresentableByAlgebraicSpaces B S hS (a ≫ b)) :
    IsRepresentableByAlgebraicSpaces B S hS a
```

## Tag 07WE, a lemma

[Tag 07WE](https://stacks.math.columbia.edu/tag/07WE) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheaf_of_locallySurjective_representable_subfunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/SheafFromSubsheaves.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/SheafFromSubsheaves.lean#L674).

> **Stacks 07WE.** A Zariski sheaf on the big fppf site over `S` which is covered, locally for
> the fppf topology, by fppf subsheaves whose inclusions are representable by algebraic spaces is
> an fppf sheaf.

```lean
theorem isSheaf_of_locallySurjective_representable_subfunctors
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (B.zariskiTopology.over (B.obj hS)) F)
    (I : Type v) (G : I → Subfunctor F)
    (hG : ∀ i, Presheaf.IsSheaf (BigFppfOver.topology B S hS) (G i).toFunctor)
    (hrep : ∀ i, IsRepresentableByAlgebraicSpaces B S hS (G i).ι)
    (hcover : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) (iSup G).ι) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.3, Tag 02YP](https://stacks.math.columbia.edu/tag/02YP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
