---
declaration: section
origin: cited
lean: Stacks.AffineSpace.affineNSpace
statement: formalized
proof: formalized
---

# 27.5 Affine n-space

Section 27.5 of the Stacks Project, [Tag 01LZ](https://stacks.math.columbia.edu/tag/01LZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01M0, a definition

[Tag 01M0](https://stacks.math.columbia.edu/tag/01M0) in the Stacks Project.

**`Stacks.AffineSpace.affineNSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/AffineSpace.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/AffineSpace.lean#L287). The attribute's comment: “affine n-space over S, the relative spectrum of the polynomial algebra O\_S[T\_1, ..., T\_n], as a scheme over S”. References: EGA IV (5.5.5).

> **Affine `n`-space over a scheme.** For a scheme `S` and an integer `n ≥ 0`, affine `n`-space
> `𝐀ⁿ_S = Spec_S(𝒪_S[T_1, …, T_n])` over `S` is the relative spectrum of the quasi-coherent sheaf
> of `𝒪_S`-algebras `𝒪_S[T_1, …, T_n]`, as a scheme over `S`. For `S = Spec R` this is affine
> `n`-space `𝐀ⁿ_R` over `R`.
>
> Here `𝒪_S[T_1, …, T_n]` is the sheaf associated to the presheaf `U ↦ 𝒪_S(U)[T_1, …, T_n]`,
> whose sections over an affine open `U` are `𝒪_S(U)[T_1, …, T_n]`
> (`Stacks.AffineSpace.bijective_toSheafify_app`), and the result is Mathlib's `𝔸(n; S)` over `S`
> by `Stacks.AffineSpace.affineSpaceIso`.

```lean
abbrev affineNSpace (n : ℕ) : Over S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.5, Tag 01LZ](https://stacks.math.columbia.edu/tag/01LZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
