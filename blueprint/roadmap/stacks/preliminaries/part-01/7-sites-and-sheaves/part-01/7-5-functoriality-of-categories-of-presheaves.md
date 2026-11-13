---
declaration: section
origin: cited
lean: ColimCategory.objEquiv, ColimCategory.homEquiv, CategoryTheory.structuredArrow_op_span_and_parallelPair_completion, isFiltered_op_structuredArrow, CategoryTheory.Functor.lanUnit, CategoryTheory.NatTrans.naturality, CategoryTheory.Functor.whiskeringLeft, CategoryTheory.Functor.lan
statement: formalized
proof: formalized
---

# 7.5 Functoriality of categories of presheaves

Section 7.5 of the Stacks Project, [Tag 00VC](https://stacks.math.columbia.edu/tag/00VC). 6 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 053L, an equation

[Tag 053L](https://stacks.math.columbia.edu/tag/053L) in the Stacks Project.

**`ColimCategory.objEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/IndexEquivalence.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/IndexEquivalence.lean#L50). The attribute's comment: “Ob”.

> The type of *objects* of `I^u_V` is exactly the comprehension
> `{(U, φ) | U : Ob C, φ : V ⟶ u U}`, formalized as the dependent pair type
> `Σ U : C, (V ⟶ u U)`.

```lean
def objEquiv : I u V ≃ Σ U : C, (V ⟶ u.obj U)
```

**`ColimCategory.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/IndexEquivalence.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/IndexEquivalence.lean#L62). The attribute's comment: “Mor”.

> The type of *morphisms* in `I^u_V` from `(U, φ)` to `(U', φ')` is exactly the comprehension
> `{f : U ⟶ U' | u f ∘ φ = φ'}`, formalized as the subtype of morphisms `f : U ⟶ U'` satisfying
> `φ ≫ u f = φ'` (note the diagrammatic-order composition in Mathlib).

```lean
def homEquiv (X Y : I u V) :
    (X ⟶ Y) ≃ { f : X.right ⟶ Y.right // X.hom ≫ u.map f = Y.hom }
```

## Tag 00X4, a lemma

[Tag 00X4](https://stacks.math.columbia.edu/tag/00X4) in the Stacks Project.

**`CategoryTheory.structuredArrow_op_span_and_parallelPair_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/StructuredArrowCompletion.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/StructuredArrowCompletion.lean#L70).

> If `C` has fibre products and equalizers and `u : C ⥤ D` preserves them, then for every
> `V : D`, in `(StructuredArrow V u)ᵒᵖ` every span can be completed to a commutative square and every
> parallel pair can be coequalized.

```lean
theorem structuredArrow_op_span_and_parallelPair_completion
    (u : C ⥤ D) [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u]
    [PreservesLimitsOfShape WalkingParallelPair u]
    (V : D) :
    (∀ (w x y : (StructuredArrow V u)ᵒᵖ) (a : w ⟶ x) (b : w ⟶ y),
        ∃ (z : (StructuredArrow V u)ᵒᵖ) (c : x ⟶ z) (d : y ⟶ z),
          a ≫ c = b ≫ d) ∧
    (∀ (x y : (StructuredArrow V u)ᵒᵖ) (a b : x ⟶ y),
        ∃ (z : (StructuredArrow V u)ᵒᵖ) (c : y ⟶ z),
          a ≫ c = b ≫ c)
```

## Tag 00X3, a lemma

[Tag 00X3](https://stacks.math.columbia.edu/tag/00X3) in the Stacks Project.

**`isFiltered_op_structuredArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/StructuredArrowFiltered.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/StructuredArrowFiltered.lean#L101). References: SGA 5 V (2.3.3), “special case”.

> **Stacks 00X3.** Let `u : C ⥤ D` be a functor. Suppose `C` has a terminal
> object whose image under `u` is terminal in `D`, and `C` has fibre products
> which `u` preserves. Then for every `V : D` the opposite of the comma category
> `StructuredArrow V u` is filtered.

```lean
theorem isFiltered_op_structuredArrow
    (u : C ⥤ D) [HasTerminal C] [HasPullbacks C]
    [PreservesLimitsOfShape (Discrete PEmpty.{1}) u]
    [PreservesLimitsOfShape WalkingCospan u] (V : D) :
    IsFiltered (StructuredArrow V u)ᵒᵖ
```

## Tag 00VD, a lemma

[Tag 00VD](https://stacks.math.columbia.edu/tag/00VD) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.lanUnit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.lanUnit#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionIndexCategory.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionIndexCategory.lean#L28) (StacksFrontier): “the canonical map `F(U) ⟶ u_p F (u U)` is the unit of `u_p ⊣ u^p`”.
- [`CategoryTheory.NatTrans.naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.NatTrans.naturality#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionIndexCategory.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionIndexCategory.lean#L30) (StacksFrontier): “compatibility with the restriction maps is naturality of that unit”. References: EGA 0 (8.2.1), “more general”.

## Tag 00VE, a lemma

[Tag 00VE](https://stacks.math.columbia.edu/tag/00VE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean#L26) (StacksFrontier): “the restriction functor `u^p : PSh(D) ⥤ PSh(C)` is precomposition with `u.op`”. References: EGA III (7.1.3), “partial”.
- [`CategoryTheory.Functor.lan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.lan#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean#L28) (StacksFrontier): “the functor `u_p : PSh(C) ⥤ PSh(D)` is left Kan extension along `u.op`”.
- [`CategoryTheory.Functor.lanAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.lanAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionLeftAdjoint.lean#L30) (StacksFrontier): “`u_p` is left adjoint to `u^p`”. References: SGA 4 IV (4.6.1), “partial”.

## Tag 04D2, a lemma

[Tag 04D2](https://stacks.math.columbia.edu/tag/04D2) in the Stacks Project.

**`presheafPushforward_yoneda_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PresheafPullbackPushforward.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PresheafPullbackPushforward.lean#L98). References: SGA 4 I (5.4), “Clause 3”.

> **Stacks 04D2.** The pushforward `u_p` sends `h_U` to `h_{u(U)}`.
> Both `(presheafPushforward04D2 u).obj (yoneda.obj U)` and `yoneda.obj (u.obj U)` are
> left Kan extensions of `yoneda.obj U` along `u.op`, so they are canonically isomorphic.

```lean
noncomputable def presheafPushforward_yoneda_iso (U : C) :
    (presheafPushforward04D2 u).obj (yoneda.obj U) ≅ yoneda.obj (u.obj U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.5, Tag 00VC](https://stacks.math.columbia.edu/tag/00VC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
