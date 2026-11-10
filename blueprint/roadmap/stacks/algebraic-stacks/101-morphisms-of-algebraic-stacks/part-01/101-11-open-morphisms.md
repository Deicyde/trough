---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representable_universallyOpen_iff_openMap_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.IsOpen, AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyOpen, AlgebraicGeometry.Stack.AlgebraicStacks.universallyOpen_baseChange_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.isOpen_comp, AlgebraicGeometry.Stack.AlgebraicStacks.universallyOpen_comp
statement: formalized
proof: formalized
---

# 101.11 Open morphisms

Section 101.11 of the Stacks Project, [Tag 06U0](https://stacks.math.columbia.edu/tag/06U0). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06U1, a lemma

[Tag 06U1](https://stacks.math.columbia.edu/tag/06U1) in the Stacks Project.

**`AlgebraicGeometry.Stack.representable_universallyOpen_iff_openMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenCriterion.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenCriterion.lean#L511).

> **Stacks 06U1.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` which is
> representable by algebraic spaces, the two conditions
>
> 1. `f` is universally open in the sense of Properties of Stacks, Section 04XB, that is
>    `AlgebraicGeometry.Stack.UniversallyOpen`; and
> 2. for every 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S` the map `|𝒵 ×_𝒴 𝒳| → |𝒵|` on the
>    points of Stacks 04XG for the topology of Stacks 04XL is open, that is
>    `AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyOpen`
>
> are equivalent.

```lean
theorem representable_universallyOpen_iff_openMap_baseChange
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    UniversallyOpen B S hS f.hom ↔ AlgebraicStacks.UniversallyOpen B S hS f
```

## Tag 06U2, a definition

[Tag 06U2](https://stacks.math.columbia.edu/tag/06U2) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenAlgebraicStack.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenAlgebraicStack.lean#L50). The attribute's comment: “part (1): open”.

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is open* when the map `|𝒳| → |𝒴|` it
> induces on the topological spaces of points is an open map.

```lean
abbrev IsOpen {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenAlgebraicStack.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenAlgebraicStack.lean#L59). The attribute's comment: “part (2): universally open”.

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is universally open* when, for every
> 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S`, the base change `𝒵 ×_{g, 𝒴, f} 𝒳 ⟶ 𝒵` of `f`
> by `g` is open in the sense of `AlgebraicGeometry.Stack.AlgebraicStacks.IsOpen`.

```lean
abbrev UniversallyOpen {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06U3, a lemma

[Tag 06U3](https://stacks.math.columbia.edu/tag/06U3) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyOpen_baseChange_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenSubmersiveBaseChange.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenSubmersiveBaseChange.lean#L200).

> **Stacks 06U3.** Universal openness is stable under base change: let `f : 𝒳 ⟶ 𝒴` be a
> universally open 1-morphism of algebraic stacks over `S` and let `R` be a 2-fibre product square
> of the cospan `(g, f)` for some `g : 𝒴' ⟶ 𝒴`. Then the base change `R.fst : R.pt ⟶ 𝒴'` of `f`
> along `g` is universally open.
>
> The square is arbitrary, so this applies to any square a consumer has already exhibited as a
> 2-fibre product rather than only to the canonical one of Stacks 04T2.

```lean
theorem universallyOpen_baseChange_of_isTwoFibreProduct
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴}
    (R : Bicategory.TwoCommSq g f) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : UniversallyOpen B S hS f) :
    UniversallyOpen B S hS R.fst
```

## Tag 06U4, a lemma

[Tag 06U4](https://stacks.math.columbia.edu/tag/06U4) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpen_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveComposition.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveComposition.lean#L70). The attribute's comment: “composition_open”.

> **Stacks 06U4.** The composite of two open 1-morphisms of algebraic stacks over `S` is
> open.

```lean
theorem isOpen_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsOpen B S hS f) (hg : IsOpen B S hS g) :
    IsOpen B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyOpen_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveUniversalComposition.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveUniversalComposition.lean#L115). The attribute's comment: “composition_universally_open”.

> **Stacks 06U4.** The composite of two universally open 1-morphisms of algebraic stacks over
> `S` is universally open.

```lean
theorem universallyOpen_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : UniversallyOpen B S hS f) (hg : UniversallyOpen B S hS g) :
    UniversallyOpen B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.11, Tag 06U0](https://stacks.math.columbia.edu/tag/06U0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
