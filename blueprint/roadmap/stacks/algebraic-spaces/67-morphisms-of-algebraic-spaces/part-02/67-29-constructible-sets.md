---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEtaleLocallyConstructible_preimage, AlgebraicGeometry.Space.isEtaleLocallyConstructible_image
statement: formalized
proof: formalized
---

# 67.29 Constructible sets

Section 67.29 of the Stacks Project, [Tag 0ECV](https://stacks.math.columbia.edu/tag/0ECV). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ECW, a lemma

[Tag 0ECW](https://stacks.math.columbia.edu/tag/0ECW) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L176).

> **Stacks 0ECW.** The inverse image of an étale-locally constructible subset of the points
> of an algebraic space over `S` under a morphism of algebraic spaces is étale locally
> constructible.
>
> A surjective étale chart `q : h_V ⟶ Y` of the target lifts by Stacks 02X1 to a surjective
> étale chart `p : h_U ⟶ X` of the source together with a morphism `α : U ⟶ V` of the site over
> `f`. Read through the homeomorphisms of Stacks 03BX, the inverse image of `E` on `U` is the
> inverse image along the scheme morphism underlying `α` of the inverse image of `E` on `V`, so
> it is locally constructible by Stacks 054I; one surjective chart suffices by Stacks 0ECT.

```lean
theorem isEtaleLocallyConstructible_preimage
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (E : Set (points B S hS Y)) (hE : IsEtaleLocallyConstructible B S hS Y E) :
    IsEtaleLocallyConstructible B S hS X (pointsMap B S hS X f ⁻¹' E)
```

## Tag 0ECX, a theorem

[Tag 0ECX](https://stacks.math.columbia.edu/tag/0ECX) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L217). References: EGA IV (1.8.4); EGA IV (1.8.4.1); EGA IV (9.5.1); SGA 1 IV (6.2).

> **Stacks 0ECX, Chevalley's theorem for algebraic spaces.** The image of an étale-locally
> constructible subset of the points of an algebraic space over `S` under a quasi-compact
> morphism locally of finite presentation is étale locally constructible.
>
> By Stacks 0ECT it is enough to test the image on an affine étale chart `g : h_V ⟶ Y`. The
> base change `h_V ×_Y X` is a quasi-compact algebraic space because `g` has quasi-compact
> source and `f` is quasi-compact, so it has an affine surjective étale chart `t : h\_T ⟶
> h\_V ×\_Y X` by Stacks 03H6. The chart `T` sits over `V` by a morphism `q` of the site and over
> `X` by an étale chart, so the inverse image of `E` on `T` is constructible, and `q` is a
> morphism of affine schemes which is locally of finite presentation because `f` is; Chevalley's
> theorem for schemes therefore makes its image constructible. That image is the inverse image
> of the image of `E` under `g`, which is where Stacks 03H4 and surjectivity of `t` on points
> are used.

```lean
theorem isEtaleLocallyConstructible_image
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f)
    (E : Set (points B S hS X)) (hE : IsEtaleLocallyConstructible B S hS X E) :
    IsEtaleLocallyConstructible B S hS Y (pointsMap B S hS X f '' E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.29, Tag 0ECV](https://stacks.math.columbia.edu/tag/0ECV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
