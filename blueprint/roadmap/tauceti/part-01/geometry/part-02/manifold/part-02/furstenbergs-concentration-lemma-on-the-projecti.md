---
declaration: theorem
origin: cited
lean: OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact
statement: formalized
proof: formalized
---

# Furstenberg's concentration lemma on the projective line

If a sequence `g : ℕ → PSL(2, 𝕜)`
escapes every compact subset of `PSL(2, 𝕜)` and preserves a finite Borel measure `μ` on
`OnePoint 𝕜`, then `μ` is supported on a set of at most two points.

```lean
OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact.{u_1} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] [DecidableEq 𝕜] [ProperSpace 𝕜] {x✝ : MeasurableSpace (OnePoint 𝕜)}
  [BorelSpace (OnePoint 𝕜)] {μ : MeasureTheory.Measure (OnePoint 𝕜)}
  [MeasureTheory.IsFiniteMeasure μ] {g : ℕ → Matrix.ProjectiveSpecialLinearGroup (Fin 2) 𝕜}
  (hg :
    Filter.Tendsto g Filter.atTop
      (Filter.cocompact (Matrix.ProjectiveSpecialLinearGroup (Fin 2) 𝕜)))
  (hinv : ∀ (n : ℕ), MeasureTheory.Measure.map (fun x => g n • x) μ = μ) : ∃ b c, μ {b, c}ᶜ = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/InvariantMeasure.html#OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact).

## Sources

- [Tau Ceti documentation: `OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/InvariantMeasure.html#OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact)
- [Source of `OnePoint.exists_measure_compl_pair_eq_zero_of_tendsto_psl_cocompact` in TauCeti/Geometry/Manifold/Instances/OnePoint/InvariantMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Instances/OnePoint/InvariantMeasure.lean#L83)
