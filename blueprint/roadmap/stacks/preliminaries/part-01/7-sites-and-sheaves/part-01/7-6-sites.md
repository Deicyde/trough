---
declaration: section
origin: cited
lean: Opens.pretopology, Opens.grothendieckTopology, Opens.pretopology_toGrothendieck, TopCat.Presheaf.IsSheaf, TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types, CategoryTheory.Pretopology.toGrothendieck_bot, CategoryTheory.sheafBotEquivalence
statement: formalized
proof: formalized
---

# 7.6 Sites

Section 7.6 of the Stacks Project, [Tag 00VG](https://stacks.math.columbia.edu/tag/00VG). 2 tags here are carried by 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00VJ, an example

[Tag 00VJ](https://stacks.math.columbia.edu/tag/00VJ) in the Stacks Project.

Declarations registered for the tag:

- [`Opens.pretopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.pretopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L23) (StacksFrontier): “the site X_Zar: coverings of U are the families of opens with union U”. References: SGA 4 III (1.9.1); SGA 4½ Arcata (1.6.4), “partial”.
- [`Opens.grothendieckTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.grothendieckTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L25) (StacksFrontier): “the Grothendieck topology on the opens of X”. References: SGA 4 III (1.9.1); SGA 4 VII (4.2.2); SGA 4½ Arcata (1.1); SGA 4½ Arcata (1.6.4).
- [`Opens.pretopology_toGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.pretopology_toGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L26) (StacksFrontier): “the covering families generate the Grothendieck topology of X_Zar”.
- [`TopCat.Presheaf.IsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L28) (StacksFrontier): “sheaves on a space are by definition sheaves on the site X_Zar”. References: EGA 0 (3.1.2); EGA 0 (3.1.4); SGA 3 IV (4.3.1), “special case”; SGA 4 IV (2.1), “partial”; SGA 4½ Arcata (1.2.3), “more general”; SGA 4½ Arcata (1.6.3), “special case”.
- [`TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L30) (StacksFrontier): “sheaves of sets on X_Zar agree with the usual unique-gluing sheaves on X”. References: EGA 0 (3.1.2), “C = Set”; SGA 3 IV (4.3.5), “special case”; SGA 4½ Arcata (1.6.3), “topological site”.

## Tag 07GE, an example

[Tag 07GE](https://stacks.math.columbia.edu/tag/07GE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Pretopology.toGrothendieck_bot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretopology.toGrothendieck_bot#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Pretopology.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Pretopology.lean#L28) (StacksCore): “the chaotic pretopology generates the bottom topology, in which only the maximal sieve covers”.
- [`CategoryTheory.sheafBotEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafBotEquivalence#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Pretopology.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Pretopology.lean#L30) (StacksCore): “sheaves on the chaotic site are the presheaves: the forgetful functor from sheaves for the bottom topology to presheaves is an equivalence of categories”. References: SGA 3 IV (4.4.2), “final observation”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.6, Tag 00VG](https://stacks.math.columbia.edu/tag/00VG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
