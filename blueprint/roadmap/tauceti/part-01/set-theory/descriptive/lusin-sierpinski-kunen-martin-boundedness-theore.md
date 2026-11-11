---
declaration: theorem
origin: cited
lean: MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one, MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one_of_isClosed
statement: formalized
proof: formalized
---

# Lusin–Sierpiński / Kunen–Martin boundedness theorem (relative form)

Let `s` be an analytic
subset of a topological space `X` and `F : X → Descriptive.tree A` a family of descriptive trees
over a countable alphabet `A : Type u`. Suppose `F x` is well-founded for every `x ∈ s` and
`{x : s | u ∈ F x.1}` is closed in the subspace `s` for every finite sequence `u : List A`. Then
some countable ordinal `β < ω₁` strictly bounds `rank (F x)` across all `x ∈ s`.

```lean
MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one.{u, u_1} {X : Type u_1} [TopologicalSpace X]
  {A : Type u} [Countable A] {s : Set X} (hs : MeasureTheory.AnalyticSet s)
  (F : X → ↥(Descriptive.tree A)) (hwf : ∀ x ∈ s, Descriptive.Tree.IsWellFounded (F x))
  (hcl : ∀ (u : List A), IsClosed {x | u ∈ F ↑x}) :
  ∃ β < Ordinal.omega 1, ∀ x ∈ s, Descriptive.Tree.rank (F x) < β
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Tree.html#MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one).

## Other forms

**Lusin–Sierpiński / Kunen–Martin boundedness theorem (ambient-closed form).** Formalized in Tau Ceti as [`MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one_of_isClosed`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Tree.html#MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one_of_isClosed).

```lean
MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one_of_isClosed.{u, u_1} {X : Type u_1}
  [TopologicalSpace X] {A : Type u} [Countable A] {s : Set X} (hs : MeasureTheory.AnalyticSet s)
  (F : X → ↥(Descriptive.tree A)) (hwf : ∀ x ∈ s, Descriptive.Tree.IsWellFounded (F x))
  (hcl : ∀ (u : List A), IsClosed {x | u ∈ F x}) :
  ∃ β < Ordinal.omega 1, ∀ x ∈ s, Descriptive.Tree.rank (F x) < β
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Tree.html#MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one)
- [Source of `MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one` in TauCeti/SetTheory/Descriptive/Tree.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/Tree.lean#L501)
