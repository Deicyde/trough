---
declaration: section
origin: cited
lean: CategoryTheory.Functor.relativelyRepresentable.map, CategoryTheory.Functor.relativelyRepresentable.isMultiplicative, CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange, AlgebraicGeometry.Space.relativelyRepresentable_prod_map, AlgebraicGeometry.Space.isSheaf_of_relativelyRepresentable, AlgebraicGeometry.Space.relativelyRepresentable_diagonal
statement: formalized
proof: formalized
---

# 65.3 Representable morphisms of presheaves

Section 65.3 of the Stacks Project, [Tag 025U](https://stacks.math.columbia.edu/tag/025U). 6 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02W9, a lemma

[Tag 02W9](https://stacks.math.columbia.edu/tag/02W9) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean#L59) (StacksFrontier): “for the Yoneda embedding of a category with fibre products, `h_f` is representable”.

## Tag 02WA, a lemma

[Tag 02WA](https://stacks.math.columbia.edu/tag/02WA) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isMultiplicative`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isMultiplicative#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean#L63) (StacksFrontier): “representable transformations are stable under composition”.

## Tag 02WB, a lemma

[Tag 02WB](https://stacks.math.columbia.edu/tag/02WB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean#L66) (StacksFrontier): “representable transformations are stable under base change”.

## Tag 02WC, a lemma

[Tag 02WC](https://stacks.math.columbia.edu/tag/02WC) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_prod_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Products.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Products.lean#L44).

> **Stacks Project, Tag 02WC.** The product of two representable transformations of
> presheaves on the big fppf site over `S` is representable.

```lean
public theorem relativelyRepresentable_prod_map
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F₁ G₁ F₂ G₂ : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a₁ : F₁ ⟶ G₁) (a₂ : F₂ ⟶ G₂)
    (h₁ : yoneda.relativelyRepresentable a₁) (h₂ : yoneda.relativelyRepresentable a₂) :
    yoneda.relativelyRepresentable (prod.map a₁ a₂)
```

## Tag 02WD, a lemma

[Tag 02WD](https://stacks.math.columbia.edu/tag/02WD) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheaf_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Sheaf.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Sheaf.lean#L39).

> A representable transformation into a sheaf on the big fppf site over `S` has a sheaf as its
> source.

```lean
public theorem isSheaf_of_relativelyRepresentable
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (ha : yoneda.relativelyRepresentable a)
    (hG : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) G) :
    Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) F
```

## Tag 05L9, a lemma

[Tag 05L9](https://stacks.math.columbia.edu/tag/05L9) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Diagonal.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Diagonal.lean#L36).

> The diagonal of a representable transformation of presheaves on the big fppf site over `S` is
> representable.

```lean
public theorem relativelyRepresentable_diagonal
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (ha : yoneda.relativelyRepresentable a) :
    yoneda.relativelyRepresentable (pullback.diagonal a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.3, Tag 025U](https://stacks.math.columbia.edu/tag/025U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
