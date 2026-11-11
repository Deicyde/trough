---
declaration: section
origin: cited
lean: Deformation.PointwiseGroupoid.finiteArrows
statement: formalized
proof: formalized
---

# 79.13 Finite collections of arrows

Section 79.13 of the Stacks Project, [Tag 04RS](https://stacks.math.columbia.edu/tag/04RS). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04RS, the section

[Tag 04RS](https://stacks.math.columbia.edu/tag/04RS) in the Stacks Project.

**`Deformation.PointwiseGroupoid.finiteArrows`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FiniteArrows.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FiniteArrows.lean#L621). The attribute's comment: “the groupoid of finite collections of arrows”.

> **Stacks 04RS.** The septuple of finite collections of arrows of a groupoid is a groupoid:
> its objects are the finite subsets `Z` of the arrows with `s(Z)` a singleton `{u}` and
> `e(u) ∈ Z`, its arrows are the pairs `(Z, z)` with `z ∈ Z`, the source of `(Z, z)` is `Z`, its
> target is `{z' ∘ z⁻¹ : z' ∈ Z}`, and the composite of `(Z₁, z₁)` with `(Z₂, z₂)` is
> `(Z₂, z₁ ∘ z₂)`.
>
> The verification is a reflection along the faithful pair of maps `Z ↦ u` and `(Z, z) ↦ z`, which
> carries the unit, the composition and the inverse of `C_fin` to those of the original groupoid.

```lean
def finiteArrows (P : PointwiseGroupoid source target comp) :
    PointwiseGroupoid (FiniteArrows.src P) (FiniteArrows.tgt P) (FiniteArrows.compose P)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.13, Tag 04RS](https://stacks.math.columbia.edu/tag/04RS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
