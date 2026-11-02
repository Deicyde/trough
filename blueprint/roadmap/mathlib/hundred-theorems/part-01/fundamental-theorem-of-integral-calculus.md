---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right, intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean
---

# Fundamental Theorem of Integral Calculus

Mathlib records this with 2 declarations.

`intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right`: **Fundamental theorem of calculus-1**, strict differentiability in the right endpoint.

If `f : ℝ → E` is integrable on `a..b` and `f x` has a finite limit `c` almost surely at `b`, then
`u ↦ ∫ x in a..u, f x` has derivative `c` at `b` in the sense of strict differentiability.

```lean
intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right.{u_3} {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {f : ℝ → E} {c : E} {a b : ℝ}
  (hf : IntervalIntegrable f MeasureTheory.volume a b)
  (hmeas : StronglyMeasurableAtFilter f (nhds b) MeasureTheory.volume)
  (hb : Filter.Tendsto f (nhds b ⊓ MeasureTheory.ae MeasureTheory.volume) (nhds c)) :
  HasStrictDerivAt (fun u => ∫ (x : ℝ) in a..u, f x) c b
```

`intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le`: **Fundamental theorem of calculus-2**: If `f : ℝ → E` is continuous on `[a, b]` (where `a ≤ b`)
and has a right derivative at `f' x` for all `x` in `(a, b)`, and `f'` is integrable on `[a, b]`,
then `∫ y in a..b, f' y` equals `f b - f a`.

```lean
intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le.{u_3} {E : Type u_3} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {a b : ℝ} [CompleteSpace E] {f f' : ℝ → E} (hab : a ≤ b)
  (hcont : ContinuousOn f (Set.Icc a b))
  (hderiv : ∀ x ∈ Set.Ioo a b, HasDerivWithinAt f (f' x) (Set.Ioi x) x)
  (f'int : IntervalIntegrable f' MeasureTheory.volume a b) : ∫ (y : ℝ) in a..b, f' y = f b - f a
```

## Depends on

- [Bochner integral](../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Affine space](../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Approximation by step functions](../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../overview/topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Differentiable function between normed vector spaces](../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extended real number](../../overview/general-algebra/numbers/extended-real-number.md)
- [Extreme value theorem](../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Fatou's lemma](../../overview/analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Giry monad](../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Local convexity](../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [M. Riesz extension theorem](../../thousand-plus/analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Monotone convergence theorem (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orthogonal projection](../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Pointwise convergence](../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Quotient space (Fundamentals)](../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right)
- [Source of `intervalIntegral.integral_hasStrictDerivAt_of_tendsto_ae_right` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L613)
- [Mathlib documentation: `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le)
- [Source of `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L1113)
- [Freek Wiedijk's 100 theorems, no. 15](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L77)
- [1000+ theorems list: Q1217677](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1537)
- [1000+ theorems project: Q1217677](https://1000-plus.github.io/?length=-1#Q1217677)
- [Wikipedia: Fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus)
- [Wikidata: Q1217677](https://www.wikidata.org/wiki/Q1217677)
