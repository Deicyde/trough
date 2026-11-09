# Vitali convergence theorem

**Vitali's convergence theorem** (non-finite measure version).

A sequence of functions `f` converges to `g` in Lp
if and only if it is uniformly integrable, uniformly tight and converges to `g` in measure.

```lean
MeasureTheory.tendstoInMeasure_iff_tendsto_Lp.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  {m : MeasurableSpace α} [NormedAddCommGroup β] {μ : MeasureTheory.Measure α} {p : ENNReal}
  {f : ℕ → α → β} {g : α → β} (hp : 1 ≤ p) (hp' : p ≠ ⊤)
  (hf : ∀ (n : ℕ), MeasureTheory.MemLp (f n) p μ) (hg : MeasureTheory.MemLp g p μ) :
  MeasureTheory.TendstoInMeasure μ f Filter.atTop g ∧
      MeasureTheory.UnifIntegrable f p μ ∧ MeasureTheory.UnifTight f p μ ↔
    Filter.Tendsto (fun n => MeasureTheory.eLpNorm (f n - g) p μ) Filter.atTop (nhds 0)
```

## Depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](caratheodorys-theorem-measure-theory.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Convergence in probability](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/convergence-in-probability.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Borel-Cantelli lemma (easy direction)](../../../undergraduate/probability-theory/definitions-of-a-probability-space/borel-cantelli-lemma-easy-direction.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.tendstoInMeasure_iff_tendsto_Lp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/UnifTight.html#MeasureTheory.tendstoInMeasure_iff_tendsto_Lp)
- [Source of `MeasureTheory.tendstoInMeasure_iff_tendsto_Lp` in Mathlib/MeasureTheory/Function/UnifTight.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/UnifTight.lean#L362)
- [1000+ theorems list: Q11352023](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L4046)
- [1000+ theorems project: Q11352023](https://1000-plus.github.io/all.html?length=-1#Q11352023)
- [Wikipedia: Vitali convergence theorem](https://en.wikipedia.org/wiki/Vitali_convergence_theorem)
- [Wikidata: Q11352023](https://www.wikidata.org/wiki/Q11352023)
