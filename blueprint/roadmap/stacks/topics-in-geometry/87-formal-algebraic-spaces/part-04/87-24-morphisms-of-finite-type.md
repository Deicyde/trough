---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType, AlgebraicGeometry.FormalSpace.IsFiniteType, AlgebraicGeometry.FormalSpace.IsFiniteType', AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType, AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType, AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.comp, AlgebraicGeometry.FormalSpace.IsFiniteType.comp, AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType.comp
statement: formalized
proof: formalized
---

# 87.24 Morphisms of finite type

Section 87.24 of the Stacks Project, [Tag 0AM3](https://stacks.math.columbia.edu/tag/0AM3). 9 tags here are carried by 42 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AM4, a definition

[Tag 0AM4](https://stacks.math.columbia.edu/tag/0AM4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L82). The attribute's comment: “part (1): locally of finite type”.

> A morphism of formal algebraic spaces over `S` is *locally of finite type* when it is
> representable by algebraic spaces and every base change of it along a scheme-valued point of its
> target is a morphism of algebraic spaces which is locally of finite type. The condition is stated
> for an arbitrary morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsLocallyOfFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L94). The attribute's comment: “part (2): finite type”. References: EGA I (10.13.3), “representable morphisms”.

> A morphism of formal algebraic spaces over `S` is *of finite type* when it is representable
> by algebraic spaces and every base change of it along a scheme-valued point of its target is a
> morphism of algebraic spaces which is of finite type. The condition is stated for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L92). The attribute's comment: “part (2): finite type”. References: EGA I (10.13.3), “representable morphisms”.

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

**`AlgebraicGeometry.FormalSpace.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L94). The attribute's comment: “representable plus Bootstrap finite type”. References: EGA I (10.13.3), “representable morphisms”.

> A morphism of formal algebraic spaces over `S` is *of finite type* when it is representable
> by algebraic spaces and every base change of it along a scheme-valued point of its target is a
> morphism of algebraic spaces which is of finite type. The condition is stated for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L105). The attribute's comment: “condition (2): representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ”.

> A morphism of formal algebraic spaces over `S` is representable by algebraic spaces and of
> finite type in the bootstrap sense of Stacks 03XZ when every base change of it along a
> scheme-valued point of its target is a morphism of algebraic spaces which is of finite type. The
> condition is stated for an arbitrary morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsBootstrapFiniteType {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L92). The attribute's comment: “condition (1): of finite type”. References: EGA I (10.13.3), “representable morphisms”.

> **Stacks 0AM4, part (2)**, which is **Stacks 0AJJ, condition (1)**. A morphism of formal
> algebraic spaces over `S` is *of finite type* when it is locally of finite type, in the sense
> of Definition 0AM4, part (1), and quasi-compact, in the sense of Definition 0AJC. The
> condition makes sense, and is stated, for an arbitrary morphism of fppf sheaves on the big
> fppf site of `S`.

```lean
abbrev IsFiniteType' {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean#L185). The attribute's comment: “the equivalence of conditions (1) and (2), for an arbitrary morphism of fppf sheaves, representability by algebraic spaces being part of both conditions rather than a hypothesis”.

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

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L162). The attribute's comment: “locally of finite type”.

> A composition of morphisms of formal algebraic spaces over `S` which are locally of finite
> type is locally of finite type.

```lean
theorem IsLocallyOfFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L196). The attribute's comment: “finite type”.

> A composition of morphisms of formal algebraic spaces over `S` which are of finite type is
> of finite type.

```lean
theorem IsFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsFiniteType B S hS f) (hg : IsFiniteType B S hS g) :
    IsFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L237). The attribute's comment: “finite type, proved for condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — rather than for Definition 0AM4, part (2), verbatim, which is defined further up the import order: the two are identified unconditionally by Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`”.

> A composition of morphisms of formal algebraic spaces over `S` which are representable by
> algebraic spaces and of finite type in the bootstrap sense of Stacks 03XZ is again such.

```lean
theorem IsBootstrapFiniteType.comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsBootstrapFiniteType B S hS f) (hg : IsBootstrapFiniteType B S hS g) :
    IsBootstrapFiniteType B S hS (f ≫ g)
```

## Tag 0AQ5, a lemma

[Tag 0AQ5](https://stacks.math.columbia.edu/tag/0AQ5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L127). The attribute's comment: “locally of finite type”.

> A base change of a morphism of formal algebraic spaces over `S` which is locally of finite
> type is locally of finite type.

```lean
theorem IsLocallyOfFiniteType.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS p
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L140). The attribute's comment: “finite type”.

> A base change of a morphism of formal algebraic spaces over `S` which is of finite type is
> of finite type.

```lean
theorem IsFiniteType.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsFiniteType B S hS f) :
    IsFiniteType B S hS p
```

**`AlgebraicGeometry.FormalSpace.IsFiniteType.of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeQuasiCompact.lean#L99). The attribute's comment: “finite type”.

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

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L341). The attribute's comment: “stated for arbitrary fppf sheaves, only the source of the second morphism being assumed a formal algebraic space”.

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S`
> with `Y` a formal algebraic space. If `f ≫ g` is locally of finite type then so is `f`.

```lean
theorem IsLocallyOfFiniteType.of_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_comp_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L377). The attribute's comment: “for a second morphism whose source is an affine formal algebraic space”.

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

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_square_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeAfterTargetCover.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeAfterTargetCover.lean#L70). The attribute's comment: “condition (1) implies condition (3), for a square whose chart of the target is an affine formal algebraic space: the general implication needs the locally of finite type assertion of Stacks 0AN2 for the relative diagonal of a morphism of formal algebraic spaces, which this library has only for a morphism whose source is an affine formal algebraic space, and that is the case the source's own proof of condition (4) uses”.

> **Stacks 0ANL, condition (1) implies condition (3), for a square whose chart of the target
> is an affine formal algebraic space.** If `f` is locally of finite type and the square
>
> `p ≫ f = t ≫ q`
>
> has `p` representable étale and `V`, the source of its target column, an affine formal
> algebraic space, then `t` is locally of finite type.
>
> This is the implication the general (1) ⟹ (3) is blocked on, in the generality the source's own
> proof of condition (4) uses it: there the chart `Vⱼ` of the target *is* affine. The two steps
> are both unconditional. First `t ≫ q = p ≫ f` is locally of finite type, `p` being locally of
> finite type by **Stacks 0AJG** and composition being **Stacks 0AQ4**. Then the cancellation of
> **Stacks 0AQ6** removes `q`: it needs the locally-of-finite-type assertion of **Stacks 0AN2**
> for the relative diagonal of `q`, which `AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType`
> `.of_comp_of_isAffineFormal` supplies from affineness of `V`.
>
> Neither column of the square is asked to be surjective, `q` is not asked to be representable
> étale, and `U` and `V` are not asked to be formal algebraic spaces beyond affineness of `V`.

```lean
theorem isLocallyOfFiniteType_square_of_isAffineFormal {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (U V : FppfSheaf B S hS) (p : U ⟶ X) (q : V ⟶ Y)
    (t : U ⟶ V) (hV : IsAffineFormalAlgebraicSpace B S hS V)
    (hp : IsRepresentableEtale B S hS p) (hsq : p ≫ f = t ≫ q) :
    IsLocallyOfFiniteType B S hS t
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAfterTargetCover_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeAfterTargetCover.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeAfterTargetCover.lean#L98). The attribute's comment: “condition (1) implies condition (4), for a morphism of formal algebraic spaces, with nothing assumed: the fibre product of a chart of the target with the morphism is a formal algebraic space by the étale case of Stacks 0AJ3, `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0ANL, condition (1) implies condition (4).** The atlas of the target and the
> atlases of the fibre products of its members with the source witness condition (4) directly,
> without going through condition (3): the chart `Vⱼ` of the target is an affine formal algebraic
> space, so `isLocallyOfFiniteType_square_of_isAffineFormal` applies to the square the chart
> `Uⱼᵢ` of `Vⱼ ×_Y X` forms with `f` and `Vⱼ ⟶ Y`.
>
> This is the implication the proof of **Stacks 0GBB** clause (5) consumes, where `f` is the
> morphism `X_red ⟶ Y_red` on the reductions. Previously only condition (3) implied condition
> (4), and condition (3) was reachable from nothing.
>
> The fibre product `Vⱼ ×_Y X` is a formal algebraic space by the étale case of Stacks 0AJ3,
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`, since
> `X` is a formal algebraic space and the chart `Vⱼ ⟶ Y` is representable étale.

```lean
theorem isLocallyOfFiniteTypeAfterTargetCover_of_isLocallyOfFiniteType {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteTypeAfterTargetCover B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnSomeSquare_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean#L151). The attribute's comment: “condition (1) implies condition (2), reading surjectivity of the source column as surjectivity of the morphism of sheaves”.

> **Stacks 0ANL, condition (1) implies condition (2).** The square formed by the identities
> of `X` and of `Y` witnesses condition (2): both columns are identities, hence representable
> étale and surjective, and the upper horizontal map is `f` itself.

```lean
theorem isLocallyOfFiniteTypeOnSomeSquare_of_isLocallyOfFiniteType {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteTypeOnSomeSquare B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_of_onEverySquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean#L164). The attribute's comment: “condition (3) implies condition (1), by instantiating condition (3) at the square formed by the identities”.

> **Stacks 0ANL, condition (3) implies condition (1).** Condition (3), instantiated at the
> square formed by the identities of `X` and of `Y`, asserts that `f` itself is locally of finite
> type.

```lean
theorem isLocallyOfFiniteType_of_onEverySquare {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteTypeOnEverySquare B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnSomeSquare_of_onEverySquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean#L174). The attribute's comment: “condition (3) implies condition (2)”.

> **Stacks 0ANL, condition (3) implies condition (2).** Condition (3) gives that `f` is
> locally of finite type, and the identity square then witnesses condition (2).

```lean
theorem isLocallyOfFiniteTypeOnSomeSquare_of_onEverySquare {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteTypeOnEverySquare B S hS f) :
    IsLocallyOfFiniteTypeOnSomeSquare B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAfterTargetCover_of_onEverySquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean#L192). The attribute's comment: “condition (3) implies condition (4), with Stacks 0AJ3 — that the fibre product of a chart of the target with the morphism is a formal algebraic space — carried as the hypothesis h0AJ3, since this library does not have it”.

> **Stacks 0ANL, condition (3) implies condition (4).** The atlas of the target and the
> atlases of the fibre products of its members with the source witness condition (4): a chart
> `Uⱼᵢ` of `Vⱼ ×_Y X` maps to `X` by a representable étale morphism, because the second
> projection is a base change of `Vⱼ ⟶ Y`, and the square it forms with `f` and `Vⱼ ⟶ Y`
> commutes by the universal property of the fibre product.
>
> The hypothesis `h0AJ3` is the assertion of Stacks 0AJ3 that `Vⱼ ×_Y X` is a formal algebraic
> space, which this library does not carry.

```lean
theorem isLocallyOfFiniteTypeAfterTargetCover_of_onEverySquare {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hY : IsFormalAlgebraicSpace B S hS Y)
    (h0AJ3 : ∀ (V : FppfSheaf B S hS) (v : V ⟶ Y), IsAffineFormalAlgebraicSpace B S hS V →
      IsRepresentableEtale B S hS v → IsFormalAlgebraicSpace B S hS (pullback v f))
    (hf : IsLocallyOfFiniteTypeOnEverySquare B S hS f) :
    IsLocallyOfFiniteTypeAfterTargetCover B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnFactoredAtlas_of_afterTargetCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTarget.lean#L223). The attribute's comment: “condition (4) implies condition (5), with the assertion that the composite of a covering of the target with coverings of the fibre products is again a covering as in Definition 0AIM carried as the hypothesis h0AIM”.

> **Stacks 0ANL, condition (4) implies condition (5).** Composing the coverings of the fibre
> products `Vⱼ ×_Y X` with the second projections gives a covering of `X` indexed by the pairs
> `(j, i)`, and the member `Uⱼᵢ ⟶ X` of it factors as `Uⱼᵢ ⟶ Vⱼ ⟶ Y` over `f` through the first
> projection, which condition (4) asserts to be locally of finite type.
>
> The hypothesis `h0AIM` is that the composite family is again a covering as in Definition 0AIM.
> Its affineness clause is inherited from the given coverings and its representable étaleness
> clause follows from `AlgebraicGeometry.FormalSpace.IsRepresentableEtale.comp` together with
> `AlgebraicGeometry.FormalSpace.isRepresentableEtale_pullback_snd`; what the library does not
> carry is the joint surjectivity of the composite family.

```lean
theorem isLocallyOfFiniteTypeOnFactoredAtlas_of_afterTargetCover {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y)
    (h0AIM : ∀ (J : Type (u + 1)) (V : J → FppfSheaf B S hS) (v : ∀ j, V j ⟶ Y),
      IsAffineEtaleCover B S hS V v → ∀ (I : J → Type (u + 1))
        (U : ∀ j, I j → FppfSheaf B S hS) (w : ∀ j i, U j i ⟶ pullback (v j) f),
        (∀ j, IsAffineEtaleCover B S hS (U j) (w j)) →
        IsAffineEtaleCover B S hS (fun ji : Σ j, I j ↦ U ji.1 ji.2)
          (fun ji ↦ w ji.1 ji.2 ≫ pullback.snd (v ji.1) f))
    (hf : IsLocallyOfFiniteTypeAfterTargetCover B S hS f) :
    IsLocallyOfFiniteTypeOnFactoredAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnEverySquare_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L61). The attribute's comment: “condition (1) implies condition (3)”.

> A morphism `f : X ⟶ Y` locally of finite type is locally of finite type on every square: for
> representable étale `p : U ⟶ X` and `q : V ⟶ Y` from formal algebraic spaces and `t : U ⟶ V`
> with `p ≫ f = t ≫ q`, the map `t` is locally of finite type.

```lean
theorem isLocallyOfFiniteTypeOnEverySquare_of_isLocallyOfFiniteType {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteTypeOnEverySquare B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeOnFactoredAtlas_of_afterTargetCover'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L76). The attribute's comment: “condition (4) implies condition (5)”.

> If `f : X ⟶ Y` is locally of finite type after a target cover, then it is locally of finite
> type on a factored atlas: there is an affine étale covering of `X` each member of which factors
> through an affine formal algebraic space representable étale over `Y` by a map locally of finite
> type.

```lean
theorem isLocallyOfFiniteTypeOnFactoredAtlas_of_afterTargetCover' {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteTypeAfterTargetCover B S hS f) :
    IsLocallyOfFiniteTypeOnFactoredAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAfterTargetCover_of_onEverySquare'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L98). The attribute's comment: “condition (3) implies condition (4)”.

> Let `X`, `Y` be formal algebraic spaces. If `f : X ⟶ Y` is locally of finite type on every
> square, then it is locally of finite type after a target cover: there is an affine étale
> covering `{Vⱼ ⟶ Y}` and, for each `j`, an affine étale covering of `Vⱼ ×_Y X` whose members are
> locally of finite type over `Vⱼ`.

```lean
theorem isLocallyOfFiniteTypeAfterTargetCover_of_onEverySquare' {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteTypeOnEverySquare B S hS f) :
    IsLocallyOfFiniteTypeAfterTargetCover B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_of_onSomeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L161). The attribute's comment: “condition (2) implies condition (1), reading surjectivity of the source column as surjectivity of the morphism of sheaves”.

> A morphism `f : X ⟶ Y` which is locally of finite type on some square is locally of finite
> type: it suffices that `p ≫ f = t ≫ q` for a surjective representable étale `p : U ⟶ X`, a
> representable étale `q : V ⟶ Y` from formal algebraic spaces and `t : U ⟶ V` locally of finite
> type.

```lean
theorem isLocallyOfFiniteType_of_onSomeSquare {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteTypeOnSomeSquare B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_of_onFactoredAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L174). The attribute's comment: “condition (5) implies condition (1), reading the covering of Definition 0AIM as a jointly surjective family of morphisms of sheaves”.

> Let `X`, `Y` be formal algebraic spaces and `f : X ⟶ Y`. If there is an affine étale
> covering `{Uᵢ ⟶ X}` each member of which factors as `Uᵢ ⟶ Vᵢ ⟶ Y` through an affine formal
> algebraic space representable étale over `Y` by a map locally of finite type, then `f` is
> locally of finite type.

```lean
theorem isLocallyOfFiniteType_of_onFactoredAtlas {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteTypeOnFactoredAtlas B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_tfae_squares`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeLocalOnSourceAndTargetRefined.lean#L188). The attribute's comment: “the equivalence of conditions (1), (2) and (3)”.

> For a morphism `f : X ⟶ Y` of formal algebraic spaces, the following are equivalent: `f` is
> locally of finite type; `f` is locally of finite type on some square; `f` is locally of finite
> type on every square.

```lean
theorem isLocallyOfFiniteType_tfae_squares {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    List.TFAE [IsLocallyOfFiniteType B S hS f,
      IsLocallyOfFiniteTypeOnSomeSquare B S hS f,
      IsLocallyOfFiniteTypeOnEverySquare B S hS f]
```

## Tag 0ANM, an example

[Tag 0ANM](https://stacks.math.columbia.edu/tag/0ANM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.existsUnique_quotientCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L86). The attribute's comment: “the quotient of the relative completion at a weak ideal of definition”.

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

**`AlgebraicGeometry.FormalSpace.exists_completionOver_quotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L375). The attribute's comment: “the induced quotient system and continuous map of the relative completion”.

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

**`AlgebraicGeometry.FormalSpace.ker_projection_eq_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L572). The attribute's comment: “the affine base change of the completion along a quotient stage”.

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

**`AlgebraicGeometry.FormalSpace.isPullback_specMap_kerProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L675). The attribute's comment: “the affine base change of the completion along a quotient stage”.

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

**`AlgebraicGeometry.FormalSpace.isPullback_formalSpectrumMap_kerProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean, line 1032](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteType.lean#L1032). The attribute's comment: “the base change of the completion along a quotient stage”.

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

**`TopologicalRing.finiteTypeModuloEveryWeakIdeal_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L147). The attribute's comment: “the relative completion along a finite type ring map is taut and of finite type modulo every weak ideal of definition of the base, which is the ring-theoretic content of the identification `T ×_{Spf A} Spf ((A')^) = T ×_{Spec (A / I)} Spec (A' / IA')`”.

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

**`AlgebraicGeometry.FormalSpace.exists_isPullback_isFiniteType_formalSpectrumMap_completionOver_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L313). The attribute's comment: “the base change identification: for a point of `Spf A` out of a quasi-compact scheme `T` of the site, `T ×_{Spf A} Spf ((A')^)` is represented by the object `T ×_{Spec (A / I)} Spec (A' / IA')` of the site, and its projection to `T` is of finite type”.

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

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_formalSpectrumMap_completionOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L367). The attribute's comment: “representability of `Spf ((A')^) → Spf A`: the morphism is representable by algebraic spaces over `S`, with no restriction on the scheme-valued point of `Spf A` along which the base change is taken”.

> **Stacks 0ANM**, the representability assertion. Let `B` be a weakly admissible
> topological ring over `S`, let `f : B →+* A` be a finite type ring map and let `g` present
> the canonical map `B ⟶ A^` to the relative completion as a morphism of quotient systems over
> `S`. Then `Spf A^ ⟶ Spf B` is representable by algebraic spaces, which is condition (1) of
> Stacks 0AN5 and the assertion Stacks 0AN6 makes about this morphism.

```lean
theorem isRepresentableByAlgebraicSpacesULift_formalSpectrumMap_completionOver
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B) (hf : f.FiniteType)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} 𝔅 S hS
      (formalSpectrumMap hB g).hom
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_completionOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L393). The attribute's comment: “finite type of `Spf ((A')^) → Spf A`: the morphism is of finite type, with no restriction on the scheme-valued point of `Spf A` along which the base change is taken. The base change along a point out of a quasi-compact scheme `T` is the source's `T ×_{Spec (A / I)} Spec (A' / IA')`”.

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

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_completionOver'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean#L120). The attribute's comment: “finite type of `Spf ((A')^) → Spf A`: the morphism is of finite type as Definition 0AM4, part (2), verbatim. What the argument produces is condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — and Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, carries it to Definition 0AM4, part (2), unconditionally. With no restriction on the scheme-valued point of `Spf A` along which the base change is taken; the base change along a point out of a quasi-compact scheme `T` is the source's `T ×_{Spec (A / I)} Spec (A' / IA')`”.

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

**`AlgebraicGeometry.FormalSpace.exists_completionOver_quotientSystem_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeQuotientSystem.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeQuotientSystem.lean#L154). The attribute's comment: “the induced quotient system and continuous map of the relative completion, with no size hypothesis on the site”.

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

- [`completionOver_isWeaklyAdmissible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=completionOver_isWeaklyAdmissible#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L156) (StacksFrontier): “the relative completion of a ring map over a weakly admissible topological ring is weakly admissible; no finite type hypothesis is needed”.
- [`isTopologicallyOfFiniteType_canonicalMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTopologicallyOfFiniteType_canonicalMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExample.lean#L160) (StacksFrontier): “the relative completion along a finite type ring map is topologically of finite type over the base, which is the ring-theoretic form of the finite type assertion”.
- [`completionOver_isWeaklyAdmissible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=completionOver_isWeaklyAdmissible#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean#L39) (StacksFrontier): “the relative completion of a ring map over a weakly admissible topological ring is weakly admissible; no finite type hypothesis is needed”.
- [`isTopologicallyOfFiniteType_canonicalMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTopologicallyOfFiniteType_canonicalMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFiniteTypeExampleUnconditional.lean#L43) (StacksFrontier): “the relative completion along a finite type ring map is topologically of finite type over the base, which is the ring-theoretic form of the finite type assertion”.

## Tag 0AQ7, a lemma

[Tag 0AQ7](https://stacks.math.columbia.edu/tag/0AQ7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_source_of_isLocallyOfFiniteType'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean#L44).

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

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeNoetherianRefined.lean#L104). The attribute's comment: “stated for an arbitrary cartesian square over `Y` rather than for the chosen fibre product `Z ×_Y X`”.

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

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_of_isPullback_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean#L92).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
