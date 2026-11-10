---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_of_isSetoidCategory_dottedArrow
statement: formalized
proof: formalized
---

# 101.40 Valuative criterion for second diagonal

Section 101.40 of the Stacks Project, [Tag 0CLQ](https://stacks.math.columbia.edu/tag/0CLQ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CLR, a lemma

[Tag 0CLR](https://stacks.math.columbia.edu/tag/0CLR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_of_isSetoidCategory_dottedArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionSecondDiagonal.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionSecondDiagonal.lean#L230).

> **Stacks 0CLR.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If the
> relative diagonal `Δ_f` is quasi-separated, and if for every diagram (0CLB) and every choice of
> `γ` as in Definition 0CLA the category of dotted arrows is a setoid, then `Δ_f` is separated.
>
> Both conditions on `Δ_f` are read in the relative sense of Stacks 04XB. The setoid hypothesis
> gives the uniqueness part of the valuative criterion for `Δ_f` through Stacks 0E8L, and
> quasi-separatedness turns that into separatedness through Stacks 03KV. This is the converse of
> the setoid assertion of Stacks 0CLC.

```lean
theorem isSeparated_relativeDiagonal_of_isSetoidCategory_dottedArrow (f : 𝒳 ⟶ 𝒴)
    (hqs : IsQuasiSeparated B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom))
    (hsetoid : ∀ D : ValuativeDiagram B S hS 𝒳 𝒴 f,
      IsSetoidCategory (CategoryTheory.DottedArrow D.x D.j f.hom D.y D.γ)) :
    IsSeparated B S hS (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.40, Tag 0CLQ](https://stacks.math.columbia.edu/tag/0CLQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
