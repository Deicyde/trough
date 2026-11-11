---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyConstructible_preimage, AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_specializes_subset
statement: formalized
proof: formalized
---

# 29.23 Constructible sets

Section 29.23 of the Stacks Project, [Tag 054H](https://stacks.math.columbia.edu/tag/054H). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 054I, a lemma

[Tag 054I](https://stacks.math.columbia.edu/tag/054I) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_preimage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Constructible.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Constructible.lean#L63). The attribute's comment: “locally constructible case”. References: EGA IV (1.8.2), “locally constructible”; EGA IV (9.2.2), “Forward implication only”.

> **Stacks Project, Tag 054I.** The inverse image of a locally constructible
> subset under a morphism of schemes is locally constructible.

```lean
public lemma isLocallyConstructible_preimage {X Y : Scheme.{u}} (f : X ⟶ Y)
    {s : Set Y} (hs : IsLocallyConstructible s) :
    IsLocallyConstructible (f ⁻¹' s)
```

## Tag 05LW, a lemma

[Tag 05LW](https://stacks.math.columbia.edu/tag/05LW) in the Stacks Project.

**`AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_specializes_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Constructible.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Constructible.lean#L85). References: EGA 0 (9.2.5), “sufficiency”; SGA 3 XV (3.3), “partial”.

> **Stacks Project, Tag 05LW.** A locally constructible subset of a scheme that contains every
> generalization of `x` contains an open neighbourhood of `x`.

```lean
public theorem mem_nhds_of_isLocallyConstructible_of_specializes_subset
    {X : Scheme.{u}} {E : Set X} {x : X} (hE : IsLocallyConstructible E)
    (h : {x' : X | x' ⤳ x} ⊆ E) :
    E ∈ 𝓝 x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.23, Tag 054H](https://stacks.math.columbia.edu/tag/054H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
