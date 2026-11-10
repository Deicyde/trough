---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.picardFirstOrderSequence
statement: formalized
proof: formalized
---

# 76.11 Picard groups of thickenings

Section 76.11 of the Stacks Project, [Tag 0DNL](https://stacks.math.columbia.edu/tag/0DNL). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DNM, a lemma

[Tag 0DNM](https://stacks.math.columbia.edu/tag/0DNM) in the Stacks Project.

**`AlgebraicGeometry.Space.picardFirstOrderSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/PicardSequence.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/PicardSequence.lean#L317). References: EGA IV (21.13.9), “The exact segment H¹(U”.

> **Stacks Project, Tag 0DNM.** Let `S` be a scheme and let `X ⊂ X'` be a first-order
> thickening of algebraic spaces over `S` with ideal sheaf `𝓘`. Then there is a canonical exact
> sequence
>
> `0 → H⁰(X,𝓘) → H⁰(X',𝒪*_{X'}) → H⁰(X,𝒪*_X) → H¹(X,𝓘) → Pic(X') → Pic(X) → H²(X,𝓘) → ⋯`
>
> which continues in every degree.
>
> It is the long exact cohomology sequence of
> `0 → 𝓘 → 𝒪*_{X'} → 𝒪*_X → 0` on the common small étale site, with the two degree-one unit
> cohomology groups read as Picard groups by Tag 040E.

```lean
def picardFirstOrderSequence : PicardFirstOrderSequence B S hS hG
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.11, Tag 0DNL](https://stacks.math.columbia.edu/tag/0DNL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
