---
declaration: section
origin: cited
lean: CategoryTheory.CosimplicialObject, CategoryTheory.CosimplicialObject.existsUnique_comp_toSimplexCategory_and_hom_app_eq, CategoryTheory.CosimplicialObject.cosimplicial_identities_of_val, CategoryTheory.CosimplicialObject.const, CategoryTheory.Arrow.cechConerve, CategoryTheory.CosimplicialObject.uliftCoyoneda_spec, CategoryTheory.CosimplicialObject.isSplitMono_δ
statement: formalized
proof: formalized
---

# 14.5 Cosimplicial objects

Section 14.5 of the Stacks Project, [Tag 016I](https://stacks.math.columbia.edu/tag/016I). 7 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 016J, a definition

[Tag 016J](https://stacks.math.columbia.edu/tag/016J) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.CosimplicialObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.CosimplicialObject#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L86) (StacksFrontier): “cosimplicial objects of C, the functor category Δ ⥤ C (morphisms are natural transformations); cosimplicial sets and abelian groups are C = sets, abelian groups”. References: SGA 4 XVII (5.5.3).

## Tag 016K, a lemma

[Tag 016K](https://stacks.math.columbia.edu/tag/016K) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.existsUnique_comp_toSimplexCategory_and_hom_app_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L302). The attribute's comment: “part (1) is `CategoryTheory.CosimplicialObject.δ_comp_δ` and its companions in Mathlib; parts (2) and (3) are stated with the coface–codegeneracy datum encoded as a functor out of the presented category `SimplexCategoryGenRel`, so that no equality of objects of `C` is transported”.

> **Stacks 016K** (parts (2) and (3), via the presented category `SimplexCategoryGenRel`).
> Let `C` be a category. (2) Given objects `Uₙ` of `C` and morphisms `δⁿⱼ : Uₙ ⟶ Uₙ₊₁`,
> `σⁿⱼ : Uₙ₊₁ ⟶ Uₙ` satisfying the cosimplicial identities — that is, a functor `F` out of the
> presentation `SimplexCategoryGenRel` of `Δ` by these generators and relations — there is a unique
> cosimplicial object `U` of `C` with `Uₙ = U ⦋n⦌`, `δⁿⱼ = U (δ j)` and `σⁿⱼ = U (σ j)`. (3) Given
> cosimplicial objects `U`, `U'` and a family of morphisms `a n : Uₙ ⟶ U'ₙ` commuting with the coface
> and the codegeneracy maps, there is a unique morphism `f : U ⟶ U'` of cosimplicial objects with
> `f.app ⦋n⦌ = a n`.

```lean
public theorem existsUnique_comp_toSimplexCategory_and_hom_app_eq
    (C : Type u) [Category.{v} C] :
    (∀ F : SimplexCategoryGenRel ⥤ C,
        ∃! U : CosimplicialObject C, SimplexCategoryGenRel.toSimplexCategory ⋙ U = F) ∧
      ∀ (U U' : CosimplicialObject C) (a : ∀ n : ℕ, U ^⦋n⦌ ⟶ U' ^⦋n⦌),
        (∀ (n : ℕ) (i : Fin (n + 2)), U.δ i ≫ a (n + 1) = a n ≫ U'.δ i) →
        (∀ (n : ℕ) (i : Fin (n + 1)), U.σ i ≫ a n = a (n + 1) ≫ U'.σ i) →
        ∃! f : U ⟶ U', ∀ n : ℕ, f.app ⦋n⦌ = a n
```

## Tag 016L, a remark

[Tag 016L](https://stacks.math.columbia.edu/tag/016L) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.cosimplicial_identities_of_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L381).

> **Stacks 016L**.
> Let `X` be a cosimplicial object of a category `C`. Writing `δᵢ : Xₙ₋₁ ⟶ Xₙ` for `X.δ` and
> `σᵢ : Xₙ₊₁ ⟶ Xₙ` for `X.σ` without recording the level, and reading `f ∘ g` as `g ≫ f`:
> (1) if `i < j` then `δⱼ ∘ δᵢ = δᵢ ∘ δⱼ₋₁`;
> (2) if `i < j` then `σⱼ ∘ δᵢ = δᵢ ∘ σⱼ₋₁`;
> (3) `σⱼ ∘ δⱼ = id` and `σⱼ ∘ δⱼ₊₁ = id`;
> (4) if `j + 1 < i` then `σⱼ ∘ δᵢ = δᵢ₋₁ ∘ σⱼ`;
> (5) if `i ≤ j` then `σⱼ ∘ σᵢ = σᵢ ∘ σⱼ₊₁`.
> Each is asserted for all indices whose bounds make both composites defined, an index repeated
> across levels being recognised by its value.

```lean
public theorem cosimplicial_identities_of_val (X : CosimplicialObject C) :
    (∀ {n : ℕ} {i : Fin (n + 2)} {j : Fin (n + 3)} {i' : Fin (n + 3)} {j' : Fin (n + 2)},
        (i : ℕ) < (j : ℕ) → (i' : ℕ) = (i : ℕ) → (j' : ℕ) + 1 = (j : ℕ) →
          X.δ i ≫ X.δ j = X.δ j' ≫ X.δ i') ∧
      (∀ {n : ℕ} {i : Fin (n + 3)} {j : Fin (n + 2)} {i' : Fin (n + 2)} {j' : Fin (n + 1)},
        (i : ℕ) < (j : ℕ) → (i' : ℕ) = (i : ℕ) → (j' : ℕ) + 1 = (j : ℕ) →
          X.δ i ≫ X.σ j = X.σ j' ≫ X.δ i') ∧
      (∀ {n : ℕ} {j : Fin (n + 1)} {i : Fin (n + 2)},
        (i : ℕ) = (j : ℕ) → X.δ i ≫ X.σ j = 𝟙 (X ^⦋n⦌)) ∧
      (∀ {n : ℕ} {j : Fin (n + 1)} {i : Fin (n + 2)},
        (i : ℕ) = (j : ℕ) + 1 → X.δ i ≫ X.σ j = 𝟙 (X ^⦋n⦌)) ∧
      (∀ {n : ℕ} {i : Fin (n + 3)} {j : Fin (n + 2)} {i' : Fin (n + 2)} {j' : Fin (n + 1)},
        (j : ℕ) + 1 < (i : ℕ) → (i' : ℕ) + 1 = (i : ℕ) → (j' : ℕ) = (j : ℕ) →
          X.δ i ≫ X.σ j = X.σ j' ≫ X.δ i') ∧
      ∀ {n : ℕ} {i : Fin (n + 2)} {j : Fin (n + 1)} {i' : Fin (n + 1)} {j' : Fin (n + 2)},
        (i : ℕ) ≤ (j : ℕ) → (i' : ℕ) = (i : ℕ) → (j' : ℕ) = (j : ℕ) + 1 →
          X.σ i ≫ X.σ j = X.σ j' ≫ X.σ i'
```

## Tag 016M, an example

[Tag 016M](https://stacks.math.columbia.edu/tag/016M) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.CosimplicialObject.const`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.CosimplicialObject.const#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L90) (StacksFrontier). References: SGA 4 Vbis (2.1.1), “special case”.

## Tag 016N, an example

[Tag 016N](https://stacks.math.columbia.edu/tag/016N) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Arrow.cechConerve`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Arrow.cechConerve#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L92) (StacksFrontier).

## Tag 0B13, an example

[Tag 0B13](https://stacks.math.columbia.edu/tag/0B13) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.uliftCoyoneda_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L527). The attribute's comment: “C[n] is Mathlib's uliftCoyoneda.obj (op n), dual to Δ[n] = SSet.stdSimplex.obj n of Tag 0176; the statement records its terms and structure maps, the simplicial structure of the family in n, and the corepresentability that characterises it”.

> **Stacks 0B13** (with `C[n]` as `uliftCoyoneda.obj (op n)`).
> For every object `n` of `Δ` the cosimplicial set `C[n] = uliftCoyoneda.obj (op n)` is
> `k ↦ Mor_Δ(n, k)`, with `φ : k ⟶ l` acting by `α ↦ α ≫ φ`; the family `n ↦ C[n]` is a simplicial
> object in cosimplicial sets, with `ψ : n ⟶ m` acting by `α ↦ ψ ≫ α`; and `C[n]` corepresents
> evaluation in degree `n`, in that `γ ↦ γ_n(id_n)` is a bijection `Mor(C[n], U) → Uₙ` for every
> cosimplicial set `U`.

```lean
public theorem uliftCoyoneda_spec :
    (∀ n k : SimplexCategory, (uliftCoyoneda.{u}.obj (op n)).obj k = ULift.{u} (n ⟶ k)) ∧
    (∀ (n k l : SimplexCategory) (φ : k ⟶ l) (α : ULift.{u} (n ⟶ k)),
      ((uliftCoyoneda.{u}.obj (op n)).map φ α).down = α.down ≫ φ) ∧
    (∀ (n m k : SimplexCategory) (ψ : n ⟶ m) (α : ULift.{u} (m ⟶ k)),
      ((uliftCoyoneda.{u}.map ψ.op).app k α).down = ψ ≫ α.down) ∧
    (∀ (n : SimplexCategory) (U : CosimplicialObject (Type u)),
      Function.Bijective fun γ : uliftCoyoneda.{u}.obj (op n) ⟶ U =>
        γ.app n (ULift.up (𝟙 n)))
```

## Tag 016O, a lemma

[Tag 016O](https://stacks.math.columbia.edu/tag/016O) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.isSplitMono_δ`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L470).

> **Stacks 016O**.
> Each coface map `X.δ i : Xₙ ⟶ Xₙ₊₁` of a cosimplicial object `X` of a category `C` has a left
> inverse, namely a degeneracy map `X.σ j`; in particular `X.δ i` is a monomorphism.

```lean
public instance isSplitMono_δ (X : CosimplicialObject C) {n : ℕ} (i : Fin (n + 2)) :
    IsSplitMono (X.δ i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.5, Tag 016I](https://stacks.math.columbia.edu/tag/016I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
