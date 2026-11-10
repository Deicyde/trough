---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction.nonempty_adjunction_preservesFiniteLimits_isRightAdjoint_and_iso_sheafPushforwardCocontinuous
statement: formalized
proof: formalized
---

# 7.23 Cocontinuous functors which have a left adjoint

Section 7.23 of the Stacks Project, [Tag 08NG](https://stacks.math.columbia.edu/tag/08NG). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08NH, a lemma

[Tag 08NH](https://stacks.math.columbia.edu/tag/08NH) in the Stacks Project.

**`CategoryTheory.Adjunction.nonempty_adjunction_preservesFiniteLimits_isRightAdjoint_and_iso_sheafPushforwardCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LeftAdjoint.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LeftAdjoint.lean#L198). The attribute's comment: “Lower shriek of a continuous functor which has a left adjoint.”. References: SGA 4 III (2.5), “v_*≃u_s and v^*≃u^s”; SGA 4 III (1.3), “special case”; SGA 4 III (2.4), “special case”.

> **Stacks 08NH.** Let `(C, J)` and `(D, K)` be sites, let `G : C ⥤ D` be a continuous functor,
> and let `W : D ⥤ C` be a left adjoint of `G`. Write
> `Λ = sheafToPresheaf J A ⋙ (Functor.whiskeringLeft Dᵒᵖ Cᵒᵖ A).obj W.op ⋙ presheafToSheaf K A`
> for the functor sending a sheaf `F` on `C` to the sheafification of the presheaf `V ↦ F(W V)`,
> that is, of `w^p F`. Then:
>
> 1. (a) `Λ` is a left adjoint of `g⁻¹ = G.sheafPushforwardContinuous A J K`, i.e. the lower shriek
>    `g_!` is the sheafification of `w^p`;
>    (b) `Λ` preserves finite limits, hence is exact, as soon as sheafification for `K` does;
> 2. if `W` is continuous, then `Λ` has itself a left adjoint, i.e. `Λ.IsRightAdjoint`;
> 3. if `W` is cocontinuous and `h : Sh(D) ⥤ Sh(C)` is the associated morphism of topoi, then
>    `g⁻¹ = h_*`, that is `G.sheafPushforwardContinuous A J K ≅ W.sheafPushforwardCocontinuous A K J`
>    (the other half of part (3), `g_! = h⁻¹`, is conjunct 1(a): `h⁻¹` is `Λ`).
>
> The conjuncts are the parts of the source, in order.

```lean
public theorem
  nonempty_adjunction_preservesFiniteLimits_isRightAdjoint_and_iso_sheafPushforwardCocontinuous
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (A : Type u₃) [Category.{v₃} A]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) {G : C ⥤ D} {W : D ⥤ C} (adj : W ⊣ G)
    [G.IsContinuous J K] [HasWeakSheafify K A] :
    -- (1)(a) `g_!` is the sheafification of `w^p`
    Nonempty
        (sheafToPresheaf J A ⋙ (Functor.whiskeringLeft Dᵒᵖ Cᵒᵖ A).obj W.op ⋙ presheafToSheaf K A ⊣
          G.sheafPushforwardContinuous A J K) ∧
      -- (1)(b) `g_!` is exact
      (∀ [HasFiniteLimits A] [PreservesFiniteLimits (presheafToSheaf K A)],
        PreservesFiniteLimits
          (sheafToPresheaf J A ⋙
            (Functor.whiskeringLeft Dᵒᵖ Cᵒᵖ A).obj W.op ⋙ presheafToSheaf K A)) ∧
      -- (2) if `w` is continuous, then `g_!` has a left adjoint
      (∀ [W.IsContinuous K J] [HasWeakSheafify J A] [∀ F : Dᵒᵖ ⥤ A, W.op.HasLeftKanExtension F],
        (sheafToPresheaf J A ⋙
            (Functor.whiskeringLeft Dᵒᵖ Cᵒᵖ A).obj W.op ⋙ presheafToSheaf K A).IsRightAdjoint) ∧
      -- (3) if `w` is cocontinuous, then `g⁻¹ = h_*`
      (∀ [W.IsCocontinuous K J] [∀ F : Dᵒᵖ ⥤ A, W.op.HasPointwiseRightKanExtension F],
        Nonempty (G.sheafPushforwardContinuous A J K ≅ W.sheafPushforwardCocontinuous A K J))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.23, Tag 08NG](https://stacks.math.columbia.edu/tag/08NG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
