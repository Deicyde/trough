---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation, AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation_unconditional
statement: formalized
proof: formalized
---

# 102.5 Descending relative objects

Section 102.5 of the Stacks Project, [Tag 0CN3](https://stacks.math.columbia.edu/tag/0CN3). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CN4, a lemma

[Tag 0CN4](https://stacks.math.columbia.edu/tag/0CN4) in the Stacks Project.

**`AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimit.lean, line 894](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimit.lean#L894). The attribute's comment: “a reduction, not a proof: inputs of the source's proof are carried as the explicit hypotheses hPresentation (Stacks 04T4 (4), (5), Stacks 04T5 (2) and the 050K/050H bookkeeping, with Stacks 04YC discharged), hDescent (what is left of Stacks 07SK and 0CN2 on a groupoid object once the essential-surjectivity clause is discharged: the descent of s, t, c, the pointwiseGroupoid field, the common stage, and Stacks 046Q), hStageStackModel (a universe-lifting datum, not a mathematical assumption: a quotient stack has hom universe one above that of AlgebraicStacks), hModelFinitePresentation (Stacks 06Q2 evaluated on a quotient stack) and hModelComparison (Stacks 044P, 044R, 046Q and 04Y1 for a base-changed groupoid); what is discharged here is Stacks 07SF for the limit with its quasi-compactness and quasi-separatedness, the essential-surjectivity clause of Stacks 07SK for the object and arrow spaces of the presenting groupoid, Stacks 04TK on the descended groupoid, and the assembly of the conclusion”.

> **Stacks 0CN4.** Let `(X_i)` be a directed inverse system of quasi-compact, quasi-separated
> algebraic spaces over `S` with affine transition morphisms, and let `X = lim X_i`. If `𝒳` is an
> algebraic stack of finite presentation over `X`, then there are a stage `i` and an algebraic
> stack `𝒳_i` of finite presentation over `X_i` with `𝒳 ≅ 𝒳_i ×_{X_i} X` as algebraic stacks
> over `X`.
>
> Five inputs are carried as explicit hypotheses — `hPresentation`, `hDescent`,
> `hStageStackModel`, `hModelFinitePresentation` and `hModelComparison`. None is a restatement of
> this conclusion, and `hStageStackModel` is a universe-lifting datum rather than a mathematical
> assumption. The module's implementation notes say what each one is, which declaration of the library it
> would come from, and — for Stacks 0CN2 — exactly why the existing result falls short. What is
> discharged here is Stacks 07SF for the limit with its quasi-compactness and
> quasi-separatedness, the essential-surjectivity clause of Stacks 07SK for the object and arrow
> spaces of the presenting groupoid, Stacks 04TK on the descended groupoid, and the assembly of the
> conclusion.

```lean
theorem exists_stage_model_of_isFinitePresentation
    (hPresentation : GroupoidPresentationOfAffineSmoothChart.{u, w} B S hS hZ)
    (hDescent : C.GroupoidStructureDescendsToStage)
    (hStageStackModel : C.StageStackModel.{u, w})
    (hModelFinitePresentation : C.ModelIsFinitePresentation.{u, w})
    (hModelComparison : C.ModelBaseChangeComparison.{u, w})
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

**`AlgebraicGeometry.Stack.StackDescentSystem.exists_stage_model_of_isFinitePresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimitTheorem.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DescendingStacksAlongLimitTheorem.lean#L76). The attribute's comment: “The directed set `I` indexes the system as a covariant diagram on the cofiltered category `Iᵒᵖ`, and `StackDescentSystem` bounds the cardinality of `Iᵒᵖ` and of its hom types by the cofinality of the cutoff of the big fppf site, which is what keeps the limit `X` inside the site. The isomorphism `𝒳 ≅ 𝒳_i ×_{X_i} X` over `X` is an equivalence in the 2-category of algebraic stacks whose forward 1-morphism followed by the projection to `X` is 2-isomorphic to the structure 1-morphism of `𝒳`.”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
