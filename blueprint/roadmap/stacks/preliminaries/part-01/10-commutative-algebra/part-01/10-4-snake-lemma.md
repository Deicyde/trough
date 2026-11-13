---
declaration: section
origin: cited
lean: CategoryTheory.ShortComplex.SnakeInput.snake_lemma_addCommGrpCat, CategoryTheory.ShortComplex.snake_lemma_of_exact_rows, CategoryTheory.ShortComplex.SnakeInput.snake_lemma
statement: formalized
proof: formalized
---

# 10.4 Snake lemma

Section 10.4 of the Stacks Project, [Tag 07JV](https://stacks.math.columbia.edu/tag/07JV). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07JW, a lemma

[Tag 07JW](https://stacks.math.columbia.edu/tag/07JW) in the Stacks Project.

**`CategoryTheory.ShortComplex.SnakeInput.snake_lemma_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Grp/SnakeLemma.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Grp/SnakeLemma.lean#L38). The attribute's comment: “the full statement for abelian groups, including both "moreover" clauses (Ker α → Ker β injective if X → Y is, Coker β → Coker γ surjective if V → W is); the exactness part alone is Mathlib's `SnakeInput.snake_lemma`, for any abelian category”.

> The snake lemma for abelian groups, with both of its "moreover" clauses. Given a commutative
> diagram of abelian groups with exact rows `L₁ = (X ⟶ Y ⟶ Z ⟶ 0)` and `L₂ = (0 ⟶ U ⟶ V ⟶ W)`,
> encoded as `S : SnakeInput AddCommGrpCat` (with `L₀` the kernels and `L₃` the cokernels of the
> vertical maps), the sequence
> `Ker α ⟶ Ker β ⟶ Ker γ ⟶ Coker α ⟶ Coker β ⟶ Coker γ` (with the connecting map `S.δ`) is
> exact; moreover, if `X ⟶ Y` is injective then `Ker α ⟶ Ker β` is injective, and if `V ⟶ W` is
> surjective then `Coker β ⟶ Coker γ` is surjective.

```lean
theorem snake_lemma_addCommGrpCat (S : SnakeInput AddCommGrpCat.{u}) :
    S.composableArrows.Exact ∧
      (Function.Injective S.L₁.f → Function.Injective S.L₀.f) ∧
      (Function.Surjective S.L₂.g → Function.Surjective S.L₃.g)
```

**`CategoryTheory.ShortComplex.snake_lemma_of_exact_rows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/SnakeLemmaExactRows.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/SnakeLemmaExactRows.lean#L103). The attribute's comment: “stated in any abelian category; the abelian-group case is `C = AddCommGrpCat`; includes both "Moreover" clauses”.

> **Snake lemma.** Let
> ```
>     X ⟶ Y ⟶ Z ⟶ 0
>     |α   |β   |γ
> 0 ⟶ U ⟶ V ⟶ W
> ```
> (maps `f, g` in the top row, `k, l` in the bottom row) be a commutative diagram with exact rows
> in an abelian category. Then
> 1. there is a unique `δ : Ker γ ⟶ Coker α` such that, with `π' : Y ×_Z Ker γ ⟶ Y`,
>   `π : Y ×_Z Ker γ ⟶ Ker γ` the projections and `ι : Coker α ⟶ Coker α ⊔_U V`,
>   `ι' : V ⟶ Coker α ⊔_U V` the coprojections, `π ≫ δ ≫ ι = π' ≫ β ≫ ι'`;
> 2. the sequence `Ker α ⟶ Ker β ⟶ Ker γ ⟶ Coker α ⟶ Coker β ⟶ Coker γ` (with this `δ`) is
>   exact; if `f` is a monomorphism then so is `Ker α ⟶ Ker β`, and if `l` is an epimorphism
>   then so is `Coker β ⟶ Coker γ`.

```lean
theorem snake_lemma_of_exact_rows (comm₁ : α ≫ k = f ≫ β) (comm₂ : β ≫ l = g ≫ γ)
    (hfg : f ≫ g = 0) (hkl : k ≫ l = 0) (h₁ : (ShortComplex.mk f g hfg).Exact) [Epi g]
    (h₂ : (ShortComplex.mk k l hkl).Exact) [Mono k] :
    ∃ δ : kernel γ ⟶ cokernel α,
      (pullback.snd g (kernel.ι γ) ≫ δ ≫ pushout.inl (cokernel.π α) k =
        pullback.fst g (kernel.ι γ) ≫ β ≫ pushout.inr (cokernel.π α) k) ∧
      (∀ δ' : kernel γ ⟶ cokernel α,
        pullback.snd g (kernel.ι γ) ≫ δ' ≫ pushout.inl (cokernel.π α) k =
          pullback.fst g (kernel.ι γ) ≫ β ≫ pushout.inr (cokernel.π α) k → δ' = δ) ∧
      (ComposableArrows.mk₅ (kernel.map α β f k comm₁) (kernel.map β γ g l comm₂) δ
        (cokernel.map α β f k comm₁) (cokernel.map β γ g l comm₂)).Exact ∧
      (Mono f → Mono (kernel.map α β f k comm₁)) ∧
      (Epi l → Epi (cokernel.map β γ g l comm₂))
```

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.SnakeInput.snake_lemma`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.SnakeInput.snake_lemma#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean#L9) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.4, Tag 07JV](https://stacks.math.columbia.edu/tag/07JV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
