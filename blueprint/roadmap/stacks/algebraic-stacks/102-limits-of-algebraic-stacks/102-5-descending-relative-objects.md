---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation_unconditional
statement: formalized
proof: formalized
---

# 102.5 Descending relative objects

Section 102.5 of the Stacks Project, [Tag 0CN3](https://stacks.math.columbia.edu/tag/0CN3). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CN4, a lemma

[Tag 0CN4](https://stacks.math.columbia.edu/tag/0CN4) in the Stacks Project.

**`AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimitTheorem.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimitTheorem.lean#L76). The attribute's comment: “The directed set `I` indexes the system as a covariant diagram on the cofiltered category `Iᵒᵖ`, and `StackDescentSystem` bounds the cardinality of `Iᵒᵖ` and of its hom types by the cofinality of the cutoff of the big fppf site, which is what keeps the limit `X` inside the site. The isomorphism `𝒳 ≅ 𝒳_i ×_{X_i} X` over `X` is an equivalence in the 2-category of algebraic stacks whose forward 1-morphism followed by the projection to `X` is 2-isomorphic to the structure 1-morphism of `𝒳`. Every step of the source's proof is proved in the library.”.

> **Stacks 0CN4.** Let `(X_i)` be a directed inverse system of quasi-compact, quasi-separated
> algebraic spaces over `S` with affine transition morphisms, and let `X = lim X_i`. If `𝒳` is an
> algebraic stack of finite presentation over `X`, then there are a stage `i` and an algebraic
> stack `𝒳_i` of finite presentation over `X_i` with `𝒳 ≅ 𝒳_i ×_{X_i} X` as algebraic stacks
> over `X`.
>
> This is the statement of `StackDescentSystem.exists_stage_model_of_isFinitePresentation` with
> none of its hypotheses. The system satisfies the chapter's convention
> (`StackDescentSystem.siteContainsBaseChangeLimits`), and under the convention the statement is
> `AlgebraicGeometry.Stack.AlgebraicStacks.finitePresentationStackDescendsStatement_holds`.

```lean
theorem exists_stage_model_of_isFinitePresentation_unconditional
    (C : StackDescentSystem B S hS hZ I)
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (f : 𝒳 ⟶ C.limitStack.{u, w})
    (hf : AlgebraicStacks.IsFinitePresentation B S hS f) :
    ∃ (i : Iᵒᵖ) (𝒳ᵢ : AlgebraicStacks.{u, w} B S hS) (fᵢ : 𝒳ᵢ ⟶ C.stageStack.{u, w} i),
      AlgebraicStacks.IsFinitePresentation B S hS fᵢ ∧
        ∃ e : Bicategory.Equivalence 𝒳
          (twoFibreProductAlgebraicStack.{u, w} B S hS fᵢ
            (C.limitStackProjection.{u, w} i)),
          Nonempty (e.hom ≫ (twoFibreProductSquareAlgebraicStacks.{u, w} B S hS fᵢ
            (C.limitStackProjection.{u, w} i)).snd ≅ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 102.5, Tag 0CN3](https://stacks.math.columbia.edu/tag/0CN3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
