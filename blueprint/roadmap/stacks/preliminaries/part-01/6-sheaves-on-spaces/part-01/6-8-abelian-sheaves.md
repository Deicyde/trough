---
declaration: section
origin: cited
lean: TopCat.Presheaf.isSheaf_iff_isSheaf_comp, TopCat.Sheaf, TopCat.instCategorySheaf
statement: formalized
proof: formalized
---

# 6.8 Abelian sheaves

Section 6.8 of the Stacks Project, [Tag 006Z](https://stacks.math.columbia.edu/tag/006Z). 1 tag here is carried by 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0070, a definition

[Tag 0070](https://stacks.math.columbia.edu/tag/0070) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.isSheaf_iff_isSheaf_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheaf_comp#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean#L32) (StacksFrontier): “an abelian presheaf is a sheaf exactly when its underlying presheaf of sets is one: the sheaf condition is unchanged by composing with a limit-preserving, isomorphism-reflecting functor, here the forgetful functor to types.”. References: SGA 4 II (6.2), “special case”; SGA 4 II (6.3.1), “topological space”.
- [`TopCat.Sheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean#L42) (StacksFrontier): “Sheaves of abelian groups on `X` are the objects of `TopCat.Sheaf AddCommGrpCat X`; Mathlib states the sheaf condition for a general target category rather than naming the abelian case, and has no notation `Ab(X)`.”. References: EGA 0 (3.1.4); EGA 0 (3.1.2); SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.18), “special case”; SGA 4 II (6.1), “special case”; SGA 4 IV (0.1), “special case”; SGA 4 IV (2.1); SGA 4 VI (1.22.1); SGA 4 Vbis (4.2.0), “Fiber of E over a scheme”; SGA 4½ Arcata (1.2.3), “more general”; SGA 4½ Arcata (1.6.3), “topological site”; SGA 4 II (2.1), “opens of a space”.
- [`TopCat.instCategorySheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.instCategorySheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/Abelian.lean#L58) (StacksFrontier): “The category structure on `Ab(X) = TopCat.Sheaf AddCommGrpCat X`, derived from the category of sheaves on the site of opens of `X`.”. References: SGA 3 IV (4.3.1), “special case”; SGA 4 II (6.1), “special case”; SGA 4 IV (0.1), “special case”; SGA 4 IV (2.1), “partial”; SGA 4 II (2.1), “opens of a space”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.8, Tag 006Z](https://stacks.math.columbia.edu/tag/006Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
