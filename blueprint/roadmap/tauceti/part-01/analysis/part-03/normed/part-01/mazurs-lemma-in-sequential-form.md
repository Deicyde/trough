---
declaration: theorem
origin: cited
lean: TauCeti.exists_tendsto_sum_smul_of_tendsto_weak, TauCeti.exists_sum_smul_norm_sub_lt_of_tendsto_weak
statement: formalized
proof: formalized
---

# Mazur's lemma, in sequential form

choose a finite real convex combination from the
`n`th tail for every `n`, so that the combinations converge in norm to the weak limit.

```lean
TauCeti.exists_tendsto_sum_smul_of_tendsto_weak.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E] {u : ℕ → E}
  {x : E}
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

Formalized in Tau Ceti as [`TauCeti.exists_tendsto_sum_smul_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Mazur.html#TauCeti.exists_tendsto_sum_smul_of_tendsto_weak).

## Other forms

**Mazur's lemma, with explicit finite coefficients.** Formalized in Tau Ceti as [`TauCeti.exists_sum_smul_norm_sub_lt_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Mazur.html#TauCeti.exists_sum_smul_norm_sub_lt_of_tendsto_weak).

```lean
TauCeti.exists_sum_smul_norm_sub_lt_of_tendsto_weak.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E]
  {u : ℕ → E} {x : E}
  (hu : Filter.Tendsto (fun n => (toWeakSpace 𝕜 E) (u n)) Filter.atTop (nhds ((toWeakSpace 𝕜 E) x)))
  (n : ℕ) {ε : ℝ} (hε : 0 < ε) :
  ∃ s w, (∀ i ∈ s, 0 ≤ w i) ∧ ∑ i ∈ s, w i = 1 ∧ ‖∑ i ∈ s, w i • u (n + i) - x‖ < ε
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_tendsto_sum_smul_of_tendsto_weak`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Mazur.html#TauCeti.exists_tendsto_sum_smul_of_tendsto_weak)
- [Source of `TauCeti.exists_tendsto_sum_smul_of_tendsto_weak` in TauCeti/Analysis/Normed/Module/Mazur.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Mazur.lean#L100)
