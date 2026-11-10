---
declaration: section
origin: cited
lean: reflection_principle
statement: formalized
proof: formalized
---

# 3.8 Reflection principle

Section 3.8 of the Stacks Project, [Tag 000F](https://stacks.math.columbia.edu/tag/000F). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 000G, a theorem

[Tag 000G](https://stacks.math.columbia.edu/tag/000G) in the Stacks Project.

**`reflection_principle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/ZFC/Reflection.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/SetTheory/ZFC/Reflection.lean#L328).

> **Stacks 000G — Reflection principle.** Given a finite family of set-theory
> formulas `φᵢ` with `n` free variables and any set `M₀`, there is a limit
> ordinal `α` such that `M₀ ⊆ V_α` and for every parameter tuple in `V_α` and
> every `i`, the relativization `φᵢ^{V_α}` agrees with `φᵢ` on the full universe.
> Here `V_ α = ZFSet.vonNeumann α` is the von Neumann hierarchy from Mathlib.

```lean
theorem reflection_principle
    (n m : ℕ) (φ : Fin m → SetFormula n) (M₀ : ZFSet.{u}) :
    ∃ α : Ordinal.{u}, Order.IsSuccLimit α ∧ M₀ ⊆ V_ α ∧
      ∀ (x : Fin n → ZFSet),
        (∀ j, x j ∈ V_ α) →
        ∀ i : Fin m,
          (φ i).realizeIn (V_ α) x ↔ (φ i).realize x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.8, Tag 000F](https://stacks.math.columbia.edu/tag/000F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
