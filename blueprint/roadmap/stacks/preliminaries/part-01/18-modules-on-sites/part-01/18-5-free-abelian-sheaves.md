---
declaration: section
origin: cited
lean: CategoryTheory.Presheaf.freeAbelianSheafObj, CategoryTheory.Presheaf.freeAbelianSheafYoneda, CategoryTheory.sheafificationAdjunction, CategoryTheory.yonedaEquiv, CategoryTheory.Sheaf.composeAndSheafify, CategoryTheory.Sheaf.adjunction, CategoryTheory.Sheaf.freeYonedaHomEquiv, CategoryTheory.Sheaf.preservesSheafification_of_adjunction
statement: formalized
proof: formalized
---

# 18.5 Free abelian sheaves

Section 18.5 of the Stacks Project, [Tag 03CQ](https://stacks.math.columbia.edu/tag/03CQ). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03AA, a definition

[Tag 03AA](https://stacks.math.columbia.edu/tag/03AA) in the Stacks Project.

**`CategoryTheory.Presheaf.freeAbelianSheafObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/FreeAbelianSheaf.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/FreeAbelianSheaf.lean#L49). The attribute's comment: “Z_G^#, the sheafification of the free abelian presheaf U ↦ ℤ[G(U)]”.

> The free abelian sheaf `ℤ_G^♯` on a presheaf of sets `G`: the sheafification of the free
> abelian presheaf `U ↦ ℤ[G(U)]`.

```lean
noncomputable def freeAbelianSheafObj (G : Cᵒᵖ ⥤ Type w) : Sheaf J AddCommGrpCat.{w}
```

**`CategoryTheory.Presheaf.freeAbelianSheafYoneda`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/FreeAbelianSheaf.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/FreeAbelianSheaf.lean#L63). The attribute's comment: “Z_X^#: the case G = h_X”.

> The free abelian sheaf `ℤ_X^♯` on an object `X` of the site: the free abelian sheaf on the
> representable presheaf `h_X`.

```lean
noncomputable abbrev freeAbelianSheafYoneda [HasWeakSheafify J AddCommGrpCat.{v}] (X : C) :
    Sheaf J AddCommGrpCat.{v}
```

## Tag 03AB, a lemma

[Tag 03AB](https://stacks.math.columbia.edu/tag/03AB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.sheafificationAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafificationAdjunction#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L28) (StacksCore): “(1) sheafification adj”. References: EGA 0 (3.5.6), “more general”; SGA 4 IV (10.4.1).
- [`CategoryTheory.yonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yonedaEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L29) (StacksCore): “(1) Yoneda”. References: EGA 0 (8.1.3); EGA 0 (8.1.4); EGA 0 (8.1.6), “more general”; EGA 0 (8.1.8), “partial, special case”; SGA 3 I (1.1); SGA 3 I (1.1.1), “more general”; SGA 3 I (1.6.1), “Hom(h_S, F) ≃ F(S)”; SGA 3 I (1.7.0), “partial”; SGA 3 IV (4.3.1), “partial”; SGA 4 I (1.4), “bijection Hom(h(X)”; SGA 4 I (8.3.2), “partial”.
- [`CategoryTheory.Sheaf.composeAndSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.composeAndSheafify#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L30) (StacksCore): “(2) Z_G^#”.
- [`CategoryTheory.Sheaf.adjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.adjunction#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L31) (StacksCore): “(2) Z_G^# ⊣ forget”.
- [`CategoryTheory.Sheaf.freeYonedaHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.freeYonedaHomEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L32) (StacksCore): “(3) Mor(Z_U^#, A)”.

## Tag 03AC, a lemma

[Tag 03AC](https://stacks.math.columbia.edu/tag/03AC) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.preservesSheafification_of_adjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.preservesSheafification_of_adjunction#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L37) (StacksCore): “free preserves (-)^#”.
- [`CategoryTheory.presheafToSheafCompComposeAndSheafifyIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.presheafToSheafCompComposeAndSheafifyIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L39) (StacksCore): “Z_G^# ≅ (Z_{G^#})^#”.
- [`AddCommGrpCat.adj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AddCommGrpCat.adj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Adjunction.lean#L40) (StacksCore): “free ⊣ forget on Ab”. References: SGA 4 I (5.8.2), “special case”; SGA 4 II (6.5), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.5, Tag 03CQ](https://stacks.math.columbia.edu/tag/03CQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
