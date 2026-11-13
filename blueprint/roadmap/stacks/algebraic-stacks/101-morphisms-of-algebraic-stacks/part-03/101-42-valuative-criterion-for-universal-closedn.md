---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_isQuasiCompactMorphism_of_valuativeCriterionExistence, AlgebraicGeometry.Stack.valuativeCriterionExistence_of_universallyClosed
statement: formalized
proof: formalized
---

# 101.42 Valuative criterion for universal closedness

Section 101.42 of the Stacks Project, [Tag 0CLV](https://stacks.math.columbia.edu/tag/0CLV). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CLW, a lemma

[Tag 0CLW](https://stacks.math.columbia.edu/tag/0CLW) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_isQuasiCompactMorphism_of_valuativeCriterionExistence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniversallyClosed.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniversallyClosed.lean#L381).

> **Stacks 0CLW.** A 1-morphism of algebraic stacks over `S` which is quasi-compact
> (**Stacks 050U**) and satisfies the existence part of the valuative criterion (**Stacks 0CLK**)
> is universally closed (**Stacks 0513**, part (2)).

```lean
theorem universallyClosed_of_isQuasiCompactMorphism_of_valuativeCriterionExistence
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : Stack.IsQuasiCompactMorphism B S hS f)
    (hex : Stack.ValuativeCriterion.Existence B S hS f) :
    UniversallyClosed B S hS f
```

## Tag 0CLX, a lemma

[Tag 0CLX](https://stacks.math.columbia.edu/tag/0CLX) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionExistence_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeExistenceUniversallyClosed.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeExistenceUniversallyClosed.lean#L387).

> **Stacks 0CLX.** A quasi-separated, universally closed 1-morphism of algebraic stacks
> satisfies the existence part of the valuative criterion.
>
> Given a valuative square `q`, the specialisation step
> `AlgebraicGeometry.Stack.ValuativeSquare.exists_valuativeSquare_genericSection` produces a
> valuative square `q₂` for the generic section of `q` whose closed point lies over the closed point
> of `Spec q.R`. Its valuation ring and fraction field are the dominating extension; the two ring
> maps come from 2-Yoneda and the full faithfulness of `Spec`; locality of the ring map is the
> closed-point condition; and the dotted arrow is the special point of `q₂` followed by the
> projection to `𝒳`.

```lean
theorem valuativeCriterionExistence_of_universallyClosed
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (hclosed : AlgebraicStacks.UniversallyClosed B S hS f) :
    ValuativeCriterion.Existence B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.42, Tag 0CLV](https://stacks.math.columbia.edu/tag/0CLV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
