---
declaration: section
origin: cited
lean: CategoryTheory.Limits.functorCategoryHasLimit, CategoryTheory.Limits.limitObjIsoLimitCompEvaluation, CategoryTheory.yoneda_relativelyRepresentable_iff_pullback_representable, CategoryTheory.Functor.relativelyRepresentable, CategoryTheory.Functor.isRepresentable_of_relativelyRepresentable_of_target_isRepresentable, CategoryTheory.yoneda_relativelyRepresentable_diag_tfae, CategoryTheory.Functor.relativelyRepresentable.diag_iff
statement: formalized
proof: formalized
---

# 4.8 Fibre products and representability

Section 4.8 of the Stacks Project, [Tag 0021](https://stacks.math.columbia.edu/tag/0021). 4 tags here are carried by 3 declarations of the repository (all in StacksCore) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0022, a lemma

[Tag 0022](https://stacks.math.columbia.edu/tag/0022) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.functorCategoryHasLimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.functorCategoryHasLimit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L60) (StacksCore): “existence”.
- [`CategoryTheory.Limits.limitObjIsoLimitCompEvaluation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.limitObjIsoLimitCompEvaluation#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L61) (StacksCore): “pointwise formula”.

## Tag 0023, a definition

[Tag 0023](https://stacks.math.columbia.edu/tag/0023) in the Stacks Project.

**`CategoryTheory.yoneda_relativelyRepresentable_iff_pullback_representable`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Pullback.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L82). The attribute's comment: “Equivalent definitions of representable presheaf morphisms”.

> **Stacks 0023** (Equivalent definitions of representable presheaf morphisms).
> A morphism of presheaves `a : F ⟶ G` on `𝒞` is relatively representable along the Yoneda embedding
> if and only if for every object `U : 𝒞` and every section `ξ ∈ G(U)` the pullback presheaf
> `h_U ×_G F` is representable.

```lean
lemma CategoryTheory.yoneda_relativelyRepresentable_iff_pullback_representable
  {F G : 𝒞ᵒᵖ ⥤ Type v} (a : F ⟶ G) :
  yoneda.relativelyRepresentable a ↔
  ∀ (U : 𝒞) (ξ : G.obj (op U)), (pullback (yonedaEquiv.symm ξ) a).IsRepresentable
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L63) (StacksCore): “The definition is same as saying the presheaf morphism `a : F ⟶ G` is representable relative to the yoneda functor”. References: SGA 3 XVIII (1.4); SGA 3 XXIV (7.1.9); SGA 4 II (1.3), “more general”.

## Tag 03KC, a lemma

[Tag 03KC](https://stacks.math.columbia.edu/tag/03KC) in the Stacks Project.

**`CategoryTheory.Functor.isRepresentable_of_relativelyRepresentable_of_target_isRepresentable`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Pullback.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L103). References: SGA 3 XIV (2.15), “more general”.

> **Stacks 03KC**.
> If `a : F ⟶ G` is a representable morphism of presheaves on `𝒞` and the target `G` is itself
> representable, then so is `F`.

```lean
lemma CategoryTheory.Functor.isRepresentable_of_relativelyRepresentable_of_target_isRepresentable
    {F G : 𝒞ᵒᵖ ⥤ Type v} (a : F ⟶ G) (ha : yoneda.relativelyRepresentable a)
    [hG : G.IsRepresentable] : F.IsRepresentable
```

## Tag 0024, a lemma

[Tag 0024](https://stacks.math.columbia.edu/tag/0024) in the Stacks Project.

**`CategoryTheory.yoneda_relativelyRepresentable_diag_tfae`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Pullback.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L120).

> **Stacks 0024**.
> For a presheaf `F` on a category `𝒞` with binary products and pullbacks, the following are
> equivalent:
> 1. the diagonal `Δ : F ⟶ F × F` is representable along Yoneda;
> 2. for every `U : 𝒞` and every `ξ ∈ F(U)`, the morphism `yonedaEquiv.symm ξ : h_U ⟶ F` is
>    representable along Yoneda;
> 3. for every pair `U, V : 𝒞` and sections `ξ ∈ F(U)`, `ξ' ∈ F(V)`, the pullback presheaf
>    `h_U ×_F h_V` is representable.

```lean
lemma CategoryTheory.yoneda_relativelyRepresentable_diag_tfae
    (F : 𝒞ᵒᵖ ⥤ Type v) [HasBinaryProducts 𝒞] [HasPullbacks 𝒞] : List.TFAE
    [
      yoneda.relativelyRepresentable (diag F),
      ∀ (U) (ξ : F.obj (op U)), yoneda.relativelyRepresentable (yonedaEquiv.symm ξ),
      ∀ (U V) (ξ : F.obj (op U)) (ξ' : F.obj (op V)),
        (pullback (yonedaEquiv.symm ξ) (yonedaEquiv.symm ξ')).IsRepresentable
    ]
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.diag_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.diag_iff#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L68) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.8, Tag 0021](https://stacks.math.columbia.edu/tag/0021)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
