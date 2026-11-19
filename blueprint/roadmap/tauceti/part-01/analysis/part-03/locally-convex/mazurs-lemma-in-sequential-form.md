---
declaration: theorem
origin: cited
lean: TauCeti.exists_tendsto_sum_smul_of_tendsto_weak, TauCeti.exists_sum_smul_mem_of_tendsto_weak
statement: formalized
proof: formalized
---

# Mazur's lemma, in sequential form

if the weak limit has a countable neighbourhood
basis (for instance in a seminormed space), choose a finite real convex combination from the
`n`th tail for every `n`, so that the combinations converge to the weak limit in the original
topology.

```lean
TauCeti.exists_tendsto_sum_smul_of_tendsto_weak.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [AddCommGroup E] [_root_.Module 𝕜 E] [_root_.Module ℝ E] [IsScalarTower ℝ 𝕜 E]
  [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul 𝕜 E] [LocallyConvexSpace ℝ E]
  {u : ℕ → E} {x : E} [(nhds x).IsCountablyGenerated]
  (hu :
    Filter.Tendsto (fun n => (toWeakSpace 𝕜 E) (u n)) Filter.atTop (nhds ((toWeakSpace 𝕜 E) x))) :
  ∃ s w,
    (∀ (n i : ℕ), i ∈ s n → 0 ≤ w n i) ∧
      (∀ (n : ℕ), ∑ i ∈ s n, w n i = 1) ∧
        Filter.Tendsto (fun n => ∑ i ∈ s n, w n i • u (n + i)) Filter.atTop (nhds x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_tendsto_sum_smul_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Mazur.html#TauCeti.exists_tendsto_sum_smul_of_tendsto_weak).

## Other forms

**Mazur's lemma, with explicit finite coefficients.** Formalized in Tau Ceti as [`TauCeti.exists_sum_smul_mem_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Mazur.html#TauCeti.exists_sum_smul_mem_of_tendsto_weak).

```lean
TauCeti.exists_sum_smul_mem_of_tendsto_weak.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [AddCommGroup E] [_root_.Module 𝕜 E] [_root_.Module ℝ E] [IsScalarTower ℝ 𝕜 E]
  [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul 𝕜 E] [LocallyConvexSpace ℝ E]
  {u : ℕ → E} {x : E}
  (hu : Filter.Tendsto (fun n => (toWeakSpace 𝕜 E) (u n)) Filter.atTop (nhds ((toWeakSpace 𝕜 E) x)))
  (n : ℕ) {U : Set E} (hU : U ∈ nhds x) :
  ∃ s w, (∀ i ∈ s, 0 ≤ w i) ∧ ∑ i ∈ s, w i = 1 ∧ ∑ i ∈ s, w i • u (n + i) ∈ U
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_tendsto_sum_smul_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Mazur.html#TauCeti.exists_tendsto_sum_smul_of_tendsto_weak)
- [Source of `TauCeti.exists_tendsto_sum_smul_of_tendsto_weak` in TauCeti/Analysis/LocallyConvex/Mazur.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/LocallyConvex/Mazur.lean#L93)
