---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.embeddingDimension, AlgebraicGeometry.Scheme.Hom.embeddingDimension
statement: formalized
proof: formalized
---

# 33.46 Embedding dimension

Section 33.46 of the Stacks Project, [Tag 0C2G](https://stacks.math.columbia.edu/tag/0C2G). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0C1Q, a definition

[Tag 0C1Q](https://stacks.math.columbia.edu/tag/0C1Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.embeddingDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/EmbeddingDimension.lean, line 49](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Variety/Tangent/EmbeddingDimension.lean#L49).

> The dimension of the cotangent space of the local ring of `X` at `x`, over its
> residue field.

```lean
abbrev Scheme.embeddingDimension (X : Scheme.{u}) (x : X) [FiniteDimensional
    (ResidueField (X.presheaf.stalk x)) (CotangentSpace (X.presheaf.stalk x))] : ℕ
```

## Tag 0C2H, a definition

[Tag 0C2H](https://stacks.math.columbia.edu/tag/0C2H) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.embeddingDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/EmbeddingDimension.lean, line 55](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Variety/Tangent/EmbeddingDimension.lean#L55).

> The dimension over `κ(x)` of the tangent space of `X` over `k` at `x`.

```lean
abbrev Scheme.Hom.embeddingDimension (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (x : X) : ℕ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.46, Tag 0C2G](https://stacks.math.columbia.edu/tag/0C2G)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
