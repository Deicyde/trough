---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsInvariantClosedMap, AlgebraicGeometry.Space.IsInvariantClosedMapInter, AlgebraicGeometry.Space.IsStronglySubmersive, AlgebraicGeometry.Space.IsUniformlySubmersive, AlgebraicGeometry.Space.IsUniformlyInvariantClosedMap, AlgebraicGeometry.Space.IsUniversallyInvariantClosedMap, AlgebraicGeometry.Space.IsUniformlyInvariantClosedMapInter, AlgebraicGeometry.Space.IsUniversallyInvariantClosedMapInter
statement: formalized
proof: formalized
---

# 83.7 Topological properties

Section 83.7 of the Stacks Project, [Tag 04A3](https://stacks.math.columbia.edu/tag/04A3). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04A4, a definition

[Tag 04A4](https://stacks.math.columbia.edu/tag/04A4) in the Stacks Project.

**`AlgebraicGeometry.Space.IsInvariantClosedMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L121). The attribute's comment: “condition (2): invariant closed subsets have closed image”.

> **Stacks 04A4, condition (2).** An invariant morphism `φ : U ⟶ X` has *closed invariant
> images* when for every `R`-invariant closed subset `Z ⊆ |U|` the image `φ(Z)` is closed in
> `|X|`.

```lean
abbrev IsInvariantClosedMap (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsInvariantClosedMapInter`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L128). The attribute's comment: “condition (3): intersections of invariant closed subsets”.

> **Stacks 04A4, condition (3).** Condition (2) holds, and moreover for every pair of
> `R`-invariant closed subsets `Z₁, Z₂ ⊆ |U|` one has `φ(Z₁ ∩ Z₂) = φ(Z₁) ∩ φ(Z₂)`.

```lean
abbrev IsInvariantClosedMapInter (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsStronglySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L147). The attribute's comment: “condition (4): strongly submersive”.

> **Stacks 04A4, condition (4).** An invariant morphism `φ : U ⟶ X` is *strongly
> submersive* when the morphism `(t, s) : R ⟶ U ×_X U` assembled from the target and the source
> of `j` is universally submersive.
>
> Invariance of `φ` is exactly the commutation `t ≫ φ = s ≫ φ` needed to form that morphism,
> so it is taken as an argument.

```lean
noncomputable abbrev IsStronglySubmersive (j : PreRelation R U) (φ : U.left ⟶ X)
    (hφ : IsInvariant j φ) : Prop
```

**`AlgebraicGeometry.Space.IsUniformlySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L203). The attribute's comment: “uniform condition (1)”.

> **Stacks 04A4, uniform condition (1).** Condition (1) holds after every flat base
> change.

```lean
abbrev IsUniformlySubmersive : Prop
```

**`AlgebraicGeometry.Space.IsUniformlyInvariantClosedMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L209). The attribute's comment: “uniform condition (2)”.

> **Stacks 04A4, uniform condition (2).** Condition (2) holds after every flat base
> change.

```lean
abbrev IsUniformlyInvariantClosedMap : Prop
```

**`AlgebraicGeometry.Space.IsUniversallyInvariantClosedMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L215). The attribute's comment: “universal condition (2)”.

> **Stacks 04A4, universal condition (2).** Condition (2) holds after every base
> change.

```lean
abbrev IsUniversallyInvariantClosedMap : Prop
```

**`AlgebraicGeometry.Space.IsUniformlyInvariantClosedMapInter`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L221). The attribute's comment: “uniform condition (3)”.

> **Stacks 04A4, uniform condition (3).** Condition (3) holds after every flat base
> change.

```lean
abbrev IsUniformlyInvariantClosedMapInter : Prop
```

**`AlgebraicGeometry.Space.IsUniversallyInvariantClosedMapInter`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L228). The attribute's comment: “universal condition (3)”.

> **Stacks 04A4, universal condition (3).** Condition (3) holds after every base
> change.

```lean
abbrev IsUniversallyInvariantClosedMapInter : Prop
```

**`AlgebraicGeometry.Space.IsUniformlyStronglySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L234). The attribute's comment: “uniform condition (4)”.

> **Stacks 04A4, uniform condition (4).** Condition (4) holds after every flat base
> change.

```lean
noncomputable abbrev IsUniformlyStronglySubmersive : Prop
```

**`AlgebraicGeometry.Space.IsUniversallyStronglySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L241). The attribute's comment: “universal condition (4)”.

> **Stacks 04A4, universal condition (4).** Condition (4) holds after every base
> change.

```lean
noncomputable abbrev IsUniversallyStronglySubmersive : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.IsSubmersive`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L142), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L114) (StacksFrontier): “condition (1): submersive”.
- [`AlgebraicGeometry.Space.UniversallySubmersive`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L151), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/TopologicalConditions.lean#L115) (StacksFrontier): “universal condition (1)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.7, Tag 04A3](https://stacks.math.columbia.edu/tag/04A3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
