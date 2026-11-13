---
declaration: section
origin: cited
lean: CategoryTheory.Functor, CategoryTheory.exists_not_isSheaf_yoneda_obj, CategoryTheory.yoneda, CategoryTheory.Yoneda.fullyFaithful
statement: formalized
proof: formalized
---

# 59.9 Presheaves

Section 59.9 of the Stacks Project, [Tag 03NB](https://stacks.math.columbia.edu/tag/03NB). 3 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03NC, a definition

[Tag 03NC](https://stacks.math.columbia.edu/tag/03NC) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L141) (StacksFrontier). References: EGA 0 (11.8.4), “more general”; SGA 3 I (1.1); SGA 3 I (2.1.1); SGA 3 IV (4.3.1); SGA 3 IV (4.3.17); SGA 3 VIIB (2.3.2), “more general”; SGA 3 VIB (6.1); SGA 3 X (9.2.1); SGA 4 I (1.1.1); SGA 4 I (1.2), “more general”; SGA 4 I (8.2.1); SGA 4 II (6.0); SGA 4 Vbis (1.2.6); SGA 4½ Arcata (1.6.3).

## Tag 03ND, an example

[Tag 03ND](https://stacks.math.columbia.edu/tag/03ND) in the Stacks Project.

**`CategoryTheory.exists_not_isSheaf_yoneda_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/NotSheaf.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Representable/NotSheaf.lean#L49). The attribute's comment: “the closing assertion: some representable presheaf on some site is not a sheaf”.

> Representable presheaves are not sheaves in every topology on every site: there are a small
> category `C`, a Grothendieck topology `J` on `C` and an object `X` of `C` such that the
> representable presheaf `h_X = yoneda.obj X` is not a sheaf for `J`. The witness is the discrete
> category on `ULift Bool` with the largest topology `⊤`, in which the empty sieve covers
> `true` while there is no morphism `true ⟶ false`.

```lean
public theorem exists_not_isSheaf_yoneda_obj :
    ∃ (C : Type u) (_ : SmallCategory C) (J : GrothendieckTopology C) (X : C),
      ¬ Presheaf.IsSheaf J (yoneda.obj X)
```

Declarations registered for the tag:

- [`CategoryTheory.yoneda`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yoneda#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L143) (StacksFrontier): “definition of h\_X, the representable presheaf `U ↦ Mor(U, X)`”. References: EGA 0 (8.1.1); EGA 0 (8.1.2); EGA 0 (8.1.3), “special case”; EGA 0 (8.1.7); EGA 0 (19.0.1); EGA I (3.4.1), “more general”; EGA I (3.4.3); EGA II (7.3.9), “more general”; EGA IV (8.14.2); SGA 3 I (1.1); SGA 3 IV (2.6); SGA 3 IV (4.5.5); SGA 3 IV (4.6.15); SGA 4 I (1.3), “(a), special case”; SGA 4 I (1.3.1); SGA 4 I (1.3.3); SGA 4 I (1.4.1); SGA 4 I (7.1.3), “C = E”; SGA 4 I (8.2.1); SGA 4 V (7.3.1.6), “more general”; SGA 4 VI (2.17).

## Tag 03NE, a lemma

[Tag 03NE](https://stacks.math.columbia.edu/tag/03NE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Yoneda.fullyFaithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Yoneda.fullyFaithful#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L145) (StacksFrontier). References: EGA 0 (8.1.7); SGA 3 I (1.1); SGA 3 I (1.1.1), “Hom\_D(X”; SGA 4 I (1.4).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.9, Tag 03NB](https://stacks.math.columbia.edu/tag/03NB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
