---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsSurjective, AlgebraicGeometry.Stack.isSurjective_comp, AlgebraicGeometry.Stack.isSurjective_of_isTwoFibreProduct, AlgebraicGeometry.Stack.isSurjective_of_isSurjective_twoCommSq_fst, AlgebraicGeometry.Stack.isSurjective_of_isSurjective_comp
statement: formalized
proof: formalized
---

# 100.5 Surjective morphisms

Section 100.5 of the Stacks Project, [Tag 04ZR](https://stacks.math.columbia.edu/tag/04ZR). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04ZS, a definition

[Tag 04ZS](https://stacks.math.columbia.edu/tag/04ZS) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsSurjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Surjective.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Surjective.lean#L99).

> **Stacks 04ZS.** A morphism of algebraic stacks is surjective if its map on points is
> surjective.

```lean
abbrev IsSurjective {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 04ZT, a lemma

[Tag 04ZT](https://stacks.math.columbia.edu/tag/04ZT) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean#L46).

> The composite of two surjective 1-morphisms of algebraic stacks over `S` is surjective.

```lean
theorem isSurjective_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsSurjective B S hS f) (hg : IsSurjective B S hS g) :
    IsSurjective B S hS (f ≫ g)
```

## Tag 04ZU, a lemma

[Tag 04ZU](https://stacks.math.columbia.edu/tag/04ZU) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjective_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveBaseChange.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveBaseChange.lean#L146).

> **Stacks 04ZU.** The base change of a surjective 1-morphism of algebraic stacks over `S` is
> surjective: in a 2-fibre-product square over the cospan `(g, f)`, if `g` is surjective then so is
> the projection to the source of `f`.

```lean
theorem isSurjective_of_isTwoFibreProduct
    {𝒵 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {g : 𝒵 ⟶ 𝒴} {f : 𝒳 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsSurjective B S hS g) : IsSurjective B S hS P.snd
```

## Tag 06PM, a lemma

[Tag 06PM](https://stacks.math.columbia.edu/tag/06PM) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjective_of_isSurjective_twoCommSq_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean#L64). References: SGA 1 VIII (3.1), “f' surj => f surj”.

> Surjectivity of a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` descends along a
> surjective 1-morphism `g : 𝒵 ⟶ 𝒴`: if some 2-commutative square over the cospan `(g, f)` has
> surjective first projection, then `f` is surjective.

```lean
theorem isSurjective_of_isSurjective_twoCommSq_fst {g : 𝒵 ⟶ 𝒴} {f : 𝒳 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hg : IsSurjective B S hS g)
    (hfst : IsSurjective B S hS P.fst) : IsSurjective B S hS f
```

## Tag 06PN, a lemma

[Tag 06PN](https://stacks.math.columbia.edu/tag/06PN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjective_of_isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveProperties.lean#L55).

> If a composite of 1-morphisms of algebraic stacks over `S` is surjective, then so is its
> second factor.

```lean
theorem isSurjective_of_isSurjective_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsSurjective B S hS (f ≫ g)) : IsSurjective B S hS g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.5, Tag 04ZR](https://stacks.math.columbia.edu/tag/04ZR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
