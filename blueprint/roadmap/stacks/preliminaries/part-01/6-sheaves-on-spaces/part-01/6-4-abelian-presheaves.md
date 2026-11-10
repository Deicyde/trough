---
declaration: section
origin: cited
lean: singletonPresheaf, CategoryTheory.Limits.functorCategoryHasLimitsOfShape, CategoryTheory.FunctorToTypes.binaryProductEquiv, TopCat.Presheaf.addNegZeroAxiomsEquivAddNegZeroGroup, TopCat.Presheaf.addNegZeroGroupEquivAdditionGroup, TopCat.Presheaf.additionGroupEquivSectionwiseGroup, AddCommGrpCat, TopCat.Presheaf
statement: formalized
proof: formalized
---

# 6.4 Abelian presheaves

Section 6.4 of the Stacks Project, [Tag 006G](https://stacks.math.columbia.edu/tag/006G). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 006H, an example

[Tag 006H](https://stacks.math.columbia.edu/tag/006H) in the Stacks Project.

**`singletonPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/Terminal.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Terminal.lean#L59). References: EGA 0 (8.1.10), “special case”.

> The singleton presheaf on a topological space `X`: the constant functor at
> `PUnit` from `(Opens X)^op` to `Type u`.

```lean
def singletonPresheaf (X : TopCat) : TopCat.Presheaf (Type u) X
```

## Tag 006I, a lemma

[Tag 006I](https://stacks.math.columbia.edu/tag/006I) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.functorCategoryHasLimitsOfShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.functorCategoryHasLimitsOfShape#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Products.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Products.lean#L25) (StacksFrontier): “presheaves of sets form a functor category, which has products because `Type u` does”. References: SGA 4 I (9.6), “(ii)”.
- [`CategoryTheory.FunctorToTypes.binaryProductEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FunctorToTypes.binaryProductEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Products.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Products.lean#L28) (StacksFrontier): “sections of a binary product over `U` are pairs of sections over `U`”.

## Tag 006J, a lemma

[Tag 006J](https://stacks.math.columbia.edu/tag/006J) in the Stacks Project.

**`TopCat.Presheaf.addNegZeroAxiomsEquivAddNegZeroGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean#L212).

> **Stacks Tag 006J**, the bijection between structures of type (2) and type (3): the
> abelian group axioms for the maps of presheaves `+`, `-`, `0` say exactly that every
> quadruple `(P(U), +, -, 0)` is an abelian group.

```lean
def addNegZeroAxiomsEquivAddNegZeroGroup : AddNegZeroAxioms P ≃ AddNegZeroGroup P
```

**`TopCat.Presheaf.addNegZeroGroupEquivAdditionGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean#L313).

> **Stacks Tag 006J**, the bijection between structures of type (3) and type (4): the
> negation and the zero are determined by the addition, and are automatically maps of
> presheaves.

```lean
noncomputable def addNegZeroGroupEquivAdditionGroup :
    AddNegZeroGroup P ≃ AdditionGroup P
```

**`TopCat.Presheaf.additionGroupEquivSectionwiseGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/GroupStructures.lean#L341).

> **Stacks Tag 006J**, the bijection between structures of type (4) and type (1): an
> abelian group structure on each `P(U)` with additive restrictions is the same thing as a
> map of presheaves `+ : P × P ⟶ P` making each `P(U)` an abelian group.

```lean
noncomputable def additionGroupEquivSectionwiseGroup :
    AdditionGroup P ≃ SectionwiseGroup P
```

## Tag 006K, a definition

[Tag 006K](https://stacks.math.columbia.edu/tag/006K) in the Stacks Project.

Declarations registered for the tag:

- [`AddCommGrpCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AddCommGrpCat#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean#L29) (StacksFrontier): “the target category of abelian groups, which supplies the group structure on each `F(U)` and makes each restriction map a homomorphism”. References: SGA 4 I (2.3.2); SGA 7 VII (3.5), “special case”.
- [`TopCat.Presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean#L33) (StacksFrontier): “an abelian presheaf on `X` is a functor `(Opens X)ᵒᵖ ⥤ AddCommGrpCat`; the objects of `PAb(X)`”. References: SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.17), “special case”; SGA 4 I (1.2), “special case”; SGA 4 II (6.0), “special case”; SGA 4½ Arcata (1.6.3), “special case”.
- [`TopCat.instCategoryPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.instCategoryPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Abelian.lean#L40) (StacksFrontier): “morphisms of abelian presheaves are natural transformations, with group homomorphisms as components; the category `PAb(X)`”. References: SGA 3 IV (4.3.1), “special case”; SGA 4 I (1.2), “special case”.

## Tag 006L, an example

[Tag 006L](https://stacks.math.columbia.edu/tag/006L) in the Stacks Project.

**`F`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/DirectSumOverPoints.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/DirectSumOverPoints.lean#L108).

> The direct-sum-of-points presheaf of abelian groups on `X`.

```lean
noncomputable def F : TopCat.Presheaf AddCommGrpCat.{u} X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.4, Tag 006G](https://stacks.math.columbia.edu/tag/006G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
