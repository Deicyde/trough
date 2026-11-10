---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAlgebraicSpace, AlgebraicGeometry.isAlgebraicSpace_yoneda, CategoryTheory.NatTrans, CategoryTheory.Functor.category
statement: formalized
proof: formalized
---

# 65.6 Algebraic spaces

Section 65.6 of the Stacks Project, [Tag 025X](https://stacks.math.columbia.edu/tag/025X). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025Y, a definition

[Tag 025Y](https://stacks.math.columbia.edu/tag/025Y) in the Stacks Project.

**`AlgebraicGeometry.IsAlgebraicSpace`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Basic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Basic.lean#L96).

> **Stacks 025Y.** A presheaf of sets on the big fppf site of `S` is an *algebraic space*
> over `S` when it is an fppf sheaf, has representable diagonal, and admits a surjective
> étale morphism from a representable presheaf.

```lean
structure IsAlgebraicSpace (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 025Z, a lemma

[Tag 025Z](https://stacks.math.columbia.edu/tag/025Z) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L236).

> **Stacks 025Z.** The representable presheaf of a scheme over `S` is an algebraic space
> over `S`.

```lean
theorem isAlgebraicSpace_yoneda (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (T : BigFppfOver B S hS) : IsAlgebraicSpace B S hS (yoneda.obj T)
```

## Tag 0260, a definition

[Tag 0260](https://stacks.math.columbia.edu/tag/0260) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.NatTrans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.NatTrans#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L298) (StacksFrontier). References: EGA 0 (3.1.4); EGA 0 (3.2.3), “more general”; EGA 0 (8.1.3); EGA 0 (8.2.1); SGA 3 I (1.1); SGA 3 I (2.1.1), “more general”; SGA 3 VIIB (2.3.2), “definition of Hom\_k-Gr(G”; SGA 4 I (1.1.1); SGA 4 I (4.3).
- [`CategoryTheory.Functor.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.category#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L308) (StacksFrontier). References: SGA 4 I (1.1.1).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.6, Tag 025X](https://stacks.math.columbia.edu/tag/025X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
