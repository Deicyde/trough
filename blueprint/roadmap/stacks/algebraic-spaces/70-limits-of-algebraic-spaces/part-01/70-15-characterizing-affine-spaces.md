---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_isFinite, AlgebraicGeometry.Space.isAffineSpace_target_of_isFinite_of_isSurjective, AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed, AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed_of_isAffineSpace, AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_reduction, AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction, AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom, AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom_of_bijective
statement: formalized
proof: formalized
---

# 70.15 Characterizing affine spaces

Section 70.15 of the Stacks Project, [Tag 07VQ](https://stacks.math.columbia.edu/tag/07VQ). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07VS, a lemma

[Tag 07VS](https://stacks.math.columbia.edu/tag/07VS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjection.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjection.lean#L235). The attribute's comment: “granted `h07VR`, the conclusion of Stacks 07VR that a finite morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the strict special case of this statement in which the morphism is also of finite presentation — the third paragraph of the source proof, which runs through Stacks 07SU, 07SK, 084Z, 07SN and 07VP. The first two conclude about inverse systems and the third adds a hypothesis, so none is the universally quantified form of this conclusion”.

> **Stacks 07VS.** Let `f : X ⟶ Y` be a surjective finite morphism of algebraic spaces over
> `S`. If `X` is affine, then so is `Y`.
>
> A finite morphism is affine and universally closed by Stacks 0414 and Stacks 0415, so the
> target is separated by Stacks 05Z2 and quasi-compact by Stacks 040W. Writing `f` as a directed
> limit of finite morphisms of finite presentation, a late stage is affine and is surjective onto
> `Y`, which reduces the claim to the case of a morphism of finite presentation.

```lean
theorem isAffineSpace_of_isSurjective_of_isFinite (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hsurj : IsSurjective B S hS f) (hfin : IsFinite B S hS f)
    (haff : IsAffineSpace B S hS X)
    (h07VR : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    IsAffineSpace B S hS Y
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAffineSpace_target_of_isFinite_of_isSurjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfFiniteSurjection.lean#L483), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffineFiniteSurjectionTags.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineFiniteSurjectionTags.lean#L31) (StacksFrontier).

## Tag 07VT, a proposition

[Tag 07VT](https://stacks.math.columbia.edu/tag/07VT) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjection.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjection.lean#L275). The attribute's comment: “granted `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the strict special case of this statement in which the morphism is also finite and of finite presentation — the third paragraph of the proof of Stacks 07VS, which runs through Stacks 07SU, 07SK, 084Z, 07SN and 07VP. The first two conclude about inverse systems and the third adds two hypotheses, so none is the universally quantified form of this conclusion”.

> **Stacks 07VT.** Let `f : X ⟶ Y` be a surjective universally closed morphism of algebraic
> spaces over `S`. If `X` is affine, then so is `Y`.
>
> The target is separated by Stacks 05Z2 and quasi-compact by Stacks 040W, so `f` is affine by
> Stacks 08GB and hence integral by Stacks 0415. Writing `f` as a directed limit of finite
> morphisms of finite presentation, a late stage is affine and is surjective onto `Y`, which
> reduces the claim to the case of a morphism which is finite and of finite presentation.

```lean
theorem isAffineSpace_of_isSurjective_of_universallyClosed (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hsurj : IsSurjective B S hS f) (hclosed : UniversallyClosed B S hS f)
    (haff : IsAffineSpace B S hS X)
    (h09YA : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    IsAffineSpace B S hS Y
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed_of_isAffineSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjectionUnconditional.lean#L211), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffineFiniteSurjectionTags.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineFiniteSurjectionTags.lean#L33) (StacksFrontier).

## Tag 07VU, a lemma

[Tag 07VU](https://stacks.math.columbia.edu/tag/07VU) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L337). The attribute's comment: “granted the three hypotheses of Stacks 07VT: `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the case of Stacks 07VT in which the morphism is finite and of finite presentation. None is the universally quantified form of this conclusion: the first two conclude about inverse systems and the third about affineness of a target”.

> **Stacks 07VU**, due to Conrad–Lieblich–Olsson 3.1.12. If the reduction of an algebraic
> space over `S` is a scheme, then the space itself is a scheme.
>
> The inclusion of `AlgebraicGeometry.Space.reduction` is a closed immersion, hence integral by
> Stacks 081Y, it is injective on points because it is a monomorphism, and it is surjective on
> points by `AlgebraicGeometry.Space.surjective_pointsMap_ι_reduction`; Stacks 07VV applies.

```lean
theorem isRepresentable_of_isRepresentable_reduction {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hred : (reduction B S hS X hX).toFunctor.IsRepresentable)
    (h09YA : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    X.IsRepresentable
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfSchemeReduction.lean#L167), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean#L117) (StacksFrontier).

## Tag 07VV, a lemma

[Tag 07VV](https://stacks.math.columbia.edu/tag/07VV) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L158). The attribute's comment: “the implication from the target, with no bijectivity hypothesis”.

> **Stacks 07VV, the implication from the target.** If the target of an integral morphism of
> algebraic spaces over `S` is a scheme, then so is its source. Bijectivity on points is not
> needed.
>
> An integral morphism is representable, so the base change of the morphism along an affine open
> of the target is an affine open subspace of the source; the affine opens of the target cover it,
> so every point of the source lies in a representable open subspace, hence in the schematic
> locus of Stacks 03JH.

```lean
theorem isRepresentable_of_isIntegralHom (hF : IsAlgebraicSpace B S hS F) (f : F ⟶ G)
    (hf : IsIntegralHom B S hS f) (hGrep : G.IsRepresentable) :
    F.IsRepresentable
```

**`AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L194). The attribute's comment: “the implication from the source, granted the three hypotheses of Stacks 07VT: `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the case of Stacks 07VT in which the morphism is finite and of finite presentation. None is the universally quantified form of this conclusion: the first two conclude about inverse systems and the third about affineness of a target”.

> **Stacks 07VV, the implication from the source.** If the source of an integral morphism of
> algebraic spaces over `S` which is bijective on points is a scheme, then so is its target.
>
> Let `α : h_V ⟶ X` be an affine open of the source through a given point. The morphism is
> universally closed by Stacks 0415, hence closed on points, so the image of `|V|` is open and
> cuts out an open subspace `W` of the target by part (1) of Tag 03BZ. Bijectivity identifies the
> point set of `X ×_Y W` with `|V|`, so the two open subspaces of `X` agree and `X ×_Y W` is
> affine; its projection to `W` is integral and surjective, so `W` is affine by Stacks 07VT and
> the given point lies in the schematic locus of Stacks 03JH.

```lean
theorem isRepresentable_of_isIntegralHom_of_bijective (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsIntegralHom B S hS f)
    (hbij : Function.Bijective (pointsMap B S hS F f)) (hFrep : F.IsRepresentable)
    (h09YA : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    G.IsRepresentable
```

**`AlgebraicGeometry.Space.isRepresentable_iff_of_isIntegralHom_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L301). The attribute's comment: “granted the three hypotheses of Stacks 07VT: `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the case of Stacks 07VT in which the morphism is finite and of finite presentation. None is the universally quantified form of this conclusion: the first two conclude about inverse systems and the third about affineness of a target”.

> **Stacks 07VV.** Let `f : X ⟶ Y` be an integral morphism of algebraic spaces over `S` which
> induces a bijection `|X| → |Y|` on points. Then `X` is a scheme if and only if `Y` is a scheme.
>
> The two implications are
> `AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom_of_bijective` and
> `AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom`; only the first uses bijectivity, and
> only the first uses the three hypotheses of Stacks 07VT.

```lean
theorem isRepresentable_iff_of_isIntegralHom_of_bijective (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsIntegralHom B S hS f)
    (hbij : Function.Bijective (pointsMap B S hS F f))
    (h09YA : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    F.IsRepresentable ↔ G.IsRepresentable
```

**`AlgebraicGeometry.Space.isRepresentable_iff_isRepresentable_of_isIntegralHom_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijectionUnconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijectionUnconditional.lean#L68).

> **Stacks 07VV.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`. Assume `f` is integral and induces a bijection `|X| → |Y|`. Then `X` is a scheme if
> and only if `Y` is a scheme.
>
> The implication from the source is
> `AlgebraicGeometry.Space.isRepresentable_target_of_isIntegralHom_of_bijective`, through Stacks
> 07VT, and the implication from the target is
> `AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom`, which needs no bijectivity.

```lean
theorem isRepresentable_iff_isRepresentable_of_isIntegralHom_of_bijective
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsIntegralHom B S hS f) (hbij : Function.Bijective (pointsMap B S hS F f)) :
    F.IsRepresentable ↔ G.IsRepresentable
```

## Tag 08B2, a lemma

[Tag 08B2](https://stacks.math.columbia.edu/tag/08B2) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_of_infinitesimal_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimal.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimal.lean#L183). The attribute's comment: “granted the three hypotheses of Stacks 07VT, carried unchanged from Stacks 07VV: `h09YA`, `h07SQ` and `hFinitePresentation`. None is the universally quantified form of this conclusion, which is about closed immersions”.

> **Stacks 08B2.** Let `f : X ⟶ Y` and `i : Y' ⟶ Y` be morphisms of algebraic spaces over `S`.
> If `i` is a closed immersion, bijective on points, if the base change of `f` along `i` is a
> closed immersion, and if either `f` is of finite type or `i` is of finite presentation, then `f`
> is a closed immersion.

```lean
theorem isClosedImmersion_of_infinitesimal_baseChange
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (i : Y' ⟶ Y) (hi : IsClosedImmersion B S hS i)
    (hbij : Function.Bijective (pointsMap B S hS Y' i))
    (hbc : IsClosedImmersion B S hS (pullback.snd f i))
    (hfin : IsFiniteType B S hS f ∨ IsFinitePresentation B S hS i)
    (h09YA : ∀ {Z Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Z ⟶ Z'),
      IsAlgebraicSpace B S hS Z → IsAlgebraicSpace B S hS Z' → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Z' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Z' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {Z Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Z ⟶ Z'),
      IsAlgebraicSpace B S hS Z → IsAlgebraicSpace B S hS Z' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS Z →
      IsAffineSpace B S hS Z') :
    IsClosedImmersion B S hS f
```

**`AlgebraicGeometry.Space.isClosedImmersion_of_isClosedImmersion_pullback_snd_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimalBaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimalBaseChange.lean#L117).

> **Stacks 08B2.** Let `f : X ⟶ Y` and `i : Y' ⟶ Y` be morphisms of algebraic spaces over `S`.
> If `i` is a closed immersion, bijective on points, if the base change of `f` along `i` is a
> closed immersion, and if either `f` is of finite type or `i` is of finite presentation, then `f`
> is a closed immersion.

```lean
theorem isClosedImmersion_of_isClosedImmersion_pullback_snd_of_bijective
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (i : Y' ⟶ Y) (hi : IsClosedImmersion B S hS i)
    (hbij : Function.Bijective (pointsMap B S hS Y' i))
    (hbc : IsClosedImmersion B S hS (pullback.snd f i))
    (hfin : IsFiniteType B S hS f ∨ IsFinitePresentation B S hS i) :
    IsClosedImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.15, Tag 07VQ](https://stacks.math.columbia.edu/tag/07VQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
