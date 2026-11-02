---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.tendstoUniformlyOn_of_ae_tendsto
mathlib_file: Mathlib/MeasureTheory/Function/Egorov.lean
---

# Egorov's theorem

**Egorov's theorem**: If `f : ι → α → β` is a sequence of strongly measurable functions that
converges to `g : α → β` almost everywhere on a measurable set `s` of finite measure,
then for all `ε > 0`, there exists a subset `t ⊆ s` such that `μ t ≤ ε` and `f` converges to `g`
uniformly on `s \ t`. We require the index type `ι` to be countable, and usually `ι = ℕ`.

In other words, a sequence of almost everywhere convergent functions converges uniformly except on
an arbitrarily small set.

```lean
MeasureTheory.tendstoUniformlyOn_of_ae_tendsto.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {ι : Type u_3} {m : MeasurableSpace α} [PseudoEMetricSpace β] {μ : MeasureTheory.Measure α}
  [SemilatticeSup ι] [Nonempty ι] [Countable ι] {f : ι → α → β} {g : α → β} {s : Set α}
  {ε : ENNReal} (hf : ∀ (n : ι), MeasureTheory.StronglyMeasurable (f n))
  (hg : MeasureTheory.StronglyMeasurable g) (hsm : MeasurableSet s) (hs : μ s ≠ ⊤)
  (hfg : ∀ᵐ (x : α) ∂μ, x ∈ s → Filter.Tendsto (fun n => f n x) Filter.atTop (nhds (g x)))
  (hε : 0 < ε) : ∃ t ⊆ s, MeasurableSet t ∧ μ t ≤ ε ∧ TendstoUniformlyOn f g Filter.atTop (s \ t)
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Uniform convergence norm (sup-norm)](../../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/uniform-convergence-norm-sup-norm.md)

## Sources

- [Mathlib documentation: `MeasureTheory.tendstoUniformlyOn_of_ae_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Egorov.html#MeasureTheory.tendstoUniformlyOn_of_ae_tendsto)
- [Source of `MeasureTheory.tendstoUniformlyOn_of_ae_tendsto` in Mathlib/MeasureTheory/Function/Egorov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/Egorov.lean#L234)
- [1000+ theorems list: Q1191709](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1510)
- [1000+ theorems project: Q1191709](https://1000-plus.github.io/all.html?length=-1#Q1191709)
- [Wikipedia: Egorov's theorem](https://en.wikipedia.org/wiki/Egorov's_theorem)
- [Wikidata: Q1191709](https://www.wikidata.org/wiki/Q1191709)
