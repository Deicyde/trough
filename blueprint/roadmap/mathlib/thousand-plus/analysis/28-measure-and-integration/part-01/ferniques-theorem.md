---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsGaussian.exists_integrable_exp_sq
mathlib_file: Mathlib/Probability/Distributions/Gaussian/Fernique.lean
---

# Fernique's theorem

**Fernique's theorem**: for a Gaussian measure, there exists `C > 0` such that the function
`x ↦ exp (C * ‖x‖ ^ 2)` is integrable.

```lean
ProbabilityTheory.IsGaussian.exists_integrable_exp_sq.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [SecondCountableTopology E] [CompleteSpace E]
  (μ : MeasureTheory.Measure E) [ProbabilityTheory.IsGaussian μ] :
  ∃ C, 0 < C ∧ MeasureTheory.Integrable (fun x => Real.exp (C * ‖x‖ ^ 2)) μ
```

## Depends on

- [Gaussian measures](../../../../overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)

## Proof depends on

- [Bounded convergence theorem](bounded-convergence-theorem.md)
- [Cauchy-Schwarz inequality](../../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Change of variables to polar co-ordinates](../../../../undergraduate/measures-and-integral-calculus/integration/change-of-variables-to-polar-co-ordinates.md)
- [Characteristic function](../../../../overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Conditional probability](../../../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Connected components](../../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../../../overview/topology/general-topology/part-01/connectedness.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Derivative of the inverse of a function](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Determinant of vectors](../../../../undergraduate/linear-algebra/multilinearity/determinant-of-vectors.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Divergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-02/divergence-theorem.md)
- [Dominated convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Dual vector space](../../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Fubini's theorem](../../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Fundamental Theorem of Integral Calculus](../../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Higher-order derivatives of functions](../../../../undergraduate/single-variable-real-analysis/differentiability/higher-order-derivatives-of-functions.md)
- [Orientation of a $\R$-vector space](../../../../undergraduate/linear-algebra/multilinearity/orientation-of-a-vector-space.md)
- [Path connectedness](../../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Stone-Weierstrass theorem](../../../../overview/topology/general-topology/part-02/stone-weierstrass-theorem.md)
- [Unitary group](../../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Fernique.html#ProbabilityTheory.IsGaussian.exists_integrable_exp_sq)
- [Source of `ProbabilityTheory.IsGaussian.exists_integrable_exp_sq` in Mathlib/Probability/Distributions/Gaussian/Fernique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Distributions/Gaussian/Fernique.lean#L161)
- [1000+ theorems list: Q5445112](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3195)
- [1000+ theorems project: Q5445112](https://1000-plus.github.io/?length=-1#Q5445112)
- [Wikipedia: Fernique's theorem](https://en.wikipedia.org/wiki/Fernique's_theorem)
- [Wikidata: Q5445112](https://www.wikidata.org/wiki/Q5445112)
