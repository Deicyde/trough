---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exists_isFinitePresentation_isClosedImmersion_of_isFiniteType, AlgebraicGeometry.Stack.AlgebraicStacks.closedImmersionIntoFinitePresentationStatement_holds_overScheme
statement: formalized
proof: formalized
---

# 102.6 Finite type closed in finite presentation

Section 102.6 of the Stacks Project, [Tag 0CQ0](https://stacks.math.columbia.edu/tag/0CQ0). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CQ1, a lemma

[Tag 0CQ1](https://stacks.math.columbia.edu/tag/0CQ1) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_isFinitePresentation_isClosedImmersion_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClosedImmersionIntoFinitePresentationArbitraryBase.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ClosedImmersionIntoFinitePresentationArbitraryBase.lean#L60).

> **Stacks 0CQ1.** Let `f : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack over a scheme `S`
> to an algebraic space over `S`, with `f` of finite type and quasi-separated and `Y` quasi-compact
> and quasi-separated. Then there are a 1-morphism of finite presentation `f' : 𝒳' ⟶ Y` and a
> closed immersion `i : 𝒳 ⟶ 𝒳'` of algebraic stacks over `Y`, that is, with `i ≫ f' ≅ f`.
>
> The source's proof, which approximates `Y` by Noetherian algebraic spaces (Stacks 07SU), takes
> place over `Spec ℤ`, where it is
> `AlgebraicGeometry.Stack.exists_finitePresentation_closedImmersion_overIntegers` with Stacks 07SU
> supplied by `AlgebraicGeometry.Space.hasNoetherianApproximation_of_isQuasiCompactSpace`.
> Construction A of Stacks 04X5 carries `f` to a quasi-separated 1-morphism, locally of finite
> type, from a quasi-compact algebraic stack to the view `Λ Y` of `Y` over `Spec ℤ`, which is again
> quasi-compact and quasi-separated; the factorization obtained there descends to `S`
> (`AlgebraicGeometry.Stack.exists_descent_changeBase`), and finite presentation and being a closed
> immersion descend along Construction A.

```lean
theorem exists_isFinitePresentation_isClosedImmersion_of_isFiniteType (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hY : IsAlgebraicSpace B S hS Y)
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y hY)
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (hYqs : Space.IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (𝒳' : AlgebraicStacks.{u, w} B S hS)
      (f' : 𝒳' ⟶ algebraicSpaceStack.{u, w} B S hS Y hY) (i : 𝒳 ⟶ 𝒳'),
      IsFinitePresentation B S hS f' ∧ IsClosedImmersion B S hS i ∧ Nonempty (i ≫ f' ≅ f)
```

## Tag 0CQ2, a lemma

[Tag 0CQ2](https://stacks.math.columbia.edu/tag/0CQ2) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.closedImmersionIntoFinitePresentationStatement_holds_overScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedClosedImmersionIntoFinitePresentationArbitraryBase.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedClosedImmersionIntoFinitePresentationArbitraryBase.lean#L248).

> **Stacks 0CQ2.** Let `f : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack over a scheme `S`
> to an algebraic space over `S`, with `f` of finite type and separated and `Y` quasi-compact and
> quasi-separated. Then there are a separated 1-morphism of finite presentation `f' : 𝒳' ⟶ Y` and a
> closed immersion `i : 𝒳 ⟶ 𝒳'` of algebraic stacks over `Y`, that is, with `i ≫ f' ≅ f`.
>
> The source's proof, which approximates `Y` by Noetherian algebraic spaces (Stacks 07SU), takes
> place over `Spec ℤ`, where it is
> `AlgebraicGeometry.Stack.exists_separated_finitePresentation_closedImmersion_overIntegers`.
> Construction A of Stacks 04X5 carries `f` to a separated 1-morphism, locally of finite type,
> from a quasi-compact algebraic stack to the view `Λ Y` of `Y` over `Spec ℤ`, which is again
> quasi-compact and quasi-separated; the factorization obtained there descends to `S`
> (`AlgebraicGeometry.Stack.exists_descent_changeBase`), and separatedness, finite presentation
> and being a closed immersion descend along Construction A.

```lean
theorem closedImmersionIntoFinitePresentationStatement_holds_overScheme (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    ClosedImmersionIntoFinitePresentationStatement.{u, w} B S hS
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 102.6, Tag 0CQ0](https://stacks.math.columbia.edu/tag/0CQ0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
