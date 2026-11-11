---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsClosedImmersion, AlgebraicGeometry.FormalSpace.isClosedImmersion_comp, AlgebraicGeometry.FormalSpace.isClosedImmersion_of_isPullback, AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_forall_scheme, AlgebraicGeometry.FormalSpace.isClosedImmersion_of_locallySurjectiveFamily, AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_forall_affine, AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_exists_affineEtaleCover, AlgebraicGeometry.FormalSpace.hasFlatClosedImmersionCover_of_isClosedImmersion
statement: formalized
proof: formalized
---

# 87.27 Closed immersions

Section 87.27 of the Stacks Project, [Tag 0ANN](https://stacks.math.columbia.edu/tag/0ANN). 7 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ANP, a definition

[Tag 0ANP](https://stacks.math.columbia.edu/tag/0ANP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsClosedImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean#L59).

> A morphism of formal algebraic spaces over `S` is a *closed immersion* when it is
> representable by algebraic spaces and every base change of it along a scheme-valued point of its
> target is a closed immersion of schemes. The condition makes sense, and is stated, for an
> arbitrary morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsClosedImmersion {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GHW, a lemma

[Tag 0GHW](https://stacks.math.columbia.edu/tag/0GHW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean#L120). References: EGA I (4.2.5), “closed immersions”.

> A composite of two closed immersions of formal algebraic spaces over `S` is a closed
> immersion.

```lean
theorem isClosedImmersion_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsClosedImmersion B S hS f) (hg : IsClosedImmersion B S hS g) :
    IsClosedImmersion B S hS (f ≫ g)
```

## Tag 0GHX, a lemma

[Tag 0GHX](https://stacks.math.columbia.edu/tag/0GHX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersion.lean#L176).

> A base change of a closed immersion of formal algebraic spaces over `S` is a closed
> immersion: in a cartesian square of fppf sheaves on the big fppf site of `S` whose right-hand
> column `f` is a closed immersion, the left-hand column `snd` is a closed immersion.

```lean
theorem isClosedImmersion_of_isPullback {X Y Y' P : FppfSheaf B S hS}
    {fst : P ⟶ X} {snd : P ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback fst snd f g)
    (hf : IsClosedImmersion B S hS f) : IsClosedImmersion B S hS snd
```

## Tag 0GHY, a lemma

[Tag 0GHY](https://stacks.math.columbia.edu/tag/0GHY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_forall_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriteria.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriteria.lean#L147). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0GHY**, the equivalence of conditions (1) and (2): a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` is a closed immersion if and only if for every scheme `T`
> over the big fppf site of `S` and every morphism `T ⟶ Y` the projection `X ×_Y T ⟶ T` is a
> closed immersion. As with the definition of a closed immersion, no hypothesis that `X` and `Y`
> are formal algebraic spaces is needed.

```lean
theorem isClosedImmersion_iff_forall_scheme {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsClosedImmersion B S hS f ↔
      ∀ (T : BigFppfOver B S hS) (g : yonedaSheaf B S hS T ⟶ Y),
        IsClosedImmersion B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_of_locallySurjectiveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionDescent.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionDescent.lean#L413). The attribute's comment: “the descent step along a surjection of sheaves, which is the sufficiency in conditions (4) and (5)”.

> **Stacks 0GHY**, the descent step along a surjection of sheaves: a morphism `f : X ⟶ Y` of
> fppf sheaves on the big fppf site of `S` is a closed immersion as soon as there is a family
> `{Y_i ⟶ Y}` whose induced map from the coproduct is a surjection of sheaves with every base
> change `X ×_Y Y_i ⟶ Y_i` a closed immersion.
>
> A scheme-valued point of `Y` lies, locally on the point, in the image of a single member of the
> family; over that covering sieve the base change of `f` is a base change of one of the given
> closed immersions, so the base change of `f` along the point is a closed immersion by effective
> fppf descent of closed immersions.
>
> Representability of `f` by algebraic spaces is **not** assumed: it is part of the conclusion,
> and it is produced by the same descent. The base change of `f` along a point of `Y` is a sheaf,
> and being represented by a closed immersion of the site after a covering sieve of that point
> already makes it pointwise `u`-small, which is all the descent step needs; the representing
> objects it returns then exhibit the base changes as algebraic spaces.
>
> This is the sufficiency in both descent conditions of the source. For condition (4) the family
> is the étale atlas of the target, and Definition 0AIM asks of it exactly that it be a surjection
> of sheaves, so this *is* condition (4) implies condition (1):
> `AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_exists_affineEtaleCover`. For condition (5)
> the family has one member, but the source asks only that it be surjective *on points*, so the
> hypothesis must be upgraded first; that is done in
> `AlgebraicGeometry.FormalSpace.isClosedImmersion_of_hasFlatClosedImmersionCover`, which is
> condition (5) implies condition (1).

```lean
theorem isClosedImmersion_of_locallySurjectiveFamily {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (I : Type (u + 1)) (Yi : I → FppfSheaf B S hS) (c : ∀ i, Yi i ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc c))
    (hci : ∀ i, IsClosedImmersion B S hS (pullback.snd f (c i))) :
    IsClosedImmersion B S hS f
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_forall_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean#L221). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 0GHY**, the equivalence of conditions (1) and (3): a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` is a closed immersion if and only if for every *affine*
> scheme `T` over the big fppf site of `S` and every morphism `T ⟶ Y` the projection
> `X ×_Y T ⟶ T` is a closed immersion. As with the definition of a closed immersion, no
> hypothesis that `X` and `Y` are formal algebraic spaces is needed.

```lean
theorem isClosedImmersion_iff_forall_affine {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsClosedImmersion B S hS f ↔
      ∀ (T : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
        ∀ (g : yonedaSheaf B S hS T ⟶ Y),
          IsClosedImmersion B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_exists_affineEtaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean#L240). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 0GHY**, the equivalence of conditions (1) and (4): a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` is a closed immersion if and only if there is a covering
> `{Y_j ⟶ Y}` as in Definition 0AIM with every base change `X ×_Y Y_j ⟶ Y_j` a closed immersion.
>
> Necessity takes the atlas of `Y` furnished by its being a formal algebraic space; sufficiency
> is the descent step, which asks nothing of `f`, so in particular does not assume `f`
> representable by algebraic spaces.

```lean
theorem isClosedImmersion_iff_exists_affineEtaleCover {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) :
    IsClosedImmersion B S hS f ↔
      ∃ (I : Type (u + 1)) (Yi : I → FppfSheaf B S hS) (g : ∀ i, Yi i ⟶ Y),
        IsAffineEtaleCover B S hS Yi g ∧
          ∀ i, IsClosedImmersion B S hS (pullback.snd f (g i))
```

**`AlgebraicGeometry.FormalSpace.hasFlatClosedImmersionCover_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean#L506). The attribute's comment: “condition (1) implies condition (5)”.

> **Stacks 0GHY**, condition (1) implies condition (5): a closed immersion `f : X ⟶ Y` of
> formal algebraic spaces over `S` admits a morphism `Z ⟶ Y` of formal algebraic spaces,
> representable by algebraic spaces, surjective, flat and locally of finite presentation, along
> which the base change of `f` is a closed immersion.
>
> The identity of `Y` serves: it is representable by algebraic spaces and étale, hence surjective
> on points, and each of its base changes along a scheme-valued point of `Y` is an isomorphism
> onto that point, so flatness and local finite presentation hold on every étale chart of it.
> The base change of `f` along the identity is `f` itself up to the canonical isomorphism.

```lean
theorem hasFlatClosedImmersionCover_of_isClosedImmersion {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : IsClosedImmersion B S hS f) :
    HasFlatClosedImmersionCover B S hS f
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_of_hasFlatClosedImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean#L535). The attribute's comment: “condition (5) implies condition (1)”.

> **Stacks 0GHY**, condition (5) implies condition (1): if there is a morphism `Z ⟶ Y` of
> formal algebraic spaces representable by algebraic spaces, surjective, flat and locally of
> finite presentation along which the base change of `f` is a closed immersion, then `f` is a
> closed immersion.
>
> Surjectivity here is the source's, surjectivity on points; it is upgraded to a surjection of
> sheaves by
> `AlgebraicGeometry.FormalSpace.isLocallySurjective_of_isSurjective_of_flat`, and the descent
> step then applies to the one-member family `{Z ⟶ Y}`.

```lean
theorem isClosedImmersion_of_hasFlatClosedImmersionCover {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : HasFlatClosedImmersionCover B S hS f) : IsClosedImmersion B S hS f
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_iff_hasFlatClosedImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionTfae.lean#L555). The attribute's comment: “conditions (1) and (5)”.

> **Stacks 0GHY**, the equivalence of conditions (1) and (5): a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` is a closed immersion if and only if there is a morphism
> `Z ⟶ Y` of formal algebraic spaces, representable by algebraic spaces, surjective, flat and
> locally of finite presentation, with `X ×_Y Z ⟶ Z` a closed immersion.

```lean
theorem isClosedImmersion_iff_hasFlatClosedImmersionCover {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) :
    IsClosedImmersion B S hS f ↔ HasFlatClosedImmersionCover B S hS f
```

## Tag 0ANQ, a lemma

[Tag 0ANQ](https://stacks.math.columbia.edu/tag/0ANQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L129). The attribute's comment: “the source is McQuillan”.

> **Stacks 0ANQ**, the McQuillan property of the source. The source of a closed immersion of
> formal algebraic spaces over `S` whose target is a McQuillan affine formal algebraic space is
> again a McQuillan affine formal algebraic space.

```lean
theorem hasSomeSurjectivePresentation_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (hX : HasSomeSurjectivePresentation B S hS X)
    (_hY : IsFormalAlgebraicSpace B S hS Y) (f : Y ⟶ X)
    (hf : IsClosedImmersion B S hS f) :
    HasSomeSurjectivePresentation B S hS Y
```

**`AlgebraicGeometry.FormalSpace.isClosed_ker_toRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L322). The attribute's comment: “closed kernel”.

> **Stacks 0ANQ**, the closed-kernel assertion. The continuous homomorphism presenting a
> morphism of formal spectra of weakly admissible topological rings over `S` has closed kernel,
> its target being separated.

```lean
theorem isClosed_ker_toRingHom {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {A C : Type u} [CommRing A] [TopologicalSpace A] [CommRing C] [TopologicalSpace C]
    [IsTopologicalRing C] [IsLinearTopology C C]
    (hC : TopologicalRing.IsWeaklyAdmissible C) {D : QuotientSystem B S hS A}
    {E : QuotientSystem B S hS C} (g : ContinuousHom D E) :
    IsClosed (RingHom.ker g.toRingHom : Set A)
```

**`AlgebraicGeometry.FormalSpace.denseRange_of_isClosedImmersion_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L357). The attribute's comment: “dense image”.

> **Stacks 0ANQ**, the dense-image assertion. The continuous homomorphism presenting a closed
> immersion of formal spectra of weakly admissible topological rings over `S` has dense image.

```lean
theorem denseRange_of_isClosedImmersion_formalSpectrumMap
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S} {A C : Type u} [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A] [CommRing C]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C} (g : ContinuousHom D E)
    (hg : IsClosedImmersion B S hS (formalSpectrumMap hA g)) :
    DenseRange g.toRingHom
```

**`AlgebraicGeometry.FormalSpace.isTaut_of_isClosedImmersion_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L89). The attribute's comment: “tautness”.

> **Stacks 0ANQ**, the tautness assertion. The continuous homomorphism presenting a closed
> immersion of formal spectra of weakly admissible topological rings over `S` is taut. A closed
> immersion is representable by objects of the site, which is condition (2) of Stacks 0AN5, and
> condition (2) of that lemma gives tautness.

```lean
theorem isTaut_of_isClosedImmersion_formalSpectrumMap
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S} {A C : Type u} [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A] [CommRing C]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C} (g : ContinuousHom D E)
    (hg : IsClosedImmersion B S hS (formalSpectrumMap hA g)) :
    RingHom.IsTaut g.toRingHom
```

**`AlgebraicGeometry.FormalSpace.exists_formalSpectrumMap_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L174). The attribute's comment: “presenting homomorphism”.

> **Stacks 0ANQ**, the presenting homomorphism. A closed immersion into the formal spectrum
> of a weakly admissible topological ring `A` over `S`, from a formal algebraic space `Y`, is the
> formal spectrum of a continuous homomorphism `A ⟶ C` of weakly admissible topological rings
> over `S`, for a ring `C` presenting `Y`.
>
> The source carries the pullback of the canonical presentation of the target by its quotient
> spectra, whose transition morphisms are thickenings and whose section-ring projections are
> surjective; `C` is the limit of those section rings, weakly admissible because the transitions
> have locally nilpotent kernels. The recognition statement of
> `AlgebraicGeometry.FormalSpace.DirectedQuotients` identifies `Y` with `Spf C`, and the full
> faithfulness of `Spf`, Stacks 0AN0, turns the resulting morphism of formal spectra into the
> homomorphism.

```lean
theorem exists_formalSpectrumMap_of_isClosedImmersion
    (hA : TopologicalRing.IsWeaklyAdmissible A) (D : QuotientSystem B S hS A)
    {Y : FppfSheaf B S hS} (_hY : IsFormalAlgebraicSpace B S hS Y)
    (f : Y ⟶ formalSpectrum D) (hf : IsClosedImmersion B S hS f) :
    ∃ (C : Type u) (_ : CommRing C) (_ : TopologicalSpace C) (_ : IsTopologicalRing C)
      (_ : IsLinearTopology C C) (E : QuotientSystem B S hS C),
      TopologicalRing.IsWeaklyAdmissible C ∧
        ∃ (e : Y ≅ formalSpectrum E) (g : ContinuousHom D E),
          f = e.hom ≫ formalSpectrumMap hA g
```

## Tag 0ANR, an example

[Tag 0ANR](https://stacks.math.columbia.edu/tag/0ANR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isPullback_baseChange_quotientCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuotientCompletionBaseChange.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuotientCompletionBaseChange.lean#L261). The attribute's comment: “base change”.

> **Stacks 0ANR, the base-change identification.** Let `T` be an fppf sheaf over `S` and let
> `t : T ⟶ Spec (A/I)` be a morphism to a quotient stage of `Spf A`. Then the fibre product of
> `Spf ((A/K)^∧) ⟶ Spf A` with the induced morphism `T ⟶ Spf A` is
> `T ×_{Spec (A/I)} Spec (A/(K + I))`:
> ```
> T ×_{Spec (A/I)} Spec (A/(K + I)) ⟶ Spf ((A/K)^∧)
>                ↓                           ↓
>                T                   ⟶     Spf A
> ```
> is cartesian. A morphism to `Spf A` out of a quasi-compact scheme admits such a factorisation
> by Stacks 0AIA, which is the shape in which the source states this.

```lean
theorem isPullback_baseChange_quotientCompletion
    (I : TopologicalRing.WeakIdealOfDefinitionIndex A) (T : FppfSheaf B S hS)
    (t : T ⟶ (formalSpectrumDiagram D).obj (OrderDual.toDual I)) :
    IsPullback
      (pullback.fst
        ((Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map
          ((BigAffineFppf.inclusion B S hS).map
            (φ.stageMap I (quotientCompletionStageIdeal K I)
              (continuousHom_le_comap_quotientCompletionStageIdeal B S hS D E φ hφ I)))) t ≫
        formalSpectrumInclusion E (OrderDual.toDual (quotientCompletionStageIdeal K I)))
      (pullback.snd
        ((Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map
          ((BigAffineFppf.inclusion B S hS).map
            (φ.stageMap I (quotientCompletionStageIdeal K I)
              (continuousHom_le_comap_quotientCompletionStageIdeal B S hS D E φ hφ I)))) t)
      (formalSpectrumMap hA φ)
      (t ≫ formalSpectrumInclusion D (OrderDual.toDual I))
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_formalSpectrumMap_quotientCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuotientCompletionBaseChange.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuotientCompletionBaseChange.lean#L487). The attribute's comment: “closed immersion”.

> **Stacks 0ANR.** The morphism `Spf ((A/K)^∧) ⟶ Spf A` induced by the canonical map
> `A → (A/K)^∧` is a closed immersion of formal algebraic spaces over `S`, in the sense of
> Stacks 0ANP.
>
> The stage inclusions `Spec (A/I) ⟶ Spf A` are jointly surjective with each base change of it
> along them the closed immersion `Spec (A/(K + I)) ⟶ Spec (A/I)`; the descent step of
> Stacks 0GHY concludes, representability by algebraic spaces being part of what that step
> returns rather than a hypothesis of it.

```lean
theorem isClosedImmersion_formalSpectrumMap_quotientCompletion :
    AlgebraicGeometry.FormalSpace.IsClosedImmersion B S hS (formalSpectrumMap hA φ)
```

**`TopologicalRing.ker_canonicalMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/ClosedImmersion.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/ClosedImmersion.lean#L91). The attribute's comment: “kernel”.

> The kernel of the canonical map to the completion of a quotient by a closed ideal
> is that ideal.

```lean
public theorem ker_canonicalMap_eq {A : Type u} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (K : Ideal A)
    (hK : IsClosed (K : Set A)) :
    RingHom.ker
      (TopologicalRing.CompletionOver.canonicalMap (Ideal.Quotient.mk K)) = K
```

**`TopologicalRing.exists_not_surjective_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/ClosedImmersion.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/ClosedImmersion.lean#L1073). The attribute's comment: “nonsurjectivity”.

> For some weakly admissible ring and closed ideal, the map to the completed quotient
> is not surjective.

```lean
theorem exists_not_surjective_canonicalMap :
    ∃ D : TopologicalRing.ClosedIdealQuotientCompletionSituation.{u},
      ¬ Function.Surjective D.canonicalMap
```

## Tag 0GHZ, a lemma

[Tag 0GHZ](https://stacks.math.columbia.edu/tag/0GHZ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_of_mono_of_reduction_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MonomorphismClosedImmersion.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MonomorphismClosedImmersion.lean#L770). The attribute's comment: “the reduction, its inclusion and the factorisation are data, as in Stacks 0GB8”.

> Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which is representable by
> algebraic spaces and a monomorphism, and through which the inclusion `iY : Yred ⟶ Y` of a
> reduction of `Y` factors. If `f` is locally of finite type, or `Y` is locally Noetherian, then `f`
> is a closed immersion.

```lean
theorem isClosedImmersion_of_mono_of_reduction_factors {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) (hmono : Mono f)
    {Yred : FppfSheaf B S hS} {iY : Yred ⟶ Y} (hiY : IsReduction B S hS Y Yred iY)
    (r : Yred ⟶ X) (hr : r ≫ f = iY)
    (hfin : IsLocallyOfFiniteType B S hS f ∨ IsLocallyNoetherian B S hS Y) :
    IsClosedImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.27, Tag 0ANN](https://stacks.math.columbia.edu/tag/0ANN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
