---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantOpen, AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantLocallyClosed, AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantMonomorphism, AlgebraicGeometry.Space.sourceSaturation, AlgebraicGeometry.Space.isInvariantOpen_sourceSaturation, AlgebraicGeometry.Space.exists_isZariskiCover_isInvariantOpen_isQuasiCompactSpace
statement: formalized
proof: formalized
---

# 78.18 Invariant subspaces

Section 78.18 of the Stacks Project, [Tag 044E](https://stacks.math.columbia.edu/tag/044E). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 044F, a definition

[Tag 044F](https://stacks.math.columbia.edu/tag/044F) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean#L71). The attribute's comment: “part (1): invariant open subspaces”.

> **Stacks 044F, part (1).** An open subspace of the object space of a groupoid in algebraic
> spaces is *invariant* when every arrow whose source lies in it has its target in it.

```lean
abbrev IsInvariantOpen (G : GroupoidInAlgebraicSpaces site S hS B)
    (W : Subfunctor G.objects.obj) : Prop
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantLocallyClosed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean#L80). The attribute's comment: “part (2): invariant locally closed subspaces”.

> **Stacks 044F, part (2).** A locally closed subspace of the object space of a groupoid in
> algebraic spaces is *invariant* when its inverse images under the source and the target map agree
> as subspaces of the space of arrows.

```lean
abbrev IsInvariantLocallyClosed (G : GroupoidInAlgebraicSpaces site S hS B)
    (Z : Subfunctor G.objects.obj) : Prop
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantMonomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InvariantSubspaces.lean#L89). The attribute's comment: “part (3): invariant monomorphisms”.

> **Stacks 044F, part (3).** A monomorphism into the object space of a groupoid in algebraic
> spaces is *invariant* when its base change along the target map and its base change along the
> source map are isomorphic as algebraic spaces over the space of arrows.

```lean
noncomputable abbrev IsInvariantMonomorphism (G : GroupoidInAlgebraicSpaces site S hS B)
    {T : AlgebraicSpaces site S hS} (i : T ⟶ G.objects) [Mono i] : Prop
```

## Tag 044G, a lemma

[Tag 044G](https://stacks.math.columbia.edu/tag/044G) in the Stacks Project.

**`AlgebraicGeometry.Space.sourceSaturation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean#L139). The attribute's comment: “the saturation s(t⁻¹(W)) of a subspace of the object space”.

> **Stacks 044G.** The *saturation* of a subspace `W` of the object space of a groupoid in
> algebraic spaces: the subspace whose point set is `s(t⁻¹(W))`, the union of the orbits meeting
> `W`.

```lean
noncomputable def sourceSaturation (G : GroupoidInAlgebraicSpaces B S hS A)
    (W : Subfunctor G.objects.obj) : Subfunctor G.objects.obj
```

**`AlgebraicGeometry.Space.isInvariantOpen_sourceSaturation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean#L289). The attribute's comment: “part (1): the saturation is an invariant open subspace”.

> **Stacks 044G, part (1).** For an open source morphism the saturation of an open subspace of
> the object space is an invariant open subspace.

```lean
theorem isInvariantOpen_sourceSaturation (G : GroupoidInAlgebraicSpaces B S hS A)
    (hs : IsOpenMorphism B S hS G.source.hom) (W : Subfunctor G.objects.obj)
    (hW : IsOpenSubspace B S hS W) :
    GroupoidInAlgebraicSpaces.IsInvariantOpen G (sourceSaturation B S hS G W)
```

**`AlgebraicGeometry.Space.exists_isZariskiCover_isInvariantOpen_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantOpenSaturation.lean#L338). The attribute's comment: “part (2): covering by invariant quasi-compact open subspaces”.

> **Stacks 044G, part (2).** For an open source morphism and a quasi-compact target morphism,
> the object space of a groupoid in algebraic spaces has a Zariski covering by invariant
> quasi-compact open subspaces: the saturations of the members of an affine Zariski covering
> supplied by Stacks 03FY.

```lean
theorem exists_isZariskiCover_isInvariantOpen_isQuasiCompactSpace
    (G : GroupoidInAlgebraicSpaces B S hS A)
    (hs : IsOpenMorphism B S hS G.source.hom)
    (ht : IsQuasiCompact B S hS G.target.hom) :
    ∃ (I : Type u) (V : I → Subfunctor G.objects.obj),
      IsZariskiCover B S hS I V ∧
        ∀ i, GroupoidInAlgebraicSpaces.IsInvariantOpen G (V i) ∧
          IsQuasiCompactSpace B S hS (V i).toFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.18, Tag 044E](https://stacks.math.columbia.edu/tag/044E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
