---
declaration: section
origin: cited
lean: PresheafOfModules.freeObj, CategoryTheory.yonedaEquiv, CategoryTheory.Adjunction.whiskerRight, AddCommGrpCat.adj, CategoryTheory.Adjunction.leftAdjoint_preservesColimits, CategoryTheory.Limits.PreservesCoproduct.iso
statement: formalized
proof: formalized
---

# 18.4 Free abelian presheaves

Section 18.4 of the Stacks Project, [Tag 03CP](https://stacks.math.columbia.edu/tag/03CP). 3 tags here are carried by 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03A7, a definition

[Tag 03A7](https://stacks.math.columbia.edu/tag/03A7) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.freeObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.freeObj#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L38) (StacksFrontier): “for the constant presheaf of rings ℤ this is the free abelian presheaf U ↦ ℤ[G(U)], and Z\_X is its value at the presheaf yoneda X”.

## Tag 03A8, a lemma

[Tag 03A8](https://stacks.math.columbia.edu/tag/03A8) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.yonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yonedaEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L20) (StacksFrontier): “(1) Yoneda”. References: EGA 0 (8.1.3); EGA 0 (8.1.4); EGA 0 (8.1.6), “more general”; EGA 0 (8.1.8), “partial, special case”; SGA 3 I (1.1); SGA 3 I (1.1.1), “more general”; SGA 3 I (1.6.1), “Hom(h\_S, F) ≃ F(S)”; SGA 3 I (1.7.0), “partial”; SGA 3 IV (4.3.1), “partial”; SGA 4 I (1.4), “bijection Hom(h(X)”; SGA 4 I (8.3.2), “partial”.
- [`CategoryTheory.Adjunction.whiskerRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.whiskerRight#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L21) (StacksFrontier): “(2), (3) Z\_G ⊣ forget”.
- [`AddCommGrpCat.adj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AddCommGrpCat.adj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L22) (StacksFrontier): “free ⊣ forget on Ab”. References: SGA 4 I (5.8.2), “special case”; SGA 4 II (6.5), “special case”.

## Tag 03A9, a lemma

[Tag 03A9](https://stacks.math.columbia.edu/tag/03A9) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.whiskerRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.whiskerRight#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L25) (StacksFrontier): “Z\_(-) is a left adjoint”.
- [`CategoryTheory.Adjunction.leftAdjoint_preservesColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.leftAdjoint_preservesColimits#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L26) (StacksFrontier): “preserves coproducts”. References: SGA 4 I (5.4), “more general”; SGA 4 I (8.7.1.7), “more general”; SGA 4 IV (3.1.3), “partial”; SGA 4 IV (4.5.1), “more general”.
- [`CategoryTheory.Limits.PreservesCoproduct.iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.PreservesCoproduct.iso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Adjunction/Whiskering.lean#L27) (StacksFrontier): “Z\_\{∐ G\_i} ≅ ⊕ Z\_\{G\_i}”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.4, Tag 03CP](https://stacks.math.columbia.edu/tag/03CP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
