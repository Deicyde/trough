---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isImmersion_isLocalAtTarget_fppf, AlgebraicGeometry.Space.locallySeparated_isLocalAtTarget_fppf
statement: formalized
proof: formalized
---

# 74.12 Descending properties of morphisms in the fppf topology

Section 74.12 of the Stacks Project, [Tag 042E](https://stacks.math.columbia.edu/tag/042E). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 042U, a lemma

[Tag 042U](https://stacks.math.columbia.edu/tag/042U) in the Stacks Project.

**`AlgebraicGeometry.Space.isImmersion_isLocalAtTarget_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionFppfLocalAtTarget.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionFppfLocalAtTarget.lean#L122).

> Being an immersion is fppf local on the base for morphisms of algebraic spaces over `S`: such
> a morphism is an immersion exactly when its base change to every member of some fppf covering of
> its target is an immersion.

```lean
theorem isImmersion_isLocalAtTarget_fppf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (immersionProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fppf B S hS)
```

## Tag 042F, a lemma

[Tag 042F](https://stacks.math.columbia.edu/tag/042F) in the Stacks Project.

**`AlgebraicGeometry.Space.locallySeparated_isLocalAtTarget_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallySeparatedFppfLocalAtTarget.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocallySeparatedFppfLocalAtTarget.lean#L116).

> **Stacks 042F.** Local separatedness of morphisms of algebraic spaces over `S` is local on
> the base for the fppf topology: a morphism is locally separated exactly when its base change to
> every member of some fppf covering of its target is locally separated.
>
> Local separatedness of `f : X ⟶ Y` is the relative diagonal `Δ_f : X ⟶ X ×_Y X` being an
> immersion. Pulling a covering `{Y i ⟶ Y}` back along `X ×_Y X ⟶ Y` gives a covering of
> `X ×_Y X` whose base changes of `Δ_f` are the relative diagonals of the base changes of `f`, so
> Stacks 042U for immersions applies.

```lean
theorem locallySeparated_isLocalAtTarget_fppf :
    (locallySeparatedMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fppf B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.12, Tag 042E](https://stacks.math.columbia.edu/tag/042E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
