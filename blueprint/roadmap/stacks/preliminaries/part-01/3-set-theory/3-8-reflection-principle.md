---
declaration: section
origin: cited
lean: reflection_principle, exists_superset_forall_realizeIn_iff_forall_realize
statement: formalized
proof: formalized
---

# 3.8 Reflection principle

Section 3.8 of the Stacks Project, [Tag 000F](https://stacks.math.columbia.edu/tag/000F). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 000G, a theorem

[Tag 000G](https://stacks.math.columbia.edu/tag/000G) in the Stacks Project.

**`reflection_principle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/ZFC/Reflection.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/SetTheory/ZFC/Reflection.lean#L328). The attribute's comment: “each formula separately, with `M = V_α`”.

> **Reflection principle, formula by formula.** Given a finite family of set-theory
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

**`exists_superset_forall_realizeIn_iff_forall_realize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/ZFC/Reflection.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/SetTheory/ZFC/Reflection.lean#L345).

> **Stacks 000G — Reflection principle.** Given a finite family `φ₁, …, φₘ` of formulas of
> set theory in the free variables `x₁, …, xₙ` and a set `M₀`, there is a set `M` with
> `M₀ ⊆ M` such that for all `x₁, …, xₙ ∈ M`, the conjunction of the relativizations `φᵢ^M`
> holds if and only if the conjunction of the `φᵢ` holds in the universe of sets; moreover
> `M = V_α` for a limit ordinal `α`.

```lean
theorem exists_superset_forall_realizeIn_iff_forall_realize
    (n m : ℕ) (φ : Fin m → SetFormula n) (M₀ : ZFSet.{u}) :
    ∃ M : ZFSet.{u}, M₀ ⊆ M ∧
      (∀ x : Fin n → ZFSet.{u}, (∀ j, x j ∈ M) →
        ((∀ i : Fin m, (φ i).realizeIn M x) ↔ ∀ i : Fin m, (φ i).realize x)) ∧
      ∃ α : Ordinal.{u}, Order.IsSuccLimit α ∧ M = V_ α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.8, Tag 000F](https://stacks.math.columbia.edu/tag/000F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
