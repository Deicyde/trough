---
declaration: section
origin: cited
lean: CategoryTheory.Mono, AlgebraicGeometry.FormalSpace.mono_comp, AlgebraicGeometry.FormalSpace.Mono.of_isPullback, AlgebraicGeometry.FormalSpace.mono_tfae, AlgebraicGeometry.FormalSpace.mono_tfae', AlgebraicGeometry.FormalSpace.mono_tfae_flatCover
statement: formalized
proof: formalized
---

# 87.26 Monomorphisms

Section 87.26 of the Stacks Project, [Tag 0AQA](https://stacks.math.columbia.edu/tag/0AQA). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AQB, a definition

[Tag 0AQB](https://stacks.math.columbia.edu/tag/0AQB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/Defs.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Defs.lean#L63) (StacksFrontier): “monomorphism of the underlying sheaves”. References: EGA IV (8.11.5.1); SGA 1 V (3.6); SGA 3 VIIB (2.4.1); SGA 3 VIII (3.4); SGA 4 I (10.4); SGA 4 II (3.2).

## Tag 0GHT, a lemma

[Tag 0GHT](https://stacks.math.columbia.edu/tag/0GHT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.mono_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean#L67).

> The composition of two monomorphisms of formal algebraic spaces over `S` is a
> monomorphism.

```lean
theorem mono_comp {X Y Z : FppfSheaf B S hS} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : Mono f) (hg : Mono g) : Mono (f ≫ g)
```

## Tag 0GHU, a lemma

[Tag 0GHU](https://stacks.math.columbia.edu/tag/0GHU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.Mono.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean#L75).

> A base change of a monomorphism of formal algebraic spaces over `S` is a monomorphism: in
> the cartesian square with `f` on the right and `p` on the left, if `f` is a monomorphism then so
> is `p`.

```lean
theorem Mono.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : Mono f) : Mono p
```

## Tag 0GHV, a lemma

[Tag 0GHV](https://stacks.math.columbia.edu/tag/0GHV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.mono_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean#L250). The attribute's comment: “conditions (1), (2), (3), (4) and (5)”.

> For a morphism `f : X ⟶ Y` of formal algebraic spaces over `S`, with `Y` a formal algebraic
> space, the following are equivalent:
>
> 1. `f` is a monomorphism;
> 2. for every scheme `T` over `S` in the site and every `T ⟶ Y` the projection
>    `X ×_Y T ⟶ T` is a monomorphism;
> 3. the same for every affine scheme `T` over `S` in the site;
> 4. there is a covering `{Y_j ⟶ Y}` as in Definition 0AIM such that each `X ×_Y Y_j ⟶ Y_j` is a
>    monomorphism;
> 5. there is a family `{Y_j ⟶ Y}` with `∐ Y_j ⟶ Y` a surjection of sheaves such that each
>    `X ×_Y Y_j ⟶ Y_j` is a monomorphism.

```lean
theorem mono_tfae {X Y : FppfSheaf B S hS} (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [Mono f,
        IsMonoOnSchemeBaseChanges B S hS f,
        IsMonoOnAffineBaseChanges B S hS f,
        HasMonoFormalAtlas B S hS f,
        HasMonoLocallySurjectiveFamily B S hS f]
```

**`AlgebraicGeometry.FormalSpace.mono_tfae'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Monomorphism.lean#L273). The attribute's comment: “conditions (1), (2), (3) and (5)”.

> For an arbitrary morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S`,
> conditions (1), (2), (3) and (5) of `AlgebraicGeometry.FormalSpace.mono_tfae` are
> equivalent.

```lean
theorem mono_tfae' {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    List.TFAE
      [Mono f,
        IsMonoOnSchemeBaseChanges B S hS f,
        IsMonoOnAffineBaseChanges B S hS f,
        HasMonoLocallySurjectiveFamily B S hS f]
```

**`AlgebraicGeometry.FormalSpace.mono_tfae_flatCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MonomorphismFlatCover.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MonomorphismFlatCover.lean#L426). The attribute's comment: “condition (6), and its equivalence with the conditions (1), (2), (3), (4) and (5)”.

> **Stacks 0GHV**, its condition (6) together with the conditions (1), (2), (3), (4) and (5).
> For a morphism `f : X ⟶ Y` of formal algebraic spaces over `S`, with `Y` a formal algebraic
> space, the following are equivalent:
>
> 1. `f` is a monomorphism;
> 2. for every scheme `T` over `S` in the site and every `T ⟶ Y` the projection
>    `X ×_Y T ⟶ T` is a monomorphism;
> 3. the same for every affine scheme `T` over `S` in the site;
> 4. there is a covering `{Y_j ⟶ Y}` as in Definition 0AIM such that each `X ×_Y Y_j ⟶ Y_j` is a
>    monomorphism;
> 5. there is a family `{Y_j ⟶ Y}` with `∐ Y_j ⟶ Y` a surjection of sheaves such that each
>    `X ×_Y Y_j ⟶ Y_j` is a monomorphism;
> 6. there is a morphism `Z ⟶ Y` of formal algebraic spaces over `S` which is representable by
>    algebraic spaces, surjective, flat and locally of finite presentation such that
>    `X ×_Y Z ⟶ Z` is a monomorphism.
>
> The equivalence of the first five conditions is
> `AlgebraicGeometry.FormalSpace.mono_tfae`; condition (6) is absorbed into it by the identity of
> `Y`, which is such a cover, and by the fact that such a cover is a surjection of sheaves.

```lean
theorem mono_tfae_flatCover {X Y : FppfSheaf B S hS} (hY : IsFormalAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [Mono f,
        IsMonoOnSchemeBaseChanges B S hS f,
        IsMonoOnAffineBaseChanges B S hS f,
        HasMonoFormalAtlas B S hS f,
        HasMonoLocallySurjectiveFamily B S hS f,
        HasMonoFlatCover B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.26, Tag 0AQA](https://stacks.math.columbia.edu/tag/0AQA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
