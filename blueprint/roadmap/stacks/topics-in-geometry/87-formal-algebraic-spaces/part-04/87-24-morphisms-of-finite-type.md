---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType, AlgebraicGeometry.FormalSpace.IsFiniteType, AlgebraicGeometry.FormalSpace.IsFiniteType', AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType, AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType, AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.comp, AlgebraicGeometry.FormalSpace.IsFiniteType.comp, AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType.comp
statement: formalized
proof: formalized
---

# 87.24 Morphisms of finite type

Section 87.24 of the Stacks Project, [Tag 0AM3](https://stacks.math.columbia.edu/tag/0AM3). 9 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AM4, a definition

[Tag 0AM4](https://stacks.math.columbia.edu/tag/0AM4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L82). The attribute's comment: “part (1): locally of finite type”.

> A morphism of formal algebraic spaces over `S` is *locally of finite type* when it is
> representable by algebraic spaces and every base change of it along a scheme-valued point of its
> target is a morphism of algebraic spaces which is locally of finite type. The condition is stated
> for an arbitrary morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsLocallyOfFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L94). The attribute's comment: “part (2): finite type”. References: EGA I (10.13.3), “representable morphisms”.

> A morphism of formal algebraic spaces over `S` is *of finite type* when it is representable
> by algebraic spaces and every base change of it along a scheme-valued point of its target is a
> morphism of algebraic spaces which is of finite type. The condition is stated for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L92). The attribute's comment: “part (2): finite type”. References: EGA I (10.13.3), “representable morphisms”.

> **Stacks 0AM4, part (2)**, which is **Stacks 0AJJ, condition (1)**. A morphism of formal
> algebraic spaces over `S` is *of finite type* when it is locally of finite type, in the sense
> of Definition 0AM4, part (1), and quasi-compact, in the sense of Definition 0AJC. The
> condition makes sense, and is stated, for an arbitrary morphism of fppf sheaves on the big
> fppf site of `S`.

```lean
abbrev IsFiniteType' {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0AJJ, a lemma

[Tag 0AJJ](https://stacks.math.columbia.edu/tag/0AJJ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L94). The attribute's comment: “representable plus Bootstrap finite type”. References: EGA I (10.13.3), “representable morphisms”.

> A morphism of formal algebraic spaces over `S` is *of finite type* when it is representable
> by algebraic spaces and every base change of it along a scheme-valued point of its target is a
> morphism of algebraic spaces which is of finite type. The condition is stated for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L105). The attribute's comment: “condition (2): representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ”.

> A morphism of formal algebraic spaces over `S` is representable by algebraic spaces and of
> finite type in the bootstrap sense of Stacks 03XZ when every base change of it along a
> scheme-valued point of its target is a morphism of algebraic spaces which is of finite type. The
> condition is stated for an arbitrary morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsBootstrapFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L92). The attribute's comment: “condition (1): of finite type”. References: EGA I (10.13.3), “representable morphisms”.

> **Stacks 0AM4, part (2)**, which is **Stacks 0AJJ, condition (1)**. A morphism of formal
> algebraic spaces over `S` is *of finite type* when it is locally of finite type, in the sense
> of Definition 0AM4, part (1), and quasi-compact, in the sense of Definition 0AJC. The
> condition makes sense, and is stated, for an arbitrary morphism of fppf sheaves on the big
> fppf site of `S`.

```lean
abbrev IsFiniteType' {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean#L186). The attribute's comment: “the equivalence of conditions (1) and (2), for an arbitrary morphism of fppf sheaves, representability by algebraic spaces being part of both conditions rather than a hypothesis”.

> **Stacks 0AJJ.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S`. Then
> `f` is of finite type — locally of finite type and quasi-compact in the sense of Definition
> 0AJC — exactly when it is representable by algebraic spaces and of finite type in the
> Bootstrap sense of Stacks 03XZ.
>
> Both conditions contain being locally of finite type: the Bootstrap condition for being of
> finite type is the conjunction of the Bootstrap condition for being locally of finite type
> with the Bootstrap condition for being quasi-compact, which is the content of Stacks 03XF,
> part (3), in the universe-lifted form of
> `StacksFrontier.AlgebraicGeometry.Spaces.LargeValuedFiniteType`. What is left is the comparison
> of Definition 0AJC with the Bootstrap condition for being quasi-compact, which is Stacks 0AM2
> above. The witnesses that the source and the
> target are formal algebraic spaces are not used, so the statement is for an arbitrary
> morphism of fppf sheaves; each condition carries its own representability witness, so
> representability is not a hypothesis.

```lean
theorem isFiniteType_iff_isBootstrapFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsFiniteType' B S hS f ↔ IsBootstrapFiniteType B S hS f
```

## Tag 0AQ4, a lemma

[Tag 0AQ4](https://stacks.math.columbia.edu/tag/0AQ4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L162). The attribute's comment: “locally of finite type”.

> A composition of morphisms of formal algebraic spaces over `S` which are locally of finite
> type is locally of finite type.

```lean
theorem IsLocallyOfFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L196). The attribute's comment: “finite type”.

> A composition of morphisms of formal algebraic spaces over `S` which are of finite type is
> of finite type.

```lean
theorem IsFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsFiniteType B S hS f) (hg : IsFiniteType B S hS g) :
    IsFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L237). The attribute's comment: “finite type, proved for condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — rather than for Definition 0AM4, part (2), verbatim, which is defined further up the import order: the two are identified unconditionally by Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`”.

> A composition of morphisms of formal algebraic spaces over `S` which are representable by
> algebraic spaces and of finite type in the bootstrap sense of Stacks 03XZ is again such.

```lean
theorem IsBootstrapFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsBootstrapFiniteType B S hS f) (hg : IsBootstrapFiniteType B S hS g) :
    IsBootstrapFiniteType B S hS (f ≫ g)
```

## Tag 0AQ5, a lemma

[Tag 0AQ5](https://stacks.math.columbia.edu/tag/0AQ5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L127). The attribute's comment: “locally of finite type”.

> A base change of a morphism of formal algebraic spaces over `S` which is locally of finite
> type is locally of finite type.

```lean
theorem IsLocallyOfFiniteType.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS p
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L140). The attribute's comment: “finite type”.

> A base change of a morphism of formal algebraic spaces over `S` which is of finite type is
> of finite type.

```lean
theorem IsFiniteType.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsFiniteType B S hS f) :
    IsFiniteType B S hS p
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L99). The attribute's comment: “finite type”.

> **Stacks 0AQ5, the global half.** A base change of a morphism of formal algebraic spaces
> over `S` which is of finite type is of finite type: both halves of the condition are stable
> under base change.

```lean
theorem IsFiniteType.of_isPullback' {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsFiniteType' B S hS f) :
    IsFiniteType' B S hS p
```

## Tag 0AQ6, a lemma

[Tag 0AQ6](https://stacks.math.columbia.edu/tag/0AQ6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L341). The attribute's comment: “stated for arbitrary fppf sheaves, only the source of the second morphism being assumed a formal algebraic space”.

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S`
> with `Y` a formal algebraic space. If `f ≫ g` is locally of finite type then so is `f`.

```lean
theorem IsLocallyOfFiniteType.of_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_comp_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L377). The attribute's comment: “for a second morphism whose source is an affine formal algebraic space”.

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S`
> with `Y` an affine formal algebraic space. If `f ≫ g` is locally of finite type then so is
> `f`.

```lean
theorem IsLocallyOfFiniteType.of_comp_of_isAffineFormal {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 0ANL, a lemma

[Tag 0ANL](https://stacks.math.columbia.edu/tag/0ANL) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalTfae.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalTfae.lean#L81). The attribute's comment: “the equivalence of conditions (1) to (5); surjectivity in conditions (2), (4) and (5) is surjectivity of morphisms of sheaves, as in Definition 0AIM, and item (6) of the source is the placeholder "add more here", which states nothing”.

> **Being locally of finite type is local on the source and the target.** For a morphism
> `f : X ⟶ Y` of formal algebraic spaces over `S`, the following are equivalent:
>
> 1. `f` is locally of finite type;
> 2. there is a commutative square `p ≫ f = t ≫ q` with `U`, `V` formal algebraic spaces, `p`
>    and `q` representable étale, `p` surjective and `t` locally of finite type;
> 3. for every commutative square `p ≫ f = t ≫ q` with `U`, `V` formal algebraic spaces and
>    `p`, `q` representable étale, the map `t` is locally of finite type;
> 4. there is a covering `{Vⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Uⱼᵢ ⟶ Vⱼ ×_Y X}` as in Definition 0AIM with each `Uⱼᵢ ⟶ Vⱼ` locally of finite type;
> 5. there is a covering `{Uᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Uᵢ ⟶ Vᵢ ⟶ Y` with `Vᵢ` an affine formal algebraic space, `Vᵢ ⟶ Y` representable étale and
>    `Uᵢ ⟶ Vᵢ` locally of finite type.

```lean
theorem isLocallyOfFiniteType_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    List.TFAE [IsLocallyOfFiniteType B S hS f,
      IsLocallyOfFiniteTypeOnSomeSquare B S hS f,
      IsLocallyOfFiniteTypeOnEverySquare B S hS f,
      IsLocallyOfFiniteTypeAfterTargetCover B S hS f,
      IsLocallyOfFiniteTypeOnFactoredAtlas B S hS f]
```

## Tag 0ANM, an example

[Tag 0ANM](https://stacks.math.columbia.edu/tag/0ANM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.existsUnique_quotientCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L86). The attribute's comment: “the quotient of the relative completion at a weak ideal of definition”.

> The quotient of the relative completion `A^` by the kernel of its projection to `A / JA`
> is canonically `A / JA`, by the unique isomorphism compatible with that projection.

```lean
theorem existsUnique_quotientCompletionEquiv
    {B A : Type u} [CommRing B] [TopologicalSpace B] [CommRing A] (f : B →+* A)
    (J : TopologicalRing.WeakIdealOfDefinitionIndex B) :
    ∃! e : (TopologicalRing.CompletionOver f ⧸
        RingHom.ker (TopologicalRing.CompletionOver.projection f J)) ≃+*
          (A ⧸ TopologicalRing.extendedIdeal f J),
      ∀ x : TopologicalRing.CompletionOver f,
        e (Ideal.Quotient.mk _ x) = TopologicalRing.CompletionOver.projection f J x
```

**`AlgebraicGeometry.FormalSpace.exists_completionOver_quotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L375). The attribute's comment: “the induced quotient system and continuous map of the relative completion”.

> **Stacks 0ANM.** A finite type ring map out of a weakly admissible topological ring
> over `S` gives the relative completion a quotient system over `S` and a continuous map from
> the base whose underlying ring map is the canonical one.

```lean
theorem exists_completionOver_quotientSystem
    [IsTopologicalRing B] [IsLinearTopology B B]
    (f : B →+* A) (hf : letI : Algebra B A := f.toAlgebra; Algebra.FiniteType B A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (D : QuotientSystem 𝔅 S hS B) (hD : D.HasLargeSite) :
    ∃ (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
      (g : ContinuousHom D E),
      g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f
```

**`AlgebraicGeometry.FormalSpace.ker_projection_eq_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L572). The attribute's comment: “the affine base change of the completion along a quotient stage”.

> For an open ideal `L` of the relative completion inside the kernel of the projection at
> `J`, that kernel is the sum of `L` and the ideal generated by the image of `J`. This is the
> identity `ker (A^ → A / JA) = J·A^ + L`, which holds because the kernel is the closure of
> `J·A^` and `L` is open.

```lean
theorem ker_projection_eq_sup {B A : Type u} [CommRing B] [TopologicalSpace B]
    [CommRing A] (f : B →+* A) (J : TopologicalRing.WeakIdealOfDefinitionIndex B)
    (L : Ideal (TopologicalRing.CompletionOver f))
    (hLopen : IsOpen (L : Set (TopologicalRing.CompletionOver f)))
    (hL : L ≤ RingHom.ker (TopologicalRing.CompletionOver.projection f J)) :
    RingHom.ker (TopologicalRing.CompletionOver.projection f J) =
      J.1.map (TopologicalRing.CompletionOver.canonicalMap f) ⊔ L
```

**`AlgebraicGeometry.FormalSpace.isPullback_specMap_kerProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L675). The attribute's comment: “the affine base change of the completion along a quotient stage”.

> **Stacks 0ANM.** The affine base change of the relative completion along a quotient stage:
> `Spec (A / JA) = Spec (B / J) ×_{Spec (B / M)} Spec (A^ / L)`, for an open ideal `L` of `A^`
> inside `ker (A^ → A / JA)` and an ideal `M ⊆ J` of `B` whose image lies in `L`.

```lean
theorem isPullback_specMap_kerProjection {B A : Type u} [CommRing B]
    [TopologicalSpace B] [CommRing A] (f : B →+* A)
    (J : TopologicalRing.WeakIdealOfDefinitionIndex B)
    {M : Ideal B} {L : Ideal (TopologicalRing.CompletionOver f)}
    (hMJ : M ≤ J.1) (hLopen : IsOpen (L : Set (TopologicalRing.CompletionOver f)))
    (hLK : L ≤ RingHom.ker (TopologicalRing.CompletionOver.projection f J))
    (hML : M ≤ Ideal.comap (TopologicalRing.CompletionOver.canonicalMap f) L) :
    IsPullback
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.factor hLK)))
      (Spec.map (CommRingCat.ofHom (Ideal.quotientMap
        (RingHom.ker (TopologicalRing.CompletionOver.projection f J))
        (TopologicalRing.CompletionOver.canonicalMap f) (le_comap_ker_projection f J))))
      (Spec.map (CommRingCat.ofHom (Ideal.quotientMap L
        (TopologicalRing.CompletionOver.canonicalMap f) hML)))
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.factor hMJ)))
```

**`AlgebraicGeometry.FormalSpace.isPullback_formalSpectrumMap_kerProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 1032](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L1032). The attribute's comment: “the base change of the completion along a quotient stage”.

> **Stacks 0ANM.** The base change of the formal spectrum of the relative completion along
> a quotient stage of the base is the spectrum of the corresponding quotient of `A`, that is
> `Spec (A / JA) = Spec (B / J) ×_{Spf B} Spf A^`.

```lean
theorem isPullback_formalSpectrumMap_kerProjection
    (hB : TopologicalRing.IsWeaklyAdmissible B) (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f)
    (J : TopologicalRing.WeakIdealOfDefinitionIndex B)
    (hJK : J.1 ≤ Ideal.comap g.toRingHom (kerProjectionIdeal f J).1) :
    IsPullback
      ((Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).map
        ((BigAffineFppf.inclusion 𝔅 S hS).map
          (g.stageMap J (kerProjectionIdeal f J) hJK)))
      (formalSpectrumInclusion E (OrderDual.toDual (kerProjectionIdeal f J)))
      (formalSpectrumInclusion D (OrderDual.toDual J))
      (formalSpectrumMap hB g)
```

**`TopologicalRing.finiteTypeModuloEveryWeakIdeal_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L149). The attribute's comment: “the relative completion along a finite type ring map is taut and of finite type modulo every weak ideal of definition of the base, which is the ring-theoretic content of the identification `T ×_{Spf A} Spf ((A')^) = T ×_{Spec (A / I)} Spec (A' / IA')`”.

> **Stacks 0ANM.** Let `B` be a weakly pre-admissible linearly topologized ring and let
> `f : B →+* A` be a finite type ring map. The canonical map from `B` to the relative completion
> `A^ = lim_J A ⧸ JA` is taut, and for every weak ideal of definition `J` of `B` the induced
> map `B ⧸ J → A^ ⧸ J A^` is of finite type; indeed `A^ ⧸ J A^ = A ⧸ JA`. This is condition (a)
> of Stacks 0ANU for the canonical map.

```lean
theorem finiteTypeModuloEveryWeakIdeal_canonicalMap [IsTopologicalRing B]
    [IsLinearTopology B B] (f : B →+* A) (hB : IsWeaklyPreAdmissible B) (hf : f.FiniteType) :
    FiniteTypeModuloEveryWeakIdeal (CompletionOver.canonicalMap f)
```

**`AlgebraicGeometry.FormalSpace.exists_isPullback_isFiniteType_formalSpectrumMap_completionOver_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L315). The attribute's comment: “the base change identification: for a point of `Spf A` out of a quasi-compact scheme `T` of the site, `T ×_{Spf A} Spf ((A')^)` is represented by the object `T ×_{Spec (A / I)} Spec (A' / IA')` of the site, and its projection to `T` is of finite type”.

> **Stacks 0ANM**, the representability and the finite type assertions, at a point of
> `Spf B` out of a quasi-compact scheme. Let `B` be a weakly admissible topological ring over
> `S`, let `f : B →+* A` be a finite type ring map and let `g` present the canonical map
> `B ⟶ A^` to the relative completion as a morphism of quotient systems over `S`. For every
> point `T ⟶ Spf B` whose source is a quasi-compact object of the site, the base change
> `T ×_{Spf B} Spf A^` is represented by an object `V` of the site — the source's
> `T ×_{Spec (B / I)} Spec (A / IA)` — and the projection `V ⟶ T` is of finite type.
>
> This is the source's own argument: the point factors through a stage `Spec (B / I) ⟶ Spf B`
> by Stacks 0AIA, the base change along the factorisation is
> `T ×_{Spec (B / I)} Spec (A / IA)`, and `Spec (A / IA) ⟶ Spec (B / I)` is of finite type
> because `B / I → A / IA` is.

```lean
theorem exists_isPullback_isFiniteType_formalSpectrumMap_completionOver_of_compactSpace
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B) (hf : f.FiniteType)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E) (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f)
    (U : BigFppfOver 𝔅 S hS) (hU : CompactSpace ((BigFppfOver.toScheme 𝔅 S hS).obj U))
    (a : (Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).obj U ⟶ formalSpectrum D) :
    ∃ (V : BigFppfOver 𝔅 S hS) (q : V ⟶ U)
      (r : (Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).obj V ⟶ formalSpectrum E),
      IsPullback r ((Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).map q)
        (formalSpectrumMap hB g) a ∧
      Space.IsFiniteTypeULift.{u + 1} 𝔅 S hS ((uliftYoneda.{u + 1}).map q)
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_completionOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L398). The attribute's comment: “finite type of `Spf ((A')^) → Spf A`: the morphism is of finite type, with no restriction on the scheme-valued point of `Spf A` along which the base change is taken. The base change along a point out of a quasi-compact scheme `T` is the source's `T ×_{Spec (A / I)} Spec (A' / IA')`”.

> **Stacks 0ANM**, the finite type assertion. With `B`, `f` and `g` as above,
> `Spf A^ ⟶ Spf B` is of finite type: it is representable by algebraic spaces and every base
> change of it along a scheme-valued point of `Spf B` is a morphism of algebraic spaces which
> is of finite type.
>
> The source's argument is the quasi-compact one — a point out of a quasi-compact scheme
> factors through a thickening stage by Stacks 0AIA, and the base change along the
> factorisation is `T ×_{Spec (B / I)} Spec (A / IA)`. The passage from there to an arbitrary
> scheme-valued point is the locality of the two halves of being of finite type on the target,
> `AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeULift_pullback_of_compact_pullback` and
> `AlgebraicGeometry.FormalSpace.isQuasiCompactULift_of_compact_pullback`.

```lean
theorem isFiniteType_formalSpectrumMap_completionOver
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B) (hf : f.FiniteType)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f) :
    IsFiniteType 𝔅 S hS (formalSpectrumMap hB g)
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_completionOver'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean#L115). The attribute's comment: “finite type of `Spf ((A')^) → Spf A`: the morphism is of finite type as Definition 0AM4, part (2), verbatim. What the argument produces is condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — and Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, carries it to Definition 0AM4, part (2), unconditionally. With no restriction on the scheme-valued point of `Spf A` along which the base change is taken; the base change along a point out of a quasi-compact scheme `T` is the source's `T ×_{Spec (A / I)} Spec (A' / IA')`”.

> Let `f : B →+* A` be a finite type ring map over a weakly admissible topological ring `B`,
> and `g` a continuous homomorphism whose underlying ring map is the canonical map `B → A^` to the
> relative completion. Then `Spf A^ ⟶ Spf B` is of finite type in the sense of Definition 0AM4,
> part (2): locally of finite type — representable by algebraic spaces, with every base change of
> it along a scheme-valued point of `Spf B` a morphism of algebraic spaces which is locally of
> finite type — and quasi-compact in the sense of Definition 0AJC.

```lean
theorem isFiniteType_formalSpectrumMap_completionOver'
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B) (hf : f.FiniteType)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f) :
    IsFiniteType' 𝔅 S hS (formalSpectrumMap hB g)
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdmissible_and_relative_isAffineHom_and_isFiniteType_completionOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean#L157). The attribute's comment: “the relative completion `(A')^` is weakly admissible, `Spf ((A')^) → Spf A` is representable by schemes (every base change along an object of the site is represented by an object of the site, by an affine morphism), and it is of finite type as Definition 0AM4, part (2); no size hypothesis on the site”.

> **Stacks 0ANM**, every assertion of the example. Let `B` be a weakly admissible topological
> ring over `S`, let `f : B →+* A` be a finite type ring map and let `g` present the canonical map
> `B ⟶ A^` to the relative completion `A^ = lim_{I ⊆ B w.i.d.} A / IA` as a morphism of quotient
> systems over `S`. Then
>
> 1. `A^` is a weakly admissible topological ring;
> 2. `Spf A^ ⟶ Spf B` is representable, in the source's sense of representable by schemes
>    (Stacks 0AN5 (2)): every base change of it along an object of the site is represented by an
>    object of the site, and the projection is moreover an affine morphism;
> 3. `Spf A^ ⟶ Spf B` is of finite type in the sense of Definition 0AM4, part (2).
>
> Representability by schemes is Stacks 0AKN for the two affine formal algebraic spaces, applied
> to representability by algebraic spaces
> (`isRepresentableByAlgebraicSpacesULift_formalSpectrumMap_completionOver`); both formal spectra
> have presentations by affine thickenings with no condition on the size of the site
> (`hasThickeningPresentation_formalSpectrum`).

```lean
theorem isWeaklyAdmissible_and_relative_isAffineHom_and_isFiniteType_completionOver
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B) (hf : f.FiniteType)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f) :
    TopologicalRing.IsWeaklyAdmissible (TopologicalRing.CompletionOver f) ∧
      (MorphismProperty.inverseImage (@AlgebraicGeometry.IsAffineHom.{u})
        (BigFppfOver.toScheme 𝔅 S hS)).relative
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)) (formalSpectrumMap hB g) ∧
      IsFiniteType' 𝔅 S hS (formalSpectrumMap hB g)
```

**`AlgebraicGeometry.FormalSpace.exists_completionOver_quotientSystem_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeQuotientSystem.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeQuotientSystem.lean#L154). The attribute's comment: “the induced quotient system and continuous map of the relative completion, with no size hypothesis on the site”.

> **Stacks 0ANM**, with no size hypothesis on the site. A finite type ring map out of a
> weakly admissible topological ring over `S` gives the relative completion a quotient system
> over `S` and a continuous map from the base whose underlying ring map is the canonical one.
> The stages `Spec (A / JA)` lie in the site because `Spec (B / J)` does and `B / J → A / JA` is
> of finite type.

```lean
theorem exists_completionOver_quotientSystem_of_finiteType
    [IsTopologicalRing B] [IsLinearTopology B B]
    (f : B →+* A) (hf : letI : Algebra B A := f.toAlgebra; Algebra.FiniteType B A)
    (hB : TopologicalRing.IsWeaklyAdmissible B) (D : QuotientSystem 𝔅 S hS B) :
    ∃ (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
      (g : ContinuousHom D E),
      g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f
```

Declarations registered for the tag:

- [`completionOver_isWeaklyAdmissible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=completionOver_isWeaklyAdmissible#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L158) (StacksFrontier): “the relative completion of a ring map over a weakly admissible topological ring is weakly admissible; no finite type hypothesis is needed”.
- [`isTopologicallyOfFiniteType_canonicalMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTopologicallyOfFiniteType_canonicalMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L162) (StacksFrontier): “the relative completion along a finite type ring map is topologically of finite type over the base, which is the ring-theoretic form of the finite type assertion”.

## Tag 0AQ7, a lemma

[Tag 0AQ7](https://stacks.math.columbia.edu/tag/0AQ7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_source_of_isLocallyOfFiniteType'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean#L44).

> **Stacks 0AQ7.** If `Y` is a locally Noetherian formal algebraic space
> over `S` and `f : X ⟶ Y` is a morphism of formal algebraic spaces over `S` which is locally of
> finite type, then `X` is locally Noetherian.
>
> The atlas of `Y` by Noetherian affine formal algebraic spaces base changes to a family of
> fibre products covering `X`, and the atlases of those fibre products assemble into an atlas of
> `X`. Its members are locally of finite type over the members of the atlas of `Y` by Stacks
> 0ANL, condition (1) implies condition (3), hence Noetherian by clause (5) of Stacks 0AKQ,
> which Stacks 0AKN makes unconditional.
>
> The fibre products `Vⱼ ×_Y X` are formal algebraic spaces by **Stacks 0AJ3**, which this
> library proves outright for a base which is a formal algebraic space.

```lean
theorem isLocallyNoetherian_source_of_isLocallyOfFiniteType'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyNoetherian B S hS X
```

## Tag 0AQ8, a lemma

[Tag 0AQ8](https://stacks.math.columbia.edu/tag/0AQ8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean#L104). The attribute's comment: “stated for an arbitrary cartesian square over `Y` rather than for the chosen fibre product `Z ×_Y X`”.

> **Stacks 0AQ8.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of formal
> algebraic spaces over `S`. If `Z` is locally Noetherian and `f` is locally of finite type, then
> `Z ×_Y X` is locally Noetherian.
>
> The projection `p : Z ×_Y X ⟶ Z` is a base change of `f`, so it is locally of finite type by
> Stacks 0AQ5, and `Z ×_Y X` is a formal algebraic space by Stacks 0AJ3; Stacks 0AQ7 applies to
> `p`. The fibre product is presented as an arbitrary cartesian square, so the statement covers
> either order of its two legs.

```lean
theorem isLocallyNoetherian_of_isPullback'
    {W X Y Z : FppfSheaf B S hS} {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyNoetherian B S hS W
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_of_isPullback_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean#L92).

> **Stacks 0AQ8.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of fppf sheaves over `S`.
> If `Z` is a locally Noetherian formal algebraic space and `f` is locally of finite type, then
> `Z ×_Y X` is locally Noetherian.
>
> The projection `p : Z ×_Y X ⟶ Z` is a base change of `f`, so it is locally of finite type by
> Stacks 0AQ5; being representable by algebraic spaces it makes `Z ×_Y X` a formal algebraic space
> by Stacks 0AJI, and Stacks 0AQ7 applies to `p`. The fibre product is presented as an arbitrary
> cartesian square, so the statement covers either order of its two legs; `X` and `Y` need not be
> formal algebraic spaces.

```lean
theorem isLocallyNoetherian_of_isPullback_of_isLocallyOfFiniteType
    {W X Y Z : FppfSheaf B S hS} {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyNoetherian B S hS W
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.24, Tag 0AM3](https://stacks.math.columbia.edu/tag/0AM3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
