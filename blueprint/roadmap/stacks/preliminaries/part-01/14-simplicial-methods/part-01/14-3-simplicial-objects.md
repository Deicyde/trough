---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject, SSet, CategoryTheory.SimplicialObject.bijective_comp_toSimplexCategory_op_and_whiskerLeft, CategoryTheory.SimplicialObject.δ_comp_δ, CategoryTheory.SimplicialObject.δ_comp_σ_of_le, CategoryTheory.SimplicialObject.δ_comp_σ_self, CategoryTheory.SimplicialObject.δ_comp_σ_succ, CategoryTheory.SimplicialObject.δ_comp_σ_of_gt
statement: formalized
proof: formalized
---

# 14.3 Simplicial objects

Section 14.3 of the Stacks Project, [Tag 0169](https://stacks.math.columbia.edu/tag/0169). 6 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 016A, a definition

[Tag 016A](https://stacks.math.columbia.edu/tag/016A) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SimplicialObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L45) (StacksFrontier): “(1), (3), (4), (5): simplicial objects of C, the functor category Δᵒᵖ ⥤ C (morphisms are natural transformations); (3) is C = abelian groups”. References: SGA 4 V (7.1.0); SGA 4 Vbis (1.2.6); SGA 4 Vbis (3.0.1); SGA 4 Vbis (5.1.0).
- [`SSet`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SSet#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L48) (StacksFrontier): “(2)”. References: SGA 4 Vbis (3.0.1), “special case”.

## Tag 016B, a lemma

[Tag 016B](https://stacks.math.columbia.edu/tag/016B) in the Stacks Project.

**`CategoryTheory.SimplicialObject.bijective_comp_toSimplexCategory_op_and_whiskerLeft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L73). The attribute's comment: “part (1) is `CategoryTheory.SimplicialObject.δ_comp_δ` and its companions in Mathlib; parts (2) and (3) are stated in terms of the presented category `SimplexCategoryGenRel`, so that no equality of objects of `C` is transported”.

> **Stacks 016B** (parts (2) and (3), via the presented category `SimplexCategoryGenRel`).
> Restriction along the canonical functor `SimplexCategoryGenRel.toSimplexCategory` from the
> category presented by the generators `δ^n_j`, `σ^n_j` and the relations of [Stacks, Tag 0167]
> is bijective on simplicial objects of `C` and on morphisms of simplicial objects: every system
> `(U_n, d^n_j, s^n_j)` satisfying those relations — that is, every functor
> `SimplexCategoryGenRelᵒᵖ ⥤ C` — comes from a unique simplicial object `U` with `U_n = U([n])`,
> `d^n_j = U(δ^n_j)` and `s^n_j = U(σ^n_j)`, and every family of morphisms `U_n ⟶ U'_n`
> commuting with the faces and the degeneracies comes from a unique morphism of simplicial
> objects.

```lean
public theorem bijective_comp_toSimplexCategory_op_and_whiskerLeft (C : Type u)
    [Category.{v} C] :
    Function.Bijective (fun X : SimplicialObject C => toSimplexCategory.op ⋙ X) ∧
      ∀ X Y : SimplicialObject C,
        Function.Bijective (fun f : X ⟶ Y => Functor.whiskerLeft toSimplexCategory.op f)
```

## Tag 016C, a remark

[Tag 016C](https://stacks.math.columbia.edu/tag/016C) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SimplicialObject.δ_comp_δ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_δ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L50) (StacksFrontier): “(1)”.
- [`CategoryTheory.SimplicialObject.δ_comp_σ_of_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_of_le#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L51) (StacksFrontier): “(2)”.
- [`CategoryTheory.SimplicialObject.δ_comp_σ_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_self#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L52) (StacksFrontier): “(3), dⱼ ∘ sⱼ = id”.
- [`CategoryTheory.SimplicialObject.δ_comp_σ_succ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_succ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L53) (StacksFrontier): “(3), dⱼ₊₁ ∘ sⱼ = id”.
- [`CategoryTheory.SimplicialObject.δ_comp_σ_of_gt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_of_gt#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L54) (StacksFrontier): “(4)”.
- [`CategoryTheory.SimplicialObject.σ_comp_σ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.σ_comp_σ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L55) (StacksFrontier): “(5)”.

## Tag 016D, an example

[Tag 016D](https://stacks.math.columbia.edu/tag/016D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SimplicialObject.const`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.const#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L57) (StacksFrontier). References: SGA 3 IV (4.3.17), “special case”; SGA 4 Vbis (1.2.6); SGA 4 Vbis (3.2.3).

## Tag 016E, an example

[Tag 016E](https://stacks.math.columbia.edu/tag/016E) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Arrow.cechNerve`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Arrow.cechNerve#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L59) (StacksFrontier). References: SGA 3 X (6.3); SGA 3 X (9.7.1); SGA 4 Vbis (1.2.7).

## Tag 016F, a lemma

[Tag 016F](https://stacks.math.columbia.edu/tag/016F) in the Stacks Project.

**`CategoryTheory.SimplicialObject.isSplitMono_σ`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L138).

> **Stacks 016F**.
> Each degeneracy map `X.σ i : Xₙ ⟶ Xₙ₊₁` of a simplicial object `X` of a category `C` has a left
> inverse, namely the face map `X.δ i.castSucc`; in particular `X.σ i` is a monomorphism.

```lean
public instance isSplitMono_σ (X : SimplicialObject C) {n : ℕ} (i : Fin (n + 1)) :
    IsSplitMono (X.σ i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.3, Tag 0169](https://stacks.math.columbia.edu/tag/0169)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
